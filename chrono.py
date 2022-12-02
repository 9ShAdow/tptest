import sys
import socket
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import threading
import time

host = "localhost" # "", "127.0.0.1
port = 10000

print(f"Ouverture de la socket sur le serveur {host} port {port}")
client_socket = socket.socket()
client_socket.connect((host, port))
print("Serveur est connecté")

 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        "Tant que arret_thread est faux faire Compteur = compteur + 1  "


        arret_thread = bool
        
        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        
        lab = QLabel("Compteur :")
        self.text = QLineEdit("0")
        #self.name = QLabel("")

        start = QPushButton("Start")
        stop = QPushButton("stop")
        reset = QPushButton("Reset")
        connect = QPushButton("Connect")
        quitter = QPushButton("Quitter")
        

    # Ajouter les composants au grid ayout

        grid.addWidget(lab, 0, 0)
        grid.addWidget(self.text, 1, 0, 1, 2)
        grid.addWidget(start, 2, 0, 1, 2)
        grid.addWidget(reset, 3, 0)
        grid.addWidget(stop, 3, 1)
        grid.addWidget(connect, 4, 0)
        grid.addWidget(quitter,4,1)
        grid.activate





        start.clicked.connect(self.start)
       
        reset.clicked.connect(self.__reset)
        quitter.clicked.connect(self.__quitter)
        stop.clicked.connect(self.stop)
        self.setWindowTitle("INTERFACE GRAPHIQUE DE SHAD")

        self.timer = QTimer()
        self.timer.timeout.connect(self.avance)
        self.time = QTime(0, 0, 0)
        self.text.setText(self.time.toString("s"))
        self.show()
        
        self.text.setReadOnly(True)
    # demarrer time
    def start(self):
        self.timer.start(1000)
  
    def stop(self):
        self.timer.stop()
   
  
   
    def avance(self):
        self.time = self.time.addSecs(1)
        self.text.setText(self.time.toString("s"))


    """def arret_thread(self):
        self.thread.stop()
        pass"""



    """def start(self):
        self.thread = threading.Thread(target=self.__start)
        while True:
            self.text.setText("0")
            time.sleep(1)
            self.text.setText(f"{int(self.text.text()) + 1}")
            time.sleep(1)
            pass
        self.thread = threading.Thread(target=self.__start)
        self.thread.start()
    """        
    
    """def __start(self):
         while True:
            self.text.setText("0")
            self.text.setText(f"{int(self.text.text()) + 1}")
            time.sleep(1)
            pass
            #self.timer.start(1000)
            #self.text.setText(f"{int(self.text.text()) + 1}")
            #self.startButton.setEnabled(False)
            #self.stopButton.setEnabled(True)"""
    
    def __reset(self):
        self.text.setText("0")
        #self.timer.stop()
        #self.startButton.setEnabled(True)
        #self.stopButton.setEnabled(False)
        pass
    
    def __quitter(self):
        self.close()
        pass


  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()