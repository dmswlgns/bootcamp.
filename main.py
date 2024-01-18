





def add(*args):
    print(args)
    print(*args)   #언패킹
    return sum(args)

print(add(1,3,8))

# def run_something_with_args(func,*args):
#     return func(*args)
#
# print(run_something_with_args(add,1,3,8))

print(sum((1,2,4)))

