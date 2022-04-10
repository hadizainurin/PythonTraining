from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget #QWidget == QMainWindow
import sys

def window():
    app = QApplication(sys.argv) #sys.argv is giving application setup
    win = QMainWindow()
    #Create a Window Border
    win.setGeometry(1000, 200, 300, 300) #where you want to show your screen on xpos, ypos, width, height
    #Create Window title
    win.setWindowTitle("Hadi Application")

    label = QtWidgets.QLabel(win)
    label.setText("Label 1")
    label.move(50,50) #Take x,y
    label = QtWidgets.QLabel(win)
    label.setText("Label 2")
    label.move(30,30) #Take x,y
    #Shows Window nicely
    win.show() 
    #Add an exit method
    sys.exit(app.exec())

window()