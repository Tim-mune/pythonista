# class Pet:
#     def __init__(self,name,species) :
#         allowed=['cat','dog','fish','rat']
#         if species not in allowed:
#             raise ValueError('you cannot have such a pet')
#         self.name=name
#         self.species=species
# cat=Pet('gray','cat')
# print(cat.name) 

class Chicken:
    total_eggs=0
    def __init__(self,species,name):
        self.species=species
        self.name=name
        self.eggs=0
    def lay_egg(self):
        self.eggs+=1
        Chicken.total_eggs+=1
        return self.eggs
            
        