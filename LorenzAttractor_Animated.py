import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import sys 


class Simulation(object):
    def __init__(self, x, y, z, a, b, c, deltatime):
        self.app = QtGui.QApplication(sys.argv)
        self.window = gl.GLViewWidget() #create a window
        self.window.setGeometry(480, 270, 800, 600) #set the geometry of the window(padding x, padding y, scale x, scale y)
        self.window.setWindowTitle("Simulation")    #set the window title
        self.window.setCameraPosition(distance=30, elevation=100) #set the camera position
        self.window.show() #show the window
        
        self.x, self.y, self.z = x, y, z 
        self.a, self.b, self.c, self.deltatime = a, b, c, deltatime
        
        global points_list 
        points_list = [] #create an empty points_list
        #self.start()
        self.Update() #run the update function
        

    #run algorithm and draw lines
    def Update(self):
        #here starts the algorithm
        dx = (self.a * (self.y - self.x)) * self.deltatime
        dy = (self.x * (self.b - self.z) - self.y) * self.deltatime
        dz = (self.x * self.y - self.c * self.z) * self.deltatime
        self.x = self.x + dx
        self.y = self.y + dy
        self.z = self.z + dz
        #here ends the algorithm
        newpoint = (self.x, self.y, self.z) # create a newpoint tuple
        #add the new point to the points list
        points_list.append(newpoint) #add the tuple to the points_list
        print(points_list)
        global points
        points = np.array(points_list) #convert the points list to an array of tuples
        self.draw() #run the draw function
        
    def draw(self):
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
        self.Update()
    
sim = Simulation(0.01, 0, 0, 10, 28, 8/3, 0.01)
sim.animation()