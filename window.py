import sys
from PyQt4 import QtGui,QtCore 

class mainFrame(QtGui.QMainWindow):

    def __init__(self):
        super(mainFrame, self).__init__();
        self.setGeometry(50,50,500,500);
        self.setWindowTitle("Jeffrey's Application")
        self.setWindowIcon(QtGui.QIcon('jlogo.png'));


        endApplication = QtGui.QAction("&Quit Application", self);
        endApplication.setShortcut("Ctrl+X");
        endApplication.setStatusTip("Leave the application");
        endApplication.triggered.connect(self.close_application)

        printToConsole = QtGui.QAction("&Print to console", self);
        printToConsole.triggered.connect(self.printToConsole);
        
        
        self.buttonQuit();
        self.statusBar();

        
        #Creates menu bar
        mainMenu = self.menuBar(); #We make this object because we want to modify it
        fileMenu = mainMenu.addMenu("&File") #Adds sub menu to large menubar
        fileMenu = mainMenu.addMenu("&Stupid random function")
        fileMenu.addAction(endApplication); #Application function created beforheand added to the menu
        fileMenu.addAction(printToConsole);


    def buttonQuit(self):
        quitButton = QtGui.QPushButton("Quit",self); 
      
        quitButton.clicked.connect(self.button_resize);


       
        quitButton.resize(quitButton.sizeHint())
        quitButton.move(100,100);
        self.show();

        

    def close_application(self):
        print("Application closed");
        sys.exit();

    def button_resize(self):
        self.setWindowTitle("ZenithList")

    def printToConsole(self):
        from random import randint
        for i in range(0,8):
            print(i*randint(0,8));
            
    

    



def frameLoop():
    app = QtGui.QApplication(sys.argv);
    appFrame = mainFrame()
    sys.exit(app.exec_());


frameLoop();
