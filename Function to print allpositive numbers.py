j=[]
def positive_numbers(num_list):
    for i in num_list:
        if(i>0):
            j.append(i)
    return j
        
list1=[12,-7,5,64,-14]
print("The input is: ",list1)
print("Output: ",positive_numbers(list1))





