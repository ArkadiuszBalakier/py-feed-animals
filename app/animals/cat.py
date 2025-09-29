from app.animals.animal import Animal


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True, appetite: int = 3,):
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse():
        print("The hunt began!")