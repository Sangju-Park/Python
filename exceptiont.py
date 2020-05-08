#예외사항 처리
'''dataa=input("정수를 입력하세요 > ")
try:
    print(int(dataa)**2)
   
except IndexError as e:
    print("거시기 해 주세요")
except ValueError as e:
    print("정수를 입력해 주세요")
    print(type(e))
    print(e)
    finally:#빠져나올때 무조건 실행함
    print("다시하세요")'''


#의도적 예외발생
'''try:
    raise NotADirectoryError("메시지")
except NotADirectoryError as na:
    print(na)'''   

'''def test():
    raise NotImplementedError'''

'''def average_score(scores):
    for score in scores:
        try:
            if not 0 <= score <= 100:
                raise ValueError("0과 100사이에 입력하세요")
        except ValueError as vl:
            print(vl)
        else:
            return sum(scores),len(scores) 

print(average_score([-10,20,30,40,-20]))'''

#finally
'''
try:
    file = open("file.txt","w")
    dddd

except Exception as e:
    print(e)
finally:
    file.close()

print("파일 제대로 닫혔는지 확인")
print(file.closed)'''

#finally return or break
def test():
    print("함수 시작")
    try:
        print("try 구문의 1번 지점")
        ㅎㅎㅎㅎ
        print("try 구문의 2번 지점")
    except:
        print("except 구문 지점")
    finally:
        print("finally 구문 지점")

    print("함수 끝")
test()