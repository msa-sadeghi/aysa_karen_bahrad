# def lcm(x,y):
#     if x > y:
#         res = x
#     else:
#         res = y
        
#     while True:
#         if (res % x == 0) and (res % y == 0):
#             break
#         res += 1
#     return res

# n1 = int(input("enter a number: "))
# n2 = int(input("enter a number: "))

# print(lcm(n1,n2))




# for i in range(5):
#     print("hello")
#     if i == 2:
#         break
# for i in range(5):
#     if i == 2:
#         continue
#     print("hello", i)


# for num in range(10,100):
#     if num % 2 == 0:
#         continue
#     if num % 3 == 0:
#         continue
#     if num % 5 == 0:
#         continue
#     if num % 7 == 0:
#         continue
#     print(num)

"""
    
Fahrenheit = Celsius × (9 / 5) + 32
Celsius = (Fahrenheit - 32) × (5 / 9)

"""

def convert_to_F(c):
    return c * 9/5 + 32

print(convert_to_F(12))

def convert_to_C(f):
    return (f - 32) * (5/9)

print(convert_to_C(23))



# for i in range(100_000, 1_235_001, 2):
#     s += i
    
# print(s)

# name = 'Alenna'
# for i in range(3):
#     for i in name:
#         print(i+'!')


# for i in range(4):
#     if i == 3:
#         break
#     print("salaam")
    
    
# for i in range(4):
#     if i == 2:
#         continue
#     print("salaam")

x = {}

names = ["person1", "person2", "person3"]
foods = ["food1", "food2", "food3"]
for i in range(3):
    name = names[i]
    food = foods[i]
    x[name] = food
    
print(x)

