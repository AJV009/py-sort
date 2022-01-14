
my_list = input("Enter the list of numbers (separated with comma): ")
my_list = my_list.split(',')

# select sort method
print("1. Bubble Sort")
print("2. Merge Sort")
print("3. Insertion Sort")
method = input("Enter the method you want to use: ")

# bubble sort
def bubblesort(list):
   for iter_num in range(len(list)-1,0,-1):
      for idx in range(iter_num):
         if list[idx]>list[idx+1]:
            temp = list[idx]
            list[idx] = list[idx+1]
            list[idx+1] = temp
   return list

# merge sort
def merge_sort(unsorted_list):
   if len(unsorted_list) <= 1:
      return unsorted_list
   middle = len(unsorted_list) // 2
   left_list = unsorted_list[:middle]
   right_list = unsorted_list[middle:]
   left_list = merge_sort(left_list)
   right_list = merge_sort(right_list)
   return list(merge(left_list, right_list))

def merge(left_half,right_half):
   res = []
   while len(left_half) != 0 and len(right_half) != 0:
      if left_half[0] < right_half[0]:
         res.append(left_half[0])
         left_half.remove(left_half[0])
      else:
         res.append(right_half[0])
         right_half.remove(right_half[0])
   if len(left_half) == 0:
      res = res + right_half
   else:
      res = res + left_half
   return res

# Insertion sort
def insertion_sort(InputList):
   for i in range(1, len(InputList)):
      j = i-1
      nxt_element = InputList[i]
   while (InputList[j] > nxt_element) and (j >= 0):
      InputList[j+1] = InputList[j]
      j=j-1
   InputList[j+1] = nxt_element
   return InputList

if (method == "1"):
   print(bubblesort(my_list))
elif (method == "2"):
    print(merge_sort(my_list))
elif (method == "3"):
    print(insertion_sort(my_list))
else:
    print("Invalid method")
