import sys
from PyQt4 import QtGui,QtCore #Module needed to add button event handling

#Python OOP for GUI, makes sense for anything that may interact with it in a dynamic way

class mainFrame(QtGui.QMainWindow):

    def __init__(self): ##Core application stuff, template for the rest of GUI
        super(mainFrame, self).__init__();
        self.setGeometry(50,50,500,500);
        self.setWindowTitle("Jeffrey's Application")
        self.setWindowIcon(QtGui.QIcon('jlogo.png'));
        self.buttonQuit();

    ##Adding a button to the window
    def buttonQuit(self):
        quitButton = QtGui.QPushButton("Quit",self); ##Takes parameter of name and parent calss
        #Exits current instance of QCore appliation
        quitButton.clicked.connect(QtCore.QCoreApplication.instance().quit);

        #Resizing button and moving button
        quitButton.resize(100,50)
        quitButton.move(100,100);
        self.show();

        

        

    



def frameLoop():
    app = QtGui.QApplication(sys.argv);
    appFrame = mainFrame()
    sys.exit(app.exec_());


frameLoop();
