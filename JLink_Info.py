#-*- coding:utf-8 -*-

__author__ = 'YangZhiyong'

print '杨志勇'

import sys, os, subprocess
import time


JLINK_UPLOAD = '''
power on
r
loadbin %BIN% 0x00014000
r
q
'''


JLINK_EXE = r'G:\Program Files\SEGGER\JLinkARM_V464a\JLink.exe'
JLINK_SCRIPT = r'jlink.script'

print time.time()

sp = subprocess.Popen([JLINK_EXE, JLINK_SCRIPT],
                      stdout=subprocess.PIPE,
                      stdin=subprocess.PIPE,
                      stderr=subprocess.PIPE)


# print sp.pid
print sp.returncode
# print sp

# time.sleep(5)
sp.wait()
print 'wait'

# print sp.stdout.read()
# print sp.stdin.read()
# print sp.stderr.read()
#
# sp.stdin.write('q')

print sp.communicate()

sp.wait()

print 'Finished'

# print sp.stdout.read()
