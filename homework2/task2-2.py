list1 = ['key1', 'key2']
list2 = ['value1']
dict(filter(lambda x: x[0] is not None, map(lambda key, value: (key, value), list1, list2)))
{'key2': None, 'key1': 'value1'}
list2 = ['value1', 3, 6]
dict(filter(lambda x: x[0] is not None, map(lambda key, value: (key, value), list1, list2)))
{'key2': 3, 'key1': 'value1'}