#initializer:constructor

#Speical method in a class
#initializer: method is called whenver the blueprint is used
#To create an object
#method function is inside a class

#method your create you have to hhave thhe self: keyworkd

class Human():

    def __init__(self):
        print("The initializer wass called")
        
    def learn_self(self,object,gender,name):
        object.gender=gender
        object.name=name
        if object.gender=="Male":
            object.ribs=24
            object.curse="Suffer"
        else :
          object.ribs=23
          object.curse="Pain"
    
    def print_self(self):
        print("----------------------")
        print("name",self.name)
        print("gender",self.gender)
        print("ribs",self.ribs)
        print("curse",self.curse)
        print("---------------------")
    
# adam=Human(name="adam",gender="Male") #object from a class
adam=Human()
adam.learn_self(name="adam",gender="Male",object=adam)
adam.print_self()

eve=Human()
eve.learn_self(name="eve",gender="Female",object=eve)
eve.print_self()
# eve=Human(name="eve",gender="Female")
# print("name",eve.name)
# print("gender",eve.gender)
# print("ribs",eve.ribs)
# print("curse",eve.curse)