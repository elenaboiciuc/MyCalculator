from library import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class Custom_MainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.number7.clicked.connect(self.method_for_button_no_7)
        self.number8.clicked.connect(self.method_for_button_no_8)
        self.number9.clicked.connect(self.method_for_button_no_9)
        self.number5.clicked.connect(self.method_for_button_no_5)
        self.number1.clicked.connect(self.method_for_button_no_1)
        self.number2.clicked.connect(self.method_for_button_no_2)
        self.number6.clicked.connect(self.method_for_button_no_6)
        self.number3.clicked.connect(self.method_for_button_no_3)
        self.number4.clicked.connect(self.method_for_button_no_4)
        self.number0.clicked.connect(self.method_for_button_no_0)
        self.Sum.clicked.connect(self.method_for_button_sum)
        self.Dif.clicked.connect(self.method_for_button_dif)
        self.Multip.clicked.connect(self.method_for_button_multip)
        self.Devide.clicked.connect(self.method_for_button_devide)
        self.equal_button.clicked.connect(self.method_for_button_equal)
        self.delete_button.clicked.connect(self.method_for_button_delete)

    def method_for_button_no_7(self):
        # Get the text value from the Digital Output (QLineEdit)
        text_number = str(self.lineEdit.text())
        if text_number == "0":
            text_number = "7"
        else:
            text_number += "7"
        self.lineEdit.setText(text_number)

    def method_for_button_no_8(self):
        # Get the text value from the Digital Output (QLineEdit)
        text_number = str(self.lineEdit.text())
        if text_number == "0":
            text_number = "8"
        else:
            text_number += "8"
        self.lineEdit.setText(text_number)

    def method_for_button_no_9(self):
        # Get the text value from the Digital Output (QLineEdit)
        text_number = str(self.lineEdit.text())
        if text_number == "0":
            text_number = "9"
        else:
            text_number += "9"
        self.lineEdit.setText(text_number)

    def method_for_button_no_5(self):
        # Get the text value from the Digital Output (QLineEdit)
        text_number = str(self.lineEdit.text())
        if text_number == "0":
            text_number = "5"
        else:
            text_number += "5"
        self.lineEdit.setText(text_number)

    def method_for_button_no_1(self):
        # Get the text value from the Digital Output (QLineEdit)
        text_number = str(self.lineEdit.text())
        if text_number == "0":
            text_number = "1"
        else:
            text_number += "1"
        self.lineEdit.setText(text_number)

    def method_for_button_no_2(self):
        # Get the text value from the Digital Output (QLineEdit)
        text_number = str(self.lineEdit.text())
        if text_number == "0":
            text_number = "2"
        else:
            text_number += "2"
        self.lineEdit.setText(text_number)

    def method_for_button_no_6(self):
        # Get the text value from the Digital Output (QLineEdit)
        text_number = str(self.lineEdit.text())
        if text_number == "0":
            text_number = "6"
        else:
            text_number += "6"
        self.lineEdit.setText(text_number)

    def method_for_button_no_3(self):
        # Get the text value from the Digital Output (QLineEdit)
        text_number = str(self.lineEdit.text())
        if text_number == "0":
            text_number = "3"
        else:
            text_number += "3"
        self.lineEdit.setText(text_number)

    def method_for_button_no_4(self):
        # Get the text value from the Digital Output (QLineEdit)
        text_number = str(self.lineEdit.text())
        if text_number == "0":
            text_number = "4"
        else:
            text_number += "4"
        self.lineEdit.setText(text_number)

    def method_for_button_no_0(self):
        # Get the text value from the Digital Output (QLineEdit)
        text_number = str(self.lineEdit.text())
        if text_number == "0":
            text_number = "0"
        else:
            text_number += "0"
        self.lineEdit.setText(text_number)

    def method_for_button_sum(self):
        # Get the text value from the Digital Output (QLineEdit)
        text_number = str(self.lineEdit.text())
        if text_number == "0" or text_number.endswith('+'):
            pass
        else:
            text_number += "+"
        self.lineEdit.setText(text_number)

    def method_for_button_dif(self):
        # Get the text value from the Digital Output (QLineEdit)
        text_number = str(self.lineEdit.text())
        if text_number == "0" or text_number.endswith('-'):
            pass
        else:
            text_number += "-"
        self.lineEdit.setText(text_number)

    def method_for_button_multip(self):
        # Get the text value from the Digital Output (QLineEdit)
        text_number = str(self.lineEdit.text())
        if text_number == "0" or text_number.endswith('*'):
            pass
        else:
            text_number += "*"
        self.lineEdit.setText(text_number)

    def method_for_button_devide(self):
        # Get the text value from the Digital Output (QLineEdit)
        text_number = str(self.lineEdit.text())
        if text_number == "0" or text_number.endswith('/'):
            pass
        else:
            text_number += "/"
        self.lineEdit.setText(text_number)

    def method_for_button_equal(self):
        expression = self.lineEdit.text()

        try:
            # Evaluate the expression safely
            total = eval(expression)  # Use eval to calculate total
        except ZeroDivisionError:
            self.lineEdit.setText("Error: Division by zero")  # Handle division by zero
            return
        except Exception:
            self.lineEdit.setText("Error: Invalid input")  # Handle any other errors
            return

        # Display the total
        self.lineEdit.setText(str(total))


    def method_for_button_delete(self):
        self.lineEdit.setText("0")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Custom_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())