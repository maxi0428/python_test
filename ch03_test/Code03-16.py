# i, k = 0, 0

# for i in range(2, 10, 1) :
#      print("## %d 단 ##" %i)
#      for k in range(1, 10, 1) :
#           print("%d X %d = %2d" %(i, k, i * k))
#      print("")	

# while True :
#     print("ㅋ")

hap, i = 0,0

for i in range(3333, 10000) :
     if i % 1234 == 0 :
          continue
     if hap >= 100000 - i :
          break
     hap += i

print(" %d" % hap)


for num in range(3, 101):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num)