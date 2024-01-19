# class Cat():
#     def __init__(self,name,age,nemsis):
#         self.name=name
#         self.age=age
#         self.nemsis=nemsis
# a_cat=Cat("totoro",4,'another_cat')
# another_cat=Cat("mimi",5,'another_cat')
#
# furball=Cat('Frumpy',8,'another_cat')
#
# print(furball.name)
# print(a_cat.name)
# print(another_cat.name)
#
# print(furball.age)
# print(a_cat.age)
# print(another_cat.age)
#
#
# print(furball.nemsis)
# print(a_cat.nemsis)
# print(another_cat.nemsis)
#
# print(type(furball))
#
#
# # print(a_cat.age)
# # print(a_cat.name)
# # print(a_cat.nemsis.name)

# class Car():
#     def exclamin(self):
#         print("Im a car")
# class Yogo(Car):
#     def exclamin(self):
#         print("im a Yogo")
#     def need_a_push(self):
#         print("need help")
#
# car1=Car()
# car2=Yogo()
#
# car1.exclamin()
# car2.exclamin()
#
# car2.need_a_push()


# class Person():
#     def __init__(self,name):
#         self.name=name
# class MDPerson(Person):
#     def __init__(self,name):
#         self.name="Doctor"+ " "+name
# class JDPerson(Person):
#     def __init__(self, name):
#         self.name = name+" Esquire"
#
# eun=MDPerson("eun")
#
# print(eun.name)
#
# kim=JDPerson("kim")
#
# print(kim.name)
#
# park=Person("park")
#
# print(park.name)

# class Person():
#     def __init__(self,name):
#         self.name=name
#
# class EmailPerson(Person):
#     def __init__(self,name,email):
#         super().__init__(name)
#         self.email=email
#
#
# eun=EmailPerson("eun","eunjihun")
#
# print(eun.name)
# print(eun.email)

# class Animal():
#     def says(self):
#         return 'I speak!'
#
# class Horse(Animal):
#     def says(self):
#         return "Neigh!"
#
# class Donkey(Animal):
#     def says(self):
#         return "Hee-haw!"
#
# class Mule(Donkey,Horse):
#     pass
#
# class Hinny(Horse,Donkey):
#     pass
#
# print(Mule.mro())
#
# print(Hinny.mro())














