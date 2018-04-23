import tensorflow as tf


'''
Created on Sun April 22 10:16:55 2018

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

y_1 = 2; y_2= 4; y_3 = 1;

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

#So in this case i will solve X_1^T W_1W_2W_3W_4W_5 - Y_1 = 76

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
          
      
print("Final Solution", sess.run(Y) - Y_1)
print("\n")



#I will try to solve x2, X_2^T W_1W_2W_3W_4W_5 - Y_2 , we know y_2 = 4. We can take x2^transpose
# Rule Row, Column and it is always good to try to them on paper first. What changes on my second code
#is just the x2 transpose. instead of [1,2,0] i will now have [4,3,1] and Y2 = 4 and introduce variable K

print("Start Example 2 solving x_2")
print("\n")

X = tf.constant([4,3,1], shape=[3,1])
Y_2 = 4 
W_1 = tf.constant([0,2,0,1,3,1,4,0,1],shape =[3,3])
W_2 = tf.constant([1,0,1,0,1,1,2,0,1], shape = [3,3])
W_3 = tf.constant([0,0,1,1,0,1,1,1,1], shape =[3,3])
W_4 = tf.constant([1,0,1,0,1,1,1,1,0], shape = [3,3])
W_5 = tf.constant([1,0,1],shape = [3,1])


X_transpose = tf.transpose(X)
sess = tf.Session()

print("X_transpose", sess.run(X_transpose))

print("\n")

K = tf.matmul(X_transpose, W_1)
sess = tf.Session()
with sess.as_default():
    K.eval()
    print("X_transposeW_1=",sess.run(K))
print("\n")

K = tf.matmul(K, W_2)
sess = tf.Session()

with sess.as_default():
    K.eval()
    print("X_transposeW_1W_2=",sess.run(K))
print("\n")

K = tf.matmul(K, W_3)
sess = tf.Session()
with sess.as_default():
    K.eval()
    print("X_transposeW_1W_2_W_3=",sess.run(K))
print("\n") 
K = tf.matmul(K, W_4)
sess = tf.Session()

with sess.as_default():
    K.eval()
    print("X_transposeW_1W_2W_3W_4=",sess.run(K))
print("\n")
K = tf.matmul(K, W_5)
sess = tf.Session()
with sess.as_default():
    K.eval()
    print("X_transposeW_1W_2_W_3W_4W_5=",sess.run(K))
     
     
print("\n")         
      
print("Final Solution", sess.run(K) - Y_2)

print("\n")

# Finalizing the problem. x3, X_3^T W_1W_2W_3W_4W_5 - Y_3 , I will introduce variable n

print("Start Example 3 solving x_3")
print("\n")

X = tf.constant([0,3,1], shape=[3,1])
Y_3 = 1 
W_1 = tf.constant([0,2,0,1,3,1,4,0,1],shape =[3,3])
W_2 = tf.constant([1,0,1,0,1,1,2,0,1], shape = [3,3])
W_3 = tf.constant([0,0,1,1,0,1,1,1,1], shape =[3,3])
W_4 = tf.constant([1,0,1,0,1,1,1,1,0], shape = [3,3])
W_5 = tf.constant([1,0,1],shape = [3,1])


X_transpose = tf.transpose(X)
sess = tf.Session()

print("X_transpose", sess.run(X_transpose))

print("\n")

n = tf.matmul(X_transpose, W_1)
sess = tf.Session()
with sess.as_default():
    n.eval()
    print("X_transposeW_1=",sess.run(n))
print("\n")

n = tf.matmul(n, W_2)
sess = tf.Session()

with sess.as_default():
    n.eval()
    print("X_transposeW_1W_2=",sess.run(n))
print("\n")

n = tf.matmul(n, W_3)
sess = tf.Session()
with sess.as_default():
    n.eval()
    print("X_transposeW_1W_2_W_3=",sess.run(n))
print("\n") 
n = tf.matmul(n, W_4)
sess = tf.Session()

with sess.as_default():
    n.eval()
    print("X_transposeW_1W_2W_3W_4=",sess.run(n))
print("\n")
n = tf.matmul(n, W_5)
sess = tf.Session()
with sess.as_default():
    n.eval()
    print("X_transposeW_1W_2_W_3W_4W_5=",sess.run(n))
     
     
print("\n")         
      
print("Final Solution", sess.run(n) - Y_3)



'''
Here is a nice play ground

https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset
=xor&regDataset=reg-plane&learningRate=0.03&regularizationRate=
0&noise=0&networkShape=4,4,4&seed=0.37235&showTestData=
false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=
false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=
false&collectStats=false&problem=classification&initZero=false&hideText=false

'''
