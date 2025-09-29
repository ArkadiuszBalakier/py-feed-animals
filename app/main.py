from app.animals.animal import Animal
from app.animals.cat import Cat

lion = Animal("simba", 25)
lion.print_name()
food_points = lion.feed()
print(food_points)
print(lion.is_hungry)
print(lion.feed())

cat = Cat("Cat")
cat.print_name()
cat.feed()

cat2 = Cat("Cat2",False)
cat2.print_name()
points = cat2.feed()
print(points)
cat2.catch_mouse()