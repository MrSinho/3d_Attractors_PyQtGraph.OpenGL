import numpy as np 
import pyqtgraph as pg
from pyqtgraph.Qt import *
import pyqtgraph.opengl as gl
import sys


class Simulation():
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        self.window = gl.GLViewWidget()     
        self.window.setGeometry(100, 100, 800, 600) #set the geometry of the window(x padding, y padding, dimension x, dimension y)
        self.window.setWindowTitle("I am going to draw a line") #set the title
        self.window.show()  #show the window

        
        global points_list
        points_list = [] #create an empty list
        self.draw() #call the draw function

    def draw(self):
        point1 = (0, 0, 0)  #specify the (x, y, z) values of the first point in a tuple
        point2 = (5, 6, 8)  #specify the (x, y, z) values of the second point in a tuple

        points_list.append(point1) #add the point1 tuple to the points_list
        points_list.append(point2) #add the point2 tuple to the points_list
        print(points_list)
        points_array = np.array(points_list) #convert the list to an array
        drawing_variable = gl.GLLinePlotItem(pos = points_array, width = 1, antialias = True)   #make a variable to store drawing data(specify the points, set antialiasing)
        self.window.addItem(drawing_variable) #draw the item

    def start(self):
        QtGui.QApplication.instance().exec_() #run the window properly

Simulation().start()
