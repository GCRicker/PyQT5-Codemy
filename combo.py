import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add a title
        self.setWindowTitle("Hello World!!")

        # set Vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a Label
        my_label = qtw.QLabel("Pick something from the list")
        # Change the font size of the label
        my_label.setFont(qtg.QFont('Helvetica',26))

        self.layout().addWidget(my_label)

        # Create a Combo Box
        my_combo =qtw.QComboBox(self, editable=True, insertPolicy=qtw.QComboBox.InsertAtTop)
        # Add Items to the Combo Box
        my_combo.addItem("Cheese")
        my_combo.addItem("Pepperoni")
        my_combo.addItem("Peppers")

        # Place Combo Box on screen
        self.layout().addWidget(my_label)

        #Create a button
        my_button = qtw.QPushButton("Press Me!",
            clicked = lambda:press_it())
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

        def press_it():
            # Add name to label
            my_label.setText(f'You picked {my_combo.currentText()}!')
            

app = qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()

