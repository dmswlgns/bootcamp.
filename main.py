

print("1.화씨->섭씨 2.화씨->섭씨 3.소수판정 4.구간소수출력 5.종료")


while True:
    number = int(input("항목을 고르세요:"))
    if number==1:
        F=int(input("화씨온도를 입력하세요:"))
        print(f'화씨온도가 {F}이면 섭씨온도는 {(F-32)*5/9:.2f}입니다.')

    elif number==2:
        C = int(input("섭씨온도를 입력하세요:"))
        print(f'섭씨온도가 {C}이면 화씨온도는 {(C*9/5)+32:.2f}입니다.')
    elif number==3:
        num=int(input("숫자입력:"))
        if num<2:
            print(f"{num}는 소수가 아닙니다")
        else:
            is_prime=True
            for i in range(2,num):
                if num%i==0:
                    is_prime=False
            if is_prime:
                print(f"{num}는 소수입니다.")
            else:
                print(f"{num}는 소수가 아닙니다.")
    elif number==4:
        numbers=input("첫번쨰수 두번쨰수:").split()

        num_1=int(numbers[0])
        num_2=int(numbers[1])
        if num_1>num_2:
            num_1,num_2=num_2,num_1
        for k in range(num_1,num_2+1):
            if k<2:
                pass
            else:
                is_prime = True
                for i in range(2,k):
                    if k%i==0:
                        is_prime=False
                if is_prime:
                    print(k,end=" ")
        print()
    elif number==5:
        break








