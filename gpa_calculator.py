#!usr/bin/python3
""" gpa_calculator.py | Wed, May 10, 2017 | Roman S. Collins

    https://nook.marlboro.edu/public/offices/registrar/gpa

"""
VERSION = "v0.1 (alpha)"
WIDTH, HEIGHT = 320, 400

# To set PID and Task Manager label/name
import setproctitle
setproctitle.setproctitle("GPA Calculator {}".format(VERSION))

# For Qt5 GUI API
# from PyQt5.QtWidgets import QApplication, QWidget, \
#                             QAbstractScrollArea, QAbstractSlider, \
#                             QButtonGroup, QPushButton, \
#                             QBoxLayout, QGridLayout, \
#                             QVBoxLayout, QHBoxLayout, \
#                             QLineEdit, QListWidget, \
#                             QListWidgetItem, QLabel

# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

# Unused
# from heapq import *

# Class for storing data
class GPA_Data:
    def __init__(self):
        self.gpa = 0
        self.qp = 0
        #
        num_equiv = {"A+": 4.33, "A": 4.0, "A-": 3.67,
                     "B+": 3.33, "B": 3.0, "B-": 2.67,
                     "C+": 2.33, "C": 2.0, "C-": 1.67,
                     "D+": 1.33, "D": 1.0, "D-": 0.67,
                     "F": 0.0,
                     "a+": 4.33, "a": 4.0, "a-": 3.67,
                     "b+": 3.33, "b": 3.0, "b-": 2.67,
                     "c+": 2.33, "c": 2.0, "c-": 1.67,
                     "d+": 1.33, "d": 1.0, "d-": 0.67,
                     "f": 0.0,
                     }

        # GPA, Total Credits, Total Quality Points
        self.courses = {"GPA": 0, "TC": 0, "TQP": 0}

    def __str__(self):
        return str(self.courses)

    def add_course(self, name, grade=0):
        if isinstance(name, str):
            if isinstance(grade, str):
                self.courses[name] = grade
            else:
                print("Course grade must be an int, float, or a valid letter grade.")
        else:
            print("Course name must be a string.")

        self.update()

    def add_grade(self, name, grade):
        if name in self.courses:
            self.courses[name] = grade
        else:
            print("Course must be a valid course (already added), if not, add it with the method\
                   add_course().")

        self.update()

    def update(self):
        for k, v in self.courses:
            if k != ("GPA" or "TC" or "TQP"):
                print(k, v)

class Win(QWidget):
    def __init__(self, title="GPA Calculator {}".format(VERSION)):
        super().__init__()
        self.title = title
        self.padd = 4
        self.res = (320, 400)

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

        # # Remove Course Button
        del_course_button = QPushButton("Delete Course(s)", self)
        del_course_button.setToolTip("Press to remove the checked courses.")
        # del_course_button.move(HEIGHT//3, WIDTH//3)
        del_course_button.clicked.connect(self.clicked_del_course_button)

        # TODO:
        # Enable adding and deleting courses via enter key on keyboard,

        # Add widgets to grid
        # grid.addWidget(add_course_button)
        # grid.addWidget(del_course_button)

        # hlayout.addWidget(add_course_button)
        # hlayout.addWidget(del_course_button)

        self.gpa_label = QLabel("GPA:")
        self.gpa_label.setAlignment(Qt.AlignCenter)
        llayout.addWidget(self.gpa_label)

        # Course List View
        self.courses_list_view = QListWidget()
        vlayout.addWidget(self.courses_list_view)
        print(dir(self.courses_list_view))

        aclayout.addWidget(self.add_course_name_textbox)
        aclayout.addWidget(self.add_course_credits_textbox)
        aclayout.addWidget(self.add_course_grade_textbox)
        aclayout.addWidget(add_course_button)

        vlayout.addWidget(del_course_button)

        self.show()

    @pyqtSlot()
    def clicked_add_course_button(self):
        # print("Test add course button!")
        course_name = self.add_course_name_textbox.text()
        course_credits = self.add_course_credits_textbox.text()
        course_grade = self.add_course_grade_textbox.text()

        # print("Course Name: {} Credits: {} Grade: {}".format(course_name,
        #                                                      course_credits,
        #                                                      course_grade))

        self.add_course_name_textbox.setText("")
        self.add_course_credits_textbox.setText("")
        self.add_course_grade_textbox.setText("")

        self.courses_list_view.addItem("{} {} {}".format(course_name,
                                         course_credits,
                                         course_grade))

        # TODO:
        # Add Course to data structure for storing data on courses
        # and calculating GPA

        # TODO:
        # Move cursor to self.add_course_name_textbox after every entry

    @pyqtSlot()
    def clicked_del_course_button(self):
        print("Test del course button!")

        # TODO:
        # Enable delete the selected course from the textview

        # TODO:
        # Remove course from the GPA_Data data structure

        # TODO:
        # Select the course just above the deleted course

        # Show the window, ALWAYS LAST
        # self.show()

def main():
    gpadata = GPA_Data()

    gui = Interface()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Win()
    sys.exit(app.exec_())

# main()

# def main():
#     num_equiv = {"A+": 4.33, "A": 4.0, "A-": 3.67,
#                  "B+": 3.33, "B": 3.0, "B-": 2.67,
#                  "C+": 2.33, "C": 2.0, "C-": 1.67,
#                  "D+": 1.33, "D": 1.0, "D-": 0.67,
#                  "F": 0.0,
#                  "a+": 4.33, "a": 4.0, "a-": 3.67,
#                  "b+": 3.33, "b": 3.0, "b-": 2.67,
#                  "c+": 2.33, "c": 2.0, "c-": 1.67,
#                  "d+": 1.33, "d": 1.0, "d-": 0.67,
#                  "f": 0.0,
#                  }
#     grades_list = []
#     course_grades = {"GPA": 0}

#     keep_adding = True
#     while keep_adding:
#         # Ask for input of course name and amount of credits
#         ask_name = input("Course name: ")

#         ask_credits = None
#         while not isinstance(ask_credits, int):
#             try:
#                 ask_credits = input("Number of credits: ")
#                 if isinstance(ask_credits, str):
#                     ask_credits = int(ask_credits)
#                 if isinstance(ask_credits, str):
#                     ask_credits = float(ask_credits)
#             except ValueError:
#                 print("Please enter a number, not {}".format(type(ask_credits)))
#                 pass

#         if not ask_name:
#             stop = input("Are you sure you would like to exit? (y/N): ")
#             if stop.lower() == "y":
#                 keep_adding = False
#                 break
#             if stop.lower() == "n":
#                 keep_adding = True
#                 continue

#         # Ask for a grade for the course
#         if ask_name:
#             grade = input("Enter grade: ")

#             if isinstance(grade, str):
#                 try:
#                     grade = int(grade)
#                 except ValueError:
#                     pass

#             if isinstance(grade, str):
#                 try:
#                     grade = float(grade)
#                 except ValueError:
#                     pass

#             if grade:
#                 # course_grades[ask_name] = grade
#                 if isinstance(grade, float) or isinstance(grade, int):
#                     course_grades[ask_name] = {"Credits": ask_credits,
#                                                "Grade": grade}
#                 elif grade in num_equiv:
#                     course_grades[ask_name] = {"Credits": ask_credits,
#                                                "Grade": num_equiv[grade]}

#             course_grades = calculate_gpa(course_grades)

#         # print(course_grades)

#     # gpa = sum(q_point) / len(q_point)
#     # print(gpa)

# def calculate_gpa(course_grades):
#     # print("\n", course_grades, "\n")
#     quality_points = {"Total Quality Points": 0, "Total Credits": 0}
#     for k, v in course_grades.items():
#         # print(course_grades)
#         if k != "GPA":
#             print(k, v)
#             # course_grades["GPA"] += v
#             quality_points[k] = course_grades[k]["Credits"] * \
#                                 course_grades[k]["Grade"]

#             quality_points["Total Quality Points"] += quality_points[k]
#             quality_points["Total Credits"] += course_grades[k]["Credits"]

#     course_grades["GPA"] = quality_points["Total Quality Points"] / \
#                            quality_points["Total Credits"]

#     # print("\n", course_grades, "\n")

#     return course_grades


# if __name__ == "__main__":
#     main()