class House:
    def __init__(self, name, qty_floors):
        self.name = name
        self.qty_floors = qty_floors

    def go_to(self, new_floor):
        if new_floor < 1 or self.qty_floors < new_floor:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.qty_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей {self.qty_floors}'

h1 = House('ЖК Горький', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

print(len(h1))
print(h1)
print(len(h2))
print(h2)
