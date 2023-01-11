# Задание 1. 

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.cursor = -1

    def __iter__(self):
        self.item = []
        for items in self.list_of_list:
                self.item.extend(items)
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.item):
            raise StopIteration
        else:
            return self.item[self.cursor]

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        # print(flat_iterator_item, check_item) # можно запустить для проверки идентичности списков

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()