__author__ = 'EYE'

import sys, os
import platform

if platform.system() == 'Darwin':
    print 'OSX Config'
    JLINK_EXE = r'JLinkExe'
    JLINK_DIR = r'/Users/EYE/Dev/JLink_MacOSX_V462a/'
    JLINK_SCRIPT = r'jlink.script'
    SOFTDEVICE_FILE = r'/Volumes/OSX ML/Users/EYE/workspace/Nordic/s110_nrf51822_5.1.0/s110_nrf51822_5.1.0_softdevice.hex'

    sys.path.append(JLINK_DIR)
    os.environ['DYLD_LIBRARY_PATH'] = JLINK_DIR

else:
    print 'Windows Config'
    JLINK_EXE = r'JLink.exe'
    JLINK_DIR = r'G:\Program Files\SEGGER\JLinkARM_V464a\\'
    JLINK_SCRIPT = r'jlink.script'
    SOFTDEVICE_FILE = r'G:\Nordic Semiconductor\s110_nrf51822_5.1.0\s110_nrf51822_5.1.0_softdevice.hex'

DEVIDE          = r'NRF51822'
INTERFACE       = r'SWD'
SPEED           = r'500'

BIN_FILE = r'/Volumes/OSX ML/Users/EYE/workspace/eclipse_cdt/OSX_GNUARM_Test/Debug/OSX_GNUARM_Test.hex'

__all__ = [JLINK_DIR, JLINK_EXE, BIN_FILE, DEVIDE, INTERFACE, SPEED, SOFTDEVICE_FILE]


