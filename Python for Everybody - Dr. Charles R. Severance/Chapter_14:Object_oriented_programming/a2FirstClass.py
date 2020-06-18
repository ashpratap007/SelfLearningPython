class PartyAnimal:
    x = 0
    # This object has one attribute (x) and one method(party).
    # The methods have a special first parameter that we name by conventionself.
    
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)  #The following line is another way to call thepartymethod within the an object:

# In this variation, we access the code from within the class and explicitly pass theobject pointeranas
# the first parameter (i.e.,selfwithin the method). You canthink ofan.party() as shorthand for the above line

print("Type", type(an))
print("Dir", dir(an))
print("Type", type(an.x))  #you can see both thexinteger attribute and the party method areavailable in the object
print("Type", type(an.party))