import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile = "P4_Interfaz_para_arduino_v2.ui"  # Nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

import serial as conexion

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    #    self.btn_agregar.clicked.connect(self.agregar)
        self.btn_accion.clicked.connect(self.accion)
        self.arduino = None

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.realiza_lecturas)

        self.btn_control_led.clicked.connect(self.control_led)

    def control_led(self):
        c = self.btn_control_led.text()
        # print(ac)
        if c == "PRENDER":
            self.btn_control_led.setText("APAGAR")
            self.arduino.write("1".encode())
        else: #pagar
            self.btn_control_led.setText("PRENDER")
            self.arduino.write("0".encode())


    def accion(self):
        ac = self.btn_accion.text()
        #print(ac)
        if ac == "CONECTAR":
            self.btn_accion.setText("DESCONECTAR")
            com = "COM" + self.txt_com.text()
            if self.arduino == None:#nunca me he conectado
                self.arduino = conexion.Serial(port=com, baudrate=9600, timeout=1000)
                self.txt_estado.setText("CONECTADO")
            else: #ya me he conectado, pero la conexion esta cerrada
                self.arduino.open()
                self.txt_estado.setText("RECONECTADO")
            self.segundoPlano.start(100)
        else:
            self.btn_accion.setText("CONECTAR")
            self.segundoPlano.stop()
            self.arduino.close()
            self.txt_estado.setText("DESCONECTADO")


    def realiza_lecturas(self):
        if self.arduino != None:
            if self.arduino.isOpen():
                try:
                    #print(self.arduino.inWaiting())
                    if self.arduino.inWaiting()>0:
                        v = self.arduino.readline().decode().replace("\n", "")
                        #print(v)
                        self.listWidget.addItem(v)
                except Exception as ex:
                    print(ex)

    #def agregar(self):
    #    nombre = self.txt_nombre.text()
    #    self.listWidget.addItem(nombre)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())