my_list =[];
my_list.extend([10,20,30,40])
print(my_list)

my_list.insert(1,15)
print(my_list)

my_list.extend([50,60,70])
print(my_list)

my_list.remove(70)
print(my_list)

my_list.sort()
print(my_list)

index_30 = my_list.index(30)

print(f"Index of 30 is {index_30}")