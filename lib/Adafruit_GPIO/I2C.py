import os
import machine
from ustruct import unpack
from array import array

class Device(object):
    """Class for communicating with an I2C device using the adafruit-pureio pure
    python smbus library, or other smbus compatible I2C interface. Allows reading
    and writing 8-bit, 16-bit, and byte array values to registers
    on the device."""
    def __init__(self, address, i2c_interface):
        """Create an instance of the I2C device at the specified address on the
        specified I2C bus number."""
        self._address = address

        if i2c_interface is None:
            # Use pure python I2C interface if none is specified.
            from machine import I2C
            self._bus = I2C(0, I2C.MASTER, baudrate=100000)
        else:
            # Otherwise use the provided class to create an smbus interface.
            self._bus = i2c_interface

    def writeRaw8(self, value):
        """Write an 8-bit value on the bus (without register)."""
        value = value & 0xFF
        self._bus.writeto(self._address, value)

    def write8(self, register, value):
        """Write an 8-bit value to the specified register."""
        value = value & 0xFF
        self._bus.writeto_mem(self._address, register, value)

    def write16(self, register, value):
        """Write a 16-bit value to the specified register."""
        value = value & 0xFFFF
        self._bus.writeto_mem(self._address, register, value)

    def writeList(self, register, data):
        """Write bytes to the specified register."""
        self._bus.writeto_mem(self._address, register, data)

    def readList(self, register, length):
        """Read a length number of bytes from the specified register.  Results will be returned as a bytearray."""
        return self._bus.readfrom_mem(self._address, register, length)

    def readRaw8(self):
        """Read an 8-bit value on the bus (without register)."""
        return self._bus.readfrom(self._address, 1)

    def readU8(self, register):
        """Read an unsigned byte from the specified register."""
        return unpack("B",self._bus.readfrom_mem(self._address, register, 1))[0]

    def readS8(self, register):
        """Read a signed byte from the specified register."""
        return unpack("b",self._bus.readfrom_mem(self._address, register, 1))[0]

    def readU16(self, register):
        """Read an unsigned 16-bit value from the specified register, with the specified endianness (default little endian, or least significant byte first)."""
        return unpack("H",self._bus.readfrom_mem(self._address, register, 2))[0]

    def readS16(self, register):
        """Read a signed 16-bit value from the specified register, with the specified endianness (default little endian, or least significant byte first)."""
        return unpack("h",self._bus.readfrom_mem(self._address, register, 2))[0]

    def readU16LE(self, register):
        """Read an unsigned 16-bit value from the specified register, in little endian byte order."""
        return unpack("<H",self._bus.readfrom_mem(self._address, register, 2))[0]

    def readU16BE(self, register):
        """Read an unsigned 16-bit value from the specified register, in big endian byte order."""
        return unpack(">H",self._bus.readfrom_mem(self._address, register, 2))[0]

    def readS16LE(self, register):
        """Read a signed 16-bit value from the specified register, in little endian byte order."""
        return unpack("<h",self._bus.readfrom_mem(self._address, register, 2))[0]

    def readS16BE(self, register):
        """Read a signed 16-bit value from the specified register, in big endian byte order."""
        return unpack(">h",self._bus.readfrom_mem(self._address, register, 2))[0]

    def readU32(self, register):
        """Read an unsigned 32-bit value from the specified register, with the specified endianness (default little endian, or least significant byte first)."""
        return unpack("L",self._bus.readfrom_mem(self._address, register, 4))[0]

    def readS32(self, register):
        """Read a signed 32-bit value from the specified register, with the specified endianness (default little endian, or least significant byte first)."""
        return unpack("l",self._bus.readfrom_mem(self._address, register, 4))[0]

    def readU32LE(self, register):
        """Read an unsigned 32-bit value from the specified register, in little endian byte order."""
        return unpack("<L",self._bus.readfrom_mem(self._address, register, 4))[0]

    def readU32BE(self, register):
        """Read an unsigned 32-bit value from the specified register, in big endian byte order."""
        return unpack(">L",self._bus.readfrom_mem(self._address, register, 4))[0]

    def readS32LE(self, register):
        """Read a signed 32-bit value from the specified register, in little endian byte order."""
        return unpack("<l",self._bus.readfrom_mem(self._address, register, 4))[0]
 
    def readS32BE(self, register):
        """Read a signed 32-bit value from the specified register, in big endian byte order."""
        return unpack(">l",self._bus.readfrom_mem(self._address, register, 4))[0]
