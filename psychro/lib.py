'''
Module Name:'lib'
Path:'<package_root>/lib'
Version:'1.0.0.2023.02.10'
Author:'A K M Aminul Islam'
Author_Email:'aminul71bd@gmail.com'
Company:'Newtonia Ltd'
Last Update:2022/02/14
Description:"This module, lib.py is used as the gateway module of the package \
    'psychro'. It calles all the classes and modules necessary to the usersto \
    from the src directory and forwards to the users. "
'''
# import necessary modules
from __future__ import division
from psychro.src.Pressure import Pressure
from psychro.src.Temperature import Temperature
import psychro.src.psychro_functions as psyf

# Module version
__version__='1.0.0.2023.02.10'
version='1.0.0.2023.02.10'



# satVaporPressure() returns saturated vapor pressure in mHg 
# at the given temperature between 0 to 150 C
def satVaporPressure(temperature=None):
    return psyf.satVaporPressure(temperature)


# satTemperature() returns saturated temperature in Celcius 
# at the given vapor pressure in mHg unit
def satTemperature(vaporPressure=None):
    return psyf.satTemperature(vaporPressure)


# dryAirPressure(T) calculates the pressure of dry air in Pa at the given temperature
def dryAirPressure(temperature=None):
    return psyf.dryAirPressure(temperature)


# humidAirPressure(temperature) calculates the total pressure in Pa exerted by
# water vapor and dry air in a closed system
def humidAirPressure(temperature = None, relHumidity = None):
    return psyf.humidAirPressure(temperature, relHumidity)


# dewPoint() calculates dew point which is the temperature(C) at which air turns
# saturated by cooling with the current content of water vapor. 
# It is also called saturated temperature. 
def dewPoint(temperature = None, relHumidity = None):
    return psyf.dewPoint(temperature, relHumidity)


# saturatedTemperature() returns dew point
def saturatedTemperature(temperature = None, relHumidity = None):
    return psyf.saturatedTemperature(temperature, relHumidity)


# partialPressure() calculates partial pressure of water vapor in air when dry 
# bulb temperature(C) and relative humidity are given
def partialPressure(temperature=None, relHumidity=None):
    return psyf.partialPressure(temperature, relHumidity)


# relativeHumidity() calculates relative humidity when dry bulb temperature(C) 
# and dewpoint are given
def relativeHumidity(temperature=None, dewpoint=None):
    return psyf.relativeHumidity(temperature, dewpoint)


# moleFraction() calculates the ratio of moles of water vapor in air to 
# the moles of wet air molecules when dry bulb temperature(C), relative humidity  
# are given (moles of vapor/moles of wet air)
def moleFraction(temperature=None, relHumidity=None, pressure=None):
    return psyf.moleFraction(temperature, relHumidity, pressure)


# absoluteHumidity = mass of vapor / mass of dry air (kgV/kgDA)
def absoluteHumidity(temperature=None, relHumidity=None, pressure=None):
    return psyf.absoluteHumidity(temperature, relHumidity, pressure)


# moistureContent = mass of vapor / mass of dry air (kgV/kgDA)
def moistureContent(temperature=None, relHumidity=None, pressure=None):
    return psyf.moistureContent(temperature, relHumidity, pressure)


# humidityRatio = mass of vapor / mass of dry air (kgV/kgDA)
def humidityRatio(temperature=None, relHumidity=None, pressure=None):
    return psyf.moistureContent(temperature, relHumidity, pressure)


# specificHumidity = mass of vapor / mass of dry air (kgV/kgDA)
def specificHumidity(temperature=None, relHumidity=None, pressure=None):
    return psyf.moistureContent(temperature, relHumidity, pressure)
	

# massFraction() calculates the mass ratio of water vapor to dry air  when dry 
# bulb temperature(C), relative humidity and pressure are given (kgV/kgHA) 
def massFraction(temperature=None, relHumidity=None, pressure=None):
    return psyf.massFraction(temperature, relHumidity, pressure)


# volumetricHumidity() calculates the mass of water vapor per unit volume (kgV/m3) 
# of humid air when dry bulb temperature(C), relative humidity and pressure are given 
def volumetricHumidity(temperature=None, relHumidity=None, pressure=None):
    return psyf.volumetricHumidity(temperature, relHumidity, pressure)


# vaporDensity() is same as volumetricHumidity(); unit:kgV/m3
def vaporDensity(temperature=None, relHumidity=None, pressure=None):
    return psyf.vaporDensity(temperature, relHumidity, pressure)


# humidVolume() calculates the volume of humid air per unit mass (m3/kgDA) 
# of dry air when dry bulb temperature(C), relative humidity and humid air pressure are given 
def humidVolume(temperature=None, relHumidity=None, pressure=None):
    return psyf.humidVolume(temperature, relHumidity, pressure)


# humidDensity() calculates the mass of humid air per unit volume of humid air (kgHA/m3) 
# when dry bulb temperature(C), relative humidity and humid air pressure are given 
def humidDensity(temperature=None, relHumidity=None, pressure=None):
    return psyf.humidDensity(temperature, relHumidity, pressure)


# humidMolarMass() calculates the molar mass of humid air (g/mol) 
# at the given dry bulb temperature(C), relative humidity and humid air pressure 
def humidMolarMass(temperature=None, relHumidity=None, pressure=None): 
    return psyf.humidMolarMass(temperature, relHumidity, pressure)


# wetBulbTemperature() calculates wet bulb temperature when dry bulb temperature(C), 
# atmospheric pressure(Pa) and relative humidity(%) are given 
def wetBulbTemperature(temperature=None, relHumidity=None, pressure=None):
    return psyf.wetBulbTemperature(temperature, relHumidity, pressure)


# humidSaturationEnthalpy() calculates saturation enthalpy of humid air in kJ/kgDA 
# at the given saturated temperature at which relative humidity is 100% 
# (Ref. Temp. = 298.15K = 25C) 
def humidSaturationEnthalpy(temperature=None,pressure=Pressure(1,'atm')):
    return psyf.humidSaturationEnthalpy(temperature,pressure)


# humidAirEnthalpy() calculates enthalpy of unsaturated humid air in kJ/kgDA 
# at the given dry bulb temperature, relative humidity and pressure 
# (Ref. Temp. = 298.15K = 25C) 
def humidAirEnthalpy(temperature=None, relHumidity=None, pressure=None):
    return psyf.humidAirEnthalpy(temperature, relHumidity, pressure)


# dryAirEnthalpy() calculates enthalpy change of dry air in kJ/kgDA 
# at the given temperature with respect to the standard temperature (273.15 K) 
def dryAirEnthalpy(temperature=None,pressure=None):
    return psyf.dryAirEnthalpy(temperature,pressure)


# waterVaporEnthalpy() calculates enthalpy change of water vapor in kJ/kgDA 
# at the given temperature with respect to the standard temperature (298.15 K) 
def waterVaporEnthalpy(temperature=None,relHumidity=None,pressure=None):
    return psyf.waterVaporEnthalpy(temperature,relHumidity,pressure)
