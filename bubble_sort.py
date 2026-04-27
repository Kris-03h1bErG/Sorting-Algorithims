from basic_function import is_sorted , generate_unsortedlist
unsorted_list = generate_unsortedlist(10)
print(f"unsorted list: {unsorted_list}")
def bubble_sort(unsorted_list):
    print("starting bubble sort")
    while True:
        if is_sorted(unsorted_list):
            print(f"List sorted! {unsorted_list}")
            return unsorted_list
        else:
            for i in range(len(unsorted_list) - 1):                
                if  unsorted_list[i] > unsorted_list[i + 1]:
                    unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1] , unsorted_list[i] 
                    print(f"new swaped list: {unsorted_list}")
bubble_sort(unsorted_list)