'''
Module Name:'Unit'
Path:'<package_root>/src/Unit.py'
Module Version:'1.1.0.2023.02.09'
Author;'A K M Aminul Islam'
author_Email:'aminul71bd@gmail.com'
Company:'Newtonia Ltd.'
Last Update:2023/02/15
Description: 'This module contains Unit class that holds necessary physical units.'
Dependency: psychro.src.Prefix
'''

from psychro.src.Prefix import Prefix

__version__='1.1.0.2023.02.09'
version='1.1.0.2023.02.09'


# dataType() function returns the type of a data
# type(2.0) returns "(type 'float')"
def dataType(data=None):
    s=str(type(data)).split(' ')[1]
    return s.split("'")[1]



# resolveUnit(unit='mm') returns a tuple of unit, it's prefix, it's quantity; (prefix,unit,quantity)
def resolveUnit(unit='mm',quantity=''):

    unit_names={'C':['C','Celcius'],'F':['F','Fahrenheit','Fahrenheits'],'K':['K','Kelvin','Kelvins'],\
    'Bar':['Bar','Bars'], 'bar':['bar','bars'],'atm':['atm'],'Atm':['ATM','Atm'],'Pa':['Pa','Pascal','Pascals'],\
    'pa':['pa','pascal','pascals'], 'psi':['psi'],'Psi':['Psi','PSI'], 'mHg':['mHg'], 'mhg':['mhg'],\
    'torr':['torr','torrs'],'Torr':['Torr','Torrs'],'J':['J','Joule','Joules'], 'j':['j','joule','joules'],\
    'cal':['cal','calorie','calories'], 'Cal':['Cal','Calorie','Calories'],'btu':['btu'],'Btu':['Btu','BTU'], \
    'wh':['wh','watthour','watthours'], 'Wh':['Wh','Watthour','Watthours'],\
    'ev':['ev','electronvolt','electronvolts','electron-volt','electron-volts'],\
    'eV':['eV','electronVolt','electronVolts','electron-Volt','electron-Volts'],'hp':['hp','horsepower','horsepowers'],\
    'W':['W','w','Watt','watt','Watts','watts'], 'w':['w','watt','watts'], 'ton':['ton','Ton'], \
    'm':['m','meter','meters','metre','metres'], 'inch':['inch','inches'], 'ft':['ft','foot','feet'], \
    'yd':['yd','yard','yards'],'mile':['mile','miles']}

    unit_quantities={'TEMPERATURE':['C','K','F'],'PRESSURE':['Pa','pa','mHg','mhg','Atm','atm','bar','Bar','psi','Psi','torr','Torr'],\
    'ENERGY':['J','j','Cal','cal','Btu','btu','wh','Wh','eV','ev'],'POWER':['W','w','hp','ton'],\
	'LENGTH':['m','inch','ft','yd','mile']}	

    prefix_value=1; unit_found=''; unit_key=''; physical_quantity=''; match_index=-1; confirm_index=-1;
    unit_keys=[];short_prefix='';prefix=None

    try:
        # Loading bare unit keys of the given physical quantity
        quantity_found=False
        for key in unit_quantities.keys():
            if key == quantity.upper(): 
                unit_keys = unit_quantities[key]; quantity_found=True;break
        if not quantity_found:raise ValueError('Unknown Physical Quantity')
        physical_quantity=quantity.upper();

        # if Length of unit=1, verify unit and return it; unit example: 'm','C','K','J'
        if len(unit)==1:
            for u in unit_keys:
                if u==unit:
                    unit_found=u; prefix_value=1; break
            if unit_found=='': raise ValueError(unit+' is not a valid unit of '+physical_quantity)
        # if Length of unit=2, verify unit and return prefix and unit
        # unit example: 'cm','kC','kK','MJ'
        elif len(unit)==2:
            for u in unit_keys:
                if u in unit: match_index=unit.index(u);break
            if match_index==-1: raise ValueError(unit+' is not a valid unit of '+physical_quantity)
            if match_index==0:unit_found=u; prefix_value=1
            elif match_index==1:                
                unit_key=unit_found=unit[1];
                # find the prefix value
                prefix=Prefix(unit[0]);  
                if prefix.getSymbol()==None: raise ValueError('Invalid Prefix')		
                prefix_value=prefix.getValue()

        # if Length of unit greater than 2, verify unit and return prefix and unit
        # unit example: 'centimeter','Celcius','kiloK','MegaJoules'
        elif len(unit)>2:
            # Checking unit names present in the unit string
            for u in unit_keys:
                for name in unit_names[u]:
                    if name in unit: 
                        match_index=unit.index(name); 
                        if len(unit)-match_index == len(name):
                            unit_found=name; confirm_index=match_index; unit_key=u; break; break

            if confirm_index==-1:raise ValueError(unit+' is not a unit of of '+physical_quantity) 
            elif confirm_index==0: pass
            elif confirm_index>0:
                # Searching for prefix
                prefix_str=unit[:confirm_index];
                prefix=Prefix(prefix_str)
                if prefix.getSymbol()==None: raise ValueError('Invalid prefix in unit')
                prefix_value=prefix.getValue()
 
    except ValueError as e:
        print(e); return (None,None,None)
    else:        
        return (prefix_value,unit_found,physical_quantity)


# Unit('unit') creates physical unit object
class Unit:
    # unit constructor
    def __init__(self,unit='mm',quantity='length'):
        try:
            (self.__unit_prefix, self.__unit, self.__physical_quantity)=resolveUnit(unit,quantity)
            if self.__unit==None: raise ValueError('Invalid Unit')
        except ValueError as ve: 
            self=None; del(self)            

    # getPrefix() returns unit prefix set by the user
    def getPrefix(self):
        return self.__unit_prefix
    
    # getPrefix() returns prefix value
    def getUnit(self):
        return self.__unit

    # getPhysicalType() returns the physical quantity that belongs this unit
    def getQuantity(self):
        return self.__physical_quantity

    # __str__() returns value for output of str(unit) and print(unit)
    def __str__(self):
        if self.__unit != None:
            return self.__physical_quantity+':'+str(int(self.__unit_prefix))+' '+self.__unit
            #elif self.__unit_prefix < 1:return self.__physical_quantity+':'+str(self.__unit_prefix)+' '+self.__unit
            #else: return self.__physical_quantity+':'+self.__unit
        else: return ''

    # __repr__() returns the value it represents
    def __repr__(self):
        return str(self)
