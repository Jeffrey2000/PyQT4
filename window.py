import sys
from PyQt4 import QtGui,QtCore 

class mainFrame(QtGui.QMainWindow):

    def __init__(self):
        super(mainFrame, self).__init__();
        self.setGeometry(50,50,500,500);
        self.setWindowTitle("Jeffrey's Application")
        self.setWindowIcon(QtGui.QIcon('jlogo.png'));

        #sets the name of the dropdown label, only creating labels not actual menubar
        endApplication = QtGui.QAction("&Quit Application", self);
        endApplication.setShortcut("Ctrl+X");
        endApplication.setStatusTip("Leave the application");
        endApplication.triggered.connect(self.close_application)

        printToConsole = QtGui.QAction("&Print to console", self);
        printToConsole.triggered.connect(self.printToConsole);
        
        
        self.buttonQuit();

        extractAction = QtGui.QAction(QtGui.QIcon('jlogo.png'),'Close Application',self);
        extractAction.triggered.connect(self.close_application)

        self.toolbar = self.addToolBar("Extraction")
        self.toolbar.addAction(extractAction);
        
        self.statusBar();

        
        #Creates menu bar
        mainMenu = self.menuBar(); #We make this object because we want to modify it
        fileMenu = mainMenu.addMenu("&File") #Adds sub menu to large menubar
        randomFunction = mainMenu.addMenu("&Stupid random function")
        fileMenu.addAction(endApplication); #Application function created beforheand added to the menu
        randomFunction.addAction(printToConsole);


    def buttonQuit(self):
        quitButton = QtGui.QPushButton("Quit",self); 
      
        quitButton.clicked.connect(self.button_resize);


       
        quitButton.resize(quitButton.sizeHint())
        quitButton.move(100,100);
        self.show();

        

    def close_application(self):
        userChoice = QtGui.QMessageBox.question(self, "Close Application",'Leave?',
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if userChoice == QtGui.QMessageBox.Yes:
            print("Leaving the application...")
            sys.exit();
        else:
            pass
            

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
