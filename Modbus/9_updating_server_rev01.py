#!/usr/bin/env python3
# pylint: disable=missing-any-param-doc,differing-param-doc
"""Pymodbus Server With Updating Thread.

This is an example of having a background thread updating the
context while the server is operating. This can also be done with
a python thread::

    from threading import Thread
    Thread(target=updating_writer, args=(context,)).start()
"""
from threading import Thread
import time
import logging
import re
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusServerContext,
    ModbusSlaveContext,
)
from pymodbus.device import ModbusDeviceIdentification
# from pymodbus.server.asynchronous import StartSerialServer
from pymodbus.version import version


# --------------------------------------------------------------------------- #
# configure the service logging
# --------------------------------------------------------------------------- #
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# --------------------------------------------------------------------------- #
# define your callback process
# --------------------------------------------------------------------------- #


def updating_writer(extra):
    """Run for tests
    :param arguments: The input arguments to the call
    """
    print("Check register")
    slave_id = 0x1
    value = context[slave_id].getValues(0x3, 3001, count=1)

    time.sleep(5)
    while value[0] != 0:
        value = context[slave_id].getValues(0x3, 3001, count=1)
        time.sleep(5)
    context[slave_id].setValues(0x6, 1000, [0x10])

if __name__ == "__main__":

    datablock=ModbusSequentialDataBlock(0x00, [0x00] * 3100)
    context={
        0x01: ModbusSlaveContext(
            hr=datablock,
        ),
        0xF8: ModbusSlaveContext(
            hr=datablock,
        ),
    }
    store = ModbusServerContext(slaves=context, single=False)

    Thread(target=updating_writer, args=(store,)).start()