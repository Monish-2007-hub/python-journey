list1 = [1, 2, 2, 1]
list2 = [1, 2, 3, 1]
copy_list1 = list1.copy()
copy_list1.reverse()
copy_list2 = list2.copy()
copy_list2.reverse()

if(list1 == copy_list1):
    print("List1: ", list1, "is a palindrome")
else:
    print("List1 is not a palindrome")

if(list2 == copy_list2):
    print("List2: ", list2, "is a palindrome")
else:
    print("List2 is not a palindrome")
