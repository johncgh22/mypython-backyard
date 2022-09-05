import numpy as np

a = np.array([[1,2,3,4,5],
             [6,7,8,9,10],
         [11,12,13,14,15],
         [16,17,18,19,20]])

b = np.random.randint(100, size=(2,3,4))
print(b)

c = np.random.binomial(10, p=0.5, size=(5, 10))
print(c)

d = np.random.choice([10,20,30], size=(5, 10))
print(d)

np.save("myArray.npy",a)
np.savetxt("myArray2.csv", a, delimiter=",")

