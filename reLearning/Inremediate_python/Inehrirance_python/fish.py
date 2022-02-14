from animal import Animal


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water")

    def breath(self):
        super().breath()
        print("doing this underwater.")
