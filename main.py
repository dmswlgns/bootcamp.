
import random
drinks_foods = {"위스키": "초콜릿", "와인": "치즈", "소주": "삽겹살", "고량주": "양꼬치"}

drinks=list(drinks_foods.keys())
food=list(drinks_foods.values())

print(f'1){drinks[0]}, 2){drinks[1]}, 3){drinks[2]}, 4){drinks[3]}, 5)아무거나 6)종료')
while True:
    select=int(input("주류를 고르세요: "))
    if select==1:
        print(f"{drinks[0]}와 어울리는 안주는 {drinks_foods[drinks[0]]}입니다")
    if select == 2:
        print(f'{drinks[1]}와 어울리는 안주는 {food[1]}입니다')
    if select == 3:
        print(f'{drinks[2]}와 어울리는 안주는 {food[2]}입니다')
    if select == 4:
        print(f'{drinks[3]}와 어울리는 안주는 {food[3]}입니다')
    if select == 5:
        k = random.choice([0,1,2,3])
        print(f'{drinks[k]}와 어울리는 안주는 {food[k]}입니다')
    if select ==6:
        print("다음에 또 오세요")
        break
