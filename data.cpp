#include<iostream>
#include<string>
#include<unordered_map>
#include<variant>

/* using std::cout; */
/* using std::endl; */
/* using std::string; */
/* using std::to_string; */
/* using std::tuple; */
/* using std::get; */
/* using std::unordered_map; */

using namespace std;

class GradePointAverageData {
    public:
        double grandTotalCredits;
        double grandTotalQualityPoints;
        double gpa;

        unordered_map<string, tuple<float, float, float>> courses;
        unordered_map<string, float> equivalents = {
            {"A+", 4.33}, {"A", 4.0}, {"A-", 3.67},
            {"B+", 3.33}, {"B", 3.0}, {"B-", 2.67},
            {"C+", 2.33}, {"C", 2.0}, {"C-", 1.67},
            {"D+", 1.33}, {"D", 1.0}, {"D-", 0.67},
            {"F", 0.0}, {"S", -1.0}, {"U", -1.0},
            {"W", -1.0}, {"W", -1.0}, {"I", -1.0},
            {"P", -1.0}, {"PI", -1.0}
        };

        string toString() {
            string output_string;
            output_string += "{";

            if (!courses.empty()) {
                for (auto keyval : courses) {
                    tuple<float, float, float> tupleTemp = keyval.second;

                    string nameString = keyval.first; // Name
                    string creditsString = to_string(get<0>(tupleTemp));
                    string qualityPointsString = to_string(get<1>(tupleTemp));
                    string gradeString = to_string(get<2>(tupleTemp));

                    // TODO:
                    // inefficient string concatenation
                    output_string += nameString + ": (" + \
                                     creditsString + ", " + \
                                     qualityPointsString + ", " + \
                                     gradeString + ")";
                }
            } else {
                return NULL;
            }

            output_string += "}";
            return output_string;
        }

        bool addCourse(string courseName, float courseCredits, float courseGrade) {
            try {
                float qualityPoints = (courseGrade * courseCredits);

                grandTotalCredits += courseCredits;
                grandTotalQualityPoints += qualityPoints;

                tuple<float, float, float> tData(courseCredits, qualityPoints, courseGrade);
                courses[courseName] = tData;

                updateGPA();

                return true;
            } catch (...) {
                return false;
            }
        }

        bool addCourse(string courseName, float courseCredits, string courseGrade) {
            try {
                float courseGotGrade = equivalents.at(courseGrade);
                if (courseGotGrade < 0.0) {
                    // TODO:
                    // For now this will fail to add to the data structure,
                    // but the user should be notified that the grade
                    // does not affect gpa
                    return false;
                }

                float qualityPoints = (courseGotGrade * courseCredits);

                grandTotalCredits += courseCredits;
                grandTotalQualityPoints += qualityPoints;

                tuple<float, float, float> tData(courseCredits, qualityPoints, courseGotGrade);
                courses[courseName] = tData;

                updateGPA();

                return true;
            } catch (...) {
                return false;
            }
        }

        void updateGPA() {
            gpa = grandTotalQualityPoints / grandTotalCredits;
        }
};

int main() {
    GradePointAverageData gpa_data;

    // Course data should take these inputs to store data:
    //
    // + The name of the course as a std::string
    //
    // + The number of credits as either a std::int or std::float
    //
    // + The grade for the course as either a std::float or std::string,
    //   std::strings will be found in GradePointAverageData.equivalents
    //   and added to GradePointAverageData.courses after conversion to
    //   the correct float, with each insertion and deletion,
    //   GradePointAverageData.update() will run, calculating the gpa
    //
    // Course data toString() should iterate over the hash table
    // creating a string from the key value pairs outputing a string
    // displaying the data for debugging

    string name1 = "Introduction to Programming in C++";
    float credits1 = 4;
    string grade1 = "A";
    gpa_data.addCourse(name1, credits1, grade1);

    string name2 = "Plays of Shakespeare";
    float credits2 = 4;
    string grade2 = "A";
    gpa_data.addCourse(name2, credits2, grade2);

    // Now with a string for the grade
    string name3 = "Chemistry 101";
    float credits3 = 4;
    string grade3 = "A"; // toString should find "B-" in equivalents
    gpa_data.addCourse(name3, credits3, grade3);

    string name4 = "Physics 201";
    float credits4 = 4;
    string grade4 = "A";
    gpa_data.addCourse(name4, credits4, grade4);

    cout << gpa_data.toString() << endl;
    cout << gpa_data.gpa << endl;

    return 0;
}
