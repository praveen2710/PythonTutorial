from inheritance_parent import Parent

class Child(Parent):
    def __init__(self,last_name,eye_color,first_name,no_of_toys):
        print("Child constructor is called")
        Parent.__init__(self,last_name,eye_color)
        self.first_name = first_name
        self.no_of_toys = no_of_toys


randy_orton  = Child("rads","blue","orty",6)
print(randy_orton.eye_color)

