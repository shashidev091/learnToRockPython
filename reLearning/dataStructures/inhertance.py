class A:
    def __init__(self):
        print('__init__ of class A')

    def feature(self):
        print("Feature 1 is working")

    def feature_2(self):
        print("feature 2 in working")


# class B(A):
class B:
    def __init__(self):
        # super().__init__()
        print("init of B")

    def feature_one(self):
        print("class B is woking")

    # def call_class_a_feature(self):
    #     self.feature()


class Combine(A, B):
    def __init__(self):
        super().__init__()
        B.__init__(self)

    def show(self):
        print("Hello brother")
        self.feature_one()

# class_b = B()
# class_b.feature()
# class_b.feature_2()
# class_b.call_class_a_feature()


combine = Combine()
combine.show()
