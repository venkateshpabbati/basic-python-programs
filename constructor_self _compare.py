class computer:

    def __init__(self):
        self.name = 'venky'
        self.age = 32

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
        
c1 = computer()
c1.age = 30
c2 = computer()

if c1.compare(c2):
    print('they are same')
else:
    print('they are different')

print(c1.age)
print(c2.age)

