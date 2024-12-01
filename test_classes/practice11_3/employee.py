class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = int(salary)
    def give_raise(self, raise_amount = 5000):
        self.salary += int(raise_amount)