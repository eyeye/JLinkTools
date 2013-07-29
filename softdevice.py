#-*- coding:utf-8 -*-
__author__ = 'YangZhiyong'

from intelhex import IntelHex
import os
import config

def separate():

    softdeviceDir = os.getcwd() + r'/softdevice/'

    if not os.path.exists(softdeviceDir):
        print u'创建scripts文件夹'
        os.mkdir(softdeviceDir)

    softdeviceFileDir, softdeviceFileName = os.path.split(config.SOFTDEVICE_FILE)
    softdeviceFileName, softdeviceFileExt = os.path.splitext(softdeviceFileName)

    mianFileName = softdeviceDir + softdeviceFileName + '_main.bin'
    uicrFileName = softdeviceDir + softdeviceFileName + '_uicr.bin'

    softdeviceFile = IntelHex(config.SOFTDEVICE_FILE)
    softdeviceFile.tobinfile(fobj=mianFileName, start=0, size=80*1024)
    softdeviceFile.tobinfile(fobj=uicrFileName, start=0x10001000, size=0x20)

if __name__ == '__main__':
    separate()


