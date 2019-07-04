import serial,time,numpy,re,time



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
                :returns unicode: response of device """
        try:
            self.__adapter.select(self.__gpib)
            return self.__adapter.query(cmd)

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()\r Or device did not send a reply!!!"

    def disable(self):
        """ Disable the temperature stabilisation PID loop
                :returns string: The status of the Cryocon PID loop """
        try:
            self.__adapter.select(self.__gpib)
            self.__adapter.write('STOP')
            return str(self.__adapter.query('CONT?'))

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"


    def enable(self):
        """ Enable the temperature stabilisation PID loop
                :returns string: The status of the Cryocon PID loop """
        try:
            self.__adapter.select(self.__gpib)
            self.__adapter.write('CONT')
            return str(self.__adapter.query('CONT?'))

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"

    def status(self):
        """ Requests the status of the Cryocon PID loop
                :returns string: The status of the Cryocon PID loop: ON or OFF"""
        try:
            self.__adapter.select(self.__gpib)
            return str(self.__adapter.query('CONT?'))

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"

    def set_setpoint(self,temp):
        """ Set the setpoint temperature of the control loop
                :param temp: setpoint temperature in Kelvin eg.: 15.4'
                :returns float: The setpoint temperature in Kelvin"""
        try:
            self.__adapter.select(self.__gpib)
            self.__adapter.write('LOOP 1:SETPT ' + str(temp))
            payload=self.__adapter.query('LOOP 1:SETPT?')
            return numpy.float64(re.findall("\d+\.\d+", payload))[0]

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"

    def read_setpoint(self):
        """ Requests the setpoint temperature of the control loop
                :returns float: The setpeoint temperature in Kelvin """
        try:
            self.__adapter.select(self.__gpib)
            payload=self.__adapter.query('LOOP 1:SETPT?')
            return numpy.float64(re.findall("\d+\.\d+", payload))[0]

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"

    def read_sensor_temperature(self):
        """ Requests the temperature value of the sensor
                :returns float: The actual temperature value of the sensor in Kelvin """
        try:
            self.__adapter.select(self.__gpib)
            return  numpy.float64(re.findall("\d+\.\d+", self.__adapter.query('INPUT? A')))[0]

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"


    def read_frimware_version(self):
        """ Request the firmware version of the Cryocon temperature controller
                :returns float: firmware version  """
        try:
            self.__adapter.select(self.__gpib)
            return numpy.float64(re.findall("\d+\.\d+", self.__adapter.query('SYSTEM:FWREV?')))[0]

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"

    def status_range(self):
        """ Requests the status of the Cryocon PID output power setting
                :returns string: The status of the Cryocon output power setting: LOW, MID, HI"""
        try:
            self.__adapter.select(self.__gpib)
            return str(self.__adapter.query('LOOP 1:RANGE?'))

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"

    def set_range_mid(self):
        """ Set the the Cryocon PID output power to MID (5.0W)
                :returns string: The status of the Cryocon output power setting: LOW, MID, HI"""
        try:
            self.__adapter.select(self.__gpib)
            self.__adapter.write('LOOP 1:RANGE MID')
            return str(self.__adapter.query('LOOP 1:RANGE?'))

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"

    def set_range_low(self):
        """ Set the the Cryocon PID output power to LOW (0.5W)
                :returns string: The status of the Cryocon output power setting: LOW, MID, HI"""
        try:
            self.__adapter.select(self.__gpib)
            self.__adapter.write('LOOP 1:RANGE LOW')
            return str(self.__adapter.query('LOOP 1:RANGE?'))

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"
