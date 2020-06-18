# When we construct multiple objects from our class, we might want to 
# set up dif-ferent initial values for each of the objects. We can pass 
# data to the constructorsto give each object a different initial value:


class PartyAnimal:
    x=0
    name=''

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

s = PartyAnimal("Sally")
j = PartyAnimal("Jim")

s.party()
j.party()
s.party()

# The constructor has both aselfparameter that points to the object
# instanceand additional parameters that are passed into the constructor
# as the object isconstructed:
# s = PartyAnimal('Sally')
# Within the constructor, the second line copies the parameter (nam) that is 
# passedinto thenameattribute within the object instance.
# self.name = nam
# The output of the program shows that each of the
# objects (sandj) contain their own independent copies of x and nam:
