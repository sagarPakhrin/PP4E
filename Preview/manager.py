from person import Person

class Manager(Person):
    def __init__(self,name,age,pay):
        Person.__init__(self,name,age,'manager')

    def giveRaise(self,percent,bonus=0.1):
        Person.giveRaise(self,percent + bonus)


if __name__ == "__main__":
    tom = Manager(name = "Tom Jones",age = 50)
    print(tom)
