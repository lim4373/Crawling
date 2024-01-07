n_list= [[1,2,3 ],
         [4,5,6],
         [7,8,9]]
# sublist [1,2,3][4,5,6][7,8,9]
my_list = []
for sublist in n_list :
    for num in sublist:
        my_list.append(num)
print(my_list)

#print([ num for sublist in n_list for num in sublist])