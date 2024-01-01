#!/usr/bin/python3

"""Simulation console."""

import cmd
from Simulation import *


class SimulationCommand(cmd.Cmd):
	prompt = '(SAGED): '
	cir = Circuit()
	net = []

	def emptyline(self):
		pass

	def do_quit(self, arg):
		"""Quit command to exit the program"""
		return True

	def do_EOF(self, arg):
		"""handle EOF to exit command"""
		print()
		return True
	
	def do_cir(self, arg):
		print(self.cir)
	
	def do_reset(self, arg):
		self.cir = Circuit()
		self.net = []

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
		print(res[op[0]])

def parse(arg=""):
	return arg.split()

if __name__ == '__main__':
	SimulationCommand().cmdloop()
