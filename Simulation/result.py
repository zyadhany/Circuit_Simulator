from helper import *
import threading

def ResOP(arg=[]):
    tex = TextDisplay()
    tex.display_text('tmp/tmp_new_op.opinfo')
    pass

def ResAc(arg=[]):
    tex = TextDisplay()
    thread = threading.Thread(target=tex.display_text, args=('tmp/tmp_new_op.opinfo',))
    thread.start()
    pass

RES_OP = {'op':ResOP, 'ac':ResAc}