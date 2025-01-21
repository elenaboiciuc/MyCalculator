#Import the main window UI class from the library module
from library import Ui_MainWindow

#Import necessary PyQt6 modules
from PyQt6 import QtCore, QtGui, QtWidgets

#Import the sys module for system-related functions
import sys


class Custom_MainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        #The super() function is used to call a method from the parent class.
        #In this case, it calls the setupUi method from Ui_MainWindow, which is the parent class of Custom_MainWindow.
        super().setupUi(MainWindow)

        #Connect button clicks to their respective methods
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
        self.open_parenthesis.clicked.connect(self.method_for_button_open_parenthesis)
        self.close_parenthesis.clicked.connect(self.method_for_button_close_parenthesis)
        self.point.clicked.connect(self.method_for_button_point)
        self.backspace.clicked.connect(self.method_for_button_backspace)
        self.Sum.clicked.connect(self.method_for_button_sum)
        self.Dif.clicked.connect(self.method_for_button_dif)
        self.Multip.clicked.connect(self.method_for_button_multip)
        self.Devide.clicked.connect(self.method_for_button_devide)
        self.equal_button.clicked.connect(self.method_for_button_equal)
        self.delete_button.clicked.connect(self.method_for_button_delete)

    def method_for_button_no_0(self):
        # Get the current text from the QLineEdit widget / from the calculator
        text_number = str(self.lineEdit.text())
        # Check if the current text contains an error message
        if "Error" in text_number:
            # Replace the error message with '0'
            text_number = "0"
        # Check if the current text is '0'
        elif text_number == "0":
            # Keep the text as '0' (no change needed)
            text_number = "0"
        else:
            # Append '0' to the current text
            text_number += "0"
        # Update the QLineEdit widget with the new text
        self.lineEdit.setText(text_number)

    def method_for_button_no_1(self):
        text_number = str(self.lineEdit.text())
        if "Error" in text_number:
            text_number = "1"
        # Check if the current text is '0'/if 1 is the first button pressed
        elif text_number == "0":
            text_number = "1"
        else:
            text_number += "1"
        self.lineEdit.setText(text_number)

    def method_for_button_no_2(self):
        text_number = str(self.lineEdit.text())
        if "Error" in text_number:
            text_number = "2"
        elif text_number == "0":
            text_number = "2"
        else:
            text_number += "2"
        self.lineEdit.setText(text_number)

    def method_for_button_no_3(self):
        # Get the text value from the Digital Output (QLineEdit)
        text_number = str(self.lineEdit.text())
        if "Error" in text_number:
            text_number = "3"
        elif text_number == "0":
            text_number = "3"
        else:
            text_number += "3"
        self.lineEdit.setText(text_number)

    def method_for_button_no_4(self):
        text_number = str(self.lineEdit.text())
        if "Error" in text_number:
            text_number = "4"
        elif text_number == "0":
            text_number = "4"
        else:
            text_number += "4"
        self.lineEdit.setText(text_number)

    def method_for_button_no_5(self):
        text_number = str(self.lineEdit.text())
        if "Error" in text_number:
            text_number = "5"
        elif text_number == "0":
            text_number = "5"
        else:
            text_number += "5"
        self.lineEdit.setText(text_number)

    def method_for_button_no_6(self):
        text_number = str(self.lineEdit.text())
        if "Error" in text_number:
            text_number = "6"
        elif text_number == "0":
            text_number = "6"
        else:
            text_number += "6"
        self.lineEdit.setText(text_number)

    def method_for_button_no_7(self):
        text_number = str(self.lineEdit.text())
        if "Error" in text_number:
            text_number = "7"
        elif text_number == "0":
            text_number = "7"
        else:
            text_number += "7"
        self.lineEdit.setText(text_number)

    def method_for_button_no_8(self):
        text_number = str(self.lineEdit.text())
        if "Error" in text_number:
            text_number = "8"
        elif text_number == "0":
            text_number = "8"
        else:
            text_number += "8"
        self.lineEdit.setText(text_number)

    def method_for_button_no_9(self):
        text_number = str(self.lineEdit.text())
        if "Error" in text_number:
            text_number = "9"
        elif text_number == "0":
            text_number = "9"
        else:
            text_number += "9"
        self.lineEdit.setText(text_number)

    def method_for_button_open_parenthesis(self):
        current_text = self.lineEdit.text()
        if "Error" in current_text:
            current_text = "("
        elif current_text == "0":
            current_text = "("
        # Check if the current text ends with an operator or '('
        elif current_text[-1] in "+-*/(":
            # Append '(' to the current text
            current_text += "("
        self.lineEdit.setText(current_text)

    def method_for_button_close_parenthesis(self):
        current_text = self.lineEdit.text()
        # Count the number of opening and closing parentheses in the current text
        open_parens = current_text.count('(')
        close_parens = current_text.count(')')
        if "Error" in current_text:
            current_text = ""
        # Check if the current text is not empty and ends with a digit or ')' and has more opening than closing parentheses
        elif (current_text and current_text[-1].isdigit() or current_text[-1] == ')') and open_parens > close_parens:
            current_text += ")"
        self.lineEdit.setText(current_text)

    def method_for_button_point(self):
        current_text = self.lineEdit.text()
        if "Error" in current_text:
            current_text = "0."
        elif not current_text:
            # Set the current text to '0.'
            current_text = "0."
        # Check if the last character is '0' and it's either the only character or follows an operator or '('
        elif current_text[-1] == '0' and (len(current_text) == 1 or current_text[-2] in "+-*/("):
            # Append '.' to the current text
            current_text += "."
        # Check if the last character is a digit and there is no '.' in the current number segment
        elif current_text[-1].isdigit() and '.' not in current_text.split()[-1]:
            # Append '.' to the current text
            current_text += "."
        # Check if the last character is an operator
        elif current_text[-1] in "+-*/":
            # Append '0.' to the current text
            current_text += "0."
        self.lineEdit.setText(current_text)

    def method_for_button_backspace(self):
        current_text = self.lineEdit.text()
        if "Error" in current_text or len(current_text) == 1:
            current_text = "0"
        else:
            # Remove the last character from the current text
            current_text = current_text[:-1]
        self.lineEdit.setText(current_text)

    def method_for_button_sum(self):
        text_number = str(self.lineEdit.text())
        # Check if the current text ends with an operator
        if text_number[-1] in '+-*/':
            pass  # Do nothing
        else:
            # Append '+' to the current text
            text_number += "+"
        self.lineEdit.setText(text_number)

    def method_for_button_dif(self):
        text_number = str(self.lineEdit.text())
        if text_number[-1] in '+-*/':
            pass
        else:
            text_number += "-"
        self.lineEdit.setText(text_number)

    def method_for_button_multip(self):
        text_number = str(self.lineEdit.text())
        if text_number[-1] in '+-*/':
            pass
        else:
            text_number += "*"
        self.lineEdit.setText(text_number)

    def method_for_button_devide(self):
        text_number = str(self.lineEdit.text())
        if text_number[-1] in '+-*/':
            pass
        else:
            text_number += "/"
        self.lineEdit.setText(text_number)

    def method_for_button_equal(self):
        expression = self.lineEdit.text()
        try:
            # Evaluate the expression safely
            total = eval(expression)  # Use eval to calculate total
            if total == int(total):
                # Convert to integer if the decimal part is zero
                total = int(total)
        except ZeroDivisionError:
            # Handle division by zero error
            self.lineEdit.setText("Error:   Division by zero")
            return
        except Exception:
            # Handle any other errors (e.g., invalid input)
            self.lineEdit.setText("Error:       Invalid input")
            return

        self.lineEdit.setText(str(total))

    def method_for_button_delete(self):
        # Reset the QLineEdit widget's text to '0'
        self.lineEdit.setText("0")


if __name__ == "__main__":
    # Create an instance of the QApplication
    app = QtWidgets.QApplication(sys.argv)
    # Create an instance of the QMainWindow
    MainWindow = QtWidgets.QMainWindow()
    # Create an instance of the Custom_MainWindow and set up the UI
    ui = Custom_MainWindow()
    ui.setupUi(MainWindow)
    # Show the main window
    MainWindow.show()
    # Execute the application and enter the main event loop
    sys.exit(app.exec())
