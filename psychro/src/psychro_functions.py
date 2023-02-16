''''
Module Name:'psychro_functions'
Path:'<package_root>/src/psychro_functions.py'
Version:'1.0.0.2023.02.10'
Author:'A K M Aminul Islam'
Author_Email:'aminul71bd@gmail.com'
Company:'Newtonia Ltd.'
Last Update:2022/02/15
Description:'This module, psychro_functions.py is used to creates the functions \
    necessary to calculate the psychrometric data.'
	'Dry Air=(20.95% 02, 78.09% N2, 0.93% Ar, 0.04% CO2)'
	'Molar Mass= 28.947 g/mol '

Assumption: Open system and constant atmospheric pressure of 1 atm

'''
from __future__ import division
from psychro.src.Pressure import Pressure
from psychro.src.Temperature import Temperature
import math

__version__='1.0.0.2023.02.10'
version='1.0.0.2023.02.10'



# Antoine equation for pure water 
# ================================
# Psat= Saturated Vapor Pressure (The pressure at which a closed air-water system remains in equilibrium)
# 1g(Psat)=A-B/(T+C)
# For 0-60C: A=8.10765, B=1750.286, C=235.0; Source: page:235, Elementary Principles of Chemical Processes
# For 60-150C: A=7.96681, B=1668.21, C=228.0 

# satVaporPressure() calculates saturated water vapor pressure in mmHg 
# at the given temperature between 0 and 150 deg celcius using Antoine Equation  
# Argument temperature is a temperature object
# 0 <= Temperature <=150 C
# Function No:01
def satVaporPressure(temperature=None):
    try: 
        if temperature==None: 
            raise ValueError("Temperature arguement of vaporPressure() is missing")
        temperature.toC() 
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        elif temperature.getValue()>=0 and temperature.getValue()<60: 
            p=10**(8.10765-(1750.286/(temperature.getValue()+235))) 
        elif temperature.getValue()>=60 and temperature.getValue()<=150: 
            p=10**(7.96681-(1668.21/(temperature.getValue()+228.0)))
        else: raise ValueError("Invalid Temperature Value for Antoine equation.") 
    except Exception as e:
	    print(e)
    else:
        return Pressure(p,unit='mmHg',is_absolute=True) 
	
	

# satTemperature() calculates saturated water vapor temperature in degree celcius 
# at the given water vapor pressure (in mmHg) using Antoine Equation 
# T = B/(A - lg(P)) - A
# Function No:02
def satTemperature(vapPressure=None): 
    try:
        if vapPressure==None: 
            raise ValueError("Saturated vapor pressure arguement of satTemperature() is missing") 
        vapPressure.tomHg() 
        if vapPressure.getValue()<0.149444: 
            t=(1750.286/(8.10765-math.log10(vapPressure.getValue()*1000)))-235.0 
        elif (vapPressure.getValue()>=0.149444 and vapPressure.getValue()<=3.577306): 
            t=(1668.21/(7.96681-math.log10(vapPressure.getValue()*1000)))-228.0 
        else: raise ValueError("Saturated vapor pressure value is out of range for Antoine equation.")
    except Exception as e: print(e)
    else:	
        return Temperature(t,'C')



# dryAirPressure(T) calculates the pressure of dry air in Pa at the given temperature
# Sea-level pressure at 15 C = 101325 Pa = partial pressure of water vapor + partial pressure of dry air
# P2/P1 = (T2+273.15)/(T1+273.15) where T1, T2 are celcius temperature
# At 15C, partial pressure of water = satVaporPressure(15C) = 1703.7623626481663 Pa
# Dry Air Pressure = 345.727*(T+273.15) Pa where T in degree C
# Function No:03
def dryAirPressure(temperature=None):
    try:
        if temperature==None: 
            raise ValueError("Temperature is not set in the argument of dryAirPressure()") 
        temperature.toC()
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        temp15C=Temperature(15,'C'); temperature.toK()
        satp_at15=satVaporPressure(temp15C); satp_at15.toPa()
        airp_at15=Pressure(101325-satp_at15.getValue(),'Pa')
    except Exception as e: print(e)
    else:
        return Pressure(airp_at15.getValue()*temperature.getValue()/288.15,'Pa',is_absolute=True)



# humidAirPressure(temperature) calculates the total pressure in Pa exerted by
# water vapor and dry air in a closed system
# Function No:04
def humidAirPressure(temperature = None, relHumidity = None):
    try:
        if temperature==None: 
            raise ValueError("Temperature is not set in the argument of humidAirPressure()")
        elif relHumidity==None: 
            raise ValueError("Relative humidity is not set in the arguement of humidAirPressure()") 
        elif relHumidity < 0 or relHumidity > 100: 
            raise ValueError("Relative humidity is out of range") 
        temperature.toC()
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        dryairpressure=dryAirPressure(temperature)
        watervaporpressure=satVaporPressure(temperature); watervaporpressure.toPa()
        totalpressure=watervaporpressure.getValue()+dryairpressure.getValue()
    except Exception as e: print(e)
    else:
        return Pressure(totalpressure,'Pa',is_absolute=True)



# dewPoint() calculates dew point which is the temperature(C) at which air is saturated 
# with the current content of water vapor. It is the same as saturated temperature. 
# Function No:05
def dewPoint(temperature = None, relHumidity = None):
    try: 
        if temperature==None: 
            raise ValueError("Temperature is not set in the arguement of dewPoint()") 
        elif relHumidity==None: 
            raise ValueError("Relative humidity arguement of dewPoint() is missing") 
        elif relHumidity < 0 or relHumidity > 100: 
            raise ValueError("Relative humidity is out of range") 
        if relHumidity==0: return None 
        elif relHumidity==100: return temperature 
        temperature.toC()
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        #satPressure=Saturated vapor pressure at the given temperature 
        satPressure=satVaporPressure(temperature);  
        satPressure.toPa();
        partialPressure=relHumidity*satPressure.getValue()/100;
        vapPressure=Pressure(partialPressure,'Pa')
    except Exception as e: print(e)
    else:
        return satTemperature(vapPressure) 

# saturatedTemperature() calculates dew point which is the temperature(C) at which air is saturated 
# with the current content of water vapor. It is the same as saturated temperature. 
# Function No:05/2
def saturatedTemperature(temperature = None, relHumidity = None):
    try: 
        if temperature==None: 
            raise ValueError("Temperature arguement of saturatedTemperature() is missing") 
        elif relHumidity==None: 
            raise ValueError("Relative humidity is not set in the arguement of saturatedTemperature()") 
        elif relHumidity < 0 or relHumidity > 100: 
            raise ValueError("Relative humidity is out of range") 
        if relHumidity==0: return None 
        elif relHumidity==100: return temperature 
        temperature.toC() 
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        #satPressure=Saturated vapor pressure at the given temperature 
        satPressure=satVaporPressure(temperature);  
        satPressure.toPa();
        partialPressure=relHumidity*satPressure.getValue()/100;
        vapPressure=Pressure(partialPressure,'Pa')
    except Exception as e: print(e)
    else:
        return satTemperature(vapPressure) 


# partialPressure() calculates partial pressure of water vapor in air when dry 
# bulb temperature(C) and relative humidity are given
# Function No:06 
def partialPressure(temperature=None, relHumidity=None):
    try: 
        if temperature==None: 
            raise ValueError("Temperature is not set in the arguement of partialPressure()") 
        elif relHumidity==None: 
            raise ValueError("Relative humidity is not set in the arguement of partialPressure()")
        elif relHumidity < 0 or relHumidity > 100: 
            raise ValueError("Relative humidity is out of range") 
        temperature.toC() 
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        # satpressure=Saturated vapor pressure at the given temperature 
        satpressure=satVaporPressure(temperature); satpressure.toPa()
    except Exception as e: print(e)
    else:	
        return Pressure(relHumidity*satpressure.getValue()/100,'Pa')
	
	
		
# relativeHumidity() calculates relative humidity when dry bulb temperature(C) 
# and wet bulb temperature are given 
# Function No:07
def relativeHumidity(temperature=None, dewpoint=None):
    try: 
        if temperature==None: 
            raise ValueError("Temperature is not set in the arguement of relativeHumidity()") 
        elif dewpoint==None: 
            raise ValueError("Dew point is not set in the arguement of relativeHumidity()") 
        temperature.toC(); dewpoint.toC()
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        if temperature.getValue() < dewpoint.getValue(): 
            raise ValueError("Dew point cannot be greater than the air temperature.")

        if abs(temperature.getValue() - dewpoint.getValue()) < 10:
            # satpressure=Saturated vapor pressure at the given temperature 
            # satpressureDewPoint=Saturated vapor pressure at the dewpoint 
            dryairp = dryAirPressure(dewpoint); dryairp.toPa()		
            satpressureDewPoint=satVaporPressure(dewpoint); satpressureDewPoint.toPa()
            # mole fraction at dewpoint
            y=satpressureDewPoint.getValue()/(dryairp.getValue()+satpressureDewPoint.getValue())
            # considering same mole fraction at the given temperature obtained by heating
            # y = Pw/(Pw+Pair)
            dryairp = dryAirPressure(temperature); dryairp.toPa()
            watervaporpp = dryairp.getValue()*y/(1-y)
            satpressure=satVaporPressure(temperature); satpressure.toPa()
            RH=100*watervaporpp/satpressure.getValue()
        else: 
            # satpressure=Saturated vapor pressure at the given temperature 
            # satpressureDewPoint=Saturated vapor pressure at the dewpoint 
            satpressure=satVaporPressure(temperature); satpressure.toPa()	
            satpressureDewPoint=satVaporPressure(dewpoint); satpressureDewPoint.toPa()            
            RH=100*satpressureDewPoint.getValue()/satpressure.getValue() 
 
    except Exception as e: print(e)
    else: return RH


 
# moleFraction() calculates the ratio of moles of water vapor in air to 
# the moles of wet air molecules when dry bulb temperature(C), relative humidity  
# are given (moles of vapor/moles of wet air)
# Function No:08
def moleFraction(temperature=None, relHumidity=None, pressure=None):
    try: 
        if temperature==None: 
            raise ValueError("Temperature is not set in the arguement of moleFraction()") 
        elif pressure==None: 
            raise ValueError("Pressure arguement value is not set in moleFraction()") 
        elif relHumidity==None: 
            raise ValueError("Relative humidity is not set in the arguement of moleFraction()") 
        temperature.toC()
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        elif relHumidity < 0 or relHumidity > 100: 
            raise ValueError("Relative humidity is out of range") 
        temperature.toC(); pressure.toPa()
        # satpressure=Saturated vapor pressure at the given temperature 
        satpressure=satVaporPressure(temperature); satpressure.toPa()
    except Exception as e: print(e)
    else:
        return relHumidity*satpressure.getValue()/(100*pressure.getValue())



# absoluteHumidity = mass of vapor / mass of dry air (kg vapor/kg DA)
# Function No:09
def absoluteHumidity(temperature=None, relHumidity=None, pressure=None): 
    try:
        if temperature==None: 
            raise ValueError("Temperature is not set in the arguement of absoluteHumidity()") 
        elif relHumidity==None: 
            raise ValueError("Relative humidity is not set in the arguement of absoluteHumidity()") 
        elif pressure==None: 
            raise ValueError("Pressure arguement value is not set in absoluteHumidity()") 
        elif relHumidity < 0 or relHumidity > 100: 
            raise ValueError("Relative humidity is out of range") 
        temperature.toC(); pressure.toPa()
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        # satpressure=Saturated vapor pressure at the given temperature 
        satpressure=satVaporPressure(temperature); satpressure.toPa()    
        y=relHumidity*satpressure.getValue()/(100*pressure.getValue())
    except Exception as e: print(e)
    else:
        return (0.6218*y/(1-y),'kg/kgDA') # 0.6218=18/28.947 



# moistureContent = mass of vapor / mass of dry air (kg vapor/kg DA)
# Function No:09/2
def moistureContent(temperature=None, relHumidity=None, pressure=None): 
    try:
        if temperature==None: 
            raise ValueError("Temperature is not set in the arguement of moistureContent()") 
        elif relHumidity==None: 
            raise ValueError("Relative humidity is not set in the arguement of moistureContent()") 
        elif pressure==None: 
            raise ValueError("Pressure arguement value is not set in moistureContent()") 
        elif relHumidity < 0 or relHumidity > 100: 
            raise ValueError("Relative humidity is out of range") 
        temperature.toC(); pressure.toPa()
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        # satpressure=Saturated vapor pressure at the given temperature 
        satpressure=satVaporPressure(temperature); satpressure.toPa()    
        y=relHumidity*satpressure.getValue()/(100*pressure.getValue())
    except Exception as e: print(e)
    else:
        return (0.6218*y/(1-y),'kg/kgDA') # 0.6218=18/28.947


# massFraction() calculates the mass ratio of water vapor to humid air 
# when dry bulb temperature(C), relative humidity are given (kg vapor/kg wet air)
# Function No:10 
def massFraction(temperature=None, relHumidity=None, pressure=None):
    try:
        if temperature==None: 
            raise ValueError("Temperature is not set in the arguement of massFraction()") 
        elif relHumidity==None: 
            raise ValueError("Relative humidity is not set in the arguement of massFraction()") 
        elif pressure==None: 
            raise ValueError("Pressure arguement value is not set in massFraction()") 
        elif relHumidity < 0 or relHumidity > 100: 
            raise ValueError("Relative humidity is out of range") 
        temperature.toC()
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        x=absoluteHumidity(temperature, relHumidity, pressure)[0]
    except Exception as e: print(e)
    else:
        return (x/(1+x),'kg/kgHA')

# volumetricHumidity() calculates the mass of water vapor per unit volume (kg/m3) 
# of humid air when dry bulb temperature(C), relative humidity and pressure are given 
# VolumetricHumidity=m/V=pp*M/RT 
# Function No:11
def volumetricHumidity(temperature=None, relHumidity=None, pressure=None): 
    try:
        if temperature==None: 
            raise ValueError("Temperature is not set in the arguement of volumetricHumidity()") 
        elif relHumidity==None: 
            raise ValueError("Relative humidity is not set in the arguement of volumetricHumidity()") 
        elif pressure==None: 
            raise ValueError("Air pressure is not set in the arguement of volumetricHumidity()") 
        elif relHumidity < 0 or relHumidity > 100: 
            raise ValueError("Relative humidity is out of range")
        temperature.toC(); pressure.toPa()
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        # satpressure=Saturated vapor pressure at the given temperature 
        satpressure=satVaporPressure(temperature); satpressure.toPa() 
        pp=Pressure(relHumidity*satpressure.getValue()/100,'Pa');
        temperature.toK(); pp.toPa() 
    except Exception as e: print(e)
    else:
        return (0.002165*pp.getValue()/temperature.getValue(),'kg/m3') #0.002165=18/(8.314*1000) 

# vaporDensity() calculates the mass of water vapor per unit volume (kg/m3) 
# of humid air when dry bulb temperature(C), relative humidity and pressure are given 
# VolumetricHumidity=m/V=pp*M/RT 
# Function No:11/2
def vaporDensity(temperature=None, relHumidity=None, pressure=None): 
    try:
        if temperature==None: 
            raise ValueError("Temperature is not set in the arguement of vaporDensity()") 
        elif relHumidity==None: 
            raise ValueError("Relative humidity is not set in the arguement of vaporDensity()") 
        elif pressure==None: 
            raise ValueError("Air pressure is not set in the arguement of vaporDensity()") 
        elif relHumidity < 0 or relHumidity > 100: 
            raise ValueError("Relative humidity is out of range")
        temperature.toC(); pressure.toPa() 
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        # satpressure=Saturated vapor pressure at the given temperature 
        satpressure=satVaporPressure(temperature); satpressure.toPa() 
        pp=Pressure(relHumidity*satpressure.getValue()/100,'Pa');
        temperature.toK(); pp.toPa() 
    except Exception as e: print(e)
    else:
        return (0.002165*pp.getValue()/temperature.getValue(),'kg/m3') #0.002165=18/(8.314*1000) 


 
# humidVolume() calculates the volume of humid air per unit mass (m3/kgDA) 
# of dry air when dry bulb temperature(C), relative humidity and humid air pressure are given 
# Humid Volume=V/m=RT/(1-y)PM 
# Function No:12
def humidVolume(temperature=None, relHumidity=None, pressure=None):
    try: 
        if temperature==None: 
            raise ValueError("Temperature is not set in the arguement of humidVolume()") 
        elif relHumidity==None: 
            raise ValueError("Relative humidity is not set in the arguement of humidVolume()") 
        elif pressure==None: 
            raise ValueError("Air pressure is not set in the arguement of humidVolume()") 
        elif relHumidity < 0 or relHumidity > 100: 
            raise ValueError("Relative humidity is out of range")
        temperature.toC(); pressure.toPa() 
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        # satpressure=Saturated vapor pressure at the given temperature 
        satpressure=satVaporPressure(temperature); satpressure.toPa() 
        y=relHumidity*satpressure.getValue()/(100*pressure.getValue())	
        temperature.toK(); pressure.toPa()
    except Exception as e: print(e)
    else:		
        return (287.2*temperature.getValue()/(pressure.getValue()*(1-y)),'m3/kgDA') #287.2=8.314*1000/28.947 



# humidDensity() calculates the mass of humid air per unit volume of humid air (kg/m3) 
# when dry bulb temperature(C), relative humidity and humid air pressure are given 
# Humid Density.(m+m0)/V.(1-(M-18)y/M)'T/RT; y=mole fraction 
# Function No:13
def humidDensity(temperature=None, relHumidity=None, pressure=None):
    try: 
        if temperature==None: 
            raise ValueError("Temperature is not set in the arguement of humidDensity()") 
        elif relHumidity==None: 
            raise ValueError("Relative humidity is not set in the arguement of humidDensity()") 
        elif pressure==None: 
            raise ValueError("Air pressure is not set in the arguement of humidDensity()") 
        elif relHumidity < 0 or relHumidity > 100: 
            raise ValueError("Relative humidity is out of range")
        temperature.toC(); pressure.toPa() 
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        # satpressure=Saturated vapor pressure at the given temperature 
        satpressure=satVaporPressure(temperature); satpressure.toPa() 
        y=relHumidity*satpressure.getValue()/(100*pressure.getValue()) 
        temperature.toK();pressure.toPa()
    except Exception as e: print(e)
    else:
        return ((1-0.37817*y)*0.0034817*pressure.getValue()/temperature.getValue(),'kgHA/m3') 
        #0.37817=(29.847-18)/28.947; 0.0034847=28.947/8.314*1000 



# humidMolarMass() calculates the molar mass of humid air (g/mol) 
# at the given dry bulb temperature(C), relative humidity and humid air pressure 
# Function No:14
def humidMolarMass(temperature=None, relHumidity=None, pressure=None): 
    try:
        if temperature==None: 
            raise ValueError("Temperature is not set in the arguement of humidMolarMass()") 
        elif relHumidity==None: 
            raise ValueError("Relative humidity is not set in the arguement of humidMolarMass()") 
        elif pressure==None: 
            raise ValueError("Pressure arguement value is not set in humidMolarMass()") 
        elif relHumidity < 0 or relHumidity > 100: 
            raise ValueError("Relative humidity is out of range")
        temperature.toC()
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        y=moleFraction(temperature, relHumidity, pressure) 
    except Exception as e: print(e)
    else:
        return ((1-y)*28.947+y*18, 'g/mol')


	
# wetBulbTemperature() calculates wet bulb temperature when dry bulb temperature(C), 
# atmospheric pressure(Pa) and relative humidity(%) are given 
# Method:Following constant wet bulb temperature line 
# Function No:15
def wetBulbTemperature(temperature=None, relHumidity=None, pressure=None): 
    try:
        if temperature==None: 
	        raise ValueError("Temperature is not set in the argument of wetBulbTemperature()") 
        elif relHumidity==None: 
            raise ValueError("Relative humidity is not set in the argument of wetBulbTemperature()") 
        elif pressure==None: 
            raise ValueError("Air pressure is not set in the argument of wetBulbTemperature()") 
        elif relHumidity<0 or relHumidity>100: 
            raise ValueError("Incorrect value of Relative humidity") 
		
        if relHumidity==100: return temperature 
        temperature.toC(); pressure.toPa()
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        # gradient of wet bulb temperature line=-0.00041667 (kg moisture/kg DA)/degC 
        # pp=partial pressure; x,x0=mass fraction;x=x0-0.00041667(t-temperature) 
        x0=massFraction(temperature, relHumidity, pressure)[0] 
        new_temp = Temperature(0.8*temperature.getValue(),'C')

        dewpoint=dewPoint(temperature,relHumidity); new_dewpoint=Temperature(dewpoint.getValue(),'C') 
        while True: 
            x=x0-0.00041667*(new_temp.getValue()-temperature.getValue()) 
            y=x/(0.6218+x) 
            pp=y*pressure.getValue() 
            satpressure=satVaporPressure(new_temp); satpressure.toPa() 
            new_RH=pp*100/satpressure.getValue() 
            if new_RH>99.5 and new_RH<100.5:break 
            elif new_RH>100: 
                new_temp=Temperature(new_temp.getValue()*1.1,'C') 
                continue 
            new_dewpoint=dewPoint(new_temp,new_RH) 
            new_temp=Temperature(0.9*new_temp.getValue(),'C') 
            if new_temp.getValue()>new_dewpoint.getValue(): 
                diff=new_temp.getValue()-new_dewpoint.getValue() 
                new_temp=Temperature(0.9*new_temp.getValue(),'C') 
            elif new_temp.getValue()==new_dewpoint.getValue(): break 
            else: 
                diff = new_dewpoint.getValue() - new_temp.getValue()
                new_temp=Temperature(new_temp.getValue()*1.1,'C') 
            if diff < 0.00001: break 
    except Exception as e: print(e)
    else: return new_temp 


# calculateWetBulbTemp() calculates wet bulb temperature when dry bulb temperature(C), 
# atmospheric pressure(Pa) and relative humidity(%) are given 
# Method: Ferrel Equation
#     Pw=Psat,wb - A*P*(T-Twb) where A=0.0006666667(1+0.00115*Twb) 
# Function No:16
def calculateWetBulbTemperature(temperature=None, relHumidity=None, pressure=None):
    try: 
        if temperature==None: 
	        raise ValueError("Temperature is not set in the argument of calculateWetBulbTemp()") 
        elif relHumidity==None: 
            raise ValueError("Relative humidity is not set in the argument of calculateWetBulbTemp()") 
        elif pressure==None: 
            raise ValueError("Air pressure is not set in the argument of calculateWetBulbTemp()") 
        elif relHumidity<0 or relHumidity>100: 
            raise ValueError("Incorrect value of Relative humidity")		
        if relHumidity==100: return temperature
		
        temperature.toC(); pressure.toPa()
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        sat_pressue=satVaporPressure(temperature); sat_pressue.toPa()
        Twb_old = Temperature(0,'C')	# in C
        Twb_new = Temperature(0.7*temperature.getValue(),'C') # in C
        while abs(Twb_old.getValue()-Twb_new.getValue()) > 0.000001:
            A=0.0006666667*(1+0.00115*Twb_new.getValue())
            drybulb_pp=Pressure(relHumidity*sat_pressue.getValue()/100,'Pa',True)
            wetbulbsatp_value=drybulb_pp.getValue() + A*pressure.getValue()*(temperature.getValue()-Twb_new.getValue())
            wetbulbsatp=Pressure(wetbulbsatp_value,'Pa',True)
            Twb_old=Twb_new;
            Twb_new=satTemperature(wetbulbsatp)
    except Exception as e: print(e) 
    else: return Twb_new




# ------------------------------------ --------------------- 
# Enthalpy Change in Air 
# ------------------------------------ --------------------- 
# Reference State: water(liquid,273.15K,1 atm), 02, N2, Ar, CO2(gas,273.15,1 atm) 
# Critical data: 
#     H20(Tc=647.3K,Pc=220.5bar,Zc=0.229,w=0.344) 
#     02(Tc=154.6K,Pc=50.5bar,Zc=0.288,w=0.021) 
#     N2(Tc=126.2K,Pc=33.9bar,Zc=0.290,w=0.04) 
#     Ar(Tc=150.8K,Pc=48.7bar,Zc=0.291,w=0) 
#     CO2(Tc=304.2K,Pc=73.8bar,Zc=0.274,w=0.225) 
# At 25C, delHv (Enthalpy of evaporation) for H20=2442.5 J/g=43965 J/mol; at 100C, delHv=2257 J/g=40626 J/mol 
# Cp/R=A+B*1-+C.T..2+D/T.'2; T in K. Ref. Temperature=298 K 
# avg, <Cp>/R=INT(CpdT,T,298.15)=A+0.5.B*(T+298.15)+C.(T*2+298.15**2+298.15*T)/31-0/(298.15*TY 
# delH=<Cp>*(T-298.15)*R+H2-H1 
# resudal enthalpy for gas, Hr.(0.083-1.097/Tr**1.6)+w*(0.139-0.894/Tr**4.2) where Tr=T/Tc 

# resudualEnthalpy(T,P,Tc,Pc,w) calculates resudal enthalpy at the given temperature
# and pressure using the critical thermodynamic data
# Function No:17
def resudualEnthalpy(T,P,Tc,Pc,w): 
    T.toK(); Tc.toK(); P.toBar(); Pc.toBar() 
    R=8.314; Tr = T.getValue()/Tc.getValue(); Pr = P.getValue()/Pc.getValue() 
    return (((0.083-1.097/Tr**1.6)+w*(0.139-0.894/Tr**4.2))*Pr*R*Tc.getValue(),'J/mol') 


# delHH2O() calculates enthalpy change of water vapor in J/mol 
# at the given temperature with respect to the room temperature (298.15 K) 
# Function No:18
def delHH2O(temperature,pressure): 
    temperature.toK(); pressure.tobar() 
    T=temperature.getValue();
    CpIntegralWater=8.712+0.00125*(273.15+298.15)/2-0.00000018*(298.15*298.15+273.15*273.15+298.15*273.15) 
    HO = CpIntegralWater*25*8.314+43965 # J/mol 
    if T==298.15: return (HO,'J/mol')
    CpIntegral = 3.47+0.000725*(T+298.15)-12100/(298.15*T) 
    Tc=Temperature(647.3,'K'); Pc=Pressure(220.5,'bar'); w=0.344 
    H2=resudualEnthalpy(temperature,pressure,Tc,Pc,w)[0] 
    H1=resudualEnthalpy(Temperature(298.15,'K'),pressure,Tc,Pc,w)[0] 
    return (HO+CpIntegral*(T-298.15)*8.314 + H2-H1,'J/mol')

	
# de1HO2() calculates enthalpy change of oxygen gas in )/mol 
# at the given temperature with respect to the room temperature (298.15 K) 
# Function No:19
def de1HO2(temperature,pressure): 
    temperature.toK(); pressure.tobar() 
    T=temperature.getValue();
    if T==298.15: return (0,'J/mol')
    CpIntegral = 3.639 + 0.000506*(T+298.15)-22700/(298.15*T) 
    Tc = Temperature(154.6,'K'); Pc=Pressure(50.5,'bar'); w=0.021 
    H2=resudualEnthalpy(temperature,pressure,Tc,Pc,w)[0] 
    H1=resudualEnthalpy(Temperature(298.15,'K'),pressure,Tc,Pc,w)[0] 
    return (CpIntegral*(T-298.15)*8.314+H2-H1,'J/mol')


# delHN2() calculates enthalpy change of nitrogen gas in J/mol 
# at the given temperature with respect to the room temperature (298.15 K) 
# Function No:20
def delHN2(temperature,pressure): 
    temperature.toK(); pressure.tobar() 
    T=temperature.getValue();
    if T==298.15: return (0,'J/mol')	
    CpIntegral=3.280+0.000593*(T+298.15)+4000/(298.15*T) 
    Tc=Temperature(126.2,'K'); Pc=Pressure(33.9,'bar'); w=0.04 
    H2=resudualEnthalpy(temperature,pressure,Tc,Pc,w)[0] 
    H1=resudualEnthalpy(Temperature(298.15,'K'),pressure,Tc,Pc,w)[0] 
    return (CpIntegral*(T-298.15)*8.314+H2-H1,'J/mol') 


# delHCO2() calculates enthalpy change of carbon dioxide gas in J/mol 
# at the given temperature with respect to the room temperature (298.15 K) 
# Function No:21
def delHCO2(temperature,pressure): 
    temperature.toK(); pressure.tobar() 
    T=temperature.getValue();
    if T==298.15: return (0,'J/mol')	
    CpIntegral=5.457*0.001045*(T+298.15)-115700/(298.15*T) 
    Tc=Temperature(304.2,'K'); Pc=Pressure(73.8,'bar'); w=0.225 
    H2=resudualEnthalpy(temperature,pressure,Tc,Pc,w)[0] 
    H1=resudualEnthalpy(Temperature(298.15,'K'), pressure, Tc, Pc, w)[0] 
    return (CpIntegral*(T-298.15)*8.314+H2-H1,'J/mol') 


# delHAr() calculates enthalpy change of argon gas in J/mol 
# at the given temperature with respect to the room temperature (298.15 K) 
# Function No:22
def delHAr(temperature,pressure): 
    temperature.toK(); pressure.tobar() 
    T=temperature.getValue();
    if T==298.15: return (0,'J/mol')
    CpIntegral=2.5001 
    Tc=Temperature(150.8,'K'); Pc=Pressure(48.7,'bar'); w=0 
    H2=resudualEnthalpy(temperature,pressure,Tc,Pc,w)[0] 
    H1=resudualEnthalpy(Temperature(298.15,'K'),pressure,Tc,Pc,w)[0] 
    return (CpIntegral*(T-298.15)*8.314+H2-H1,'J/mol') 
	
	
# delHDryAir() calculates enthalpy change of dry air in J/mol 
# at the given temperature with respect to the standard temperature (298.15 K) 
# Function No:23
def delHDryAir(temperature,pressure): 
    temperature.toK(); pressure.tobar() 
    T=temperature; P=pressure 
    delH=de1HO2(T,P)[0]*0.2095+delHN2(T,P)[0]*0.7809+delHAr(T,P)[0]*0.0092+delHCO2(T,P)[0]*0.0004 
    return (delH,'J/mol')
	
	
# delHHumidAir() calculates enthalpy change of humid air in J/mol 
# at the given temperature with respect to the room temperature (298.15 K) 
# Function No:24
def delHHumidAir(temperature=None, relHumidity=None, pressure=None): 
    if temperature==None: 
        raise ValueError("Temperature is not set in the argument of delHHumidAir()") 
    elif relHumidity==None: 
        raise ValueError("Relative humidity is not set in the argument of delHHumidAir()") 
    elif pressure==None: 
        raise ValueError("Air pressure is not set in the argument of delHHumidAir()") 
    elif relHumidity<0 or relHumidity>100: 
        raise ValueError("Incorrect value of Relative humidity") 
    temperature.toC()
    if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
    y=moleFraction(temperature, relHumidity, pressure) 
    temperature.toK(); 
    delH=(1-y)*delHDryAir(temperature,pressure)[0] + y*delHH2O(temperature,pressure)[0] 
    return (delH,'J/mol') 



# humidSaturationEnthalpy() calculates saturation enthalpy of humid air in kJ/kgDA 
# at the given saturated temperature at which relative humidity is 100% 
# (Ref. Temp.=273.15K)
# Function No:25
def humidSaturationEnthalpy(temperature=None,pressure=Pressure(1,'atm')):
    try:
        if temperature==None: 
            raise ValueError("Temperature is not set in the argument of humidSaturationEnthalpy()") 
        elif pressure==None: 
            raise ValueError("Air pressure is not set in the argument of humidSaturationEnthalpy()") 
        relHumidity=100;
        temperature.toC()
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        y=moleFraction(temperature, relHumidity, pressure)
        molarmassha=humidMolarMass(temperature, relHumidity, pressure)[0]
        x=massFraction(temperature, relHumidity, pressure)[0]
        temperature.toK(); 
        delH=(1-y)*delHDryAir(temperature,pressure)[0] + y*delHH2O(temperature,pressure)[0]
    except Exception as e:print(e)
    else:	
        # Enthalpy correction (Reference Temperature Correction)
	    # At 273.15 (0C), enthalpy=9.47 kJ/kgDA, humid air enthalpy = -16.883390422273617 kJ/kgDA
        zero_correction=26.35339042
        return (zero_correction + delH/(molarmassha*(1-x)),'kJ/kgDA')



# humidAirEnthalpy() calculates enthalpy of unsaturated humid air in kJ/kgDA 
# at the given dry bulb temperature, humidity and pressure 
# (Ref. Temp. = 273.15K = 0C)
# Function No:26
def humidAirEnthalpy(temperature=None, relHumidity=None, pressure=None):
    try:
        if temperature==None: 
            raise ValueError("Temperature is not set in the argument of humidAirEnthalpy()") 
        elif relHumidity==None: 
            raise ValueError("Relative humidity is not set in the argument of humidAirEnthalpy()") 
        elif pressure==None: 
            raise ValueError("Air pressure is not set in the argument of humidAirEnthalpy()") 
        elif relHumidity<0 or relHumidity>100: 
            raise ValueError("Incorrect value of Relative humidity")
        temperature.toC()
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        wetbulbtemp=wetBulbTemperature(temperature, relHumidity, pressure)
    except Exception as e:print(e)
    else:
        return humidSaturationEnthalpy(wetbulbtemp,pressure)


# dryAirEnthalpy() calculates enthalpy change of dry air in kJ/kgDA 
# at the given temperature with respect to the standard temperature (273.15 K) 
# Function No:27
def dryAirEnthalpy(temperature=None,pressure=None):
    try:
        if temperature==None: 
            raise ValueError("Temperature argument of dryAirEnthalpy() is not set") 
        elif pressure==None: 
            raise ValueError("Air pressure argument of dryAirEnthalpy() is not set") 
        temperature.toK(); pressure.tobar() 
        T=temperature; P=pressure 
        delH=de1HO2(T,P)[0]*0.2095+delHN2(T,P)[0]*0.7809+delHAr(T,P)[0]*0.0092+delHCO2(T,P)[0]*0.0004 
        # Current Reference Level = 25C, Change it to 0C; 
        zero_correction= 26.273618984842212
    except Exception as e:print(e)
    else: return (zero_correction + delH/28.947,'kJ/kgDA')	



# waterVaporEnthalpy() calculates enthalpy change of dry air in kJ/kgDA 
# at the given temperature with respect to the standard temperature (298.15 K) 
# Function No:28
def waterVaporEnthalpy(temperature=None,relHumidity=None,pressure=None):
    try:
        if temperature==None: 
            raise ValueError("Temperature is not set in the argument of waterVaporEnthalpy()") 
        elif relHumidity==None: 
            raise ValueError("Relative humidity is not set in the argument of waterVaporEnthalpy()") 
        elif pressure==None: 
            raise ValueError("Air pressure is not set in the argument of waterVaporEnthalpy()") 
        elif relHumidity<0 or relHumidity>100: 
            raise ValueError("Incorrect value of Relative humidity") 
        temperature.toC()
        if temperature.getValue()<0:raise ValueError("Temperature is out of valid range (0-150C)")
        temperature.toK(); pressure.tobar() 
        T=temperature; P=pressure
    except Exception as e:print(e)
    else: return (absoluteHumidity(T, relHumidity,P)[0]*delHH2O(T,P)[0]/18,'kJ/kgDA')
	