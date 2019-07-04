import serial,time
from plx_gpib_ethernet import *



#class com_error:
#    """This class implements the serial connection error function """
#    def check(self,response):
#
#        self.com_error_name = ['Invalid command', 'Command format incorrect', '<param> format incorrect', '<param> out of range','Sensor status error','Invalid error clear command']
#        self.com_error_value =['*F,01\r','*F,02\r','*F,03\r','*F,04\r','*F,05\r','*F,06\r']
#
#        for i in self.com_error_value:
#            if response == i:
#                print 'ERROR: '+ self.com_error_name[self.com_error_value.index(i)]
#                return
#        print 'Unknown ERROR!'
#        return


class control():
    """This class implements the methods to control the Cryocon temperature controller"""
    def __init__(self):
        ''' Constructor for this class. '''
        self.__adapter = 0

    def __del__(self):
        ''' Destructor for this class. '''
        if self.__is_open:
            self.close()


    def open(self, ip='169.254.128.218',socket_port=1235, gpib=12):
        """ Open connection to GPIB adapter and creates a socket
                :param ip: IP address of the GPIB adapter. Default='169.254.128.218'
                :param gpib: GPIB address of the Cryocon Controller. Default=12
                :param socket_port: Defines the socket port at which the GPIB adapter gets linked to. Default=1235
                :returns Boolean value True or False """
        self.__adapter = PrologixGPIBEthernet(ip,socket_port)
        self.__GPIB = gpib
        self.__is_open = self.__adapter.connect()
        self.__adapter.select(gpib)
        return self.__is_open

    def close(self):
        """ Close socket """
        self.__adapter.close()

    def send_cmd(self,cmd):
        """ Send string via serial connection
                :param cmd: string which gets send to device'
                :returns answer from device in string format """
        try:
            return self.__adapter.query(cmd)

        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"

    def read_frimware_version(self):
        """ Request the sensor value for the controller voltage
                :returns int  """
        try:
            self.__port.write('*RV\r')
            time.sleep(0.1)
            rec_str = self.__port.read(1024)
            p=rec_str.find('*S,')+3
            if p==2:
                self.check(rec_str)
                return 0
            else:
                return int(rec_str[p:len(rec_str)])/100.0
        except:
            print"ERROR no communication possible, check if the connection has been opened with open()"



# class sensor(com_error):
#     """This class implements sensor readout functions"""
#     def __init__(self,port):
#         ''' Constructor for this class. '''
#         self.__port=port
#
#     def __del__(self):
#         ''' Destructor for this class. '''
#
#
#
#
#     def enable_averaging(self):
#         """ This function enables the sensor averaging
#                 :returns Boolean True or False for command acknowledged """
#         self.__port.write('*AE\r')
#         time.sleep(0.1)
#         rec_str = self.__port.read(1024)
#         if rec_str=='*S\r':
#             return True
#         else:
#             return False
#
#     def disable_averaging(self):
#         """ This function disables the sensor averaging
#                 :returns Boolean True or False for command acknowledged """
#         self.__port.write('*AD\r')
#         time.sleep(0.1)
#         rec_str = self.__port.read(1024)
#         if rec_str=='*S\r':
#             return True
#         else:
#             return False
#
#
#     def contr_voltage(self):
#         """ Request the sensor value for the controller voltage
#                 :returns int  """
#         self.__port.write('*SS,00\r')
#         time.sleep(0.1)
#         rec_str = self.__port.read(1024)
#         p=rec_str.find('*S,00:')+6
#         if p==5:
#             self.check(rec_str)
#             return 0
#         else:
#             return int(rec_str[p:len(rec_str)])/100.0
#
#     def contr_current(self):
#         """ Request the sensor value for the controller current
#                 :returns int in mA """
#         self.__port.write('*SS,01\r')
#         time.sleep(0.1)
#         rec_str = self.__port.read(1024)
#         p=rec_str.find('*S,01:')+6
#         if p==5:
#             self.check(rec_str)
#             return 0
#         else:
#             return int(rec_str[p:len(rec_str)])/10.0
#
#     def contr_temperature(self):
#         """ Request the sensor value for the controller temperature
#                 :returns int in mA """
#         self.__port.write('*SS,02\r')
#         time.sleep(0.1)
#         rec_str = self.__port.read(1024)
#         p=rec_str.find('*S,02:')+6
#         if p==5:
#             self.check(rec_str)
#             return 0
#         else:
#             return int(rec_str[p:len(rec_str)])/10.0
#
#
#     def compressor_supply_pressure(self):
#         """ Request the sensor value for the compressor supply pressure
#                 :returns int in mA """
#         self.__port.write('*SS,03\r')
#         time.sleep(0.1)
#         rec_str = self.__port.read(1024)
#         p=rec_str.find('*S,03:')+6
#         if p==5:
#             self.check(rec_str)
#             return 0
#         else:
#             return int(rec_str[p:len(rec_str)])/10.0
#
#     def compressor_return_pressure(self):
#         """ Request the sensor value for the compressor return pressure
#                 :returns int in mA """
#         self.__port.write('*SS,04\r')
#         time.sleep(0.1)
#         rec_str = self.__port.read(1024)
#         p=rec_str.find('*S,04:')+6
#         if p==5:
#             self.check(rec_str)
#             return 0
#         else:
#             return int(rec_str[p:len(rec_str)])/10.0
#
#     def compressor_motor_temperature(self):
#         """ Request the sensor value for the motor capsule temperature
#                 :returns int in mA """
#         self.__port.write('*SS,05\r')
#         time.sleep(0.1)
#         rec_str = self.__port.read(1024)
#         p=rec_str.find('*S,05:')+6
#         if p==5:
#             self.check(rec_str)
#             return 0
#         else:
#             return int(rec_str[p:len(rec_str)])/10.0
#
#     def compressor_supply_temperature(self):
#         """ Request the sensor value for the helium supply temperature
#                 :returns int in mA """
#         self.__port.write('*SS,06\r')
#         time.sleep(0.1)
#         rec_str = self.__port.read(1024)
#         p = rec_str.find('*S,06:') + 6
#         if p == 5:
#             self.check(rec_str)
#             return 0
#         else:
#             return int(rec_str[p:len(rec_str)])/10.0
#
#
#
# class compressor(com_error):
#     """This class implements sensor readout functions"""
#     def __init__(self,port,comp_time_disabled):
#         ''' Constructor for this class. '''
#         self.__port=port
#         self.__comp_time_disabled=comp_time_disabled
#         self.__delay=600 # 600sec time delay between power cycle
#
#     def __del__(self):
#         ''' Destructor for this class. '''
#         return self.__comp_time_disabled
#
#
#     def runtime(self):
#         """ Request the sensor value for the helium supply temperature
#                 :returns int in mA """
#         self.__port.write('*GT,01\r')
#         time.sleep(0.1)
#         rec_str = self.__port.read(1024)
#         p = rec_str.find('*S,') + 3
#         if p == 2:
#             self.check(rec_str)
#             return 0
#         else:
#             return int(rec_str[p:len(rec_str)],16)/3600.0
#
#     def reset(self):
#         """ This function resets the compressor
#                 :returns Boolean True or False for command acknowledged """
#         self.__port.write('*RH\r')
#         time.sleep(0.1)
#         rec_str = self.__port.read(1024)
#         if rec_str=='*S\r':
#             return True
#         else:
#             return False
#
#     def disable(self):
#         """ This function shuts down the compressor
#                 :returns Boolean True or False for command acknowledged """
#         self.__port.write('*DH\r')
#         time.sleep(0.1)
#         rec_str = self.__port.read(1024)
#         if rec_str=='*S\r':
#             self.__comp_time_disabled=time.time()
#             return True
#         else:
#             return False
#
#     def enable(self):
#         """ This function starts the compressor, with a time delay between shut off, of 10 min
#                 :returns Boolean True or False for command acknowledged """
#         if self.__comp_time_disabled +self.__delay <= time.time(): # 600sec time delay before restart of the compressor
#             self.__port.write('*EH\r')
#             time.sleep(0.1)
#             rec_str = self.__port.read(1024)
#             if rec_str=='*S\r':
#                 return True
#             else:
#                 return False
#         else:
#             print "The compressor can be restarted in %.1f minutes." % (float(self.__comp_time_disabled +self.__delay-time.time())/60.0)
#             return False
#
#
# class error(com_error):
#     """This class implements error readout functions"""
#     def __init__(self,port):
#         ''' Constructor for this class. '''
#         self.__port=port
#         self.error_list = ['E_Pressure','E_Temperature','E_Overload','E_Surge']
#
#     def __del__(self):
#         ''' Destructor for this class. '''
#
#
#     def read(self):
#         """ Request the error register values of the unit
#                 :returns int  value of the error register"""
#         self.__port.write('*ER\r')
#         time.sleep(0.1)
#         rec_str = self.__port.read(1024)
#         p=rec_str.find('*S,')+3
#         error = int(rec_str[p:len(rec_str)],16)
#
#         for i in range(len(self.error_list)):
#             if error >>(i) & 1 :
#                 print 'ERROR: ' + self.error_list[i] +'\n'
#
#         if p==2:
#             self.check(rec_str)
#             return 0
#         else:
#             return int(rec_str[p:len(rec_str)],16)
#
#     def clear(self):
#         """ Request the error register values of the unit
#                 :returns int  value of the error register"""
#         self.__port.write('*EC,0000\r')
#         time.sleep(0.1)
#         rec_str = self.__port.read(1024)
#         p=rec_str.find('*S,')+3
#         error = int(rec_str[p:len(rec_str)],16)
#
#         for i in range(len(self.error_list)):
#             if error >>(i) & 1 :
#                 print 'ERROR: ' + self.error_list[i] +' could not be cleared!\n'
#
#         if p==2:
#             self.check(rec_str)
#             return 0
#         else:
#             print 'All ERRORs are cleared!'
#             return int(rec_str[p:len(rec_str)],16)