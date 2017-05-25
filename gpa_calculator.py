#!/usr/bin/python3
""" gpa_calculator.py | Wed, May 10, 2017 | Roman S. Collins | MIT License

    https://nook.marlboro.edu/public/offices/registrar/gpa

"""
VERSION = "v0.7 (alpha)"
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

        # For storage and calculation of courses, grades,
        # credits, and the resulting GPA
        self.gpa_data = GPA_Data()

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.padd, self.padd, self.res[0], self.res[1])

        # # Vertical Box Layout
        vlayout = QVBoxLayout()
        aclayout = QHBoxLayout() # Horizontal layout for add course
                                 # text entry and buttons
        llayout = QHBoxLayout() # Horizontal layout for label
        vlayout.addLayout(llayout)
        vlayout.addLayout(aclayout)
        self.setLayout(vlayout)

        # Add Course Text Box Labels

        # Add Course Text Box Entries
        self.add_course_name_textbox = QLineEdit(self)
        self.add_course_name_textbox_label = QLabel("Course Title:")
        self.add_course_name_textbox_layout = QVBoxLayout()
        self.add_course_name_textbox_layout.addWidget(self.add_course_name_textbox_label)
        self.add_course_name_textbox_layout.addWidget(self.add_course_name_textbox)
        # self.add_course_name_textbox.setText("Course Title")
        self.add_course_credits_textbox = QLineEdit(self)
        self.add_course_credits_textbox_label = QLabel("Credits:")
        self.add_course_credits_textbox_layout = QVBoxLayout()
        self.add_course_credits_textbox_layout.addWidget(self.add_course_credits_textbox_label)
        self.add_course_credits_textbox_layout.addWidget(self.add_course_credits_textbox)
        # self.add_course_credits_textbox.setText("Credits")
        self.add_course_grade_textbox = QLineEdit(self)
        self.add_course_grade_textbox_label = QLabel("Grade:")
        self.add_course_grade_textbox_layout = QVBoxLayout()
        self.add_course_grade_textbox_layout.addWidget(self.add_course_grade_textbox_label)
        self.add_course_grade_textbox_layout.addWidget(self.add_course_grade_textbox)
        # self.add_course_grade_textbox.setText("Grade")

        # Add Course Button
        self.add_course_button = QPushButton("Add Course", self)
        self.add_course_button_label = QLabel("")
        self.add_course_button_layout = QVBoxLayout()
        self.add_course_button_layout.addWidget(self.add_course_button_label)
        self.add_course_button_layout.addWidget(self.add_course_button)
        self.add_course_button.setAutoDefault(True)
        self.add_course_button.setToolTip("Press to add a course to calculate.")
        # self.add_course_button.move(HEIGHT//2, WIDTH//2)
        self.add_course_button.clicked.connect(self.clicked_add_course_button)
        # print(dir(self.add_course_button))

        # # Remove Course Button
        self.del_course_button = QPushButton("Delete Course(s)", self)
        self.del_course_button.setToolTip("Press to remove the checked courses.")
        # self.del_course_button.move(HEIGHT//3, WIDTH//3)
        self.del_course_button.clicked.connect(self.clicked_del_course_button)

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
        # self.courses_table.setHorizontalHeaderLabels(["Name:", "Credits:", "Grade:"])
        self.courses_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.courses_table.horizontalHeader().setVisible(False)
        self.courses_table.verticalHeader().setVisible(False)
        vlayout.addWidget(self.courses_table)

        # TODO:
        # Create method to update if data is updated

        # Test Courses:
        # row_count = self.courses_table.rowCount()
        # self.courses_table.insertRow(row_count)
        # self.courses_table.setItem(row_count, 0, QTableWidgetItem("Test0"))
        # self.courses_table.setItem(row_count, 1, QTableWidgetItem("2"))
        # self.courses_table.setItem(row_count, 2, QTableWidgetItem("2.67"))

        # row_count = self.courses_table.rowCount()
        # self.courses_table.insertRow(row_count)
        # self.courses_table.setItem(row_count, 0, QTableWidgetItem("Test1"))
        # self.courses_table.setItem(row_count, 1, QTableWidgetItem("3"))
        # self.courses_table.setItem(row_count, 2, QTableWidgetItem("3.33"))

        # row_count = self.courses_table.rowCount()
        # self.courses_table.insertRow(row_count)
        # self.courses_table.setItem(row_count, 0, QTableWidgetItem("Test2"))
        # self.courses_table.setItem(row_count, 1, QTableWidgetItem("4"))
        # self.courses_table.setItem(row_count, 2, QTableWidgetItem("4.00"))

        aclayout.addLayout(self.add_course_name_textbox_layout)
        aclayout.addLayout(self.add_course_credits_textbox_layout)
        aclayout.addLayout(self.add_course_grade_textbox_layout)
        aclayout.addLayout(self.add_course_button_layout)

        vlayout.addWidget(self.del_course_button)

        self.update()
        self.show()

    def update(self):
        self.gpa_label.setText("GPA: {:.2f}".format(self.gpa_data.gpa))

        # TODO:
        # Create method to update table if data is updated

    @pyqtSlot()
    def clicked_add_course_button(self):
        # try:
        #     new_data = {"Name": str(self.add_course_name_textbox.text()),
        #                 "Credits": int(self.add_course_credits_textbox.text()),
        #                 "Grade": float(self.add_course_grade_textbox.text())}
        # except ValueError:
        #     return

        # row_count = self.courses_table.rowCount()
        # self.courses_table.insertRow(row_count)

        # self.courses_table.setItem(row_count, 0, QTableWidgetItem(new_data["Name"]))
        # self.courses_table.setItem(row_count, 1, QTableWidgetItem(str(new_data["Credits"])))
        # self.courses_table.setItem(row_count, 2, QTableWidgetItem(str(new_data["Grade"])))

        # # TODO:
        # # Add Course to data structure for storing data on courses
        # # and calculating GPA

        # self.gpa_data.add_course(new_data["Name"], new_data["Credits"], new_data["Grade"])

        # # TODO:
        # # Move cursor to self.add_course_name_textbox after every entry

        # # TODO:
        # # Set GPA label to the current GPA value

        # self.add_course_name_textbox.setText("")
        # self.add_course_credits_textbox.setText("")
        # self.add_course_grade_textbox.setText("")
        try:
            try:
                self.gpa_data.add_course(self.add_course_name_textbox.text(),
                                         int(self.add_course_credits_textbox.text()),
                                         self.add_course_grade_textbox.text())
            except TypeError:
                self.gpa_data.add_course(self.add_course_name_textbox.text(),
                                         int(self.add_course_credits_textbox.text()),
                                         float(self.add_course_grade_textbox.text()))
        except ValueError:
            return

        row_count = self.courses_table.rowCount()
        self.courses_table.insertRow(row_count)

        self.courses_table.setItem(row_count,
                                   0,
                                   QTableWidgetItem(self.add_course_name_textbox.text()))

        self.courses_table.setItem(row_count,
                                   1,
                                   QTableWidgetItem(self.add_course_credits_textbox.text()))

        self.courses_table.setItem(row_count,
                                   2,
                                   QTableWidgetItem(self.add_course_grade_textbox.text().upper()))

        self.add_course_name_textbox.setText("")
        self.add_course_credits_textbox.setText("")
        self.add_course_grade_textbox.setText("")

        # print(self.gpa_data)

        # Updates
        self.update()

    # https://stackoverflow.com/questions/14588479/retrieving-cell-data-from-a-selected-cell-in-a-tablewidget
    @pyqtSlot()
    def clicked_del_course_button(self):
        index = self.courses_table.currentRow()
        item = self.courses_table.item(index, 0).text()
        self.gpa_data.del_course(item)
        self.courses_table.removeRow(index)


        # TODO:
        # Multiple selection

        # TODO:
        # Remove course from the GPA_Data data structure

        # Updates
        self.update()

def main():
    gui = Interface()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Win()
    sys.exit(app.exec_())
