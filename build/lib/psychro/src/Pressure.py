'''
Module Name:'Pressure'
Path:'<package_root>/src/Pressure.py'
Module Version:'1.1.0.2023.02.08'
Author;'A K M Aminul Islam'
author_Email:'aminul71bd@gmail.com'
Company:'Newtonia Ltd.'
Last Update:2023/02/15
Description: 'This module defines a pressure object by using pressure class'
Dependency: psychro.src.Unit, __future__ 
'''
from __future__ import division
from psychro.src.Unit import Unit


__version__='1.0.0.2023.02.08'
version='1.0.0.2023.02.08'

# dataType() function returns the type of a data
# type(2.0) returns "(type 'float')"
def dataType(data=None):
    s=str(type(data)).split(' ')[1]
    return s.split("'")[1]

# This Pressure class creates pressure object with value and unit
# Type of pressure value can be either 'abs' (absolute) and 'rel ('relative )
# Absolute Pressure = Atmospheric Pressure +/- Relative pressure
# is_absolute=False means relative pressure
class Pressure: 

    def __init__ (self,value=100,unit='Pa',is_absolute=True):
        self.__unit_prefix=1; self.__unit= ''; self.__physical_type=''; self.__value=0;
        try:
            if value==None or unit==None: raise ValueError("Pressure value or unit not set.")
            if dataType(unit)!='str': raise ValueError("Pressure unit must be string.")
            if dataType(value) not in ['int','float']: raise ValueError("Invalid DataType of Pressure Value")
            if is_absolute not in [True, False]: raise ValueError("Invalid Argument: is_absolute")
            # resolving unit
            if unit=='Pa': self.__unit_prefix=1; self.__unit='Pa'; self.__physical_type='PRESSURE'
            else:
                (self.__unit_prefix,self.__unit,self.__physical_type) = self.__resolve_unit(unit)
                if self.__physical_type == None: raise ValueError('Invalid Unit: Not Pressure Unit')
            self.__value=value*self.__unit_prefix; self.__unit_prefix=1; self.__isAbsolute=is_absolute
            # testing Pressure values
            if not self.validatePressureValue(self.__value): 
                raise ValueError('Invalid Pressure Value')
        except ValueError as e:print(e) # in release version: return None


    def changeValue(self,value=100,is_absolute=True):
        current_value=self.__value; current_isAbsolute=self.__isAbsolute
        try:
            if not self.validatePressureValue(self,value): 
                raise ValueError('Invalid Pressure Value')
        except ValueError as e:
            self.__value=current_value; self.__isAbsolute=current_isAbsolute 
        else:			
            self.__value=value; self.__isAbsolute=is_absolute
 

    def getValue(self):
        return self.__value 
 
    def getUnit(self):
        return self.__unit 

    def getUnitPrefix(self):
        return self.__unit_prefix 

    def getQuantity(self):
        return self.__physical_type

    def isAbsolute(self):
        return self.__isAbsolute

    # __repr__(self) returns always pascal pressure
    def __repr__ (self): 
        copy_temp=self.copy();copy_temp.toPa(); return str(copy_temp.__value)+' Pa'

    # __str__(self) returns the string version of pressure; 
	# print(pressure) and str(pressure) calls this method
    def __str__(self): 
        if self.__isAbsolute: return "PRESSURE: {0:.3g} {1} absolute".format(self.__value,self.__unit)
        return "PRESSURE: {0:.6g} {1} relative".format(self.__value,self.__unit)
	
	
	# private function
	# __resolve_unit(self) verifies unit and resolves unit into a tuple (prefix,unit,quantity)
    def __resolve_unit(self,unit='Pa',quantity='Pressure'):
        try:
            unit_obj=Unit(unit,quantity)
            if unit_obj == None: raise ValueError('Invalid Unit of Pressure')
            physical_type = unit_obj.getQuantity()
            if physical_type != 'PRESSURE':raise ValueError('Invalid Unit of Pressure')
            unit_prefix = unit_obj.getPrefix()
            unit = unit_obj.getUnit()
            return (unit_prefix,unit,physical_type)
        except ValueError: return (None,None,None)

    # deepcopy() of energy object
    def copy(self):
        return Pressure(self.__value,self.__unit,self.__isAbsolute)

    # validates the pressure value with the real world limitation
    def validatePressureValue(self,value=1):
        try:
            if self.__isAbsolute == True and self.__value < 0: raise ValueError("Absolute Pressure Value cannot be negative")
            elif self.__isAbsolute == False:
                if self.__unit in ['atm','Atm'] and self.__value < -1.0: raise ValueError("Invalid Pressure Value")
                elif self.__unit in ['pa','Pa'] and self.__value < -101500: raise ValueError("Invalid Pressure Value")
                elif self.__unit in ['mHg','mhg'] and self.__value < -0.76: raise ValueError("Invalid Pressure Value")
                elif self.__unit in ['bar','Bar'] and self.__value < -1.015: raise ValueError("Invalid Pressure Value")
                elif self.__unit in ['psi','Psi'] and self.__value < -14.7: raise ValueError("Invalid Pressure Value")
        except ValueError: return False
        else: return True

    # convert to Pa from atm, bar, Hg pressure unit
    def toPa(self):
        if self.__unit in ['Pa','pa']:return
        elif self.__unit in ['bar','Bar']: 
            self.__value = 100000*self.__value; # 100kPa=1bar
        elif self.__unit in ['atm','Atm']: 
            self.__value = 101325*self.__value; # 1atm=101325Pa
        elif self.__unit in ['mHg','mhg']: 
            self.__value = 133322.368421*self.__value; # 101325Pa=0.76mHg
        elif self.__unit in ['psi','Psi']: 
            self.__value = 6894.733261*self.__value; # 101325Pa=14.696psi;
        elif self.__unit in ['torr','Torr']: 
            self.__value = 101325*self.__value/760; # 1 torr = 133.322 Pa; 
        self.__unit='Pa'

    def topa(self): return self.toPa()

    # convert to bar pressure
    def tobar(self):
        if self.__unit in ['bar','Bar']:return
        self.toPa(); self.__value=self.__value/100000
        self.__unit='bar'

    def toBar(self):
        self.tobar()

    # convert to psi pressure 
    def topsi(self):
        if self.__unit in ['psi','Psi']:return
        self.toPa(); self.__value=self.__value*1.450382e-4
        self.__unit='psi'

    def toPsi(self):
        self.topsi()

    # convert to mHg pressure
    def tomHg(self):
        if self.__unit in ['mHg','mhg']:return
        self.toPa(); self.__value=self.__value*7.500616827e-6
        self.__unit='mHg'

    def tomhg(self):
        self.tomHg()


    # convert to atm pressure
    def toatm(self):
        if self.__unit in ['atm','Atm']:return
        self.toPa(); self.__value=self.__value*9.869232667e-6
        self.__unit='atm'

    def toAtm(self):
        self.toatm()


    # convert to torr pressure
    def totorr(self):
        if self.__unit in ['torr','Torr']:return
        self.toPa(); self.__value=self.__value*7.5006375541921e-3
        self.__unit='torr'

    def toTorr(self):
        self.totorr()