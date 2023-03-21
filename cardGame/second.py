class User:
    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age
    def full_name(self):
        return self.first+self.last
    def initials(self):
        return self.first[0]+self.last[0]
    def likes(self,likes):
        return self.first+ 'likes'+likes
    def is_senior(self):
        return self.age>=65
    def birthday(self):
        return self.age+1
user1=User('joe','mwangi',36)        
user2=User('kim','kardashian',33)        
print(user1,user2)
print(user1.full_name())
print(user1.initials())
print(user1.likes('food'))
print(user1.is_senior())
print(user1.birthday())