# Задание 1. 

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.item = []
        self.count = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            raise StopIteration
        for items in self.list_of_list:
            self.item.extend(items)
        self.count = 1
        item = self.item
        return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(*
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        # print(flat_iterator_item, check_item) # можно запустить для проверки идентичности списков

        assert flat_iterator_item == check_item

    assert list(*FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()