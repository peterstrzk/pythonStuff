class NewClass:
    def __init__(self, model, color):
        self.x = "siema"
        self.model = model
        self.color = color


    def asking_about_car(self):
        print(self.x)
        print(f"Your car is {self.model} with {self.color} ")

a = input("Choose your car brand \n")
b = input("Choose a color \n")
n = NewClass(a, b)
n.asking_about_car()
