'''
Module Name:'Temperature'
Path:'<package_root>/src/Temperature.py'
Module Version:'1.1.0.2023.02.08'
Author;'A K M Aminul Islam'
author_Email:'aminul71bd@gmail.com'
Company:'Newtonia Ltd.'
Last Update:2023/02/15
Description: 'This module creates Temperature object using Temperature class. \
    It supports three units: celcius, kelvin and Fahrenheit.'
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

# This Temperature class creates temperature object with value and unit
class Temperature: 

    #F=1.8'C+32; K=C+273.15

    def __init__ (self,value=25,unit='C'):
        self.__unit_prefix=1; self.__unit= ''; self.__physical_type=''; self.__value=0
        try:
            if value==None or unit==None: raise ValueError("Temperature value or unit not set.")
            if dataType(unit)!='str': raise ValueError("Temperature unit must be string.")
            if dataType(value) not in ['int','float']: raise ValueError("Invalid DataType of Temperature Value")
            # resolving unit
            if unit=='C': self.__unit_prefix=1; self.__unit='C'; self.__physical_type='TEMPERATURE'
            else:
                (self.__unit_prefix,self.__unit,self.__physical_type) = self.__resolve_unit(unit)
                if self.__physical_type == None:raise ValueError('Invalid Unit: Not Temperature Unit')
            self.__value=value*self.__unit_prefix; self.__unit_prefix=1;
            # testing temperature values
            if self.__unit == 'K' and self.__value < 0: raise ValueError("Invalid Temperature Value")
            elif self.__unit == 'C' and self.__value < -273.15: raise ValueError("Invalid Temperature Value")
            elif self.__unit == 'F' and self.__value < -169.53: raise ValueError("Invalid Temperature Value")
		
        except ValueError as e:print(e) # in release version: return None


    def changeValue(self,value=25):
        current_value=self.__value
        try:
            if value==None or dataType(value) not in ['int','float']:                 
                raise ValueError("Invalid Temperature Value")
            if self.__unit in ['K','Kelvin'] and value < 0: raise ValueError("Invalid Temperature Value")
            elif self.__unit in ['C','Celcius'] and value < -273.15: raise ValueError("Invalid Temperature Value")
            elif self.__unit in ['F','Fahrenheit'] and value < -169.53: raise ValueError("Invalid Temperature Value")
        except ValueError as e:
            self.__value=current_value
        else:			
            self.__value=value
 
    def getValue(self):
        return self.__value 
 
    def getUnit(self):
        return self.__unit 

    def getUnitPrefix(self):
        return self.__unit_prefix 

    def getQuantity(self):
        return self.__physical_type

    # __repr__(self) returns always celcius temperature
    def __repr__ (self): 
        copy_temp=self.copy();copy_temp.toC();
        return str(copy_temp.__value)+' C'

    # __str__(self) returns the string version of temperature; 
	# print(temperature) and str(temperature) calls this method
    def __str__(self): 
        return "{0:s}: {1:.6g} degree {2:s}".format(self.__physical_type,self.__value,self.__unit)
	
	
	# private function
	# __resolve_unit(self) verifies unit and resolves unit into a tuple (prefix,unit,quantity)
    def __resolve_unit(self,unit='C',quantity='Temperature'):
        try:
            unit_obj=Unit(unit,quantity)
            if unit_obj == None: raise ValueError('Invalid Unit of Temperature')
            physical_type = unit_obj.getQuantity()
            if physical_type != 'TEMPERATURE':raise ValueError('')
            unit_prefix = unit_obj.getPrefix()
            unit = unit_obj.getUnit()
            return (unit_prefix,unit,physical_type)
        except ValueError: return (None,None,None)

    # deepcopy() of temperatue object
    def copy(self):
        return Temperature(self.__value,self.__unit)

    # changing unit
    def toC(self):
        if self.__unit in ['C','Celcius']: return
        elif self.__unit in ['F','Fahrenheit','Fahrenheits']:
            self.__value = (self.__value - 32)/1.8; self.__unit='C'
        elif self.__unit in ['K','Kelvin','Kelvins']:
            self.__value = self.__value - 273.15; self.__unit='C'

    def toF(self):
        self.toC(); self.__value=self.__value*1.8 + 32; self.__unit='F'

    def toK(self):
        self.toC(); self.__value=self.__value + 273.15; self.__unit='K'







			