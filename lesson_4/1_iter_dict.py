"""
    Сделать свою реализацию словаря, в котором будет переопределен метод __iter__,
    чтобы он возвращал итератор не по ключам, а сразу по паре ключ, значение.
    Используйте наследование от встроеного типа dict, и полиморфизм для метода __iter__.
    Конструктор базового класса переопределять не нужно.
    Чтобы получить пары ключ-значение используйте либо метод базового self.items() либо
    функцию zip() для self.keys() и self.values()
"""

from typing import Iterator, Tuple, Hashable, Any


class MyDict(dict):
    def __iter__(self) -> Iterator[Tuple[Hashable, Any]]:
        return iter(self.items())


if __name__ == '__main__':
    dict_ = MyDict({i: i ** 2 for i in range(10)})
    for key, value in dict_:
        print(key, value)