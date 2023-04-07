## 함수 선언 부분 ##
def para2_func(v1, v2) :
     result = 0
     result = v1 + v2
     return result

def para3_func(v1, v2, v3) :
     result = 0
     result = v1 + v2 + v3
     return result

def varArgs_func(*args) :
     result = len(args)
     return result

def varArgs_func2(offset,*args) :
     total = offset
     for i in args :
          total = total + i
     return total

## 전역 변수 선언 부분 ##
hap = 0

## 메인 코드 부분 ##
hap = para2_func(10, 20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" % hap)
hap = para3_func(10, 20, 30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d" % hap)
result = varArgs_func(1,2,3,4,7,8)
print("varArgs_func===> %d" %result)
alist = [1,2,3,4,5]
total = varArgs_func2(1,2,3,4,5)
print("varArgs_func===> %d" %total)
