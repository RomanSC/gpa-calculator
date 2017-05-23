#!/usr/bin/python3
""" gpa_calculator.py | Wed, May 10, 2017 | Roman S. Collins | MIT License

    https://nook.marlboro.edu/public/offices/registrar/gpa

"""
VERSION = "v0.5 (alpha)"
WIDTH, HEIGHT = 400, 500

# To set PID and Task Manager label/name
import setproctitle
setproctitle.setproctitle("GPA Calculator {}".format(VERSION))

# For Qt5 GUI API
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

# For storing data
from gpa_data import GPA_Data

class Win(QWidget):
    def __init__(self, title="GPA Calculator {}".format(VERSION)):
        super().__init__()
        self.title = title
        self.padd = 4
        self.res = (WIDTH, HEIGHT)

        # TODO:
        # Create instance of GPA_Data here

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.padd, self.padd, self.res[0], self.res[1])

        # # Grid Box Layout
        # # http://zetcode.com/gui/pyqt5/layout/
        # glayout = QGridLayout()
        # self.setLayout(glayout)

        # # Vertical Box Layout
        vlayout = QVBoxLayout()
        # hlayout = QHBoxLayout()
        # vlayout.addLayout(hlayout)
        aclayout = QHBoxLayout() # Horizontal layout for add course
                                 # text entry and buttons
        llayout = QHBoxLayout() # Horizontal layout for label
        vlayout.addLayout(llayout)
        vlayout.addLayout(aclayout)
        self.setLayout(vlayout)

        # Add Course Text Box Entries
        self.add_course_name_textbox = QLineEdit(self)
        self.add_course_credits_textbox = QLineEdit(self)
        self.add_course_grade_textbox = QLineEdit(self)

        # Add Course Button
        add_course_button = QPushButton("Add Course", self)
        add_course_button.setToolTip("Press to add a course to calculate.")
        # add_course_button.move(HEIGHT//2, WIDTH//2)
        add_course_button.clicked.connect(self.clicked_add_course_button)
        # print(dir(add_course_button))

        # # Remove Course Button
        del_course_button = QPushButton("Delete Course(s)", self)
        del_course_button.setToolTip("Press to remove the checked courses.")
        # del_course_button.move(HEIGHT//3, WIDTH//3)
        del_course_button.clicked.connect(self.clicked_del_course_button)

        # TODO:
        # Enable adding and deleting courses via enter key on keyboard,

        # TODO:
        # Save button

        self.gpa_label = QLabel("GPA:")
        self.gpa_label.setAlignment(Qt.AlignCenter)
        llayout.addWidget(self.gpa_label)

        # Course List View
        # self.courses_list_view = QListWidget()
        # vlayout.addWidget(self.courses_list_view)
        # print()
        # print(dir(self.courses_list_view))
        # print()

        # Course Table View
        # headers = ["Name:", "Credits:", "Grade:"]
        # self.courses_table_view = QTableView()
        # vlayout.addWidget(self.courses_table_view)
        # print(dir(self.courses_table_view))
        self.courses_table = QTableWidget()
        self.courses_table.setColumnCount(3)
        self.courses_table.setHorizontalHeaderLabels(["Name:", "Credits:", "Grade:"])
        self.courses_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.courses_table.verticalHeader().setVisible(False)
        vlayout.addWidget(self.courses_table)

        # TODO:
        # Create method to update if data is updated

        # Test Courses:
        row_count = self.courses_table.rowCount()
        self.courses_table.insertRow(row_count)
        self.courses_table.setItem(row_count, 0, QTableWidgetItem("Test0"))
        self.courses_table.setItem(row_count, 1, QTableWidgetItem("2"))
        self.courses_table.setItem(row_count, 2, QTableWidgetItem("2.67"))

        row_count = self.courses_table.rowCount()
        self.courses_table.insertRow(row_count)
        self.courses_table.setItem(row_count, 0, QTableWidgetItem("Test1"))
        self.courses_table.setItem(row_count, 1, QTableWidgetItem("3"))
        self.courses_table.setItem(row_count, 2, QTableWidgetItem("3.33"))

        row_count = self.courses_table.rowCount()
        self.courses_table.insertRow(row_count)
        self.courses_table.setItem(row_count, 0, QTableWidgetItem("Test2"))
        self.courses_table.setItem(row_count, 1, QTableWidgetItem("4"))
        self.courses_table.setItem(row_count, 2, QTableWidgetItem("4.00"))

        # TODO:
        # Create labals for items

        aclayout.addWidget(self.add_course_name_textbox)
        aclayout.addWidget(self.add_course_credits_textbox)
        aclayout.addWidget(self.add_course_grade_textbox)
        aclayout.addWidget(add_course_button)

        vlayout.addWidget(del_course_button)

        self.show()

    def update_gpa_label(self):
        self.gpa_label.setText("GPA: {}".format("temp test"))

    @pyqtSlot()
    def clicked_add_course_button(self):
        try:
            new_data = {"Name": str(self.add_course_name_textbox.text()),
                        "Credits": int(self.add_course_credits_textbox.text()),
                        "Grade": float(self.add_course_grade_textbox.text())}
        except ValueError:
            return

        row_count = self.courses_table.rowCount()
        self.courses_table.insertRow(row_count)

        self.courses_table.setItem(row_count, 0, QTableWidgetItem(new_data["Name"]))
        self.courses_table.setItem(row_count, 1, QTableWidgetItem(str(new_data["Credits"])))
        self.courses_table.setItem(row_count, 2, QTableWidgetItem(str(new_data["Grade"])))

        # TODO:
        # Add Course to data structure for storing data on courses
        # and calculating GPA

        # TODO:
        # Move cursor to self.add_course_name_textbox after every entry

        # TODO:
        # Set GPA label to the current GPA value

        self.add_course_name_textbox.setText("")
        self.add_course_credits_textbox.setText("")
        self.add_course_grade_textbox.setText("")

        # Updates
        self.update_gpa_label()

    # https://stackoverflow.com/questions/14588479/retrieving-cell-data-from-a-selected-cell-in-a-tablewidget
    @pyqtSlot()
    def clicked_del_course_button(self):
        index = self.courses_table.currentRow()
        self.courses_table.removeRow(index)

        # TODO:
        # Multiple selection

        # TODO:
        # Remove course from the GPA_Data data structure

        # Updates
        self.update_gpa_label()

def main():
    gui = Interface()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Win()
    sys.exit(app.exec_())
