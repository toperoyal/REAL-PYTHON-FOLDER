n = int(input("How many many numbers to work on  :")
)
list = []
for i in range(n):
    num = int(input("enter the number",))
    list.append(num)
Sum = sum(list)
Min = min(list)
Max = max(list)
avg = Sum / len(list)
print("sum of the numbers is : ", Sum) 
print("The minimum number is ", Min)
print("The maximum number is", Max)
print("Average is :", avg)


