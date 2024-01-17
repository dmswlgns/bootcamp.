
# prime number
# numbers = input("Input first second number : ").split()
# n1 = int(numbers[0])
# n2 = int(numbers[1])
#
# if n1 > n2:
#     n1, n2 = n2, n1
#
# for number in range(n1, n2+1):
#     is_prime = True
#
#     if number < 2:
#         continue  #pass
#     else:
#         i = 2
#         while i*i < number:  # performance issue
#             if number % i == 0:
#                 is_prime = False
#                 break
#             i = i + 1
#             #print(i, end=' ')  # loop count
#         if is_prime:
#             pass
#             print(number, end=' ')


sugang=dict(python='kim',db='kang',cpp='sung')


# sugang['datastructure']='park'
#
# print(sugang)
#
# print(sugang['db'])
#
# print(sugang.get("db"))
#
# print(sugang.get("opensource","not exist"))


# for subject,prof in sugang.items():
#     print(f'{subject}과목 담담교수는 {prof}입니다')
#
#
# for k in sugang:
#     print(k)
#
# for v in sugang.values():
#     print(v)
#
# for s in sugang.items():
#     print(s)
import random


drink_food={
    "위스키":"초콜릿",
    "와인":"치즈",
    "소주":'삼겹살',
    "고량주":'양꼬치'
}
drink_food_keys=list(drink_food)

print(random.choice(drink_food_keys))

print(drink_food_keys)

drink=input(f'다음 술중에 고르세요 \n{drink_food_keys[0]},{drink_food_keys[1]},{drink_food_keys[2]},{drink_food_keys[3]},종료')

print(drink_food[drink])















