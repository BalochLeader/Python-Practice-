import time 
my_num = int(input("Enter No : "))

for x in range(my_num , 0 ,-1):
	second = x % 60
	minutes = (x // 60) % 60
	hour = ( x // 3600)
	print(f"{hour:02}:{minutes:02}:{second:02}")
	time.sleep(1)
	
	
print(f" Times Uppp ")
	
	
	
	#int 
import time 
my_num = int(input("Enter No : "))

for x in range(my_num , 0 ,-1):
	second = x % 60
	minutes = int(x / 60) % 60
	hour = int( x / 3600)
	print(f"{hour:02}:{minutes:02}:{second:02}")
	time.sleep(1)
	
	
print(f" Times Uppp ")
	
	