import serial,time
from plx_gpib_ethernet import *


class control():
    """This class implements the methods to control the Cryocon temperature controller"""
    def __init__(self):
        ''' Constructor for this class. '''
        self.__adapter = 0

    def __del__(self):
        ''' Destructor for this class. '''
        if self.__is_open:
            self.close()


    def open(self, ip='169.254.128.218', gpib=12):
        """ Open connection to GPIB adapter and creates a socket
                :param ip: IP address of the GPIB adapter. Default='169.254.128.218'
                :param gpib: GPIB address of the Cryocon Controller. Default=12
                :returns Boolean value True or False """
        self.__adapter = PrologixGPIBEthernet(ip)
        self.__gpib = gpib
        self.__is_open = self.__adapter.connect()
        return self.__is_open

    def close(self):
        """ Close socket """
        self.__adapter.close()

    def send_cmd(self,cmd):
        """ Send command to the GPIB device
                :param cmd: string which gets send to device'
                :returns answer from device in string format """
        try:
            self.__adapter.select(gpib)
            return self.__adapter.query(cmd)

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"

    def disable(self):
        """ Disable the temperature stabilisation PID loop
                :returns The status of the Cryocon PID loop """
        try:
            self.__adapter.select(gpib)
            return self.__adapter.query('STOP')

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"


    def enable(self):
        """ Enable the temperature stabilisation PID loop
                :returns The status of the Cryocon PID loop """
        try:
            self.__adapter.select(gpib)
            return self.__adapter.query('CONT')

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"

    def status(self):
        """ Requests the status of the Cryocon PID loop
                :returns The status of the Cryocon PID loop: ON or OFF"""
        try:
            self.__adapter.select(gpib)
            return self.__adapter.query('CONT?')

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"

    def set_setpoint(self,temp):
        """ Set the setpoint temperature of the control loop
                :param temp: setpoint temperature in Kelvin eg.: 15.4'
                :returns The setpoint temperature in Kelvin"""
        try:
            self.__adapter.select(gpib)
            return self.__adapter.query('LOOP 1:SETPT '+temp)

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"

    def read_setpoint(self):
        """ Requests the setpoint temperature of the control loop
                :returns The setpeoint temperature in Kelvin """
        try:
            self.__adapter.select(gpib)
            return self.__adapter.query('LOOP 1:SETPT?')

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"

    def read_sensor_temperature(self):
        """ Requests the temperature value of the sensor
                :returns The actual temperature value of the sensor in Kelvin """
        try:
            self.__adapter.select(gpib)
            return self.__adapter.query('INPUT? A')

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"


    def read_frimware_version(self):
        """ Request the firmware version of the Cryocon temperature controller
                :returns firmware version  """
        try:
            self.__adapter.select(gpib)
            return self.__adapter.query('SYSTEM:FWREV?')

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"
