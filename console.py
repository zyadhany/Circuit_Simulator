#!/usr/bin/python3

"""Simulation console."""

import cmd
import cv2
from Simulation import *
from Circuit_Detector import *
import matplotlib.pyplot as plt
import threading
from helper import *
import time
import multiprocessing

class SimulationCommand(cmd.Cmd):
	prompt = '(SAGED): '
	cir = Circuit()
	circuit_name = 'Circuit'
	net = []
	gnd = 0
	res = None

	def emptyline(self):
		pass

	def do_quit(self, arg=[]):
		"""Quit command to exit the program"""
		return True

	def do_EOF(self, arg=[]):
		"""handle EOF to exit command"""
		print()
		return True

	def do_cir(self, arg=[]):
		print(self.cir)

	def do_reset(self, arg=[]):
		self.cir = Circuit()
		self.net = []
		self.res = None

	def do_rem(self, arg):
		"""remove component (usage: rem componant)"""
		if len(arg) == 0:
			print('usage: rem componant')
			return (False)
		found = 0
		for com in self.net:
			if com[0] == arg:
				self.net.remove(com)
				self.cir.remove_elem(com[0])
				found = 1
				break
		if not found:
			print('component not found')
			return (False)

	def show_image(self, image, name=None):
		cv2.imshow(name, image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()  # Close the window after the image is displayed

	def display_image_thread(self, image, name=None):
		#thread = threading.Thread(target=self.show_image, args=(image,name,))
		#thread.start()
		#process = multiprocessing.Process(target=self.show_image, args=(image,name,))
		#process.start()
		pass

	def do_detect(self, arg, itrateValue=1):
		self.do_reset()
		res = LiveDetect()
		net = []

		if len(res['circuit']) == 0:
			print("No circuit detected")
			return (False)

		self.display_image_thread(res['srcScale'], '1')
		#time.sleep(2)
		#self.display_image_thread(res['grayScale'], '2')

		if itrateValue:
			ItrateCircValue(res['circuit'])
		for comp in res['circuit']:
			net.append(str(comp))
		BuildCirc(net, self)

	def do_add(self, arg):
		"""add element to circuit with netlest"""
		if (not len(arg)):
			print('No comp is given')
			return (False)

		net = parse(arg)
		comp = net[0][0]

		if comp not in COMP_MAPING:
			print('Component not found')
			return (False)

		for com in self.net:
			if net[0] == com[0]:
				self.do_rem(net[0])
				break

		COMP_MAPING[comp](net, self.cir)
		self.net.append(net)

	def do_run(self, arg):
		""" run simmulation:
			usage: run (opration) ->
			op :> simple dc opration
		"""
		op = parse(arg)

		if len(arg) == 0:
			print("usage: run (opration)")
			return (False)

		res = runCir(op, self.cir)
		self.res = (op[0], res)
	
	def do_res(self, arg=[]):
		if self.res == None:
			print("No Result Is here")
			return(False)
		arg = parse(arg)

		RES_OP[self.res[0]](arg)
		#tr = threading.Thread(target=RES_OP[self.res[0]], args=(arg,))
		#tr.start()

		

def parse(arg=""):
	return arg.split()

def ItrateCircValue(circuit):
	for comp in circuit:
		name = f'{comp.com_type}{comp.index}'
		comp.value = input(f'{name}: ')

def BuildCirc(net:[], cm:SimulationCommand):
	for comp in net:
		cm.do_add(comp)

if __name__ == '__main__':
	sim = SimulationCommand()
	sim.cmdloop()
