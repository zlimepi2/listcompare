def List2ProductsGreatest(list1,list2):
    products = []
    greatest = -10000000000
    for p1,p2 in zip(list1,list2):
        products.append(p1*p2)
    for each in products:
        if greatest < each:
            greatest = each
        else:
            pass
    return greatest
def List2ProductsLeast(list1,list2):
    products = []
    least = 10000000000
    for p1,p2 in zip(list1,list2):
        products.append(p1*p2)
    for each in products:
        if least < each:
            least = each
        else:
            pass
    return least
def List2AddsGreatest(list1,list2):
    products = []
    greatest = -10000000000
    for p1,p2 in zip(list1,list2):
        products.append(p1+p2)
    for each in products:
        if greatest < each:
            greatest = each
        else:
            pass
    return greatest
def List2AddsLeast(list1,list2):
    products = []
    least = 10000000000
    for p1,p2 in zip(list1,list2):
        products.append(p1+p2)
    for each in products:
        if least < each:
            least = each
        else:
            pass
    return least
choose = input("Choose 1-4, based on how you would like to compare your lists multiply greatest(1), multiply least(2), adds greatest(3), adds least(4)")
print("Enter two lists to compare in the following:")
list1 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
  
    list1.append(ele) 
list2 = []
for i in range(0, n):
    ele = int(input())
  
    list2.append(ele) 
if choose == 1:
    List2ProductsGreatest(list1,list2)
if choose == 2:
    List2ProductsLeast(list1,list2)
if choose == 3:
    List2AddsGreatest(list1,list2)
if choose == 4:
    List2AddsLeast(list1,list2)
