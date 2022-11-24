data= ["1234","123456", "12345678910", "1234567","013", "011","8543210","12345","12345674"]

list1=[]
list2=[]
def tuple_of_item(arg):
    x=0
    while x < len(arg):
        if len(arg[x])<= 4:
            list1.append(arg[x])
        elif len(arg[x])>= 7:
            list2.append(arg[x])
        x= x+1
        
    y= (list1, list2)
    print(y)
tuple_of_item(data)


