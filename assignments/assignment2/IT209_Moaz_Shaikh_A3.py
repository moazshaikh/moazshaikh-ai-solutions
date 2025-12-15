#-----------------------------------------------------------------------
# IT209_Moaz_Shaikh_A3.py - Department class utilization of Student class by Moaz Shaikh
#
# Department class is constructed to model characteristics of a university department.
# Department clas is a container class. Student class is
# utilized to incorporate multiclass modeling architecture. Department class will examine the Student
# object data and decide whether to add them to the major or not.
#
#
# Author: Moaz Shaikh 09/29/2025
#-----------------------------------------------------------------------

# Department class definition
class Department():
    univ_students = 0 # initially the number of University Students is set to 0 NOTE: Class Variable
    def __init__(self, d_code, d_name, capacity = 5, minGPA = 2.5):
        self.d_code = d_code
        self.d_name = d_name
        self.capacity = capacity
        self.minGPA = minGPA
        self.avgGPA = 0
        self.sRoster = []

    # __str__ method to display if department objects themselves are printed
    def __str__(self):
        return (self.d_name + ', ' + '(' + self.d_code + ')' + ', ' + 'capacity= ' + str(self.capacity) + ', ' + 'number of students= ' +
                str(len(self.sRoster)))


    # critical method that uses the isQualified method (next in code) to determine whether the student
    # object should be appended to the sRoster of that department and whether other changes should be made
    # otherwise it will call the isQualified method and return a reason for why the student object was not added
    def addStudent(self, student_object):
        if not isinstance(student_object, Student):
            return False, 'not a student object type'
        if len(self.sRoster) == self.capacity:
            return False, 'Department at capacity'
        if self.isQualified(student_object)[0]:
            self.sRoster.append(student_object)
            Department.univ_students += 1
            self.calcAvgGPA()
            student_object.setMajor(self.d_code)
            return True, 'added'
        else:
            return self.isQualified(student_object)


    # isQualified checks for whether the student object is enrolled, whether the student is already in roster,
    # or whether the GPA is too low and returns false with the correct reason for each condition.
    # otherwise it returns true meaning the student is qualified.
    def isQualified(self, student_object):
        if student_object.enrolled == 'n':
            return False, 'add failed: not enrolled'
        for s in self.sRoster:
            if student_object.equals(s):
                return False, 'dupe'
        if self.minGPA > student_object.gpa():
            return False, 'add failed: GPA too low'
        return True, 'qualified'


    def calcAvgGPA(self):
        totalGPA = 0
        for student in self.sRoster:
            totalGPA += student.gpa()
        average= totalGPA / len(self.sRoster)
        self.avgGPA = round(average, 2)
        return self.avgGPA

    # in order to display only some attributes of each student object in the sRoster of the DEPT,
    # a placeholder list was created and each attribute pair was appended to that list and then once
    # all attributes were appended the whole list is printed
    def dispRoster(self):
        print(f'Department name: {self.d_name}')
        placeholder_list = []
        if len(self.sRoster) == 0:
            print("There are no students")
        for s in self.sRoster:
            placeholder_list.append(s.g_num + ' ' + s.name)
        print(placeholder_list)


class Student():

    totalEnrollment = 0


    def __init__(self, name, major='IST', enrolled='y', credits=0, qpoints=0):
        self.name = name
        self.major = major
        self.enrolled = enrolled
        self.credits = credits
        self.qpoints = qpoints
        self.g_num = 'G' + '0000' + str(Student.totalEnrollment + 1)
        Student.totalEnrollment += 1

    def gpa(self):

        # Used a try and except block to handle 0 credits where the error arised would be ZeroDivisionError,
        # in which case the GPA should just be 0 and return that 0 value
        try:
            return self.qpoints / self.credits
        except ZeroDivisionError:
            return 0

    def addGrade(self, letter_grade, num_credits):
        self.letter_grade = letter_grade
        self.num_credits = num_credits
        letter_grade_value_dict = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
        # Test to make sure the number of credits entered is valid and letter grade entered is also valid and a part of
        # the dicionary we created to define letter grade values
        if self.num_credits in range(0, 5) and self.letter_grade in letter_grade_value_dict:
            letter_grade_value = letter_grade_value_dict[self.letter_grade]
            current_quality_points = self.num_credits * letter_grade_value
            self.credits += self.num_credits
            self.qpoints += current_quality_points
            return True
        else:
            return False

    def isActive(self):
        if self.enrolled == 'y':
            return True
        return False

    def classLevel(self):
        if self.credits >= 90:
            return 'Senior'
        elif self.credits >= 60:
            return 'Junior'
        elif self.credits >= 30:
            return 'Sophomore'
        else:
            return 'Freshman'

    def equals(self, other):
        if self is other: return True
        if type(other) != Student:
            return False
        if self.name == other.name and self.g_num == other.g_num:
            return True
        return False

    # new method added to alter the current major of the student object once it has qualified for the new major
    def setMajor(self, newMajor):
        self.major = newMajor
        return True

    def __str__(self):
        return (self.name + ', ' + self.g_num + ', ' + str(self.classLevel()) + ', ' + self.major + ', ' + 'active: ' +
                self.enrolled + ', ' + 'credits = ' + str(self.credits) + ', ' + 'gpa = ' + str(self.gpa()))

# Global/executable code ---------------------------------------------------
print('\nStart of Department and Student class demo **************')
input('\nTest1. Hit "Enter" to create 17 student objects for use in the demo ')
s1 = Student('David Miller', major='Hist', enrolled='y', credits=30, qpoints=90)
s2 = Student('Emma Maria Vicente', major='Math',
             enrolled='y', credits=90, qpoints=315)
s3 = Student('Chris Squire', major='Musc',
             enrolled='y', credits=45, qpoints=160)
s4 = Student('Tal Wilkenfeld', major='ARTS',
             enrolled='y', credits=70, qpoints=225)
s5 = Student('Larry Graham', major='CHHS',
             enrolled='y', credits=105, qpoints=315)
s6 = Student('Dave Holland', major='CSci',
             enrolled='y', credits=15, qpoints=39)
s7 = Student('Esperanza Spalding', major='ENGR',
             enrolled='y', credits=65, qpoints=250)
s8 = Student('Tim Bogert', major='Hist',
             enrolled='y', credits=45, qpoints=126)
s9 = Student('Gordon Sumner', major='Musc',
             enrolled='y', credits=15, qpoints=45)
s10 = Student('Paul McCartney', major='ARTS',
              enrolled='y', credits=110, qpoints=330)
s11 = Student('Tina Weymouth', major='ENGR',
              enrolled='y', credits=85, qpoints=250)
s12 = Student('John McVie', major='Hist',
              enrolled='y', credits=45, qpoints=126)
s13 = Student('Nawt enrolled', major='Hist',
              enrolled='n', credits=45, qpoints=120)
s14 = Student('Toolow G. Peyay', major='Undc',
              enrolled='y', credits=20, qpoints=38)
s15 = Student('Stanley Clark', major='Chem',
              enrolled='y', credits=95, qpoints=295)
s16 = Student('Geddy Lee', major='Chem',
              enrolled='y', credits=58, qpoints=143)
s17 = Student('Charles Mingus', major='Hist',
              enrolled='y', credits=91, qpoints=340)
print('\nList of Students created-------------------------------:\n ')
print('s1= ', s1)
print('s2= ', s2)
print('s3= ', s3)
print('s4= ', s4)
print('s5= ', s5)
print('s6= ', s6)
print('s7= ', s7)
print('s8= ', s8)
print('s9= ', s9)
print('s10= ', s10)
print('s11= ', s11)
print('s12= ', s12)
print('s13= ', s13)
print('s14= ', s14)
print('s15= ', s15)
print('s16= ', s16)
print('s17= ', s17)
d1 = Department('ENGR', 'Engineering', 5, 3.0)
d2 = Department('ARTS', 'Art and Architecture', 6, 2.5)
d3 = Department('CHHS', 'College of Health and Human Services', 3, 2.75)
d4 = Department('Hist', 'History Department', 5, 2.50)
input('\n\nTest2. Hit "Enter" to see the list of 4 Department objects created ')
print('\n\nDepartments established---------------------------------:')
print(d1)
print(d2)
print(d3)
print(d4)
input('\n\n\nTest3. Hit "Enter" to add s1 - s5 to ENGR Department- print student list\n')
d1.addStudent(s1)
d1.addStudent(s2)
d1.addStudent(s3)
d1.addStudent(s4)
d1.addStudent(s5)
d1.dispRoster()
input('\n\n\n\nTest4. Hit "Enter" to add additional student to ENGR - should fail, over capacity - ----: ')
a, b = d1.addStudent(s15)
print('\nAttempting to add ', s15.name, ' to ', d1.d_code, ' result: ')
print('\t\t\treturn values: ', a, ' reason code: ', b)
print('\nDepartment ', d1.d_name, ' student list is now: ')
d1.dispRoster()
input('\n\n\n\nTest5. Hit "Enter" to add two students to the ARTS Department ')
print('\nAttempting to add ', s6.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s6)
print('\t\t\treturn values: ', a, ' reason code: ', b)
print('\nAttempting to add ', s7.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s7)
print('\t\t\treturn values: ', a, ' reason code: ', b)
d2.dispRoster()
input('\n\n\n\nTest6. Hit "Enter" to add two students to the CHHS Department')
print('\nAttempting to add ', s8.name, ' to ', d3.d_code, ' result: ')
a, b = d3.addStudent(s8)
print('\t\t\treturn values: ', a, ' reason code: ', b)
print('\nAttempting to add ', s9.name, ' to ', d3.d_code, ' result: ')
a, b = d3.addStudent(s9)
print('\t\t\treturn values: ', a, ' reason code: ', b)
d3.dispRoster()
input('\n\n\n\nTest7. Hit "Enter" to try adding a student with low GPA to CHHS')
a, b = d3.addStudent(s14)
print('\nAttempting to add ', s14.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, ' reason code: ', b)
input('\n\n\n\nTest8. Hit "Enter" to try to add a non-enrolled student to the CHHS Department')
print('\nAttempting to add ', s13.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s13)
print('\t\t\treturn values: ', a, ' reason code: ', b)
input('\n\n\n\nTest9. Hit "Enter" to try adding a duplicate student ')
print('\nAttempting to add ', s8.name, ' to ', d3.d_code, ' result: ')
a, b = d3.addStudent(s8)
print('\t\t\treturn values: ', a, ' reason code: ', b)
input('\n\n\n\nTest10. Hit "Enter" to add s10 to ENGR, s11 to ARTS, s12 to CHHS.')
print(' then print all 4 department student lists')
print('\nAttempting to add ', s10.name, ' to ', d1.d_code, ' result: ')
a, b = d1.addStudent(s10)
print('\t\t\treturn values: ', a, ' reason code: ', b)
print('\nAttempting to add ', s11.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s11)
print('\t\t\treturn values: ', a, ' reason code: ', b)
print('\nAttempting to add ', s12.name, ' to ', d3.d_code, ' result: ')
a, b = d3.addStudent(s12)
print('\t\t\treturn values: ', a, ' reason code: ', b)
input('\n\n\n\nTest11. Hit "Enter" to try to add s16 to ARTS, which will fail for low gpa, ')
print(' then add a new course grade of "A"/3 credits to s15, and try the add again.')
print('\nStudent to be added to ARTS is ', s16)
a, b = d2.addStudent(s16)
print('\nResult of attempt to add ', s16.name, ' gpa: ', str(s16.gpa()), ' to ',
      d2.d_code)
print('\tis ', a, ', with reson code: ', b)
input('\n\n\n\nTest12. Adding 3 credit course with grade of "A" to ' + s16.name)
s16.addGrade("A", 3)
print('\nStudent profile is now: ', s16)
a, b = d2.addStudent(s16)
print('\nResult of second attempt to add ', s16.name, ' to ', d2.d_code)
print('\tis ', a, ', with reason code: ', b)
print('\nNote: ', s16.name, ' is now a ', s16.classLevel(), ' with gpa ',
      str(s16.gpa()))
input('\n\n\n\nTest13. Hit "Enter" to add s15 and s17 to ARTS.')
print('\nAttempting to add ', s15.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s15)
print('\t\t\treturn values: ', a, ' reason code: ', b)
print('\nAttempting to add ', s17.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s17)
print('\t\t\treturn values: ', a, ' reason code: ', b)
input('\n\n\n\nT14Hit "Enter" to see the final student list for all departments')
print('Number of students in ENGR = 5, ARTS = 6, CHHS = 3, Hist = 0 ')
print('\nNumber of students in ', d1.d_code, ' is ', len(d1.sRoster))
d1.dispRoster()
print('\nNumber of students in ', d2.d_code, ' is ', len(d2.sRoster))
d2.dispRoster()
print('\nNumber of students in ', d3.d_code, ' is ', len(d3.sRoster))
d3.dispRoster()
print('\nNumber of students in ', d4.d_code, ' is ', len(d4.sRoster))
d4.dispRoster()
print('\n\n\n***** End of A3 F24 Output **********')