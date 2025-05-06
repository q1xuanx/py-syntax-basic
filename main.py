def is_even(x):
    return x % 2 == 0

def main():
    # Set
    st = {1,2,3,3}
    print(st)
    # List
    lst = [1,2,3,3]
    fil_lst = filter(is_even, lst)
    print((list)(fil_lst))
    n1 : float = 0.2 
    n2 : float = 0.3 

    print((int)(n1 + n2))

    for i in range(1,10):
        print(i)

    #List comprehension
    say_hello = [i for i in range(5)]
    print(say_hello)

    table = [[(i + 1) * j for j in range(6)] for i in range(6)]
    print(table)

    labels = ["even" if i % 2 == 0 else "odd" for i in range(6)]
    print(labels)

    even_numbers = [i for i in range(6) if i % 2 == 0]
    print(even_numbers)
    # Flat matrix
    matrix = [[1, 2], [3, 4], [5, 6]]
    """
    items    1 2 
    items    3 4 
    items    5 6 
    """
    flat = [i for items in matrix for i in items]
    print(flat)

    colors = ['red', 'blue']
    sizes = ['S', 'M', 'L']
    combinations = [f'{color} - {size}' for color in colors for size in sizes]
    print(combinations)

    nums = [1,2,3,4,4,5]
    sts = {i for i in nums}
    print(sts)

    name: str = "pham hoang nhan"
    dict_char = {ch: name.count(ch) for ch in name if ch != ' '}
    print(dict_char)


    name_2 = "oops banana"
    dict_char2 = {ch: name_2.count(ch) for ch in name_2 if ch != ' '}
    print(dict_char2)

    to_text = "||".join([f"{k}:{v}" for k, v in dict_char2.items()])
    print(to_text)


    #Zip 
    names_1 = ["Nhan", "Pham", "Hoang"]
    score = [20, 30, 40] 

    name_score = {f'{name}-{score}' for name, score in zip(names_1, score)}
    print(name_score)

    ## Unzip 
    pairs = list(zip(names_1, score))
    names_2, score = zip(*pairs)

    #Enumerate
    # Lap qua nhung co the kem theo index 
    test_2 = [20,30,40]
    em = [f'{i}: {nums}' for i, nums in enumerate(test_2)]
    print(em)

    # Generator expression (Optimize of List comprehension)
    squares = (x * x for x in range(10))
    for i in squares:
        print(f"\r {i}")
    #Filter, map, lambda
    nums = range(10)
    # 0 1 2 3 4 5 6 7 8 9 10
    print(nums)
    result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, nums)))
    print(result)

if __name__ == "__main__": 
    main()