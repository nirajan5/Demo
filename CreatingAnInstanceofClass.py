class Employee:
    id = 7
    name = "Ramesh"
    Designation = "Cyber security Expert"
    Expr = "5 yrs"

    def display(self):
        print("ID: %d \nName: %s \nDesignation: %s \nExpr: %s" % (self.id, self.name, self.Designation, self.Expr))


# Creating a emp instance of Employee class
emp = Employee()
emp.display()



