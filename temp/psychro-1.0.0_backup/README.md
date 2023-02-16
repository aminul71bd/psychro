## psychro-1.0.0 (Soft Version of Psychrometric Chart)

Psychrometric chart provides physical and thermal properties of moist air in graphical form. Psychrometric data are used in agriculture, in weather forecasting, in refrigeration, and in many process industries. Chemical and mechanical engineers use this chart very frequently. This python package, named psychro, calculates these data using the standard thermodynamic equations. Normally, the psychrometric chart is designed to work at one atmospheric pressure. But, this software is capable of calculating the atmospheric pressures at different temperatures and humidities; thus it can calculate the psychrometric data at different pressures. Although, the psychrometric chart is used in open system where pressure remains constant, this software can be applied both in closed and open system.

Although, the psychrometric chart is used in open system where pressure is constant, this software can be applied both in closed and open system.


'lib' module of psychro package provides all the necessary functions and classes required to calculate the psychrometric data. This module is the heart of this package. 
```python
>>>
>>> import psychro.lib as lib
>>> p1=lib.Pressure(1.5,'atm')
>>> t1=lib.Temperature(60,'C')
>>>
>>> print(p1)
PRESSURE: 1.5 atm absolute
>>>
>>> print(t1)
TEMPERATURE: 60 degree C
>>>
>>> lib.dewPoint(t1,relHumidity=50)
45.752545369208406 C
>>>
>>> lib.wetBulbTemperature(t1,relHumidity=50,pressure=lib.Pressure(1,'atm'))
46.10860848000002 C
>>>
```

Typing 'lib' all the time can be avoided by importing all the resources of 'lib' module by using '*'. For example,
```python
>>> from psychro.lib import *
>>> p1=Pressure(1.5,'atm')
>>> t1=Temperature(60,'C')
>>> print(p1)
PRESSURE: 1.5 atm absolute
>>> print(t1)
TEMPERATURE: 60 degree C
>>>
>>> dewPoint(t1,relHumidity=50)
45.752545369208406 C
>>>
>>> wetBulbTemperature(t1,relHumidity=50,pressure=Pressure(1,'atm'))
46.10860848000002 C
>>>
```


 
## Introduction to Pressure class
Pressure class is used to create pressure object. This class has methods to convert from 
one unit to another. Supported pressure units are Pa(pascal), bar(barometric pressure), 
atm(atmospheric pressure), mHg(meter mercury pressure), psi(pound force per square inch), 
and torr(1 atm/760).
<!-- table -->
| **Method** | **Method Description** |
| --- | ---|
| \_\_init\_\_ (self,value=25,unit='Pa',is_absolute=True) | class constructor; numeric value, unit and pressure type (absolute or partial) are to be given. Supported units are Pa, bar, atm, mHg, psi, and torr. is_absolute is True means absolute pressure and is False means relative pressure  |
| changeValue(self,value=25,is_absolute=True) | previous pressure value can be changed by giving new value |
| getValue(self) | returns cuurent value |
| getUnit(self) | returns cuurent unit |
| getUnitPrefix(self) | returns unit prefix which is usually 1 |
| getQuantity(self) | returns type of physical quantity which is PRESSURE |
| isAbsolute(self) | returns boolean value; True means absolute pressure and False means relative |
| \_\_repr\_\_ (self) | returns pascal (Pa) value |
| \_\_str\_\_(self) | returns string representation of Pressure class |
| \_\_resolve_unit(self,unit='Pa',quantity='Pressure') | resolves the given unit string into prefix and unit |
| copy(self) | returns a deep copy of Pressure object |
| toPa(self) or topa(self) | changes the current unit to Pa; pressure value is changed accordingly |
| tobar(self) or toBar(self) | changes the current unit to bar; pressure value is changed accordingly; 1 bar = 100 kPa |
| toatm(self) or toAtm(self) | changes the current unit to atm; pressure value is changed accordingly; 1 atm = 101325 Pa |
| tomhg(self) or tomHg(self) | changes the current unit to mHg; pressure value is changed accordingly; 1 atm = 760 mmHg |
| topsi(self) or toPsi(self) | changes the current unit to psi; pressure value is changed accordingly; 14.696 psi = 1 atm |
| totorr(self) or toTorr(self) | changes the current unit to torr; pressure value is changed accordingly; 1 torr = 101325/760 Pa |

### Examples on the usage of Pressure class
```python
>>>
>>> from psychro.lib import *
>>>
>>> p1=Pressure(12.5,'megapascals')
>>> p1
12500000.0 Pa
>>> print(p1)
PRESSURE: 1.25e+07 pascals absolute
>>> p1.getValue()
12500000.0
>>> p1.getUnit()
'pascals'
>>> p1.getUnitPrefix()
1
>>> p1.isAbsolute()
True
>>> p1.toatm(); print(p1)
PRESSURE: 123 atm absolute
>>> p1.tobar(); print(p1)
PRESSURE: 125 bar absolute
>>> p1.tomHg(); print(p1)
PRESSURE: 93.8 mHg absolute
>>> p1.topsi(); print(p1)
PRESSURE: 1.81e+03 psi absolute
>>> p1.totorr(); print(p1)
PRESSURE: 9.38e+04 torr absolute
>>>
>>> p1.toPa()
>>> print(p1)
PRESSURE: 1.25e+07 Pa absolute
>>>

```

## Introduction to Temperature class
Temperature class is used to create temperature object. This class has methods to convert from one unit to another. Supported temperature units are C(Celcius), K(Kelvin), and F(Fahrenheit). Methods to access its value and units are also available.
<!-- table -->
| **Method** | **Method Description** |
| --- | ---|
| \_\_init\_\_ (self,value=25,unit='C') | class constructor; numeric value and unit are to be given. Supported units are C, K and F. Units in literal format are also supported; like Celcius, Kelvin, Fahrenheit  |
| changeValue(self,value=25) | previous temperature value can be changed by giving new value |
| getValue(self) | returns cuurent value |
| getUnit(self) | returns cuurent unit |
| getUnitPrefix(self) | returns unit prefix which is usually 1 |
| getQuantity(self) | returns type of physical quantity which is TEMPERATURE |
| \_\_repr\_\_ (self) | returns celcius (C) value |
| \_\_str\_\_(self) | returns string representation of Temperature class |
| \_\_resolve_unit(self,unit='C',quantity='Temperature') | resolves the given unit string into prefix and unit |
| copy(self) | returns a deep copy of Temperature object |
| toC(self) | changes the current unit to C; temperature value is changed accordingly |
| toK(self) | changes the current unit to K; temperature value is changed accordingly; T(K) = T(C) + 273.15 |
| toF(self) | changes the current unit to F; temperature value is changed accordingly; T(F) = 1.8*T(C) + 32 |


### Examples on the usage of Pressure class
```python
>>>
>>> t1=lib.Temperature(78,'C')
>>> t1.getValue()
78
>>> print(t1)
TEMPERATURE: 78 degree C
>>> t1.getValue()
78
>>> t1.getUnit()
'C'
>>> t1.getUnitPrefix()
1
>>> t1.getQuantity()
'TEMPERATURE'
>>> t1.toK(); print(t1)
TEMPERATURE: 351.15 degree K
>>> t1.toF(); print(t1)
TEMPERATURE: 172.4 degree F
>>> t1.toC(); print(t1)
TEMPERATURE: 78 degree C
>>>
>>>
>>> t1.changeValue(60)
>>> t1; print(t1)
60 C
TEMPERATURE: 60 degree C
>>> t1.toF(); print(t1)
TEMPERATURE: 140 degree F
>>> t1.toK(); print(t1)
TEMPERATURE: 333.15 degree K
>>> t1.toC(); print(t1)
TEMPERATURE: 60 degree C
>>>
>>>
>>> t1=lib.Temperature(78,'cC')
>>> t1;print(t1)
0.78 C
TEMPERATURE: 0.78 degree C
>>>
```


## Introduction to Psychrometric Functions
The available psychrometric functions are presented and described in the following table:
<!-- table -->
| **Function** | **Description** |
| --- | --- |
| satVaporPressure(temperature=None) | returns saturated pure water vapor pressure at the given temperatue by Antoine equation; Temperature range: 0 - 150 C |
| satTemperature(vaporPressure=None) | returns saturated pure water vapor temperature at the given vapor pressure by Antoine equation; Pressure range: 608 - 476934.84 Pa |
| dryAirPressure(temperature=None) | returns pressure of dry air at the given temperatue considering air as ideal gas |
| humidAirPressure(temperature = None, relHumidity = None) | returns pressure of air-water vapor mixture at the given temperatue and relative humidity |
| dewPoint(temperature = None, relHumidity = None) | returns dewpoint of air-vapor mixture pressure at the given temperatue and relative humidity; dewpoint is a saturated temperature reached by cooling |
| saturatedTemperature(temperature = None, relHumidity = None) | returns dewpoint of air-vapor mixture pressure at the given temperatue and relative humidity; dewpoint is a saturated temperature reached by cooling |
| partialPressure(temperature=None, relHumidity=None) | returns partial pressure of water vapor in the humid air at the given temperatue and relative humidity; Partial pressure is the ratio of the pressure of water vapor to the pressure of humid air |
| relativeHumidity(temperature=None, dewpoint=None) | returns relative humidity when the dry bulb temperature and dewpoint are known |
| moleFraction(temperature=None, relHumidity=None, pressure=None) | returns mole fraction of water vapor at the given temperature, relative humidity and pressure of humid air |
| absoluteHumidity(temperature=None, relHumidity=None, pressure=None); moistureContent(temperature=None, relHumidity=None, pressure=None); humidityRatio(temperature=None, relHumidity=None, pressure=None); specificHumidity(temperature=None, relHumidity=None, pressure=None)  | returns absolute humidity of water vapor at the given temperatue, relative humidity and humid air pressure; absolute humidity, moisture content, humidity ratio and specific humidity, all have the same definition, but just called differently; Usually expressed in kg/kgDA |
| massFraction(temperature=None, relHumidity=None, pressure=None) | returns the ratio of mass of water vapor to the mass of humid air |
| volumetricHumidity(temperature=None, relHumidity=None, pressure=None) | returns the mass of water vapor per unit volume of humid air (kgV/m3) when dry bulb temperature(C), relative humidity and pressure are given |
| vaporDensity(temperature=None, relHumidity=None, pressure=None) | returns the mass of water vapor per unit volume of humid air; Same as volumetricHumidity() |
| humidVolume(temperature=None, relHumidity=None, pressure=None) | returns the volume of humid air per unit mass of dry air (m3/kgDA) at the given temperature, relative humidity and pressure of humid air |
| humidDensity(temperature=None, relHumidity=None, pressure=None) | returns the mass of humid air per unit volume of humid air (kgHA/m3HA) at the given temperature, relative humidity and pressure of humid air |
| humidMolarMass(temperature=None, relHumidity=None, pressure=None) | returns the molar mass of humid air in g/mol at the given temperature, relative humidity and pressure of humid air |
| wetBulbTemperature(temperature=None, relHumidity=None, pressure=None) | returns the wet bulb temperature of humid air at the given temperature, relative humidity and pressure of humid air |
| humidAirEnthalpy(temperature=None, relHumidity=None, pressure=None) | returns the enthalpy of unsaturated humid air in kJ/kgDA at the given temperature, relative humidity and pressure of humid air; Reference Temperature = 0 C (273.15 K) |
| humidSaturationEnthalpy(temperature=None, pressure=None) | returns the enthalpy of saturated humid air in kJ/kgDA at the given temperature and pressure of humid air; Reference Temperature = 0 C (273.15 K) |
| dryAirEnthalpy(temperature=None, pressure=None) | returns the enthalpy of dry air in kJ/kgDA at the given temperature and pressure of humid air; Reference Temperature = 0 C (273.15 K) |
| waterVaporEnthalpy(temperature=None, relHumidity=None, pressure=None) | returns the enthalpy change of water vapor in kJ/kgDA at the given temperature, relative humidity and pressure of humid air |


```python
>>>
>>> lib.satVaporPressure(Temperature(0,'C'))
608.8740825940683 Pa
>>> lib.satVaporPressure(Temperature(50,'C'))
12336.689499395537 Pa
>>> lib.satVaporPressure(Temperature(100,'C'))
101322.73929367663 Pa
>>> lib.satVaporPressure(Temperature(150,'C'))
476934.8434661128 Pa
>>>
>>>
>>> lib.satTemperature(Pressure(1,'atm'))
100.00062490553529 C
>>> lib.satTemperature(Pressure(2,'atm'))
120.63567606164924 C
>>> lib.satTemperature(Pressure(0.1,'atm'))
46.087519471291785 C
>>> lib.satTemperature(Pressure(0.01,'atm'))
7.192558576513591 C
>>>
>>>
>>> lib.dryAirPressure(Temperature(0,'C'))
94435.33250266408 Pa
>>> lib.dryAirPressure(Temperature(-10,'C'))
90978.06241287224 Pa
>>> lib.dryAirPressure(Temperature(50,'C'))
111721.68295162327 Pa
>>> lib.dryAirPressure(Temperature(100,'C'))
129008.03340058247 Pa
>>> lib.dryAirPressure(Temperature(150,'C'))
146294.3838495417 Pa
>>>
>>> p1=lib.dryAirPressure(Temperature(150,'C'))
>>> p1.toatm(); print(p1)
PRESSURE: 1.44 atm absolute
>>>
>>>
>>>
>>> lib.humidAirPressure(Temperature(20,'C'), relHumidity=50)
103687.02142750715 Pa
>>> lib.humidAirPressure(Temperature(40,'C'), relHumidity=50)
115641.35974691421 Pa
>>> lib.humidAirPressure(Temperature(80,'C'), relHumidity=50)
169457.32024437035 Pa
>>> lib.humidAirPressure(Temperature(80,'C'), relHumidity=75)
169457.32024437035 Pa
>>> lib.humidAirPressure(Temperature(100,'C'), relHumidity=100)
230330.7726942591 Pa
>>>
>>> p1=lib.humidAirPressure(Temperature(100,'C'), relHumidity=100)
>>>
>>> p1=lib.humidAirPressure(Temperature(100,'C'), relHumidity=100)
>>> p1
230330.7726942591 Pa
>>> p1.toatm()
>>> print(p1)
PRESSURE: 2.27 atm absolute
>>>
>>>
>>>
>>> lib.dewPoint(Temperature(41,'C'), relHumidity=10)
3.4060966713632297 C
>>> lib.dewPoint(Temperature(50,'C'), relHumidity=30)
27.63877111277918 C
>>> lib.dewPoint(Temperature(100,'C'), relHumidity=100)
100 C
>>>
>>> lib.saturatedTemperature(Temperature(41,'C'), relHumidity=10)
3.4060966713632297 C
>>> lib.saturatedTemperature(Temperature(50,'C'), relHumidity=30)
27.63877111277918 C
>>> lib.saturatedTemperature(Temperature(100,'C'), relHumidity=100)
100 C
>>>
>>>
>>> lib.saturatedTemperature(lib.Temperature(50,'C'),relHumidity=30)
27.63877111277918 C
>>> lib.saturatedTemperature(lib.Temperature(41,'C'),relHumidity=10)
3.4060966713632297 C
>>> lib.saturatedTemperature(lib.Temperature(25,'C'),relHumidity=90)
23.244673536091568 C
>>> lib.saturatedTemperature(lib.Temperature(100,'C'),relHumidity=100)
100 C
>>>
>>>
>>> lib.partialPressure(lib.Temperature(25,'C'), relHumidity = 40)
1266.9042139599371 Pa
>>> lib.partialPressure(lib.Temperature(25,'C'), relHumidity = 90)
2850.5344814098585 Pa
>>> lib.partialPressure(lib.Temperature(80,'C'), relHumidity = 30)
14209.14810701147 Pa
>>> lib.partialPressure(lib.Temperature(100,'C'), relHumidity = 100)
101322.73929367663 Pa
>>>
>>>
>>> lib.relativeHumidity(lib.Temperature(41,'C'), dewpoint=lib.Temperature(3.406,'C'))
9.999931453244884
>>> lib.relativeHumidity(lib.Temperature(50,'C'), dewpoint=lib.Temperature(27.639,'C'))
30.000401191908306
>>> lib.relativeHumidity(lib.Temperature(100,'C'), dewpoint=lib.Temperature(100,'C'))
100.0
>>>
>>>
>>> lib.moleFraction(lib.Temperature(25,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
0.012503372454576235
>>> lib.moleFraction(lib.Temperature(50,'C'), relHumidity = 80,pressure=lib.Pressure(1,'atm'))
0.09740292720963661
>>> lib.moleFraction(lib.Temperature(80,'C'), relHumidity = 80,pressure=lib.Pressure(1,'atm'))
0.37395570312062426
>>> lib.moleFraction(lib.Temperature(100,'C'), relHumidity = 100,pressure=lib.Pressure(1,'atm'))
0.9999776885633026
>>>
>>>
>>> lib.absoluteHumidity(lib.Temperature(25,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(0.007873036499963014, 'kg/kgDA')
>>> lib.absoluteHumidity(lib.Temperature(50,'C'), relHumidity = 30,pressure=lib.Pressure(1,'atm'))
(0.02357295563271035, 'kg/kgDA')
>>> lib.absoluteHumidity(lib.Temperature(50,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(0.03183287780955468, 'kg/kgDA')
>>> lib.absoluteHumidity(lib.Temperature(100,'C'), relHumidity = 100,pressure=lib.Pressure(1,'atm'))
(27868.49341804995, 'kg/kgDA')
>>>
>>>
>>> lib.humidityRatio(lib.Temperature(25,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(0.007873036499963014, 'kg/kgDA')
>>> lib.moistureContent(lib.Temperature(25,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(0.007873036499963014, 'kg/kgDA')
>>> lib.specificHumidity(lib.Temperature(25,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(0.007873036499963014, 'kg/kgDA')
>>> lib.absoluteHumidity(lib.Temperature(25,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(0.007873036499963014, 'kg/kgDA')
>>>
>>>
>>> lib.moistureContent(lib.Temperature(40,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(0.018651169036146373, 'kg/kgDA')
>>> lib.humidityRatio(lib.Temperature(40,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(0.018651169036146373, 'kg/kgDA')
>>> lib.specificHumidity(lib.Temperature(40,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(0.018651169036146373, 'kg/kgDA')
>>> lib.absoluteHumidity(lib.Temperature(40,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(0.018651169036146373, 'kg/kgDA')
>>>
>>>
>>> lib.massFraction(lib.Temperature(25,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(0.0078115359919774, 'kg/kgHA')
>>> lib.massFraction(lib.Temperature(40,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(0.018309672244124765, 'kg/kgHA')
>>> lib.massFraction(lib.Temperature(70,'C'), relHumidity = 80,pressure=lib.Pressure(1,'atm'))
(0.1687100522345388, 'kg/kgHA')
>>> lib.massFraction(lib.Temperature(90,'C'), relHumidity = 90,pressure=lib.Pressure(1,'atm'))
(0.5064969093501024, 'kg/kgHA')
>>> lib.massFraction(lib.Temperature(100,'C'), relHumidity = 100,pressure=lib.Pressure(1,'atm'))
(0.9999641184723024, 'kg/kgHA')
>>>
>>>
>>> lib.volumetricHumidity(lib.Temperature(25,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(0.009199556006115257, 'kg/m3')
>>> lib.volumetricHumidity(lib.Temperature(60,'C'), relHumidity = 70,pressure=lib.Pressure(1,'atm'))
(0.09062193055693317, 'kg/m3')
>>> lib.volumetricHumidity(lib.Temperature(90,'C'), relHumidity = 70,pressure=lib.Pressure(1,'atm'))
(0.29257655108838054, 'kg/m3')
>>> lib.volumetricHumidity(lib.Temperature(90,'C'), relHumidity = 90,pressure=lib.Pressure(1,'atm'))
(0.37616985139934644, 'kg/m3')
>>> lib.volumetricHumidity(lib.Temperature(100,'C'), relHumidity = 100,pressure=lib.Pressure(1,'atm'))
(0.5878701073852604, 'kg/m3')
>>>
>>>
>>> lib.vaporDensity(lib.Temperature(25,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(0.009199556006115257, 'kg/m3')
>>> lib.vaporDensity(lib.Temperature(60,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(0.051783960318247516, 'kg/m3')
>>> lib.vaporDensity(lib.Temperature(90,'C'), relHumidity = 70,pressure=lib.Pressure(1,'atm'))
(0.29257655108838054, 'kg/m3')
>>> lib.vaporDensity(lib.Temperature(90,'C'), relHumidity = 90,pressure=lib.Pressure(1,'atm'))
(0.37616985139934644, 'kg/m3')
>>> lib.vaporDensity(lib.Temperature(100,'C'), relHumidity = 100,pressure=lib.Pressure(1,'atm'))
(0.5878701073852604, 'kg/m3')
>>>
>>>
>>> lib.humidVolume(lib.Temperature(25,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(0.85578962229208, 'm3/kgDA')
>>> lib.humidVolume(lib.Temperature(50,'C'), relHumidity = 60,pressure=lib.Pressure(1,'atm'))
(0.9881359575088555, 'm3/kgDA')
>>> lib.humidVolume(lib.Temperature(80,'C'), relHumidity = 70,pressure=lib.Pressure(1,'atm'))
(1.4878128544467244, 'm3/kgDA')
>>> lib.humidVolume(lib.Temperature(100,'C'), relHumidity =100,pressure=lib.Pressure(1,'atm'))
(47404.954324424994, 'm3/kgDA')
>>>
>>> lib.humidVolume(lib.Temperature(100,'C'), relHumidity =101,pressure=lib.Pressure(1,'atm'))
Relative humidity is out of range
>>>
>>>
>>> lib.humidDensity(lib.Temperature(25,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(1.1776459904124514, 'kgHA/m3')
>>> lib.humidDensity(lib.Temperature(60,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(1.0274390434081908, 'kgHA/m3')
>>> lib.humidDensity(lib.Temperature(80,'C'), relHumidity = 70,pressure=lib.Pressure(1,'atm'))
(0.87534852776396, 'kgHA/m3')
>>> lib.humidDensity(lib.Temperature(100,'C'), relHumidity = 100,pressure=lib.Pressure(1,'atm'))
(0.5878981281426184, 'kgHA/m3')
>>>
>>>
>>> lib.humidMolarMass(lib.Temperature(25,'C'), relHumidity = 40,pressure=lib.Pressure(1,'atm'))
(28.810125581739754, 'g/mol')
>>> lib.humidMolarMass(lib.Temperature(25,'C'), relHumidity = 0,pressure=lib.Pressure(1,'atm'))
(28.947, 'g/mol')
>>> lib.humidMolarMass(lib.Temperature(50,'C'), relHumidity = 70,pressure=lib.Pressure(1,'atm'))
(28.014013886356594, 'g/mol')
>>> lib.humidMolarMass(lib.Temperature(90,'C'), relHumidity = 70,pressure=lib.Pressure(1,'atm'))
(23.64492130230461, 'g/mol')
>>> lib.humidMolarMass(lib.Temperature(100,'C'), relHumidity = 100,pressure=lib.Pressure(1,'atm'))
(18.000244243297526, 'g/mol')
>>>
>>>
>>> lib.wetBulbTemperature(lib.Temperature(25,'C'), relHumidity =20,pressure=lib.Pressure(1,'atm'))
12.604940843220007 C
>>> lib.wetBulbTemperature(lib.Temperature(41,'C'), relHumidity =10,pressure=lib.Pressure(1,'atm'))
19.174391280000005 C
>>> lib.wetBulbTemperature(lib.Temperature(70,'C'), relHumidity =60,pressure=lib.Pressure(1,'atm'))
57.117830783695005 C
>>> lib.wetBulbTemperature(lib.Temperature(95,'C'), relHumidity=90,pressure=lib.Pressure(1,'atm'))
82.33530586163171 C
>>> lib.wetBulbTemperature(lib.Temperature(100,'C'), relHumidity=100,pressure=lib.Pressure(1,'atm'))
100 C
>>>
>>>
>>> lib.humidAirEnthalpy(lib.Temperature(25,'C'), relHumidity=20,pressure=lib.Pressure(1,'atm'))
(36.19770058040783, 'kJ/kgDA')
>>> lib.humidAirEnthalpy(lib.Temperature(40,'C'), relHumidity=20,pressure=lib.Pressure(1,'atm'))
(65.36835384686465, 'kJ/kgDA')
>>> lib.humidAirEnthalpy(lib.Temperature(40,'C'), relHumidity=70,pressure=lib.Pressure(1,'atm'))
(125.19319528787777, 'kJ/kgDA')
>>> lib.humidAirEnthalpy(lib.Temperature(30,'C'), relHumidity=80,pressure=lib.Pressure(1,'atm'))
(85.36708092701788, 'kJ/kgDA')
>>>
>>>
>>> lib.waterVaporEnthalpy(lib.Temperature(25,'C'), relHumidity=20,pressure=lib.Pressure(1,'atm'))
(9.962115046968743, 'kJ/kgDA')
>>> lib.waterVaporEnthalpy(lib.Temperature(40,'C'), relHumidity=20,pressure=lib.Pressure(1,'atm'))
(23.661890360400825, 'kJ/kgDA')
>>> lib.waterVaporEnthalpy(lib.Temperature(40,'C'), relHumidity=70,pressure=lib.Pressure(1,'atm'))
(85.99323104194706, 'kJ/kgDA')
>>> lib.waterVaporEnthalpy(lib.Temperature(30,'C'), relHumidity=80,pressure=lib.Pressure(1,'atm'))
(55.09794791557815, 'kJ/kgDA')
>>>
>>>
>>> lib.dryAirEnthalpy(lib.Temperature(25,'C'), pressure=lib.Pressure(1,'atm'))
(26.273618984842212, 'kJ/kgDA')
>>> lib.dryAirEnthalpy(lib.Temperature(40,'C'), pressure=lib.Pressure(1,'atm'))
(42.14294352576413, 'kJ/kgDA')
>>> lib.dryAirEnthalpy(lib.Temperature(30,'C'), pressure=lib.Pressure(1,'atm'))
(31.554678167105262, 'kJ/kgDA')
>>>
>>>
>>> lib.humidSaturationEnthalpy(lib.Temperature(0,'C'), pressure=lib.Pressure(1,'atm'))
(9.469999997726383, 'kJ/kgDA')
>>> lib.humidSaturationEnthalpy(lib.Temperature(10,'C'), pressure=lib.Pressure(1,'atm'))
(29.738970275577053, 'kJ/kgDA')
>>> lib.humidSaturationEnthalpy(lib.Temperature(20,'C'), pressure=lib.Pressure(1,'atm'))
(58.32944376044787, 'kJ/kgDA')
>>> lib.humidSaturationEnthalpy(lib.Temperature(30,'C'), pressure=lib.Pressure(1,'atm'))
(101.11177489028077, 'kJ/kgDA')
>>> lib.humidSaturationEnthalpy(lib.Temperature(40,'C'), pressure=lib.Pressure(1,'atm'))
(167.96904061735157, 'kJ/kgDA')
>>> lib.humidSaturationEnthalpy(lib.Temperature(50,'C'), pressure=lib.Pressure(1,'atm'))
(276.48833883590646, 'kJ/kgDA')
>>> lib.humidSaturationEnthalpy(lib.Temperature(100,'C'), pressure=lib.Pressure(1,'atm'))
(74918239.91950782, 'kJ/kgDA')
>>> lib.humidSaturationEnthalpy(lib.Temperature(99,'C'), pressure=lib.Pressure(1,'atm'))
(45888.138812525416, 'kJ/kgDA')
>>>
>>>
```


## The Author and Maintainer of psychro library
#### For any issue on this library, please feel free to mail me: aminul71bd@gmail.com
![ author's photo ](author_photo_w250.jpg)
---
## Check the integrity (md5sum) of the downloaded files
<!-- table -->
| FILE | MD5SUM |
| --- | --- |
| psychro-1.0.0.tar.gz | df7babc82e18c5f46841d7fa2cf4e70e |
| psychro-1.0.0-py3-none-any.whl | 7c93e30e27c44f8a3a6393d1dc34af88 |




















 



