#-*- coding:utf-8 -*-

__author__ = 'YangZhiyong'

print '杨志勇'

import sys, os, subprocess
import time
import platform

if platform.system() == 'Darwin':
    print 'OSX Config'
    JLINK_EXE = r'JLinkExe'
    JLINK_DIR = r'/Users/EYE/Dev/JLink_MacOSX_V462a/'
    JLINK_SCRIPT = r'jlink.script'

    sys.path.append(JLINK_DIR)
    os.environ['DYLD_LIBRARY_PATH'] = JLINK_DIR

else:
    print 'Windows Config'
    JLINK_EXE = r'G:\Program Files\SEGGER\JLinkARM_V464a\JLink.exe'
    JLINK_SCRIPT = r'jlink.script'


DEVIDE          = r'NRF51822'
INTERFACE       = r'SWD'
SPEED           = r'500'






def reset():
    print 'reset'

    command = [
    JLINK_DIR + JLINK_EXE,
    '-If', INTERFACE,
    '-Speed', SPEED,
    '-CommanderScript', JLINK_SCRIPT,
    '-Device', DEVIDE
]
    sp = subprocess.Popen(command,
                          stdout=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          stderr=subprocess.PIPE)

    # print sp.stdout.read()
    print 'PID: %r' % sp.pid
    print 'RET CODE: %r' % sp.returncode
    print 'wait'
    sp.wait()

    out, err =  sp.communicate()

    print 'STDOUT: ' + out
    print 'STDERR: ' + err

    sp.wait()

    print 'Finished'



def program():
    print 'program'

    command = [
    JLINK_DIR + JLINK_EXE,
    '-If', INTERFACE,
    '-Speed', SPEED,
    '-CommanderScript', r'program.script',
    '-Device', DEVIDE
    ]

    sp = subprocess.Popen(command,
                          stdout=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          stderr=subprocess.PIPE)

    # print sp.stdout.read()
    print 'PID: %r' % sp.pid
    print 'RET CODE: %r' % sp.returncode
    print 'wait'
    sp.wait()

    out, err =  sp.communicate()

    print 'STDOUT: ' + out
    print 'STDERR: ' + err

    sp.wait()

    print 'Finished'
    pass



def erase():
    print 'erase'
    pass


def gdbserver():
    print 'gdbserver'
    pass






# sp = subprocess.Popen(command,
#                       stdout=subprocess.PIPE,
#                       stdin=subprocess.PIPE,
#                       stderr=subprocess.PIPE)
#
# print 'PID: %r' % sp.pid
# print 'RET CODE: %r' % sp.returncode
# print 'wait'
# sp.wait()
#
# out, err =  sp.communicate()
#
# print out #repr(out)
#
# sp.wait()
#
# print 'Finished'

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
