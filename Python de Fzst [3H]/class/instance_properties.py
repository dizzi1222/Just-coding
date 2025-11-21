class Worker():
    def __init__(self, fullname, area, salary = 700):
        self.fullname = fullname
        self.area = area
        self.salary = salary 
    
juan = Worker("Juan Perez", "sales", salary = 1400)
david = Worker("David Perez", "IT", salary = 2000)

print(juan.fullname)
print(juan.area)
print(juan.salary)

print(david.fullname)
print(david.area)
print(david.salary)

