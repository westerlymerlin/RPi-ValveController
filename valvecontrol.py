"""
Raspberry Pi Valve Control System

This module provides a comprehensive interface for controlling and monitoring laboratory
valves via Raspberry Pi GPIO pins. It implements safety interlocks to prevent conflicting
valve states, handles system commands, and provides status monitoring capabilities.

Features:
- Individual valve control (open/close) with conflict prevention
- Batch operations (close all valves)
- System control commands (restart)
- Status reporting for monitoring
- Logging of all valve operations and errors

The module initializes GPIO pins, defines valve configurations with their relationships,
and provides functions for valve manipulation through a consistent interface.

Dependencies:
- RPi.GPIO: For hardware control of GPIO pins
- threading.Timer: For delayed execution of commands
- logmanager: For operational logging
"""

from threading import Timer
import os
from RPi import GPIO
from logmanager import logger


logger.info('Application starting')
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
channellist = [23, 17, 13, 19, 18, 27, 9, 24, 22, 11, 21, 26, 20, 12]
GPIO.setup(channellist, GPIO.OUT)
GPIO.output(channellist, 0)

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
        'excluded': 1
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
    """
    Parses and executes control instructions for items such as valves or system commands.

    This function handles control commands for items (e.g., valves) by executing
    the corresponding actions (opening, closing, restarting, etc.). It utilizes specific
    rules to process the commands and takes recovery measures in case of invalid inputs
    or errors.

    Parameters:
    item : str
        Specifies the name of the control item (e.g., 'valve1', 'closeallvalves', 'restart').
    command : str
        Provides the command to execute for the given item (e.g., 'open', 'close', 'pi').

    Raises:
    ValueError
        If the conversion of values such as valve number fails.
    IndexError
        If accessing an invalid index during item processing.
    """
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
        elif item == 'closeallvalves':
            allclose()
        elif item == 'restart':
            if command == 'pi':
                logger.warning('Restart command received: system will restart in 15 seconds')
                timerthread = Timer(15, reboot)
                timerthread.start()
    except ValueError:
        logger.warning('incorrect json message')
    except IndexError:
        logger.warning('bad valve number')


def valveopen(valveid):
    """
    Opens a valve based on its unique identifier if no conflicting valve is open.

    Attempts to open the valve identified by the provided valve ID. Before opening,
    it checks whether the valve marked as excluded for the specified valve is already open.
    If the excluded valve is open, the operation is aborted, logging a warning.
    If no conflict is found, the specified valve is opened, and this action is logged.

    Parameters:
        valveid (int): The unique identifier of the valve to be opened.
    """
    valve = [valve for valve in valves if valve['id'] == valveid]
    if GPIO.input([valvex for valvex in valves if valvex['id'] == valve[0]['excluded']][0]['gpio']) == 1:
        logger.warning('cannot open valve as the excluded one is also open valve %s', valveid)
        if valve[0]['excluded'] != 5:
            return
    GPIO.output(valve[0]['gpio'], 1)
    logger.info('Valve %s opened', valveid)


def valveclose(valveid):
    """
    Closes the specified valve based on its ID.

    The function identifies the valve with the given ID in the list of valves,
    ensures that the valve's GPIO pin is set to a low state, and logs the
    operation. This action effectively closes the valve. The provided valve
    ID should match an existing valve's ID within the list.

    Parameters:
        valveid (int): The ID of the valve to be closed.
    """
    valve = [valve for valve in valves if valve['id'] == valveid]
    GPIO.output(valve[0]['gpio'], 0)
    logger.info('Valve %s closed', valveid)


def allclose():
    """
    Close all valves by setting the output of the specified channels to 0.

    Summary:
    This function outputs a signal of 0 to all channels specified in the
    'channellist', effectively closing all valves. It also logs an info
    message indicating the operation.

    Parameters:
    channellist : list
        A list of GPIO channel numbers on which the output will be set to 0.

    Returns:
    None
    """
    GPIO.output(channellist, 0)
    logger.info('All Valves Closed')

def status(value):
    """
    Determines the status based on a given value.

    This function evaluates the provided integer value and returns a corresponding
    status string. Specifically, it checks whether the value equals zero to
    determine if the status is 'closed'. Any other value results in a status
    of 'open'.

    Parameters:
    value (int): The value to evaluate for determining the status.

    Returns:
    str: A string representing the status. Returns 'closed' if the value is
    0; otherwise, returns 'open'.
    """
    if value == 0:
        return 'closed'
    return 'open'



def valvestatus():
    """
    Determines the status of valves based on their GPIO input.

    This function iterates through a list of valves, checks each valve's GPIO
    input status, and compiles a list of dictionaries containing the valve ID
    and its respective status.

    Returns:
        list[dict]: A list where each dictionary contains the ID of a valve and
        its corresponding status, based on GPIO input.
    """
    statuslist = []
    for valve in valves:
        if valve['id'] > 0:
            statuslist.append({'valve': valve['id'], 'status': status(GPIO.input(valve['gpio']))})
    return statuslist


def httpstatus():
    """
    Determine and return the status of a list of valves based on their GPIO input.

    This function iterates through a list of valve objects, checks each valve's GPIO
    input to determine its status and then constructs a list of dictionaries containing
    the valve's ID, description, and current status.

    Returns:
        list[dict]: A list of dictionaries each containing the valve's `id` (int),
        `description` (str), and its current `status` (bool or other relevant type
        returned by the `status` function).
    """
    statuslist = []
    for valve in valves:
        if valve['id'] > 0:
            statuslist.append({'id': valve['id'], 'description': valve['description'],
                               'status': status(GPIO.input(valve['gpio']))})
    return statuslist


def reboot():
    """
    Reboots the local machine.

    This function logs a warning message indicating that the system is about to restart
    and then executes a system command to initiate a reboot.

    Raises:
        This function does not explicitly raise any exceptions, but it depends on the
        behavior of the underlying operating system and might fail in environments
        without sufficient permissions.

    """
    logger.warning('System is restarting now')
    os.system('sudo reboot')


GPIO.output(12, 1)   # set ready
logger.info('Application ready')
