#-*- coding:utf-8 -*-
__author__ = 'YangZhiyong'

from intelhex import IntelHex
import os
import config
import subprocess

def separate():

    softdeviceDir = os.getcwd() + r'/softdevice/'

    if not os.path.exists(softdeviceDir):
        print u'创建softdevice文件夹'
        os.mkdir(softdeviceDir)

    # softdeviceFileDir, softdeviceFileName = os.path.split(config.SOFTDEVICE_FILE)
    # softdeviceFileName, softdeviceFileExt = os.path.splitext(softdeviceFileName)

    # mianFileName = softdeviceDir + softdeviceFileName + '_main.bin'
    # uicrFileName = softdeviceDir + softdeviceFileName + '_uicr.bin'

    mianFileName = softdeviceDir + 'softdevice_main.bin'
    uicrFileName = softdeviceDir + 'softdevice_uicr.bin'

    softdeviceFile = IntelHex(config.SOFTDEVICE_FILE)

    softdeviceFile.tobinfile(fobj=mianFileName, start=0, size=80*1024)
    softdeviceFile.tobinfile(fobj=uicrFileName, start=0x10001000, size=0x20)


ScriptTemplate = '''
# JLinkExe script for resetting nrf51822
power on
Sleep 1000
st
speed 1000
# reset the device
r
Sleep 500
# NVIC CONFIG EEN (erase enabled)
w4 4001e504 2
# NVIC ERASEALL (erase all flash including UICR)
w4 4001e50c 1
r
# NVIC CONFIG WEN (enable writing)
w4 4001e504 1
# load the soft device binary.
loadbin $UICR_BIN$ 0x10001000
verifybin $UICR_BIN$ 0x10001000
loadbin $MAIN_BIN$ 0
verifybin $MAIN_BIN$ 0
r
q
'''



def download():
    print u'下载程序'
    print os.getcwd()

    scriptDir = os.getcwd() + r'/scripts'
    softdeviceDir = os.getcwd() + r'/softdevice/'

    if not os.path.exists(scriptDir):
        print u'创建scripts文件夹'
        os.mkdir(scriptDir)

    if not os.path.exists(softdeviceDir):
        print u'创建softdevice文件夹'
        os.mkdir(softdeviceDir)
    #
    # binPath, binFile = os.path.split(softdeviceDir + 'softdevice_main.bin')
    # binName, binExt  = os.path.splitext(binFile)

    mainBinFile = softdeviceDir + 'softdevice_main.bin'
    uircBinFile = softdeviceDir + 'softdevice_uicr.bin'

    # print binPath, binFile, binName, binExt

    if not os.path.exists(softdeviceDir + 'softdevice_main.bin'):
        print u'文件不存在：', config.BIN_FILE
        return

    if not os.path.exists(softdeviceDir + 'softdevice_uicr.bin'):
        print u'文件不存在：', config.BIN_FILE
        return

    scriptFilePathName = scriptDir + '/' + r'softdevice.script'

    if not os.path.exists(scriptFilePathName):
        print u'创建script文件'
        scriptFile = open(scriptFilePathName, 'w')
        scriptFile.close()

    scriptFile = open(scriptFilePathName)
    scriptFileText = scriptFile.read()
    scriptFile.close()

    ScriptText = ScriptTemplate.replace('$UICR_BIN$', '\"' + mainBinFile + '\"')
    ScriptText = ScriptText.replace('$MAIN_BIN$', '\"' + uircBinFile + '\"')

    if cmp(scriptFileText, ScriptText) != 0 :
        print u'更新文件内容:', ScriptText
        scriptFile = open(scriptFilePathName, 'w')
        scriptFile.write(ScriptText)
        scriptFile.close()
    else:
        print u'文件内容没有改变'


    command = [
    config.JLINK_DIR + config.JLINK_EXE,
    '-If', config.INTERFACE,
    '-Speed', config.SPEED,
    '-CommanderScript', scriptFilePathName,
    '-Device', config.DEVIDE
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



if __name__ == '__main__':
    separate()
    download()


