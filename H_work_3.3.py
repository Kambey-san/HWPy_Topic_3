def my_func(a: int, b: int, c: int) -> int | str:
    my_list = [a, b, c]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return 'В списке может быть только число!'

print(my_func(4, 2, 11))