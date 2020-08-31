import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import *
import pyqtgraph.opengl as gl
import sys 

class Simulation(object):   #create a class with all the following data:
    def __init__(self, x, y, z, a, deltatime):    
        self.app = QtGui.QApplication(sys.argv)
        self.window = gl.GLViewWidget() #create a window
        self.window.setGeometry(480, 270, 800, 600) #set the geometry of the window(padding x, padding y, scale x, scale y)
        self.window.setWindowTitle("Simulation")    #set the window title
        self.window.setCameraPosition(distance=30, elevation=100) #set the camera position
        self.window.show() #show the window

        self.x, self.y, self.z = x, y, z 
        self.a, self.deltatime = a, deltatime
        
        global points_list
        points_list = []    #create an empty list    

    #run algorithm and draw lines
    def Update(self):
        dx = (np.sin(self.y) - (self.a * self.x)) * self.deltatime
        dy = (np.sin(self.z) - (self.a * self.y)) * self.deltatime
        dz = (np.sin(self.x) - (self.a * self.z)) * self.deltatime
        self.x = self.x + dx
        self.y = self.y + dy
        self.z = self.z + dz
        #here ends the algorithm
        newpoint = (self.x, self.y, self.z) # create a newpoint tuple
        #add the new point to the points list
        points_list.append(newpoint) #add the tuple to the points_list
        print(newpoint)
        global points
        points = np.array(points_list) #convert the points list to an array of tuples
        self.draw() #run the draw function

    def draw(self):
        try: self.window.removeItem(self.drawpoints)
        except Exception: pass
        drawpoints = gl.GLLinePlotItem(pos=points, width=1, antialias=True) #make a variable to store drawing data(specify the points, set antialiasing)
        self.window.addItem(drawpoints) #draw the item
    
    #start properly
    def start(self):
        QtGui.QApplication.instance().exec_()

    #animate and update  
    def animation(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.Update)
        timer.start(20)
        self.start()
        
                # x   y  z      a     deltatime
sim = Simulation(0.1, 0, 0, 0.208186, 0.01)
sim.animation()
