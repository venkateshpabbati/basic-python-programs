class computer:

    def __init__(self):
        self.name = 'venky'
        self.age = 32

    def update(self):
        self.name = 'rashi'
        self.age = 30

c1 = computer()
c2 = computer()

c1.update()

print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)
