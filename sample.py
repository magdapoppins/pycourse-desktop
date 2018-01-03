from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# In version 5 of PyQt, GtGui was split into QtPrintSupport and QtWidgets
import sys


# Override the default ctor inherited from QDialogue
class Hello(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        # super(Hello, self).__init__() is another alternative

        # vertical box layout. there would also be a grid, and horizontal
        layout = QVBoxLayout()

        label = QLabel("Hello App")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout)

        # Add handler for Qt event "clicked"
        # Note: no parenthesis in end of handler!
        button.clicked.connect(self.close)
        line_edit.textChanged.connect(self.change_text_label)

        # You might find older syntax in PyQt looking like this:
        # self.connect(line_edit, SIGNAL("textChanged(QString)"), self.change_text_label)

    def change_text_label(self, text):
        self.label.setText(text)


# Create a new instance of QApplication (this instance is unique within one app)
app = QApplication(sys.argv)
# Create a dialogue and show it
dialog = Hello()
dialog.show()

app.exec_()
# By default exits with code 0, you could also use
# sys.exit(app.exec_())


