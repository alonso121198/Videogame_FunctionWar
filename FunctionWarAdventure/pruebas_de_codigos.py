

class Padre:
    def __init__(self,num=1,name="alonso"):
        self.num = 2
        self.prueba = num
        self.nombre = name
        self.theme  = None


class hijo(Padre):
    def __init__(self):
        super().__init__()


juan = hijo()
juan.theme = theme()
print(juan.num)
print(juan.prueba)
print(juan.nombre)