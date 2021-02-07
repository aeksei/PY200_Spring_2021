from typing import Any, Sequence, Optional


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

        if data:  # ToDo Проверить, что объект итерируемый. Метод self.is_iterable
            for value in data:
                self.append(value)

    def __str__(self):
        """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
        return f"{[value for value in self]}"

    def __repr__(self):
        """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
        return f"{type(self).__name__}({[value for value in self]})"

    def __len__(self):
        return self.__len

    def __step_by_step_on_nodes(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Int must be not")

        if not 0 <= index < self.__len:
            raise IndexError()

        current_node = self.head

        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __getitem__(self, item: int) -> Any:
        current_node = self.__step_by_step_on_nodes(item)

        return current_node.value

    def __setitem__(self, key, value: Any):
        current_node = self.__step_by_step_on_nodes(key)

        current_node.value = value

    def append(self, value: Any):
        """Добавление элемента в конец связного списка"""
        append_node = self.Node(value)
        if self.head is None:
            self.head = append_node
        else:
            tail = self.head  # ToDo Завести атрибут self.tail, который будет хранить последний узел
            for _ in range(self.__len - 1):
                tail = tail.next
            self.__linked_nodes(tail, append_node)

        self.__len += 1

    @staticmethod
    def __linked_nodes(left: Node, right: Optional[Node]) -> None:
        left.next = right

    def to_list(self) -> list:
        return [value for value in self]

    def insert(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError()

        if index == 0:
            insert_node = self.Node(value)
            self.__linked_nodes(insert_node, self.head)
            self.head = insert_node
            self.__len += 1

        elif 0 < index < self.__len:
            prev_node = self.__step_by_step_on_nodes(index - 1)
            current_node = prev_node.next
            insert_node = self.Node(value, next_=current_node)
            self.__linked_nodes(prev_node, insert_node)
            self.__len += 1

        elif index >= self.__len:
            self.append(value)

    def clear(self) -> None:
        self.head = None
        self.__len = 0

    def index(self, value: Any) -> int:
        index_ = 0
        for _ in self:
            if self[index_] == value:
                return index_
            elif index_ == self.__len - 1:
                raise ValueError(f"{value} is not in {self.__class__.__name__}")
            index_ += 1

    def remove(self, value: Any) -> None:
        index_ = self.index(value)
        if index_ == 0:
            self[index_] = None
            self.head = self.__step_by_step_on_nodes(index_ + 1)
            self.__len -= 1

        elif 0 < self.index(value) < self.__len:
            prev_node = self.__step_by_step_on_nodes(index_ - 1)
            remove_node = prev_node.next
            next_node = remove_node.next
            self.__linked_nodes(prev_node, next_node)
            self.__len -= 1

        elif self.index(value) == self.__len - 1:
            prev_node = self.__step_by_step_on_nodes(index_ - 1)
            prev_node = None
            self.__len -= 1

    def sort(self) -> None:
        list_ = [ord(i) if type(i) == str else i for i in self]
        self.clear()
        flag = True
        iterations = 0
        while flag:
            flag = False
            for i in range(len(list_) - iterations - 1):
                if list_[i] > list_[i + 1]:
                    list_[i], list_[i + 1] = list_[i + 1], list_[i]
                    flag = True
        iterations += 1
        for elem in list_:
            self.append(elem)

    def is_iterable(self, data) -> bool:
        """Метод для проверки является ли объект итерируемым"""
        ...

    def __contains__(self, item: Any):
        return any(item == value for value in self)


if __name__ == '__main__':
    # ll = LinkedList([1, 2, 3, 4])
    l1 = LinkedList('abcd')
    # print(ll)
    # l1[4] = 'f'
    # print(l1)
    # for value in l1:
    #     print(value)
    #
    # print('a' in l1)
    # print(l1.to_list())
    # print(l1[4])
    # print(l1.__str__())
    # print(l1.__repr__())
    # l1.insert(0, 'value')
    # print(l1)
    # l1.insert(len(l1), 'last_value')
    # print(l1)
    # print(l1.index('e'))
    # l1.remove('a')
    # l1.remove('d')
    # l1.remove('b')
    # print(l1)
    l2 = LinkedList(['\\', 'c', 'd', 5, 234, 5476, 77])
    print(l2)
    l2.sort()
    print(l2)
