class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1, m2)

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1 > r2:
            print('S1 is greater')
        else:
            print('S2 is greater')

    def __sub__(self, other):
        sub1 = self.m1 - other.m1
        sub2 = self.m2 - other.m2
        return Student(sub1, sub2)


s1 = Student(10, 20)
s2 = Student(30, 49)

s3 = s1 + s2

print(s3.m1)

is_greater = s1 > s2

print((s1 - s2).m2)
