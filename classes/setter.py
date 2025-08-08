
#initializer:constructor

#Speical method in a class
#initializer: method is called whenver the blueprint is used
#To create an object
#method function is inside a class

#method your create you have to hhave thhe self: keyworkd

#how to create a class <-->What a class is
# initialiZer <constrocture>
# self key what it is :<this>

from datetime import datetime

def write_file(f_name,txt):
    with open(f_name,'a') as file:
        file.write(f"{txt} \n")
       

class Human():

    def __init__(self,gender,name):
        print("The initializer wass called")
        self._gender=gender
        self._name=name
        if self._gender=="Male":
            self._ribs=24
            self._curse="Suffer"
        else :
          self._ribs=23
          self._curse="Pain"

    @property
    def name(self):
        now = datetime.now()
        print("Curreent date and time",now)
        write_file(f_name="log.txt",txt=f"At {now} got name from Abdi")
        return self._name
    
    @name.setter
    def name(self,new_name):
        # data integrity
        if not isinstance(new_name,str):
            print("Failed to update name")
            return
        #new_name is astring
        now = datetime.now()
        print("Curreent date and time",now)
        write_file(f_name="log.txt",txt=f"At {now} Name changed from {self._name} to {new_name}")
        self._name=new_name
        return new_name

    def print_self(self):
        print("----------------------")
        print("name",self._name)
        print("gender",self._gender)
        print("ribs",self._ribs)
        print("curse",self._curse)
        print("---------------------")


# adam=Human(name="adam",gender="Male") #object from a class
Abdi=Human(name="Abdi",gender="Male")

#Getter a property of: <name>:
#print(Abdi.name)

Abdi.name=234

Abdi.print_self()

print(Abdi.name)
print(Abdi.name)
#log when somebody

#set is to update

Abdi.name="Hamsa"

# @property

Abdi.name="Abdi"

Abdi.name="Samson"