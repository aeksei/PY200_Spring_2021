"""
Реализовать класс LinkedListWithDriver от класса LinkedList.
Дочерний класс должен уметь работать с реализованными ранее драйверами.

    1. Реализовать свойство driver, которое будет возвращать используемый драйвер и проверять, что устанавливаемый
        драйвер является экземпляром класса IStructureDriver.
    2. Реализовать метод read, который с помощью встроенного драйвера будет получать последовательность элементов и
        помещать их в самого себя. При вызове метода связанный список должен полностью перезаписываться новыми элементами.
    3. Реализовать метод write, который передавать последовательность элементов для записи драйвером.
    4. Протестировать паттерн "Стратегия" в ключе независимости работы экземляров LinkedListWithDriver от драйверов
        IStructureDriver. LinkedListWithDriver должен уметь работать со всеми экземплярами дочерних классов класс IStructureDriver.
    5. LinkedListWithDriver должен поддерживать "горячую замену" драйвера, то есть без удаления и создания нового
        экземпляра LinkedListWithDriver, а замена драйвера существующего экземпляра.
"""
from random import randint

from lesson_5.a_linkedlist import LinkedList
from lesson_5.a_driver import IStructureDriver

from lesson_5.b_fabric_method import FabricDriverBuilder


class LinkedListWithDriver(LinkedList):
    def __init__(self, data, driver: IStructureDriver = None):
        # ToDo вызвать конструктор базового класса LinkedList
        super().__init__(data)
        self.__driver = driver

    @property
    def driver(self):
        return self.__driver or FabricDriverBuilder.get_driver()

    @driver.setter
    def driver(self, driver: IStructureDriver):
        if not isinstance(driver, IStructureDriver):
            raise TypeError
        self.__driver = driver

    def read(self):
        """Взять драйвер и считать из него информацию в LinkedList"""
        output = self.driver.read()
        self.clear()
        for value in output:
            self.append(value)

    def write(self):
        """Взять драйвер и записать в него информацию из LinkedList"""
        self.driver.write(self)


if __name__ == '__main__':
    d = [randint(-10, 10) for i in range(10)]
    ll_rand = LinkedListWithDriver(d)
    print(ll_rand)
    ll_rand.driver = FabricDriverBuilder.get_driver()
    # ll.driver = FabricDriverBuilder.get_driver()
    ll_rand.driver.write(d)
    print(ll_rand.driver.read())
