def is_sorted(number_list):
    for i in range(len(number_list) - 1):                
        if number_list[i] > number_list[i + 1]:
            return False                
    return True

def generate_unsortedlist(length = 10, minimum = 1 , maximum = 100):
    import random
    unsorted_list = []
    for i in range (0,length):
        unsorted_list.append(random.randint(minimum,maximum))   
    return unsorted_list     
print(generate_list())

# make a sorted list btw later  