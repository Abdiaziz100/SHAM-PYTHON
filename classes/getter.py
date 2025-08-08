from datetime import datetime

def write_file(f_name,txt):
    with open(f_name,'a') as file:
        file.write(f"{txt} \n")
       

class Human():

    def __init__(self,gender,name):
        print("The initializer wass called")
        self.gender=gender
        self.name=name
        if self.gender=="Male":
            self.ribs=24
            self.curse="Suffer"
        else :
          self.ribs=23
          self.curse="Pain"

    def get_name(self):
        now = datetime.now()
        print("Curreent date and time",now)
        write_file(f_name="log.txt",txt=f"At {now} got name from abdi")
        return self.name

    def print_self(self):
        print("----------------------")
        print("name",self.name)
        print("gender",self.gender)
        print("ribs",self.ribs)
        print("curse",self.curse)
        print("---------------------")


# adam=Human(name="adam",gender="Male") #object from a class
abdi=Human(name="abdi",gender="Male")

#Getter a property of: <name>:
# print(adam.name)

print(abdi.get_name())

# @property
