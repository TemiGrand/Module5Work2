class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number}'

    def __len__(self):
        return self.number

    def go_to(self, new_floor):

        if not(new_floor < 1 or new_floor > self.number):
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print(f'В доме "{self.name}" этажа с номером "{new_floor}" не существует!')

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
#h1.go_to(5)
#h2.go_to(10)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))