
###BEGIN DEMONSTRATION ####

#Create a class called Dog. This create a blueprint for any object of the type Dog, and
#then we define the operation that dog can do.

class Dog: #conventional UpperCase and CamelCase
    ###METHOD ---> A function that go inside a class
    def __init__(self,name,age): #Special method, self is the actual reference to each dog
        #Store in the dog object (attributes)
        self.name = name #Store attribute permanently name = name_dog
        self.age = age #self attribute .age = whatever age 
        # pass #Instantiate the object as it is created, pass Dog("Tim")
    #You can also reference the method inside the class
    def get_name(self):
        return self.name #This will  get the dog name which come from __init__ function
    #Now lets reference the age
    def get_age(self):
        return self.age
    #Now lets create a method to modified other method
    def set_age(self, age):
        self.age = age

    # def add_one(self, x):
    #     return x + 1 #make the method take argument

    # def bark(self): ###All method parameters start with a method call self
    #     print("bark")

#pass any argument and put it to 
d = Dog("Tim", 34) #Pass the name in Dog("name") --> to the name parameter from __init__ function
d.set_age(23)
d2 = Dog("Bill", 12) #This 2nd dog object, with different name inside of their instance
print(d.get_name(), d.get_age(), d2.get_age()) #reference from method inside class

####END DEMONSTRATION ####

### Multiple calss ###

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade # 0 - 100
#     #We could have test, weighting, etc. but let start with a simple function to get grade
#     def get_grade(self): 
#         return self.grade

# #Add ability to add student to course
# class Course:
#     def __init__(self,name,max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = [] #attributes is whatever we decide to define
    
#     def add_student(self,student): #We going tot ake student
#         if len(self.students) < self.max_students:
#            self.students.append(student) #Add student to the list
#            return True
#         return False 
    
#     def get_average_grade(self):
#         # pass #We will do this later
#         value = 0 #initially start at 0
#         for student in self.students:
#             value += student.get_grade() #This code will not break as long we modified get_grade
#             #This shows we can modified object in a clean way
#         return value / len(self.students)

# s1 = Student("Tim", 19, 95)
# s2 = Student("Bill", 19, 75)
# s3 = Student("Jill", 19, 65)
# s4 = Student("Mary", 18, 50)
# #Add student to course
# course = Course("Science", 3) #Shows what happen max, student is added in ascending order
# course.add_student(s1)
# course.add_student(s2)
# course.add_student(s3)
# course.add_student(s4)
# print(course.get_average_grade())
# # print(course.students[0].name) #This will shows if we do specified the array [0]][<__main__.Student object at 0x000002835E77FFD0>, <__main__.Student object at 0x000002835E77FDF0>]

####Inheritance####
## Can you tell why this is inefficient? Notice that the only difference is the method speak
#there must be a way we can inherited from an upper level class that all the funtionality is define in one place
#So instead of __init__ Cat and Dog with the same method, we only define the speak

# class Pet: #general
#     def __init__(self,name,age): #--> pass to super().__init__(arg1,arg2)
#         self.name = name
#         self.age = age
#     def show(self): #Show functionality of pet class
#         print(f"I am {self.name} and I am {self.age} year old") #f is formatted string literals, with {self.name} is what we will used when we reference to this class

#     def speak(self):
#         print("I am a pet, what you think I can talk?")
# #Define method that is different
# class Cat(Pet): #Cat(Inheritance) so Cat is inherited from Pet
#     # def __init__(self, name, age):
#     #     self.name = name
#     #     self.age = age

#     #Add a way to define cat colouir
#     def __init__(self, name, age, color):
#         super().__init__(name, age) #super reference the super class which is the class we inherited from, its going to run anything in the initialization in Pet()
#         self.color = color #In this initializatin, we don't want to redefine attribute

#     def speak(self): #If there is a method in this lower-level class that is the same from upper-level class then the lower-level method will override the method pass froom Upper
#         print("Meow")

#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

# #Lets think about working in a company Manager & Employee. Both have same attributes name and age but different access level.
# class Dog(Pet):
#     # def __init__(self, name, age):
#     #     self.name = name
#     #     self.age = age
    
#     def speak(self):
#         print("Bark")

# class Fish(Pet):
#     pass

# p = Pet("Tim", 19) 
# p.speak()
# C = Cat("Bill", 34) #This cat is inherited from the Pet class as we define in our class
# C.show()
# C.speak()
# D = Dog("Jill", 25) #This dog object is inherited from Pet class
# D.show()
# D.speak()
# F = Fish("Bubbles", 10)
# F.speak() #This will inherit the speak from Pet() because there is no speak define in Fish()
#Speak method is different for Cat and Dog class
###END OF INHERITANCE#####

# ###Static method and class attributes###

# class Person:
#     number_of_people = 0 #the same
#     GRAVITY = -9.8

#     def __init__(self, name):
#         self.name = name #different
#         Person.add_person()

#         # Person.number_of_people += 1 #This keep track how many person we have, this way its automatically increment
    
#     @classmethod #Act on class itself #decorator to denote this specific method as a class method
#     def number_of_people_(cls): #cls has no object, its just acting on this class and not just on behalf of one instance
#         return cls.number_of_people #returning the number_of_people associate with the class itself

#     @classmethod #So we know its not referencing self, but the class
#     def add_person(cls):
#         cls.number_of_people += 1

# p1 = Person("tim")
# p2 = Person("Jill")
# p3 = Person("Mary")
# print(Person.number_of_people) #This does not work if we do not have Person.add_person() because it is confused with the the def number_of_people so fix its by naming its slightly different

###STATIC METHOD###
# class Math:
#     #How to call this class at any point
#     @staticmethod #All they do is something but does not change anything
#     def add5(x): #Act as a function define in this class
#         return x + 5
    
#     @staticmethod
#     def add10(x):
#         return x + 10

#     @staticmethod
#     def pr():
#         print("run")

# print(Math.add10(5))
# Math.pr()



#This is not specific to the class not to the instance, meaning p1.number_of_person --> 0
#The way Python intepret this is that, 1) Is this a class person? Yes 2) Does this has attribute number_of_people? No, then inherited number_of_people
####NOTED#####
#Noted you will get an error if you forgot to used () for str or int
#Variable d is assigned to an instance class dog, Dog() is the name of the class with the () as instantiating, creating a new instance of class dog
# d.bark() #call method bark
# print(d.add_one(5))
# print(type(d)) #class '__main__.Dog', this shows what module the class run (which is by default __main__)

### NOTES ###
# x = 1 # This is an int, if you put type(x) it will give int
# print(type(x)) #Type shows what class the object is, so this object is class: string or <str>

# string = "hello"
# print(string.upper())

# #Noted regarding upper() method
# #With join
# def uppercase(str_data):
#     return ''.join([chr(ord(char) - 32) for char in str_data if ord(char) >= 65])
# #No join
# def uppercase(str_data):
#     result = ''
#     for char in str_data:
#         if ord(char) >= 65:
#             result += chr(ord(char) -32)
#     return result

#Procedural programming
#This is short but consider case where we have 25000 dogs, are you going to define each dog name?
# dog1_name = "Tim", we can also used an array dogs_name = ["Tim", "Bill"] --> This will cost us time as we have to access the right index
# dog1_age = 34