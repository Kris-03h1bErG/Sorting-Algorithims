from basic_function import is_sorted , generate_unsortedlist
unsorted_list = generate_unsortedlist(5)
print(f"unsorted list: {unsorted_list}")
# This takes a while but will eventualy sort it tho past 10 is nigh imposible 
# 5 is .0004 seconds 10 is 6 minutes and 20 is 38.56 years!
def bozo_sort(unsorted_list):
    import random
    while True:
        if is_sorted(unsorted_list):
            print("list sorted!")
            break
        else:
            random.shuffle(unsorted_list)
            print(f"list not sorted shuffling again!: {unsorted_list}")
bozo_sort(unsorted_list)
