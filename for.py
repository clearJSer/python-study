# fruits = ['apple','banana','mongo']
# for index in range(len(fruits)):
#     print(fruits[index])
for num in range(10,20):
    for i in range(2,num):
        if num % i == 0:
            j = num / i 
            print('%d 等于 %d * %d' % (num,i,j))
            break
    else:
        print('%d 是一个质数' % num)