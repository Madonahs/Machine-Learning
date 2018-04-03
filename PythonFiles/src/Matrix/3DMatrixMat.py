import tensorflow as tf


'''
Created on Wed April 2 11:41:22 2018

@author: madona
Example 2 Matrix
Given W1W2 multiply the matrix

W1 = [2,0,1,0,1,2,3,0,1]
W2 = [1,0,1,2,2,1,0,3,0]

'''

#So this is a 3 by 3 Matrix my W1
#[2,0,1]
#[0,1,2]
#[3,0,1]
W1 = tf.constant([2,0,1,0,1,2,3,0,1], shape=[3,3])

#W2 contains the following
#[1,0,1]
#[2,2,1]
#[0,3,0]
W2 = tf.constant([1,0,1,2,2,1,0,3,0], shape=[3, 3])

x = tf.matmul(W1, W2)
print("3D Matrix Multiplication")
sess = tf.Session()
with sess.as_default():
    x.eval()
    
print(sess.run(x))
