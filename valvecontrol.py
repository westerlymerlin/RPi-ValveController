"""
Main valve controller module, operates the valves via the Raspberry Pi GPIO
"""

from time import sleep
from threading import Timer
import os
from RPi import GPIO
from logmanager import logger
from settings import VERSION



logger.info('Application starting')
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
channellist = [23, 17, 13, 19, 18, 27, 9, 24, 22, 11, 21, 26, 20]
GPIO.setup(channellist, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

valves = [
    {
        'id': 1,
        'gpio': channellist[0],
        'description': '4He pipette input',
        'excluded': 2
    },
    {
        'id': 2,
        'gpio': channellist[1],
        'description': '4He pipette output',
        'excluded': 1
    },
    {
        'id': 3,
        'gpio': channellist[2],
        'description': '3He pipette output',
        'excluded': 4
    },
    {
        'id': 4,
        'gpio': channellist[3],
        'description': '3He pipette input',
        'excluded': 3
    },
    {
        'id': 5,
        'gpio': channellist[4],
        'description': 'port 1',
        'excluded': 8
    },
    {
        'id': 6,
        'gpio': channellist[5],
        'description': 'ion pump',
        'excluded': 5
    },
    {
        'id': 7,
        'gpio': channellist[6],
        'description': 'gas analyser',
        'excluded': 5
    },
    {
        'id': 8,
        'gpio': channellist[7],
        'description': 'gallery A',
        'excluded': 5
    },
    {
        'id': 10,
        'gpio': channellist[8],
        'description': 'laser cell',
        'excluded': 5
    },
    {
        'id': 11,
        'gpio': channellist[9],
        'description': 'getter',
        'excluded': 5
    },
    {
        'id': 12,
        'gpio': channellist[10],
        'description': 'buffer tank',
        'excluded': 5
    },
    {
        'id': 13,
        'gpio': channellist[11],
        'description': 'turbo pump',
        'excluded': 5
    }
]


def parsecontrol(item, command):
    """Parser that recieves messages from the API or web page posts and directs
    messages to the correct function"""
    # print('%s : %s' % (item, command))
    try:
        if item[:5] == 'valve':
            valve = int(item[5:])
            if 0 < valve < 14:
                if command == 'open':
                    valveopen(valve)
                elif command == 'close':
                    valveclose(valve)
                else:
                    logger.warning('bad valve command')
            else:
                logger.warning('bad valve number')
        elif item[:7] == 'pipette':
            pipette = int(item[7:])
            if pipette == 1:
                if command == 'load':
                    he4pipetteload()
                elif command == 'unload':
                    he4pipetteunload()
                elif command == 'close':
                    he4pipetteclose()
                else:
                    logger.warning('bad pipette command')
            elif pipette == 2:
                if command == 'load':
                    he3pipetteload()
                elif command == 'unload':
                    he3pipetteunload()
                elif command == 'close':
                    he3pipetteclose()
                else:
                    logger.warning('bad pipette command')
            else:
                logger.warning('bad pipette number')
        elif item == 'closeallvalves':
            allclose()
        elif item == 'restart':
            if command == 'pi':
                logger.warning('Restart command recieved: system will restart in 15 seconds')
                timerthread = Timer(15, reboot)
                timerthread.start()
    except ValueError:
        logger.warning('incorrect json message')
    except IndexError:
        logger.warning('bad valve number')


def valveopen(valveid):
    """Open the valve specified"""
    valve = [valve for valve in valves if valve['id'] == valveid]
    if GPIO.input([valvex for valvex in valves if valvex['id'] == valve[0]['excluded']][0]['gpio']) == 1:
        logger.warning('cannot open valve as the excluded one is also open valve %s', valveid)
    else:
        GPIO.output(valve[0]['gpio'], 1)
        logger.info('Valve %s opened', valveid)


def valveclose(valveid):
    """Close the valve specified"""
    valve = [valve for valve in valves if valve['id'] == valveid]
    GPIO.output(valve[0]['gpio'], 0)
    logger.info('Valve %s closed', valveid)


def allclose():
    """Close all valves"""
    GPIO.output(channellist, 0)
    logger.info('All Valves Closed')


def he3pipetteload():
    """load the 3He pipette"""
    valveclose(3)
    sleep(1)
    valveopen(4)


def he3pipetteclose():
    """Close the 3He Pipette"""
    valveclose(3)
    valveclose(4)


def he3pipetteunload():
    """Unload the 3He pipette"""
    valveclose(4)
    sleep(1)
    valveopen(3)


def he4pipetteload():
    """Load the 4He pipette"""
    valveclose(2)
    sleep(1)
    valveopen(1)


def he4pipetteclose():
    """Close the 4He pipette"""
    valveclose(2)
    valveclose(1)


def he4pipetteunload():
    """Unload the 4He pipette"""
    valveclose(1)
    sleep(1)
    valveopen(2)


def status(value):
    """Meaningful value name for the specified valve"""
    if value == 0:
        return 'closed'
    else:
        return 'open'



def valvestatus():
    """Return the status of all valves as a jason message"""
    statuslist = []
    for valve in valves:
        if valve['id'] > 0:
            statuslist.append({'valve': valve['id'], 'status': status(GPIO.input(valve['gpio']))})
    return statuslist


def httpstatus():
    """Statud message formetted for the web status page"""
    statuslist = []
    for valve in valves:
        if valve['id'] > 0:
            statuslist.append({'id': valve['id'], 'description': valve['description'],
                               'status': status(GPIO.input(valve['gpio']))})
    return statuslist


def reboot():
    """API call to reboot the Raspberry Pi"""
    logger.warning('System is restarting now')
    os.system('sudo reboot')


GPIO.output(12, 1)   # set ready
logger.info('Running version %s', VERSION)
logger.info('Application ready')
