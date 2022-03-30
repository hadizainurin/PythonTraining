#Object is an instntiation of a class. When Class is definied, only the description for the object is defined.
#Therefore, no mermoy or storage is allocated.
#In Python, everything is an object, while in C++ you have class then you need to create
# the object, then public/private(default)/protected access specifier and attribute (data type) 
#Let create an object of parrot class
#obj = Parrot()

class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print ("My name is {}".format(self.name))
    

class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name
    
    def reveal_identity(self):
        print ("...and I am {}".format(self.hero_name))
        return super(SuperHero, self).reveal_identity()

corey = Person('Corey')
corey.reveal_identity()