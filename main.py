





# class PrettyMixin():
#     def dump(self):
#         import pprint
#         pprint.pprint(vars(self))
#
# class Thing(PrettyMixin):
#     pass
#
# t=Thing()
# t.name="Nyarlathotep"
# t.feature='Ichor'
# t.age='eldritch'
# print(t.dump())
#



# class Duck():
#     def __init__(self,input_name):
#         self.name=input_name
#
# fowl=Duck("Daffy")
# fowl.name="Dophon"
#
# print(fowl.name)

# class Duck():
#     def __init__(self,input_name):
#         self.hidden_name=input_name
#     @property
#     def name(self):
#         print('inside the getter')
#         return self.hidden_name
#     @name.setter
#     def name(self,input_name):
#         print("inside the setter")
#         self.hidden_name=input_name
#
# don=Duck("Donald")
#
# print(don.name)
# print()
# don.name="Donna"
# print()
# print(don.name)


class Circle():
    def __init__(self,radius):
        self.radius=radius
    def diameter(self):
        return 2*self.radius

a=Circle(5)

print(a.radius)

print(a.diameter())











