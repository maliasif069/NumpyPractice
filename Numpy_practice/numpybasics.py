import numpy as np
# a=np.array([[1,2,3],[2,2,4]],dtype=int)
# d=(a.reshape(3,2))
# # print(d)
# b=np.arange(1,12,2).reshape(3,2)
# print(b.T)
# # print("\n",b)
# # w=np.array([[1,2,3,7],[2,4,5,6],[9,7,8,9]],dtype=int)
# # q=w.reshape(3,4)
# # print("\n\n",q)
# # #  iterating in 2 d
# # for i in w:
# #     print(i)

    

# # slicing in 3d 
# r=np.arange(27).reshape(3,3,3)
# print(r.ravel())

# # print(r[::2,0:1,0::2])
# #  iterating in 3d
# # for j in r:
# #     print(j)
# # for j in np.nditer(r):
# #     print(j)
# # # slicing in 2d 
# # print(q[0:2,1:])
# # print(q[0,1,2])
# # print(b[2,0])
# # print(d[2,1])
# # print(w[0:2,1:2])
# # print(w[::2,::3])
# # # c=np.ones((4,3))
# # print(c)
# # print(np.linspace(-10,10,5,dtype=int))
# # print(np.identity(7).size)
# # print(c.shape)
# # print(c.dtype)
# # d=c.astype(np.int32)
# # print(d.dtype)
# # print(a**2)
# # print(a==0)
# # print(d+b)
# # print(np.max(d))
# # max min prod sum
# # 0--> col anmd 1-->row
# # print(np.sum(d,axis=0)
# # mean median mode can also be calculated
# # print(np.dot(a,b))
# # print(np.log(a))
# # print(np.round(np.random.random((2,3))*100))
# # print(np.round(d)
a4=np.arange(12).reshape(3,4)
a3=np.arange(12,24).reshape(3,4)
print(np.hstack((a4,a3)))
print(np. vstack((a4,a3)))
print(np.hsplit(a4,4))
print(np.vsplit(a3,3))
