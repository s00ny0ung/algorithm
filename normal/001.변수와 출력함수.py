'''
변수명 정하기
1) 영문과 숫자, _로 이루어진다.
2) 대소문자를 구분한다.
3) 문자나, _로 시작한다.
4) 특수문자를 사용하면 안된다(&,% 등)
5) 키워드를 사용하면 안된다.(if. for 등)
'''

a=1
print(a)
A=2
_b=4
#2b=3 #숫자로 시작하는 변수명 형태는 안된다.
print(a,A,_b)

a, b, c = 3,2,1 #동시에 데이터를 넣을 수 있다.
print(a,b,c)

#값교환
a, b = 10, 20
print(a,b)

a, b = b, a
print(a,b)

#변수타입
#정수형(int)
a=12345
print(a, type(a))

#실수형(float) 
a=12.123
print(a, type(a))

#문자형(string)
a= 'student'
print(a, type(a))

#출력방식
print("number")
a,b,c = 1,2,3
print(a,b,c)
print("number",a,b,c)
print(a,b,c,sep=',') # sep : 변수사이의 값
print(a,b,c,sep=', ')
