#!/usr/bin/env python3
# -'''- coding: utf-8 -'''-
#===============================================================================
# PySide / PyQtGraph Template App
#
# Author: Jacob Portukalian - Sky Wave Design, LLC
# contact: jacob@skywavedesign.com
#
# This app is a quick demo to get a PySide app using Qt Designer to design the 
# UI file up and running quickly.
#
#===============================================================================
try:
    # Import the PySide libraries
    from PySide import QtGui  
    from PySide import QtCore
    from PySide import QtUiTools
    # 
    import pyqtgraph
    import numpy as np
except:
    print("")
    print("There is a problem with your python3 installation")
    print("")
    print("Try running the setup script in this repository")
#===============================================================================
class MainWindow(QtGui.QMainWindow):
    #---------------------------------------------------------------------------
    # constructor
    def __init__(self, parent=None):  
        # initialize the super class
        super(MainWindow, self).__init__(parent)
        # load the ui file
        # Normally examples show you how to use a UIC tool to convert your UI
        # file into python code, however this loader class lets you do it all in
        # one step
        loader = QtUiTools.QUiLoader()
        # this step is critical to get PyQtGraph to work. 
        loader.registerCustomWidget(pyqtgraph.PlotWidget)
        # Now we can load the ui file
        file = QtCore.QFile("mainwindow.ui")
        file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()
        # now the ui file is loaded, time to start setting up widgets
        self.setCentralWidget(self.ui)
        # UI Connections
        self.ui.helloButton.clicked.connect(self.sayHello)
        self.ui.setWindowTitle("Sky Wave Design, LLC - Template PySide App")
        

        self.ui.plotWidget.plot(np.random.normal(size=100), pen=(255,0,0), name="Red curve")
        self.ui.plotWidget.plot(np.random.normal(size=110)+5, pen=(0,255,0), name="Blue curve")
        self.ui.plotWidget.plot(np.random.normal(size=120)+10, pen=(0,0,255), name="Green curve")


    
    #---------------------------------------------------------------------------
    def sayHello(self):
        """this function is just a demo for connecting a button to a function"""
        print("Hello World!")
        
#===============================================================================
# This code runs the app
#
if __name__ == '__main__':  
    import sys  
    import os

    app = QtGui.QApplication(sys.argv)  

    window  = MainWindow()  
    # note here that the PySide widget is window.ui, not window
    window.ui.show()

    app.connect(app, QtCore.SIGNAL("lastWindowClosed()"),
               app, QtCore.SLOT("quit()"))
    app.exec_()
    
