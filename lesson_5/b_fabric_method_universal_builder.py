"""
Паттерн "Фабричный метод".
    1. Реализовать класс SimpleFileBuilder для построения драйвера SimpleFileDriver
    2. В блоке __main__ убедиться в построении драйверов JsonFileDriver и SimpleFileDriver
    3. В паттерне "Стратегия" использовать фабрику для получение драйверов в getter свойства driver.
        Getter должен возвращать драйвер, если его нет, то вызывать фабрику для получения драйвера.
"""

from abc import ABC, abstractmethod

from a_driver import IStructureDriver, JsonFileDriver, SimpleFileDriver, CSVFileDriver, YamlFileDriver, \
    PickleFileDriver


class DriverBuilder(ABC):
    UNTITLED = 'untitled'

    @classmethod
    def get_file_name(cls, driver_name):
        filename = input(f'Введите название {driver_name} файла: (.{driver_name})').strip()
        filename = filename or f'{cls.UNTITLED}.{driver_name}'
        if not filename.endswith(f'.{driver_name}'):
            filename = f'{driver_name}.{driver_name}'

        return filename

    @abstractmethod
    def build(self, driver_name) -> IStructureDriver:
        ...


class DriverChoice:
    json = JsonFileDriver
    txt = SimpleFileDriver
    csv = CSVFileDriver
    yaml = YamlFileDriver
    pickle = PickleFileDriver


class BaseFileBuilder(DriverBuilder):

    def build(self, driver_name) -> IStructureDriver:
        filename = self.get_file_name(driver_name)

        return getattr(DriverChoice, driver_name)(filename)


class FabricDriverBuilder:
    default_driver = 'txt'

    @classmethod
    def get_driver(cls):
        driver_name = input("Введите название драйвера: ").strip()
        driver_name = driver_name or cls.default_driver
        builder = BaseFileBuilder()
        return builder.build(driver_name)


if __name__ == '__main__':
    driver = FabricDriverBuilder.get_driver()
    print(driver)
