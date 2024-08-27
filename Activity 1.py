class stat766:
    Semester = 2024
    class_start_date = "Aug 19, 2024"
    class_end_date = "Dec 5, 2024"


class stat766_2(stat766):
    def __init__(self, Student_name, Student_major):
        self.Student = Student_name
        self.Major = Student_major
    
class stat766_3(stat766_2):
    def Add(self):
        return self.Student + ' ' + self.Major