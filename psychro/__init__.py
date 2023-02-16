'''
Package Name:'psychro'
Path:'<package_root>/__init__.py'
Module Version:'1.0.0.2023.02.09'
Author;'A K M Aminul Islam'
Author_Email:'aminul71bd@gmail.com'
Company:'Newtonia Ltd.'
Last Update:2023/02/15

Description: 'This package is used to find the psychrometric data of pure air-water system'
Limitation:
    Temperature Range: 0-150C
    Pressur: 1 atm (But, psychrometric data at different pressure can also be
        calculated by using this software. )
'''


__version__='1.0.0'
version='1.0.0'
def getVersion():
    return version



def packageInfo():
    s=" Package Name:'psychro'\n"
    s=s+" Package Version:'1.0.0'\n"
    s=s+" Author:'A K M Aminul Islam'\n"
    s=s+" Author_Email:'aminul71bd@gmail.com'\n"
    s=s+" Company:'Newtonia Ltd.'\n"
    s=s+" Last Update:'2023/02/14'\n"
    s=s+" Description:'This package creates psychrometric data of pure air-water system'"
    s=s+"\n Limitation: Temperature Range: 0-150 degree C"
    print(s)








	