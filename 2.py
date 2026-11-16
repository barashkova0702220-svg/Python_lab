import numpy as np

a = np.arange(20).reshape(4,5)
print("Массив а:\n",a)

strok1=a[1,:]
stolb3=a[:,3]
s=a[1:4,2:5]
print ("Вторая строка:",strok1)
print ("Столбец 3:",stolb3)
print ("Подмассив:\n",s)

strok = [0,2,3]
stolb = [1,4]
s_fancy = a [np.ix_(strok,stolb)]
print ("Выбранные элементы:\n",s_fancy)

b = np.array([[-1,2,-3],[4,-5,6]])
b[b<0]=0
print("После замены отрицательных на ноль:\n",b)

B = np.arange(4).reshape(4,1)
C = np.arange(5).reshape(1,5)
D=B+C
print("Результат сложения B и C: \n",D)
print("Форма результата: \n",D.shape)