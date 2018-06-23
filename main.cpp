#include"gpa_data.h"
using namespace std;

int main() {
    // tests
    GPAData gpa_data;
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
