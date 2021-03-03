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

    def get_file_name(self, format):
        filename = input(f'Введите название {format} файла: (.{format})').strip()
        filename = filename or f'{self.UNTITLED}.{format}'
        if not filename.endswith(f'.{format}'):
            filename = f'{filename}.{format}'

        return filename

    @abstractmethod
    def build(self, format) -> IStructureDriver:
        ...


class DriverChoice:
    json = JsonFileDriver
    txt = SimpleFileDriver
    csv = CSVFileDriver
    yaml = YamlFileDriver
    pickle = PickleFileDriver


class BaseFileBuilder(DriverBuilder):

    def build(self, format) -> IStructureDriver:
        filename = self.get_file_name(format)

        driver = getattr(DriverChoice, format)

        return driver(filename)


class FabricDriverBuilder:
    default_format = 'txt'

    @classmethod
    def get_driver(cls):
        format = input("Введите название драйвера: ").strip()
        format = format or cls.default_format
        builder = BaseFileBuilder()
        return builder.build(format)


if __name__ == '__main__':
    driver = FabricDriverBuilder.get_driver()
    print(driver)
    print(driver)
