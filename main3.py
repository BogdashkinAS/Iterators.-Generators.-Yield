# Задание 3* 

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.depth = 0
        self.count = -1

    def __iter__(self):
        while self.depth < len(self.list_of_list):
            tmp_list = []
            for item in self.list_of_list:
                if isinstance(item, list):
                    tmp_list.extend(item)
                else:
                    tmp_list.append(item)
            self.depth += 1
            self.list_of_list = tmp_list
        return self
    
    def __next__(self):
        self.count += 1
        if self.count == len(self.list_of_list):
            raise StopIteration
        else:
            return self.list_of_list[self.count]

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        # print(flat_iterator_item, check_item) # можно запустить для проверки идентичности списков

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()