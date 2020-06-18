# we define a class (template), use that class to create
# an instance of that class (object), and then use the 
# instance. 
# 
# When the program finishes, all of the variables 
# are discarded. Usually, we don’t think much aboutthe creation
# and destruction of variables, but often as our objects become 
# morecomplex, we need to take some action within the object
# to set things up as theobject is constructed and possibly clean
# things up as the object is discarded.If we want our object to 
# be aware of these moments of construction and destruction,we 
# add specially named methods to our object:

class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')
    
    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)

# As Python constructs our object, it calls our__init__method to give
# us a chanceto set up some default or initial values for the object. 
# When Python encountersthe line: an = 42

# It actually “thows our object away” so it can reuse theanvariable to 
# store the value 42. Just at the moment when ouranobject is being 
# “destroyed” our destructor code (__del__) is called.

# We cannot stop our variable from being destroyed, 
# butwe can do any necessary cleanup right before our object no longer exists


# When developing objects, it is quite common to add a constructor to an object
# to set up initial values for the object. It is relatively rare to need a 
# destructor for anobject


