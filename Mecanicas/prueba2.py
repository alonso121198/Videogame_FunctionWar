class Person():
    def __init__(self):
        self.name = "alonso"


class Employee(Person):

    # tu no pones nada pero se hereda lo que no pones

    def report(self):
        print("alonso")


def main():
    pedro = Person()
    print(pedro.name)

    carlos = Employee()
    print(carlos.name)


main()