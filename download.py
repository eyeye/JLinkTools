#-*- coding:utf-8 -*-
__author__ = 'EYE'

import os
import config
import subprocess


ScriptTemplate = '''
power on
r
Sleep 100
loadbin $BIN$ 0x00014000
verifybin $BIN$ 0x00014000
r
Sleep 100
g
q
'''



def download():
    print u'下载程序'
    print os.getcwd()

    scriptPath = os.getcwd() + r'/scripts'

    if not os.path.exists(scriptPath):
        print u'创建scripts文件夹'
        os.mkdir(scriptPath)

    binPath, binFile = os.path.split(config.BIN_FILE)
    binName, binExt  = os.path.splitext(binFile)

    print binPath, binFile, binName, binExt

    if not os.path.exists(config.BIN_FILE):
        print u'文件不存在：', config.BIN_FILE
        return

    scriptFileName = 'download_' + binName + '.script'
    scriptFilePathName = scriptPath + '/' + scriptFileName

    if not os.path.exists(scriptFilePathName):
        print u'创建script文件'
        scriptFile = open(scriptFilePathName, 'w')
        scriptFile.close()

    scriptFile = open(scriptFilePathName)
    scriptFileText = scriptFile.read()
    scriptFile.close()

    ScriptText = ScriptTemplate.replace('$BIN$', '\"' + config.BIN_FILE + '\"')

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
    download()


