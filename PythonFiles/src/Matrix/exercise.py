import tensorflow as tf

'''
This exercise is on issue #13 please check the issue on our Board.
Problem approach using tensor flow:
So given the following X^TW1W2W3
X=[1,2,3]
W1 = [2,0,1,0,1,2,3,0,1]
W2 = [1,0,1,2,2,1,0,3,0]
W3 =[2,4,1]

X = [1]
    [2]
    [3]
    
W1 = [2,0,1]
     [0,1,2]
     [3,0,1]
     
W2 = [1,0,1]
     [2,2,1]
     [0,3,0]
     
W3 = [2]
     [4]
     [1]
Always remember RC| Row and Columns 
We know X transpose will change from column to row; hence

Soln = [155]
'''
print("Exercise")
X = tf.constant([1, 2, 3], shape=[3, 1])
W1 = tf.constant([2, 0, 1, 0, 1, 2, 3, 0, 1], shape=[3, 3])
W2 = tf.constant([1, 0, 1, 2, 2, 1, 0, 3, 0], shape=[3, 3])
W3 = tf.constant([2, 4, 1], shape=[3, 1])

Xt = tf.transpose(X)
sess = tf.Session()
print("Xt=",sess.run(Xt))

print("\n")

Y = tf.matmul(Xt, W1)
sess = tf.Session()
with sess.as_default():
	Y.eval()
	print("XtW1=",sess.run(Y))
print("\n")

Y = tf.matmul(Y, W2)
sess = tf.Session()

with sess.as_default():
	Y.eval()
	print("XtW1W2=",sess.run(Y))
print("\n")

Y = tf.matmul(Y, W3)
sess = tf.Session()
with sess.as_default():
	Y.eval()
	print("XtW1W2W3=",sess.run(Y))
print("\n")
