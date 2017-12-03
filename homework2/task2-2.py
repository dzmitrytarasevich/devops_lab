def main():

    list1 = ['key1', 'key2', 'key3', 'key4']
    #list1 = ['key1', 'key2']
    list2 = ['value1', 'value2', 'value3']
    return dict((n,m) for n,m in map(None, list1, list2) if n is not None)

if __name__ == '__main__':
   print main()
