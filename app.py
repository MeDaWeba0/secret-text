import sys, platform, os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

if platform.system() == "Linux":
    br = "/"
else:
    br = "\\"

dirG = os.getcwd()

try:
    os.mkdir("files")
except:
    pass

list_char = [
  ' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', '#', 'k', 'l', 'm', 'n',
  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C',
  'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
  'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6',
  '7', '8', '9', ' ', ',', '.', ';', ':', '_', '-', '!', '?', '@', '$', '%',
  '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '+', '=', '~',
  '`', '^', '|', '\n',' '
]

def error(data):
    dirLg = dirG + br + "Error-log.txt"
    msg_err = "Problem with " + data + "\n"
    try:
        f = open(dirLg, "a")
        f.write(msg_err)
        f.close()
    except:
        f = open(dirLg, "w")
        f.write(msg_err)
        f.close()

class ClGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui.ui", self)
        self.save.clicked.connect(self.savefn)
        self.load.clicked.connect(self.loadfn)
        self.enc1 = 0
        self.enc2 = 0
        self.dir_file = ""

    def valor_clear(self):
        self.enc1 = 0
        self.enc2 = 0
        self.data_e = ""

    def enc(self):
        num1 = self.enc1 ; num2 = self.enc2
        wdata = self.data_e ; todo = ""
        wlist = list(wdata) 
        
        Nl1 = int(len(wlist)) - 1 ; i = -1
        Nl2 = int(len(list_char)) -1 ; i2 = -1

        while Nl1 != i:
            i += 1
            a = str(wlist[i])
            while Nl2 != i2:
                i2 += 1
                b = str(list_char[i2])
                if a == b:
                    enc_num = i2 * num1 + num2
                    if Nl2 != i2:
                        todo += str(enc_num) + ":"
                    else:
                        todo += str(enc_num)                                      
                    i2 = Nl2
            i2 = -1

        todo = todo.strip()[:-1]
        self.valor_clear()
        return todo

    def desc(self):
        num1 = self.enc1 ; num2 = self.enc2
        wdata = self.data_e ; todo = ""
        wlist = wdata.split(":")

        Nl = int(len(wlist)) -1 ; i = -1

        while Nl != i:
            i += 1
            a = float(wlist[i])
            ar = (a-num2)/num1
            todo += list_char[round(ar)]

        self.valor_clear()
        return todo

    def loadfn(self):
        try:
            self.enc1 = float(self.num1.text())
            self.enc2 = float(self.num2.text())
        except:
            self.enc1 = 72.2
            self.enc2 = 13.3
        self.dir_file = dirG +br+"files" + br + self.filename.text() + ".mw"

        boolneed = False

        try:
            f = open(self.dir_file, "r")
            data = str(f.read())
            f.close()
            boolneed = True
        except:
            boolneed = False

        if boolneed == True:
            self.data_e = data
            data = self.desc()
            self.text.clear()
            self.text.insertPlainText(data)
            self.msg.setText("Loaded success")
        else:
            error("Load")
            self.msg.setText("File not fund")

    def savefn(self):
        try:
            self.enc1 = float(self.num1.text())
            self.enc2 = float(self.num2.text())
        except:
            self.enc1 = 72.2
            self.enc2 = 13.3
        self.dir_file = dirG +br+"files" + br + self.filename.text() + ".mw"


        text_save = self.text.toPlainText().replace("\r", "")
        self.data_e = text_save
        print(self.data_e)
        print("previa")
        finish_text = self.enc()
        f = open(self.dir_file, "w")
        print("escritura")
        f.write(finish_text)
        f.close()

        self.msg.setText("Saved success")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = ClGUI()
    GUI.setWindowTitle("secrets")
    GUI.setWindowIcon(QIcon("ico.png"))
    GUI.show()
    sys.exit(app.exec_())