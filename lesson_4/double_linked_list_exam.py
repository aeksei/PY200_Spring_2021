"""
Двусвязный список на основе односвязного списка.

    Необязательно все эти методы должны быть переопределены в явном виде. По максимуму используйте
    наследование, если поведение списков в контексте реализации указанных метод схоже.
    С точки зрения наследования по минимуму перегружайте методы. При необходимости рефакторите базовый класс,
    чтобы локализовать части кода во вспомогательные функции, которые имеют различное поведение
    в связном и двусвязном списках.
    Стремитесь к минимизации кода в дочернем классе.

    Есть какой-то метод класса DoubleLinkedList хотите отработать в явном виде ещё раз, не возбраняется.
"""

from typing import Any, Sequence, Optional
import linked_list_exam as ll


class DoubleLinkedList(ll.LinkedList):
    class DoubleLinkedNode(super().Node):
        def __init__(self, value: Any,
                     next_: Optional['DoubleLinkedNode'] = None,
                     prev_: Optional['DoubleLinkedNode'] = None):
            super().Node.__init__(value, next_)
            self.prev = prev_

        @property
        def prev(self):
            """Getter возвращает следующий узел связного списка"""
            return self.__prev

        @prev.setter
        def prev(self, prev_: Optional["DoubleLinkedNode"]):
            """Setter проверяет и устанавливает следующий узел связного списка"""
            if not isinstance(prev_, self.__class__) and prev_ is not None:
                msg = f"Устанавливаемое значение должно быть экземпляром класса {self.__class__.__name__} " \
                      f"или None, не {prev_.__class__.__name__}"
                raise TypeError(msg)
            self.__prev = prev_

    # - ** `__str__` **
    """Работает полностью аналогично базовому классу"""

    # - ** `__repr__` **
    """Работает полностью аналогично базовому классу"""

    # - ** `__getitem__` **
    """Работает полностью аналогично базовому классу
    единственный момент - __get_node() можно бы переопределить чтоб искала с
    начала или с конца списка, смотря что ближе, раз список у нас теперь двусвязный
    но мне лень"""

    # - ** `__setitem__` **
    """Работает полностью аналогично базовому классу
    единственный момент - __get_node() можно бы переопределить чтоб искала с
    начала или с конца списка, смотря что ближе, раз список у нас теперь двусвязный
    но мне лень"""

    # - ** `__len__` **
    """Работает полностью аналогично базовому классу"""

    # - ** `insert` **
    """процедуру пришлось дополнить по сравнению с LinkedList"""
    def insert(self, index: int, value: Any) -> None:
        if self.__is_index(index):
            if index == 0:  # если первый элемент
                to_insert = self.DoubleLinkedNode(value, self.__head)
                self.__head.prev = to_insert                            # тут
                self.__head = to_insert
            if index == self.__len - 1:  # если последний элемент
                self.append(value, False)
            else:  # если любой другой элемент
                left = self.__get_node(index - 1)
                right = left.next
                to_insert = self.DoubleLinkedNode(value, right, left)   # тут
                left.next = to_insert
                right.prev = to_insert                                  # и тут
            self.__len += 1

    # - ** `index` **
    """Работает полностью аналогично базовому классу"""

    # - ** `remove` **
    def remove(self, value: Any) -> None:
        """процедуру пришлось дополнить по сравнению с LinkedList"""
        index = self.index(value)
        if index == 0:  # если первый элемент
            self.__head = self.__head.next
            self.__head.prev = None             # тут
        else:  # если любой другой элемент
            left = self.__get_node(index - 1)
            current = self.__get_node(index)
            right = current.next
            left.next = right
            right.prev = left                   # и тут
        self.__len -= 1

    # - ** `append` **
    """Работает полностью аналогично базовому классу, все изменения в статическом методе __linked_nodes()"""

    @staticmethod
    def __linked_nodes(left: Node, right: Optional[Node]) -> None:
        """процедуру пришлось дополнить по сравнению с LinkedList"""
        left.next = right
        right.prev = left   # тут

    # - ** `__iter__` **
    """Работает полностью аналогично базовому классу, и там и тут пока поддерживается только положительная индексация
    если реализовывать отрицательную, методы будут работать уже по-разному, двусвязный список проще перебирать из конца
    в начало, по сравнению с односвязным"""

    # - ** `clear` **
    def clear(self) -> None:
        """Двусвязный список вот так с полпинка не очистишь, нужно удалять ссылки в каждой ноде"""
        node = self.head
        self.__head = None
        self.__tail = None
        self.__len = 0
        while True:
            if node is None:
                break

            node.prev = None
            node.next = None
