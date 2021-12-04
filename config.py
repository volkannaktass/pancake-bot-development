# importing libraries
from PyQt5.QtWidgets import * 
import sys
import json
  
# creating a class
# that inherits the QDialog class
class Window(QDialog):
  
    # constructor
    def __init__(self):
        super(Window, self).__init__()
  
        # setting window title
        self.setWindowTitle("Config")
  
        # setting geometry to the window
        self.setGeometry(100, 100, 300, 400)
  
        # creating a group box
        self.formGroupBox = QGroupBox("Bot Registration")
  
        # creating spin box to select age
        self.ageSpinBar = QSpinBox()
  
        # creating combo box to select degree
        self.degreeComboBox = QComboBox()
  
        # adding items to the combo box
        #self.degreeComboBox.addItems(["BTech", "MTech", "PhD"])
  
        # creating a line edit
        self.senderAdress = QLineEdit()
        
        self.privateKeyBar = QLineEdit()
        
        self.bnbAmount = QLineEdit()
        # calling the method that create the form
        self.createForm()
  
        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
  
        # adding action when form is accepted
        self.buttonBox.accepted.connect(self.getInfo)
  
        # addding action when form is rejected
        self.buttonBox.rejected.connect(self.reject)
  
        # creating a vertical layout
        mainLayout = QVBoxLayout()
  
        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)
  
        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)
  
        # setting lay out
        self.setLayout(mainLayout)
  
    # get info method called when form is accepted
    def getInfo(self):
        lst = []
        
        # printing the form information
        print("Sender Address : {0}".format(self.senderAdress.text()))
        senderAddress = self.senderAdress.text()
        #lst.append(self.senderAdress.text())
        print("Private Key : {0}".format(self.privateKeyBar.text()))
        privateKeyBar = self.privateKeyBar.text()
        #lst.append(self.privateKeyBar.text())
        print("BNB Amount You Want : {0}".format(self.bnbAmount.text()))
        bnbAmount = self.bnbAmount.text()
        #lst.append(self.bnbAmount.text())
        #print("Degree : {0}".format(self.degreeComboBox.currentText()))
        #print("Age : {0}".format(self.ageSpinBar.text()))
        #file1.writelines(lst)
        exDict = {
            'senderAddress': senderAddress,
            'privateKeyBar': privateKeyBar,
            'bnbAmount': bnbAmount
        }

        with open('file.txt', 'w') as file:
            file.write(json.dumps(exDict))
        # closing the window
        self.close()
  
    # creat form method
    def createForm(self):
  
        # creating a form layout
        layout = QFormLayout()
  
        # adding rows
        # for name and adding input text
        layout.addRow(QLabel("Sender Address"), self.senderAdress)
        layout.addRow(QLabel("Private Key"), self.privateKeyBar)
        layout.addRow(QLabel("BNB Amount You Want"), self.bnbAmount)  
        # for degree and adding combo box
        #layout.addRow(QLabel("Degree"), self.degreeComboBox)
  
        # for age and adding spin box
        #layout.addRow(QLabel("Age"), self.ageSpinBar)
  
        # setting layout
        self.formGroupBox.setLayout(layout)
  
  
# main method
if __name__ == '__main__':
  
    # create pyqt5 app
    app = QApplication(sys.argv)
  
    # create the instance of our Window
    window = Window()
  
    # showing the window
    window.show()
  
    # start the app
    sys.exit(app.exec())
