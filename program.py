def add_random_list (list_=[]):
    import random
    for i in range (0,21):
        list_.append(random.randint(10,12))
    return list_

def poisk (list, max=1):
    for i in range (0, len(list)-1):
        print(i,max)
        k=1
        while i+k < len (list) and list[i]==list[i+k]:
            k+=1
        if max<k:
            max=k
    return max
