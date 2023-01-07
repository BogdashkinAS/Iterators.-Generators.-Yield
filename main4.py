# Задание 4*

import types


def flat_generator(list_of_list):
    depth = 0
    while depth < len(list_of_list):
        tmp_list = []
        for item in list_of_list:
            if isinstance(item, list):
                tmp_list.extend(item)
            else:
                tmp_list.append(item)
        list_of_list = tmp_list
        depth += 1
    for item2 in list_of_list:
        yield item2
    

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        # print(flat_iterator_item, check_item) # можно запустить для проверки идентичности списков
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()