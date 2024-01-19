





# def f(n):
#     result=1
#     for i in range(2,n+1):
#         result=result*i
#     return result
#
# print(f(int(input())))


import random

# numbers=[]
# for i in range(5):
#     numbers.append(random.randint(1,100))

numbers=[random.randint(1,100) for i in range(10)]
print(numbers)
try:
    pick=int(input(f"Input index (0~{len(numbers)-1}) :"))

    print(numbers[pick])
except IndexError:
    print("Out of range : Wrong index number")
except ValueError:
    print("Input Only Number~~")
except Exception:
    print("Error occurs")



