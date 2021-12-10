from kepler import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import streamlit as st
import streamlit.components.v1 as components
import time
st.title("Orbpy by Harry Cassidy")
st.header("Orbital Characteristics")
massP = st.number_input('Mass of the Primary(Msun)')*u.Msun
massX= st.number_input('Mass of the Secondary(Mearth)')*u.Mearth
period=st.number_input('Period(Years)')*u.year
a=st.number_input('Distance(Au)')*u.au
ecc=st.number_input('Eccentricity')
if a == 0:
    test = keplerCalc(MassP=massP, MassX=massX,period=period,eccentricity=ecc,distance=a)
    a=test.calcDistance()
test = keplerCalc(MassP=massP, MassX=massX,period=period,eccentricity=ecc,distance=a)
el = test.ellipse()
plt.style.use('dark_background')
fig = plt.figure(figsize=(7,14))
ax1 = fig.subplots(2)
ax1[0].set_xlabel('Au')
ax1[0].set_ylabel('Au')
size = (1/23454.8)*300
sizesun = 0.00465047*15
if a.value > 1.3:
    size = size*3
    sizesun = sizesun*2
if a.value > 7:
    size = size*5
    sizesun = sizesun*2
ax1[0].grid(True,color='green',linewidth=0.4)
ax1[0].plot(el[0],el[1],color='green', linewidth = 0.4)
circle = plt.Circle((el[2],0),sizesun,color='yellow')
ax1[0].add_patch(circle)
circle2 = plt.Circle((1,0), size, color = 'w')
line1 = ax1[0].add_patch(circle2)
rvAmp = RV(test.MassX,test.MassP,test.period.to(u.year).value,test.ecc,test.a)
st.write('Radial Velocity',rvAmp.amplitudeCalc())



x1= np.linspace(0,40)

ax1[1].plot(rvAmp.amplitudeCalc().value*np.sin(x1/(2*np.pi)),color='green')
ax1[1].set_xticks([])
ax1[1].set_ylabel('Meters per second')


time_text = ax1[0].text(-0.005, -0.75, '', fontsize=12)

def update_line(i, x,y ,line):
    ax1[0].patches = []
    x = x[i]
    y = y[i]
    circle = plt.Circle((el[2],0),sizesun,color='yellow')
    ax1[0].add_patch(circle)
    circle = plt.Circle(([x], [y]),size,color = 'w')
    l = ax1[0].add_patch(circle)
    time_text.set_text(round((i/300),2)*period)
    return l, time_text,


x = el[0]
y = el[1]


circle = plt.Circle(([1], [0]),(1/23454.8)*100,color = 'w')
l = ax1[0].add_patch(circle)
    
    


line_ani = animation.FuncAnimation(fig, update_line, 300, fargs=(x,y, l), interval=75, blit=True)


components.html(line_ani.to_jshtml(), height=1600)
st.sidebar.header("Primary Mass Calculation")
with st.sidebar.form("Primary Mass Calculation"):
    
    massP = 1*u.Msun
    massX= st.number_input('Mass of the Secondary(Mearth)')*u.Mearth
    period=st.number_input('Period(Years)')*u.year
    a=st.number_input('Distance(Au)')*u.au
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        test = keplerCalc(MassP=massP, MassX=massX,period=period,eccentricity=ecc,distance=a)
        st.write("Primary Mass", test.calcMassP().to(u.Msun))
st.sidebar.header("Secondary Mass Calculation")
with st.sidebar.form("Secondary Mass Calculation"):
    
    massP = st.number_input('Mass of the Primary(Msun)')*u.Msun
    massX= 1*u.Mearth#st.number_input('Mass of the Secondary(Mearth)')*u.Mearth
    period=st.number_input('Period(Years)')*u.year
    a=st.number_input('Distance(Au)')*u.au
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        test = keplerCalc(MassP=massP, MassX=massX,period=period,eccentricity=ecc,distance=a)
        st.write("Secondary Mass", test.calcMassX())
        
st.sidebar.header("Period Calculation")
with st.sidebar.form("Period Calculation"):
    
    massP = st.number_input('Mass of the Primary(Msun)')*u.Msun
    massX= st.number_input('Mass of the Secondary(Mearth)')*u.Mearth
    period=1*u.year#st.number_input('Period(Years)')*u.year
    a=st.number_input('Distance(Au)')*u.au
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        test = keplerCalc(MassP=massP, MassX=massX,period=period,eccentricity=ecc,distance=a)
        st.write("Period", test.calcperiod().to(u.year))
        
st.sidebar.header("Distance Calculation")
with st.sidebar.form("Distance Calculation"):
    
    massP = st.number_input('Mass of the Primary(Msun)')*u.Msun
    massX= st.number_input('Mass of the Secondary(Mearth)')*u.Mearth
    period=st.number_input('Period(Years)')*u.year
    a=1*u.au#st.number_input('Distance(Au)')*u.au
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        test = keplerCalc(MassP=massP, MassX=massX,period=period,eccentricity=ecc,distance=a)
        st.write("Distance", test.calcDistance().to(u.au))