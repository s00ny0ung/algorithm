'''
조건문 if(분기, 중첩)
'''

x=7
if x == 7:
	print('ok')
	

#중첩if
print('*'*80)
x = 15
if x>=10:
	if x%2==1:
		print('10이상의 홀수')
		

print('*'*80)
x=9
if x > 0:
	if x < 10:
		print("10보다 작은 자연수")
		
print('*'*80)
x=7
if x>0 and x<10:
	print("10보다 작은 자연수")
	

print('*'*80)
if 0<x<10:
	print("10보다 작은 자연수")
	
print('*'*80)
print('[!]:분기문')
x = -3
if x>0:
	print('양수')
else:
	print('음수')
	

print('*'*80)
print('[!]: 다중 분기문 if~elif~else')
x = 60
if x>=90:
	print('A')
elif x >=80:
	print('B')
elif x >=70:
	print('C')
elif x >=60:
	print('D')
else:
	print('E')	