# Form implementation generated from reading ui file 'UpdateMaid.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Maid Me")
        MainWindow.setFixedSize(878, 788)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(300, 40, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(250, 120, 401, 381))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.firstName = QtWidgets.QLabel(self.formLayoutWidget)
        self.firstName.setObjectName("firstName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.firstName)
        self.firstNameValue = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.firstNameValue.setMaximumSize(QtCore.QSize(16777215, 20))
        self.firstNameValue.setObjectName("firstNameValue")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.firstNameValue)
        self.lastName = QtWidgets.QLabel(self.formLayoutWidget)
        self.lastName.setObjectName("lastName")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lastName)
        self.lastNameValue = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.lastNameValue.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lastNameValue.setObjectName("lastNameValue")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lastNameValue)
        self.fileLocationValue = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.fileLocationValue.setMaximumSize(QtCore.QSize(300, 20))
        self.fileLocationValue.setObjectName("fileLocationValue")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fileLocationValue)
        self.phoneNumberValue = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.phoneNumberValue.setMaximumSize(QtCore.QSize(16777215, 20))
        self.phoneNumberValue.setObjectName("phoneNumberValue")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.phoneNumberValue)
        self.phoneNumber = QtWidgets.QLabel(self.formLayoutWidget)
        self.phoneNumber.setObjectName("phoneNumber")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.phoneNumber)
        self.uplaodImage = QtWidgets.QPushButton(self.formLayoutWidget)
        self.uplaodImage.setObjectName("uplaodImage")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.uplaodImage)
        self.fileLocation = QtWidgets.QLabel(self.formLayoutWidget)
        self.fileLocation.setObjectName("fileLocation")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.fileLocation)
        self.available = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.available.setObjectName("available")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.available)
        self.addressValue = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.addressValue.setMaximumSize(QtCore.QSize(16777215, 20))
        self.addressValue.setObjectName("addressValue")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.ItemRole.FieldRole, self.addressValue)
        self.address = QtWidgets.QLabel(self.formLayoutWidget)
        self.address.setObjectName("address")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.ItemRole.LabelRole, self.address)
        self.addButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.addButton.setObjectName("addButton")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.ItemRole.FieldRole, self.addButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 878, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Maid Me Data Entry"))
        self.firstName.setText(_translate("MainWindow", "First Name: "))
        self.lastName.setText(_translate("MainWindow", "Last  Name: "))
        self.phoneNumber.setText(_translate("MainWindow", "Ph Number:"))
        self.uplaodImage.setText(_translate("MainWindow", "Upload Image"))
        self.fileLocation.setText(_translate("MainWindow", "File Location:"))
        self.available.setText(_translate("MainWindow", "Available"))
        self.address.setText(_translate("MainWindow", "Address:"))
        self.addButton.setText(_translate("MainWindow", "Add"))



if __name__ == '__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    def Add():
        data= {"FirstName": ui.firstNameValue.toPlainText(), "LastName": ui.firstNameValue.toPlainText(),
               "Address": ui.firstNameValue.toPlainText(),
               "Available": ui.available.isChecked()}
        print(data)
    ui.addButton.clicked.connect(Add)
    MainWindow.show()
    sys.exit(app.exec())
