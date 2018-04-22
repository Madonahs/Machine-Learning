import tensorflow as tf


'''
@author: madona

This Exercise is based on Issue 18, practice more Matrix. We are using Tensorflow
So I decided to create this problems so that we can visualize some Matrix in the NN

So in this exercise we intensify the Matrix:

X = [x1,x2,x3] = [1,4,0,2,3,3,0,1,1]

W_1 = [0,2,0,1,3,1,4,0,1]
W_2 = [1,0,1,0,1,1,2,0,1]
W_3 = [0,0,1,1,0,1,1,1,1]
W_4 = [1,0,1,0,1,1,1,1,0]
W_5 = [1,0,1]

We have 

y_1 = 2; y_2= 4; y_5 = 1;

for  j = 1,2,3

find;

X_j ^T W_1W_2W_3W_4W_5  - y_j

So the idea is to understand if you get one you are fine :) 

So this will be:

X_1^T W_1W_2W_3W_4W_5 - Y_1 = 76.

Based on this example one should be able to solve for y2 and y3 but remember to check the X_transpose.
X_2^T W_1W_2W_3W_4W_5 - Y_2 
X_3^T W_1W_2W_3W_4W_5 - Y_3 
'''

print("This Exercise is based on issue number 18")

#So in this case i will solve X_1^T W_1W_2W_3W_4W_5 - Y_1

X = tf.constant([1,2,0], shape=[3,1])
Y_1 = 2 
W_1 = tf.constant([0,2,0,1,3,1,4,0,1],shape =[3,3])
W_2 = tf.constant([1,0,1,0,1,1,2,0,1], shape = [3,3])
W_3 = tf.constant([0,0,1,1,0,1,1,1,1], shape =[3,3])
W_4 = tf.constant([1,0,1,0,1,1,1,1,0], shape = [3,3])
W_5 = tf.constant([1,0,1],shape = [3,1])


X_transpose = tf.transpose(X)
sess = tf.Session()

print("X_transpose", sess.run(X_transpose))

print("\n")

Y = tf.matmul(X_transpose, W_1)
sess = tf.Session()
with sess.as_default():
    Y.eval()
    print("X_transposeW_1=",sess.run(Y))
print("\n")

Y = tf.matmul(Y, W_2)
sess = tf.Session()

with sess.as_default():
    Y.eval()
    print("X_transposeW_1W_2=",sess.run(Y))
print("\n")

Y = tf.matmul(Y, W_3)
sess = tf.Session()
with sess.as_default():
    Y.eval()
    print("X_transposeW_1W_2_W_3=",sess.run(Y))
print("\n") 
Y = tf.matmul(Y, W_4)
sess = tf.Session()

with sess.as_default():
    Y.eval()
    print("X_transposeW_1W_2W_3W_4=",sess.run(Y))
print("\n")
Y = tf.matmul(Y, W_5)
sess = tf.Session()
with sess.as_default():
    Y.eval()
    print("X_transposeW_1W_2_W_3W_4W_5=",sess.run(Y))
     
     
print("\n")         
      
print("Final Solution", sess.run(Y) - Y_1)

















