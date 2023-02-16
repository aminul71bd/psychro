'''
Module Name:'Prefix'
Path:'<package_root>/src/Prefix.py'
Module Version:'1.0.0.2023.02.09'
Author;'A K M Aminul Islam'
Author_Email:'aminul71bd@gmail.com'
Company:'Newtonia Ltd.'
Last Update:2023/02/15
Description: 'This module contains Prefix class to store and suply SI prefixes used with physical units.'
Usage:
    >>> p=Prefix('m')
    >>> p.getName(); p.getValue(); p.getSymbol()
Dependency:''
'''

version:'1.0.0.2023.02.09'
__version__:'1.0.0.2023.02.09'


class Prefix:

    __prefix_values={'y':1e-24,'z':1e-21,'a':1e-18, 'f':1e-15, 'p':1e-12, 'n':1e-9, 'u':1e-6, 'm':1e-3,\
    'c':1e-2, 'd':1e-1, 'da':1e+1, 'h':1e+2, 'k':1e+3, 'M':1e+6, 'G':1e+9, 'T':1e+12, 'P':1e+15, \
    'E':1e+18, 'Z':1e+21, 'Y':1e+24}

    __prefix_names={'y':'yocto','z':'zepto','a':'atto', 'f':'femto', 'p':'pico', 'n':'nano', 'u':'micro',\
    'm':'milli', 'c':'centi', 'da':'deca', 'h':'hecto', 'k':'kilo', 'M':'mega', 'G':'giga', 'T':'tera',\
    'P':'peta', 'E':'exa', 'Z':'zetta', 'Y':'yotta'}

    __symbol_list=['y','z','a','f','p','n','u','m','c','d','da','h','k','M','G','T','P','E','Z','Y']

    def __init__(self,prefix='k'):
        self.__prefix_symbol=''; self.__prefix_name=''; self.__prefix_value=-1
        try:
            if len(prefix)==1:
                if prefix in Prefix.__symbol_list: self.__prefix_symbol=prefix
                else: raise ValueError('Invalid Prefix')
            elif prefix=='da': self.__prefix_symbol='da';
            else:
                for key in Prefix.__prefix_names.keys():
                    if prefix == Prefix.__prefix_names[key]:
                        self.__prefix_symbol=key; break 
                if self.__prefix_symbol=='': raise ValueError('Invalid Prefix')
            self.__prefix_name=Prefix.__prefix_names[self.__prefix_symbol]
            self.__prefix_value=Prefix.__prefix_values[self.__prefix_symbol]

        except ValueError as e: 
            self.__prefix_symbol=None; self.__prefix_name=None; self.__prefix_value=None; self=None;
            del(self); print(e);

    def getName(self): return self.__prefix_name

    def getValue(self): return self.__prefix_value

    def getSymbol(self): return self.__prefix_symbol

    #  __str__(self) returns string representation of a Prefix instance
    def __str__(self):
        if self.__prefix_symbol != None:
            return "Prefix:{0:s},{1:s}={2:g}".format(self.__prefix_symbol,self.__prefix_name,self.__prefix_value)
    
    #  __repr__(self) returns numeric representation of a Prefix instance
    def __repr__(self):
        if self.__prefix_symbol != None:
            return "{0:g}".format(self.__prefix_value)


# prefix values required for getPrefix() function
prefix_values={'y':1e-24,'z':1e-21,'a':1e-18, 'f':1e-15, 'p':1e-12, 'n':1e-9, 'u':1e-6, 'm':1e-3,\
    'c':1e-2, 'd':1e-1, 'da':1e+1, 'h':1e+2, 'k':1e+3, 'M':1e+6, 'G':1e+9, 'T':1e+12, 'P':1e+15, \
    'E':1e+18, 'Z':1e+21, 'Y':1e+24}
	
# getPrefix(value) returns a prefix object equal to the given value
def getPrefix(value=1000):
    value_found=False
    for key in prefix_values.keys():
        if value == prefix_values[key]:
            prefix=Prefix(key); value_found=True; break
    if not value_found: return None 
    return prefix
			