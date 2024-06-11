class student:
    def __init__(self,name,id,course): 
        self.Name = name
        self.Id = id
        self.Course = course
    def info(self):
        print(f"Name:{self.Name}")
        print(f"Id:{self.Id}")
        print(f"Course:{self.Course}")

person1 = student("Tithi",22,"CSE") 
person1.info()  
person2 = student("Joy",11,"Msc")
person2.info()


