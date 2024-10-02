class Freelancer:
    company = "Aerospace"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Employee:
    company = "Visa"
    eCode = 120


class Programmer(Freelancer, Employee):
    name = "Suruj"

p = Programmer()
p.upgradeLevel()
print(p.company)