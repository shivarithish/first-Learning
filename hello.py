print("hello is given by shiva")
name = input("enter ur name:")
age = int(input("enter a ur age:"))
if age>18:
    print("eligible for voting")
elif age==18:
    print("apply for voter id")
elif age<60:
    print("update ur voter id")

else:
    print("not eligible for voting")
