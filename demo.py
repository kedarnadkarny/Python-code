num_array = list(9,8,7,6,5)

print ('Before sorting: ', num_array)

num_array.sort()
print ('After sorting: ', num_array)

num_array.pop(0)
num_array.pop()
print ('After removing smallest and largest values: ', num_array)

total=0
for x in num_array:
    total += x

print("Average is: ", total/len(num_array))