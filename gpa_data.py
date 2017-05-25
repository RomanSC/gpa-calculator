#!/usr/bin/python3
""" gpa_data.py | Tue, May 23, 2017 | Roman S. Collins | MIT License

    A custom data structure for storing GPA data.

"""
class GPA_Data:
    def __init__(self):
        self.quality_points = 0
        self.credits = 0
        self.blank_credits = 0

        # Numerical equivalents for grades
        # TODO:
        # Grades like P, WP, etc... should still be stored
        # but evaluate in a way that does not effect
        # GPA
        self.equivalents = {"A+": 4.33, "A": 4.0, "A-": 3.67,
                       "B+": 3.33, "B": 3.0, "B-": 2.67,
                       "C+": 2.33, "C": 2.0, "C-": 1.67,
                       "D+": 1.33, "D": 1.0, "D-": 0.67,
                       "F": 0.0, "S": None, "U": None,
                       "W": None, "WP": None, "WF": None,
                       "I": None, "P": None, "PI": None}

        # For storing courses data like so:
        # {"Course Name 0": {"Credits": 0, "Grade": 0, "Quality Points": 0}
        #  "Course Name 1": {"Credits": 0, "Grade": 0, "Quality Points": 0}
        #  "Course Name 2": {"Credits": 0, "Grade": 0, "Quality Points": 0}}
        self.courses = {}

        self.gpa = 0

    def __str__(self):
        return str(self.courses)

    def add_course(self, name, credits=0, grade=0):
        if isinstance(grade, str):
            grade = grade.upper()

            try:
                qp = credits * self.equivalents[grade]
            except (TypeError, KeyError) as exception:
                qp = None

            if grade in self.equivalents:
                self.courses[name] = {"Credits": credits,
                                      "Grade": self.equivalents[grade],
                                      "Quality Points": qp}

        elif isinstance(grade, int) or isinstance(grade, float):
            qp = credits * grade

            self.courses[name] = {"Credits": credits,
                                  "Grade": grade,
                                  "Quality Points": qp}
        if name not in self.courses:
            raise TypeError

        self.update()

    def del_course(self, name):
        try:
            self.courses.pop(name)
        except KeyError:
            return

        self.update()

    def update(self):
        self.gpa, self.credits, self.blank_credits, self.quality_points = 0, 0, 0, 0

        for key, val in self.courses.items():
            for x in val:
                if val["Grade"] != None and val[x] != None:
                    if x == "Credits":
                        self.credits += val[x]
                    if x == "Quality Points":
                        self.quality_points += val[x]
                if x == "Grade" and val["Grade"] == None:
                    self.blank_credits += val["Credits"]

        try:
            self.gpa = self.quality_points / self.credits
            try:
                if self.gpa.is_integer():
                    self.gpa = int(self.gpa)
                if self.quality_points.is_integer():
                    self.quality_points = int(self.quality_points)
            except AttributeError:
                pass
        except ZeroDivisionError:
            pass
