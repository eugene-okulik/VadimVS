class Flower:
    stem = True
    petal = True

    def __init__(self, name, color, stem_length, cost, flower_age, life_flower=None):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.cost = cost
        self.flower_age = flower_age
        self.life_flower = life_flower

    def __repr__(self):
        return (f"{self.name}: (color={self.color}, stem_length={self.stem_length}, "
                f"cost={self.cost}, flower_age={self.flower_age})")


class Rose(Flower):
    presence_thorns = True

    def __init__(self, name, color, stem_length, cost, flower_age, life_flower=14):
        super().__init__(name, color, stem_length, cost, flower_age, life_flower)


class Tulip(Flower):
    is_spring_flower = True

    def __init__(self, name, color, stem_length, cost, flower_age, life_flower=7):
        super().__init__(name, color, stem_length, cost, flower_age, life_flower)


class Lily(Flower):
    spot_pattern = True

    def __init__(self, name, color, stem_length, cost, flower_age, life_flower=10):
        super().__init__(name, color, stem_length, cost, flower_age, life_flower)


class Bouquet:

    def __init__(self, freshness=None):
        self.freshness = freshness
        self.flowers_list = []  # Список для хранения экземпляров класса, добавляемых в этот атрибут экземпляра

    def add_arg_from_class_flower(self, flower: Flower):
        self.flowers_list.append(flower)

    def is_empty(self):  # Проверяем есть ли цветы в букете
        if not self.flowers_list:
            return True

    def wither(self):  # Когда завянет букет
        if self.is_empty():
            return "В букете нет цветов"
        self.avg_live_bouquet()
        self.live_our_bouquet()
        self.when_wither = ("Ваш букет завял" if self.result_live_bouquet < self.result_live_our_bouquet
                            else f"Завянет через {self.result_live_bouquet - self.result_live_our_bouquet}")
        return self.when_wither

    def avg_live_bouquet(self):  # Средняя жизнь всех цветов в букете (max live)
        if self.is_empty():
            return "В букете нет цветов"
        self.result_live_bouquet = (round(sum(flower.life_flower for flower in self.flowers_list)
                                          / len(self.flowers_list), 1))
        return self.result_live_bouquet

    def live_our_bouquet(self):  # средняя жизнь добавленных цветов в наш букет (our bouquet)
        if self.is_empty():
            return "В букете нет цветов"
        self.result_live_our_bouquet = (round(sum(flower.flower_age for flower in self.flowers_list)
                                              / len(self.flowers_list), 1))
        return self.result_live_our_bouquet

    def total_price(self):  # Стоимость всего букета
        if self.is_empty():
            return "В букете нет цветов"
        total_cost = sum(flower.cost for flower in self.flowers_list)
        return total_cost

    def sort_by(self, arg):  # (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
        if self.is_empty():
            return "В букете нет цветов"
        if arg != "freshness":
            sort_result = sorted(self.flowers_list, key=lambda flowers: getattr(flowers, arg))
            return sort_result
        else:
            self.freshness_flower()
            sort_result = sorted(self.flowers_list, key=lambda flower: flower.flower_age < flower.life_flower * 0.5)
            return sort_result

    def freshness_flower(self):  # Определяем свежесть каждого цветка
        if self.is_empty():
            return "В букете нет цветов"
        self.freshness = [flower for flower in self.flowers_list if flower.flower_age / flower.life_flower]
        return self.freshness

    def search_flower(self, arg):  # Метод для поиска цветов по определенному цвету
        if self.is_empty():
            return "В букете нет цветов"
        self.result_search = [flowers for flowers in self.flowers_list if arg == getattr(flowers, "color")]
        return self.result_search


# Создаем экземпляры цветов
rose1 = Rose(name="Роза", color="red", stem_length=50, cost=5, flower_age=3)
tulip1 = Tulip(name="Тюльпан", color="yellow", stem_length=30, cost=3, flower_age=1)
lily1 = Lily(name="Лилия", color="white", stem_length=40, cost=4, flower_age=2)

# Создаем экземпляр букета
bouquet = Bouquet()
bouquet2 = Bouquet()

# Добавляем цветы в букет
bouquet.add_arg_from_class_flower(rose1)
bouquet.add_arg_from_class_flower(tulip1)
bouquet.add_arg_from_class_flower(lily1)

print(bouquet2.avg_live_bouquet())  # Средняя жизнь всех цветов в букете 2, без цветов
print(bouquet.avg_live_bouquet())  # Средняя жизнь всех цветов в букете
print(bouquet.live_our_bouquet())  # Средняя жизнь добавленных цветов
print(bouquet.total_price())  # Стоимость букета
print(bouquet.sort_by("cost"))  # Сортировка по стоимости
print(bouquet.sort_by("freshness"))  # Сортировка по свежести (сначала определяем свежесть)
print(bouquet.search_flower("red"))  # Поиск красных цветов
print(bouquet.wither())  # Когда завянет букет
