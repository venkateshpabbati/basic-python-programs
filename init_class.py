class computer:

    def __init__(self, cpu, ram, company, price):
        self.cpu = cpu
        self.ram = ram
        self.company = company
        self.price = price
        

    def config(self):
        print("config is: ", self.cpu, self.ram, self.company, self.price)


com1 = computer('i5', 16, 'HP', 70000)
com2 = computer('ryzen 3', 8, 'lenovo', 65000)

com1.config()
com2.config()


