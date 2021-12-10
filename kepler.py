import numpy as np
import matplotlib.pyplot as plt
import astropy
import scipy as sp
from astropy import constants as c
from astropy import units as u

class keplerCalc:
    '''
    This class is used to calculate orbital characteristics and make the ellipse equation.
    
    Parameters:
        MassP = Mass of primary star in SOlMass
        MassX = Mass of the planet in earthMass
        period = orbital time in years
        eccentricity 
        distance = semi-major axis of the orbit in AU
    returns:
        Orbital parameters
        Ellipse equation to be used by Visual.py
    
    
    '''
    def __init__(self,MassP=1*u.Msun, MassX=1*u.Mearth,period=1*u.year,eccentricity=0.02,distance=1*u.au):
            self.MassP = MassP.to(u.kg)
            self.MassX = MassX.to(u.kg)
            self.period = period.to(u.s)
            self.ecc = eccentricity
            self.distance = distance.to(u.m)
            self.a = distance.value
            self.b = (-(distance.value**2)*((eccentricity**2)-1))**-2
    def calcMassP(self):
        mp = (4*(np.pi**2)*(self.distance**3))/(c.G*(self.period**2))-self.MassX
        self.MassP = mp
        return mp
    def calcMassX(self):
        mx = (4*(np.pi**2)*(self.distance**3))/(c.G*(self.period**2))-self.MassP
        self.MassX = mx
        return mx
    def calcperiod(self):
        p = np.sqrt((4*(np.pi**2)*(self.distance**3))/(c.G*(self.MassP+self.MassX)))
        self.period = p
        return p
    def calcDistance(self):
        a = np.cbrt(((c.G*(self.MassP+self.MassX))*(self.period**2))/(4*(np.pi**2)))
        self.distance = a
        return a
    def ellipse(self):
        if self.MassP == 0:
            mp = (4*(np.pi**2)*(self.distance**3))/(c.G*(self.period**2))-self.MassX
            self.MassP = mp
        elif self.MassX == 0:
            mx = (4*(np.pi**2)*(self.distance**3))/(c.G*(self.period**2))-self.MassP
            self.MassX = mx
        elif self.period == 0:
            p = np.sqrt((4*(np.pi**2)*(self.distance**3))/(c.G*(self.MassP+self.MassX)))
            self.period = p
        elif self.a == 0:
            self.a= np.cbrt(((c.G*(self.MassP+self.MassX))*(self.period**2))/(4*(np.pi**2)))

        
        u= 0     #x-position of the center
        v= 0   #y-position of the center
        a= self.a
        e = self.ecc #radius on the x-axis
        b= np.sqrt(-(a**2)*((e**2)-1)) #radius on the y-axis
        t = np.linspace(0, 2*np.pi, 300)
        ellipsex =  u+a*np.cos(t) 
        ellipsey =  v+b*np.sin(t) 
        focus = u - np.sqrt((a**2)-(b**2))
        return ellipsex , ellipsey , focus
        
        

    
    


class RV:
    '''
    Determines the planets effect on the host star in m/s
    
    '''
    def __init__(self,massX,massP,period,ecc,distance):
        self.massX = massX
        self.massP = massP
        self.period = period
        self.ecc = ecc
        self.a = distance
    def amplitudeCalc(self):
        K = (self.massX*2*np.pi*self.a)/(self.period*self.massP*2.1*(10**-4))
        self.amplitude = K
        return K*u.m/u.s
    
