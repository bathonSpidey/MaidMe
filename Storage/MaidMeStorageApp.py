from UpdateMaid import Ui_MainWindow
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from Collection import Collection
import cv2

class Storage(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Storage, self).__init__(parent)
        super().__init__(parent)
        self.collection=Collection("mongodb+srv://admin:MaidMe@cluster0.lkcux.mongodb.net/test", "MaidMe")
        self.name="Employees"
        self.setupUi(self)
        self.uplaodImage.clicked.connect(self.Upload)
        self.addButton.clicked.connect(self.Add)

    def Upload(self):
        self.OpenDialogBox()

    def OpenDialogBox(self):
        filename=QtWidgets.QFileDialog.getOpenFileName()
        path=filename[0]
        print(path)
        self.fileLocationValue.setPlainText(path)

    def Add(self):
        data = {"FirstName": self.firstNameValue.toPlainText(), "LastName": self.lastNameValue.toPlainText(),
                "Address": self.addressValue.toPlainText(), "PhoneNumber": self.phoneNumberValue.toPlainText(),
                "Available": self.available.isChecked()}
        if self.fileLocationValue.toPlainText() !="":
            try:
                image=cv2.imread(self.fileLocationValue.toPlainText())
                imageString=image.tostring()
                imageID = self.collection.fileSystem.put(imageString, encoding="utf-8")
                data["Image"] = {'imageID': imageID,
                                 'shape': image.shape,
                                 'dtype': str(image.dtype)
                                 }
            except:
                print(f"Not a valid file path {self.fileLocation.toPlainText()}")

        self.collection.Add(self.name,data)
        print(data)





if __name__ == '__main__':
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    w = Storage()
    w.show()
    sys.exit(app.exec())