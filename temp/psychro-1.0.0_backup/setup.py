from setuptools import setup, find_packages

# read the contents from README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name='psychro',
  version='1.0.0',
  description='This engineering package deals with the physical and thermodynamic \
  properties of the air-water system very accurately. It can calculate all the \
  psychrometric data like dewpoint, wet bulb temperature, humid enthalpy, \
  moisture content, humid volume, vapor density etc.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/aminul71bd/psychro',
  author='A K M Aminul Islam',
  author_email='aminul71bd@gmail.com',
  maintainer='A K M Aminul Islam',
  maintainer_email='aminul71bd@gmail.com',
  license='NEWTONIA FREEWARE LICENSE',
  packages=find_packages(),
  include_package_data=True,
  py_modules=['psychro.__init__','psychro.lib','psychro.src.Prefix','psychro.src.Unit',\
'psychro.src.Pressure', 'psychro.src.Temperature','psychro.src.psychro_functions'],
  data_files = [("", ["LICENSE"])],
  zip_safe=True
)
