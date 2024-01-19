





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

# numbers=[random.randint(1,100) for i in range(10)]
# print(numbers)
# try:
#     pick=int(input(f"Input index (0~{len(numbers)-1}) :"))
#
#     print(numbers[pick])
# except IndexError:
#     print("Out of range : Wrong index number")
# except ValueError:
#     print("Input Only Number~~")
# except Exception:
#     print("Error occurs")


# def desc():
#     def wrapper():
#         print("w")
#     print("a")
# #    return wrapper
# #desc()
#
#
# def something():
#     print("do something~~")
#
# something()






class FlyingMixin:
    def fly(self):
        return f"{self.name}이(가) 하늘을 훨훨 날아갑니다~~"

class SwimMixin():
    def swim(self):
        return  f"{self.name}이(가) 수영을 합니다"

class Pokemon():
    def __init__(self,name):
        self.name=name

class  Charizard(Pokemon,FlyingMixin):

    pass

class Gyarados(Pokemon,SwimMixin):
    pass

g1=Gyarados('가라도스')

c1=Charizard('리자몽')

print(c1.fly())
print(g1.swim())


#포케몬게임만들기