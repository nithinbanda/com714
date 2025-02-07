class Student:
    def __init__(self, sn, sid, sy):
        self.sname = sn
        self.sid = sid
        self.syear = sy

    def getsname(self):
        return self.sname

    def getsid(self):
        return self.sid

    def getsyear(self):
        return self.syear

    def setsyear(self, sy):
        if type(sy) is str and (sy.lower() == "research methods" or sy.lower() == "sophomore" or sy.lower() == "msc" or sy.lower() == "senior"):
            self.syear = sy
        else:
            print("You have input an invalid value! The only allowable inputs are Research Methods, Sophomore, MSc, and Senior")


class Course:
    def __init__(self, cn, cid, sl):
        self.cname = cn
        self.cid = cid
        self.slist = sl

    def getcname(self):
        return self.cname

    def getcid(self):
        return self.cid

    def printallstudents(self):
        for i in self.slist:
            print(i.getSName(), i.getSid(), i.getSYear())

    def addstudent(self, st):
        if isinstance(st, Student):
            for i in self.slist:
                if i is st:
                    print("This student is already added to the course!")
                    return
            self.slist.append(st)
        else:
            print("Sorry, this is not a student!")


c1 = Course("Research Methods", "MAA103", [])

s1 = Student("Smith", "Q1234", "MSc Computing")
s2 = Student("John", "Q5678", "MSc Software Engineering")
s3 = Student("Kelly", "Q9010", "MSc Cybersecurity")

c1.addStudent(s1)
c1.addStudent(s2)
c1.addStudent(s3)

c1.printAllStudents()
