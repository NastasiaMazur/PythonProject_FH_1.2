name = input("Please enter your name")
age = input("Please enter your age")
age = int(age)
#here the age is checked if its above 99
if age > 100:
    print("Haha, got you, you cant be older than 100")
elif age < 0:
    print("Haha, got you, you cant be younger than 0")
else:
    print(f"Hello my name is {name} and I am {age} old")