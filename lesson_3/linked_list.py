from typing import Any, Sequence, Optional
from collections.abc import Iterable

class LinkedList:
    class Node:
        """
        Внутренний класс, класса LinkedList.

        Пользователь напрямую не работает с узлами списка, узлами оперирует список.
        """
        def __init__(self, value: Any, next_: Optional['Node'] = None):
            """
            Создаем новый узел для односвязного списка

            :param value: Любое значение, которое помещено в узел
            :param next_: следующий узел, если он есть
            """
            self.value = value
            self.next = next_  # Вызывается сеттер

        @property
        def next(self):
            """Getter возвращает следующий узел связного списка"""
            return self.__next

        @next.setter
        def next(self, next_: Optional['Node']):
            """Setter проверяет и устанавливает следующий узел связного списка"""
            if not isinstance(next_, self.__class__) and next_ is not None:
                msg = f"Устанавливаемое значение должно быть экземпляром класса {self.__class__.__name__} " \
                      f"или None, не {next_.__class__.__name__}"
                raise TypeError(msg)
            self.__next = next_

        def __repr__(self):
            """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
            return f"Node({self.value}, {self.next})"

        def __str__(self):
            """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
            return f"{self.value}"

    def __init__(self, data: Sequence = None):
        """Конструктор связного списка"""
        self.__len = 0
        self.head = None  # Node
        self.tail = None

        if self.is_iterable(data):  # ToDo Проверить, что объект итерируемый. Метод self.is_iterable
            for value in data:
                self.append(value)

    def __str__(self):
        """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
        return f'{[value for value in self]}'

    def __repr__(self):
        """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
        result = [value for value in self]
        return f'{self.__class__.__name__}({result})'

    def __len__(self):
        return self.__len

    def __getitem__(self, item: int) -> Any:
        if not isinstance(item, int):
            raise TypeError()

        if not 0 <= item < self.__len:
            raise IndexError()

        current_node = self.head
        for _ in range(item):
            current_node = current_node.next
        return current_node.value

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError()

        if not 0 <= key < self.__len:
            raise IndexError()
        current_node = self.head
        for _ in range(key):
            current_node = current_node.next
        current_node.value = value

    def append(self, value: Any):
        """Добавление элемента в конец связного списка"""
        append_node = self.Node(value)
        if self.head is None:
            self.head = append_node
            self.tail = append_node
        else:
            # ToDo Завести атрибут self.tail, который будет хранить последний узел
            self.__linked_nodes(self.tail, append_node)
            self.tail = append_node
        self.__len += 1

    @staticmethod
    def __linked_nodes(left: Node, right: Optional[Node]) -> None:
        left.next = right

    def to_list(self) -> list:
        return [value for value in self]

    def insert(self, index: int, value: Any) -> None:
        if index == 0:
            first_node = self.Node(value)
            self.__linked_nodes(first_node, self.head)
            self.head = first_node
            self.__len += 1
        elif 0 < index < (self.__len - 1):
            insert_node = self.Node(value)
            prev_node = self.head
            for _ in range(index-1):
                prev_node = prev_node.next
            next_node = prev_node.next
            self.__linked_nodes(prev_node, insert_node)
            self.__linked_nodes(insert_node, next_node)
            self.__len += 1
        elif index >= self.__len:
            self.append(value)

    def clear(self) -> None:
        self.head = None
        self.__len = 0

    def index(self, value: Any) -> int:
        current_node = self.head
        for i in range(self.__len):
            if current_node.value == value:
                return i
            else:
                current_node = current_node.next
        raise ValueError(f'{value} not in list')

    def remove(self, value: Any) -> None:
        current_node = self.head
        left_node = self.head
        search_result = False
        for i in range(self.__len):
            if current_node.value == value:
                for _ in range(i-1):
                    left_node = left_node.next
                next_node = current_node.next
                current_node.value = None
                self.__linked_nodes(left_node, next_node)
                self.__len -= 1
                search_result = True
                break
            else:
                current_node = current_node.next
        if not search_result:
            raise ValueError(f'{value} not in list')

    def sort(self) -> None:
        ...

    def is_iterable(self, data) -> bool:
        """Метод для проверки является ли объект итерируемым"""
        if iter(data):
            return True


if __name__ == '__main__':
    ll = LinkedList([1, 2, 3, 4,5,6])
    ll.remove(9)
    print(ll)

    # print(l.index('b'))
