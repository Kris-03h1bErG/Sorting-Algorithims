from basic_function import is_sorted , generate_unsortedlist

unsorted_list = generate_unsortedlist(10)
#this will never sort it it waits for particles to flip bits to hopefully sort it for it
def miracle_sort(unsorted_list):
    while True:
        if is_sorted(unsorted_list):
            print("List sorted!")
            return unsorted_list 
        else:
            is_sorted(unsorted_list)
            print("List not sorted checking again!")
miracle_sort(unsorted_list)