# subjects="python c++ database linux"
# subject=input("수강신청과목 입력:")
#
#
# try:
#     print(f"해당 과목이 존재하비다 위치는 {subjects.index(subject)}입니다")
# except ValueError:
#     print("해당과목은 존재하지 않습니다")

#print("%e"% 0.333)


# subject={
#     'python':'kim',
#     'c++':'sung',
#     'data structure':'kang'
# }
#
# print("{0[python]} {0[c++]}".format(subject))
#
# print(subject['python'])

number=int(input("input number: "))

is_prime=True
i=2
while i<number:
    if number%i==0:
        is_prime=False
        break
    i+=1
if is_prime:
    print(f'{number} is prime number')
else:
    print(f'{number} is not prime number')




