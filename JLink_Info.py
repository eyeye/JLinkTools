#-*- coding:utf-8 -*-

__author__ = 'YangZhiyong'

print '杨志勇'

import sys, os, subprocess
import time


JLINK_EXE       = r'G:\Program Files\SEGGER\JLinkARM_V464a\JLink.exe'
JLINK_SCRIPT    = r'jlink.script'
DEVIDE          = r'LPC1768'
INTERFACE       = r'SWD'
SPEED           = r'500'



def reset():
    print 'reset'
    pass


def program():
    print 'program'
    pass



def erase():
    print 'erase'
    pass

def gdbserver():
    print 'gdbserver'
    pass







command = [
    JLINK_EXE,
    '-If', INTERFACE,
    '-Speed', SPEED,
    '-CommanderScript', JLINK_SCRIPT,
    '-Device', DEVIDE
];

sp = subprocess.Popen(command,
                      stdout=subprocess.PIPE,
                      stdin=subprocess.PIPE,
                      stderr=subprocess.PIPE)

print 'PID: %r' % sp.pid
print 'RET CODE: %r' % sp.returncode
print 'wait'
sp.wait()

out, err =  sp.communicate()

print out #repr(out)

sp.wait()

print 'Finished'

# print sp.stdout.read()

if __name__ == '__main__':
    print 'startup.........................'
    cmd = raw_input(
        '''
        1 - reset
        2 - program
        3 - erase
        4 - gdbserver
        ''')

    print cmd

    if cmd == '1':
        reset()
    elif cmd == '2':
        program()
    elif cmd == '3':
        erase()
    elif cmd == '4':
        gdbserver()
    else:
        print 'none cmd'
