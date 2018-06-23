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
        int quality_points;
        int credits;
        int blank_credits;
        unordered_map<string, tuple<float, float>> courses;
        float gpa;

        unordered_map<string, float> equivalents = {
            {"A+", 4.33}, {"A", 4.0}, {"A-", 3.67},
            {"B+", 3.33}, {"B", 3.0}, {"B-", 2.67},
            {"C+", 2.33}, {"C", 2.0}, {"C-", 1.67},
            {"D+", 1.33}, {"D", 1.0}, {"D-", 0.67},
            {"F", 0.0}, {"S", NULL}, {"U", NULL},
            {"W", NULL}, {"W", NULL}, {"I", NULL},
            {"P", NULL}, {"PI", NULL}
        };

        string toString() {
            string output_string;
            output_string += "{";

            if (!courses.empty())
                for (auto keyval : courses) {
                    string x = keyval.first;
                    tuple<float, float> tupleTemp = keyval.second;
                    string y = "(" + to_string(get<0>(tupleTemp)) + ", " + to_string(get<1>(tupleTemp)) + ")";
                    output_string += x + ": " + y + ", ";
                }
            else
                return NULL;

            output_string += "}";
            return output_string;
        }

        void addCourse(string courseName, float courseCredits, float courseGrade) {
            tuple<float, float> tData(courseCredits, courseGrade);
            courses[courseName] = tData;
        }

        bool addCourse(string courseName, float courseCredits, string courseGrade) {
            try {
                float courseNewGrade = equivalents.at(courseGrade);
                tuple<float, float> tData(courseCredits, courseNewGrade);
                courses[courseName] = tData;
                return true;
            } catch (...) {
                return false;
            }
        }

        void updateGPA() {
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
    float grade1 = 4.33;
    gpa_data.addCourse(name1, credits1, grade1);

    string name2 = "Plays of Shakespeare";
    float credits2 = 2;
    float grade2 = 0.00;
    gpa_data.addCourse(name2, credits2, grade2);

    // Now with a string for the grade
    string name3 = "Chemistry 101";
    float credits3 = 3;
    string grade3 = "B-"; // toString should find "B-" in equivalents
    gpa_data.addCourse(name3, credits3, grade3);

    cout << gpa_data.toString() << endl;

    return 0;
}
