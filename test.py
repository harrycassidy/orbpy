from kepler import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import streamlit as st
import streamlit.components.v1 as components
test = keplerCalc()
el = test.ellipse()
x = el[0]
y = el[1]
def update_line(i, x,y ,line):
    ax.patches = []
    x = x[i]
    y = y[i]
    circle = plt.Circle(([x], [y]),(1/23454.8)*100,color = 'red')
    l = ax.add_patch(circle)
    #line.center(x,y)
    return l,

fig = plt.figure()
ax = fig.subplots()
# Fixing random state for reproducibility
#np.random.seed(19680801)

#data = keplerCalc()
data = np.random.rand(2,25)
circle = plt.Circle(([1], [0]),(1/23454.8)*100,color = 'red')
l = ax.add_patch(circle)
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig, update_line, 100, fargs=(x,y, l), interval=50, blit=True)

st.title("Embed Matplotlib animation in Streamlit")
#st.markdown("https://matplotlib.org/gallery/animation/basic_example.html")
components.html(line_ani.to_jshtml(), height=1000)




