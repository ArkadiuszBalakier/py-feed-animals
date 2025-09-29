from app.animals.animal import Animal


class Cat(Animal):
    def __init__(
            self,
            name: str,
            is_hungry: bool = True,
            appetite: int = 3
    ) -> None:
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")
