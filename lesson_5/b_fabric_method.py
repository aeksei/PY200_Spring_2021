"""
Паттерн "Фабричный метод".
    1. Реализовать класс SimpleFileBuilder для построения драйвера SimpleFileDriver
    2. В блоке __main__ убедиться в построении драйверов JsonFileDriver и SimpleFileDriver
    3. В паттерне "Стратегия" использовать фабрику для получение драйверов в getter свойства driver.
        Getter должен возвращать драйвер, если его нет, то вызывать фабрику для получения драйвера.
"""

from abc import ABC, abstractmethod

from lesson_5.a_driver import IStructureDriver, JsonFileDriver, SimpleFileDriver, CSVFileDriver


class DriverBuilder(ABC):
    @abstractmethod
    def build(self) -> IStructureDriver:
        ...


class JsonFileBuilder(DriverBuilder):
    DEFAULT_NAME = 'untitled.json'

    @classmethod
    def build(cls) -> IStructureDriver:
        filename = input('Введите название json файла: (.json)').strip()
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.json'):
            filename = f'{filename}.json'

        return JsonFileDriver(filename)


class SimpleFileBuilder(DriverBuilder):
    DEFAULT_NAME = 'untitled.txt'

    @classmethod
    def build(cls) -> IStructureDriver:
        filename = input('Введите название txt файла: (.txt)').strip()
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.txt'):
            filename = f'{filename}.txt'

        return SimpleFileDriver(filename)


class CSVFileBuilder(DriverBuilder):
    DEFAULT_NAME = 'untitled.csv'

    @classmethod
    def build(cls) -> IStructureDriver:
        filename = input('Введите название csv файла: (.csv)').strip()
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.csv'):
            filename = f'{filename}.csv'

        return CSVFileDriver(filename)


class FabricDriverBuilder:
    DRIVER_BUILDER = {
        'json': JsonFileBuilder,
        'txt': SimpleFileBuilder,
        'csv': CSVFileBuilder
    }
    DEFAULT_DRIVER = 'csv'

    @classmethod
    def get_driver(cls):
        driver_name = input("Введите название драйвера: ")
        driver_name = driver_name or cls.DEFAULT_DRIVER

        driver_builder = cls.DRIVER_BUILDER[driver_name]
        return driver_builder.build()


if __name__ == '__main__':
    driver = FabricDriverBuilder.get_driver()
    print(driver)
