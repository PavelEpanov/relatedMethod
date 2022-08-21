class Number:
    def __init__(self, number):
        self.base = number
    def double(self):
        return self.base * 2
    def tripple(self):
        return self.base * 3

x = Number(2) # Объекты экземпляра класса
y = Number(3) # Состояние + методы
z = Number(4)
print(x.double()) # Нормальные прямые вызовы
acts = [x.double, y.tripple, z.double, y.double] # Список связанных методов
for act in acts: # Вызовы откладываются
    print(act()) # Вызовы, как если бы это были функции

bound = x.double
print(bound.__self__, bound.__func__)
print(bound.__self__.base)
print(bound()) # Вызывается bound.__func__(bound.__self__, ...)

