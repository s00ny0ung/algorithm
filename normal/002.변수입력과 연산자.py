'''
변수입력과 연산자
'''

# a=input("숫자를 입력하세요:")
# print(a)

# a, b = input('숫자를 입력하세요. : ').split()
# print(a,b)
# print(type(a), type(b))
# print(a+b) #string으로 값이 붙은 것
# print(int(a)+int(b)) #형변환이후에 값을 더한 것

print('-'*140)
print('[!]map함수를 이용해서 형변환')
a,b = map(int, input('값을 입력하세요 :').split()) 
# 1. input으로 2개 숫자를 받고
# 2. int형으로 형변환 (int 내장함수, map 내장함수)
print(a+b)
print(a+b)
print(a/b)
print(a*b) 
print(a//b) #몫
print(a%b) #나머지
print(a**2) #거듭제곱
print(a**b) #거듭제곱

print('-'*140)
a = 4.3 #int
b = 5 #float
c = a + b #형이 다른 것끼리 연산될때 범위가 더 큰 것으로 설정된다.
print(type(c)) #float