#!/usr/bin/python3
""" gpa_data.py | Tue, May 23, 2017 | Roman S. Collins | MIT License

    A custom data structure for storing GPA data.

"""
class GPA_Data:
    def __init__(self):
        self.quality_points = 0
        self.credits = 0

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

        self.update()

    def del_course(self, name):
        try:
            self.courses.pop(name)
        except KeyError:
            return

        self.update()

    def update(self):
        self.credits, self.quality_points = 0, 0

        for key, val in self.courses.items():
            for x in val:
                if val[x] != None:
                    # print(x, val[x])
                    if x == "Credits":
                        self.credits += val[x]

                    if x == "Quality Points":
                        self.quality_points += val[x]

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

def main():
    # Test so that only valid grades and numerical grades
    # are added to the data structure
    gpa_data = GPA_Data()
    gpa_data.add_course("Test Grade: A", 1, "A")
    gpa_data.add_course("Test Grade: B", 2, "B")
    gpa_data.add_course("Test Grade: C", 3, "C")
    gpa_data.add_course("Test Grade: 1.0", 3, 1.00)
    gpa_data.add_course("Test Grade: 2", 3, 2)
    gpa_data.add_course("Test Grade: 3.33", 3, 3.33)
    gpa_data.add_course("Test Grade: foo", 3, "foo")
    gpa_data.add_course("Test Grade: bar", 3, "bar")
    gpa_data.add_course("Test Grade: I", 3, "I")
    gpa_data.add_course("Test Grade: P", 3, "P")

    print("GPA: {}".format(gpa_data.gpa))
    print("QP : {}".format(gpa_data.quality_points))
    print("C  : {}".format(gpa_data.credits))
    for k, v in gpa_data.courses.items():
        print(k, v)

    # Test so that del course works and that
    # empty course list evaluates to 0
    gpa_data.del_course("Test Grade: A")
    gpa_data.del_course("Test Grade: B")
    gpa_data.del_course("Test Grade: C")
    gpa_data.del_course("Test Grade: 1.0")
    gpa_data.del_course("Test Grade: 2")
    gpa_data.del_course("Test Grade: 3.33")
    gpa_data.del_course("Test Grade: foo")
    gpa_data.del_course("Test Grade: bar")
    gpa_data.del_course("Test Grade: I")
    gpa_data.del_course("Test Grade: P")

    print("GPA: {}".format(gpa_data.gpa))
    print("QP : {}".format(gpa_data.quality_points))
    print("C  : {}".format(gpa_data.credits))
    if gpa_data.courses:
        for k, v in gpa_data.courses.items():
            print(k, v)
    elif not gpa_data.courses:
        print("{}")

    # Final test to confirm GPA was calculated correctly
    from random import randint as ri
    gpa_data.add_course("Test0 Random 3.0 Grade Course:", ri(1, 4), 3.0)
    gpa_data.add_course("Test1 Random 3.0 Grade Course:", ri(1, 4), 3.0)
    gpa_data.add_course("Test2 Random 3.0 Grade Course:", ri(1, 4), 3.0)
    gpa_data.add_course("Test3 Random 3.0 Grade Course:", ri(1, 4), 3.0)
    gpa_data.add_course("Test4 Random 3.0 Grade Course:", ri(1, 4), 3.0)
    gpa_data.add_course("Test5 Random 3.0 Grade Course:", ri(1, 4), 3.0)
    gpa_data.add_course("Test6 Random 3.0 Grade Course:", ri(1, 4), 3.0)
    gpa_data.add_course("Test7 Random 3.0 Grade Course:", ri(1, 4), 3.0)
    gpa_data.add_course("Test8 Random 3.0 Grade Course:", ri(1, 4), 3.0)
    gpa_data.add_course("Test9 Random 3.0 Grade Course:", ri(1, 4), 3.0)

    print("GPA: {}".format(gpa_data.gpa))
    print("QP : {}".format(gpa_data.quality_points))
    print("C  : {}".format(gpa_data.credits))
    if gpa_data.courses:
        for k, v in gpa_data.courses.items():
            print(k, v)
    elif not gpa_data.courses:
        print("{}")

if __name__ == "__main__":
    main()
