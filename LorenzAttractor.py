import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import *
import pyqtgraph.opengl as gl
import sys 

class Simulation(object):   #create a class with all the following data:
    def __init__(self, x, y, z, a, b, c, deltatime):    
        self.app = QtGui.QApplication(sys.argv)
        self.window = gl.GLViewWidget() #create a window
        self.window.setGeometry(480, 270, 800, 600) #set the geometry of the window(padding x, padding y, scale x, scale y)
        self.window.setWindowTitle("Simulation")    #set the window title
        self.window.setCameraPosition(distance=30, elevation=100) #set the camera position
        self.window.show() #show the window
        #set grid
        #gridx = gl.GLGridItem()
        #gridx.scale(16, 16, 16)
        #self.window.addItem(gridx)
        #gridy = gl.GLGridItem()
        #gridy.rotate(90, 0, 90, 1)
        #gridy.translate(40, 0, 40)
        #gridy.scale(4, 4, 4)
        #self.window.addItem(gridy)
        #gridz = gl.GLGridItem()
        #gridz.rotate(90, 90, 0, 1)
        #gridz.translate(0, -40, 40)
        #gridz.scale(4, 4, 4)
        #self.window.addItem(gridz)

        self.x, self.y, self.z = x, y, z 
        self.a, self.b, self.c, self.deltatime = a, b, c, deltatime
        
        global points_list
        points_list = []    #create an empty list
        #self.start()
        self.Update()
        

    #run algorithm and draw lines
    def Update(self):
        count = 0
        #here starts the algoritm, it runs 5000 times
        for i in range(0, 5000, 1): 
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
            print("this will take some time")
            global points
            points = np.array(points_list) #convert the points list to an array of tuples

        self.draw() #run the draw function
    def draw(self):
        drawpoints = gl.GLLinePlotItem(pos=points, width=1, antialias=True) #make a variable to store drawing data(specify the points, set antialiasing)
        self.window.addItem(drawpoints) #draw the item
        self.start() #open the window 
    
    #start properly
    def start(self):
        #if (sys.flags.interactive != 1) or not hasattr(QtCore, "PyQT_VERSION"):
        QtGui.QApplication.instance().exec_()
            

    #animate and update  
    def animation(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.Update)
        timer.start(20)
        self.start()
        self.Update()
    
sim = Simulation(0.001, 0, 0, 10, 28, 8/3, 0.01)
#sim.animation()
