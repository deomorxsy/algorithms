#!/usr/bin/python3

class Employee:
    'Commom base class for all employees'
    empCount = 0

    def __init(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        print("Name: ", self.name, ", Salary", self.salary)

