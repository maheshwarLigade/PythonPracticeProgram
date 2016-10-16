class Parent():

    def __init__(self, last_name,eye_color):
        print("parent constructor is called")
        self.last_name =  last_name
        self.eye_color = eye_color




class Child(Parent):

    def __init__(self,last_name,eye_color,no_of_toys):
        print("inside the child constructor")
        Parent.__init__(self,last_name,eye_color)
        self.no_of_toys = no_of_toys

miley_cyrus = Child("Cyrus","Blue",5)
print(miley_cyrus.last_name)
print(miley_cyrus.no_of_toys)
