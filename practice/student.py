
class Stude:
    def __init__(self,name,major,gpa,is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


class Car():
    def __init__(self,company,type,mileage,is_new):
        self.company = company
        self.type = type
        self.mileage = mileage
        self.is_new = is_new
    
class Computer:
    def __init__(self,cpu,ram,hdd):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
    
    def print(self):
        print("The computer config is "+ self.cpu + str(self.ram) + self.hdd )

class Quest:
    def __init__(self,question_prompt,answer):
        self.question_prompt = question_prompt
        self.answer = answer


class chef:
    def chick():
        print(" MAking chicken")

    def paneer():
        print(" MAking paneer")

    def lassi():
        print(" MAking lassi")       

class Spechef(chef):
    def mutton():
        print("Make Mutton") 