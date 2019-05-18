def add_random_list (list_=[]):
    import random
    for i in range (0,21):
        list_.append(random.randint(10,12))
    return list_
print(add_random_list())
