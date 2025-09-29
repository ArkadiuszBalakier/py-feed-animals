from app.animals.animal import Animal


class Dog(Animal):
    def __init__(self, name:str, is_hungry:bool = True, appetite:int = 7) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")