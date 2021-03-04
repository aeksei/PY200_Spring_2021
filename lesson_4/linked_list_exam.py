from typing import Any, Sequence, Optional


class LinkedList:
    # noinspection PyUnresolvedReferences
    class Node:
        """
        Внутренний класс, класса LinkedList.
        Пользователь напрямую не работает с узлами списка, узлами оперирует список.
        """

        def __init__(self, value: Any, next_node: Optional["Node"] = None):
            """
            Создаем новый узел для односвязного списка
            :param value: Любое значение, которое помещено в узел
            :param next_node: следующий узел, если он есть
            """
            self.value = value
            self.next = next_node  # Вызывается сеттер

        @property
        def next(self):
            """Getter возвращает следующий узел связного списка"""
            return self.__next

        @next.setter
        def next(self, next_: Optional["Node"]):
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
        self.__head = None
        self.__tail = None

        if data:
            if self.is_iterable(data):
                for value in data:
                    self.append(value)
            else:
                self.append(data)

    @property
    def head(self):
        """Getter возвращает первый узел связанного списка"""
        return self.__head

    @head.setter
    def head(self, value):
        """Setter выполняет проверку на содержимое для установки значения head"""
        if isinstance(value, self.Node.__class__) or value is None:
            self.__head = value
        else:
            raise TypeError(f"{value} is not a proper value for head of the list")

    @property
    def tail(self):
        """Getter возвращает последний узел связанного списка"""
        return self.__tail

    @tail.setter
    def tail(self, value):
        """Setter выполняет проверку на содержимое для установки значения head"""
        if isinstance(value, self.Node.__class__) or value is None:
            self.__tail = value
        else:
            raise TypeError(f"{value} is not a proper value for tail of the list")

    def __str__(self):
        """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
        return f"{self.to_list()}"

    def __repr__(self):
        """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
        return f"{type(self).__name__}({self.to_list()})"

    def __len__(self):
        return self.__len

    def __getitem__(self, index: int) -> Any:
        if self.__is_index(index):
            if index < self.__len:
                item = self.__get_node(index)
                return item.value
            else:
                raise IndexError(f"Index {index} out of bounds")
        else:
            raise TypeError(f"Value {index} is not a valid index")

    def __setitem__(self, index, value):
        if self.__is_index(index):
            item = self.__get_node(index)
            item.value = value
        else:
            raise TypeError(f"Value {index} is not a valid index")

    def __node_iterator(self):
        """Итератор это подвид генератора, а с генераторами мы уже работать умеем с PY110"""
        node = self.head
        while True:
            if node is None:
                raise StopIteration

            yield node
            node = node.next

    def __iter__(self):
        return self.__node_iterator()

    def append(self, value: Any, increase_index=True):
        """Добавление элемента в конец связного списка"""
        append_node = self.Node(value)
        if self.__head is None:
            self.__head = append_node
            self.__tail = append_node
        else:
            self.__linked_nodes(self.__tail, append_node)
            self.__tail = append_node

        if increase_index:
            self.__len += 1

    def to_list(self) -> list:
        return [value for value in self]    # Итерирование мы уже реализовали с помощью магии, вот пусть оно и работает

    def insert(self, index: int, value: Any) -> None:
        if self.__is_index(index):
            if index == 0:  # если первый элемент
                to_insert = self.Node(value, self.__head)
                self.__head = to_insert
            if index == self.__len - 1:  # если последний элемент
                self.append(value, False)
            else:   # если любой другой элемент
                left = self.__get_node(index - 1)
                right = left.next
                to_insert = self.Node(value, right)
                left.next = to_insert
            self.__len += 1

    def clear(self) -> None:    # в питоне только так, за нас память чистит сборщик мусора
        self.__head = None
        self.__len = 0

    def index(self, value: Any) -> int:
        """Вообще-то раз у нас есть нормальный итератор, здесь можно воспользоваться enumerate(self)"""
        index = 0
        for node in self:
            if node.value == value:
                return index
            index += 1

        raise ValueError(f"{value} is not not in list")

    def remove(self, value: Any) -> None:
        """Ищем узел по значению и удаляем его из списка"""
        index = self.index(value)
        if index == 0:  # если первый элемент
            self.__head = self.__head.next
        else:  # если любой другой элемент
            left = self.__get_node(index - 1)
            current = self.__get_node(index)
            right = current.next
            left.next = right
        self.__len -= 1

    def sort(self) -> None:
        """сортирует список по возрастанию"""
        ll_to_list = self.to_list()
        sorted_ll = sorted(ll_to_list)
        self.clear()
        for value in sorted_ll:
            self.append(value)

    def __get_node(self, index: int) -> Any:
        """Возвращает узел по индексу"""
        current_node = self.__head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def __is_index(self, index) -> bool:
        if not isinstance(index, int):
            return False
        elif index > self.__len:
            return False
        return True

    @staticmethod
    def __linked_nodes(left: Node, right: Optional[Node]) -> None:
        left.next = right

    @staticmethod
    def is_iterable(data) -> bool:
        """Метод для проверки является ли объект итерируемым"""
        try:
            _ = (e for e in data)
            return True
        except TypeError:
            return False
