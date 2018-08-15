# Copyright (C) 2018 Madonah Syombua
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import tensorflow as tf
import numpy as np

'''
Created on Wed Mar  8 10:33:30 2018

@author: madona

So we will do some exercise here on Matrix, i am hoping all team members
can do matrix multiplication on paper; this is the best practice.
In my first Example i will use the simplest Numpy
'''

#Matrix  3D Example 1
A = np.array([[3,0,1],[1,2,1],[0,3,0]])
B = np.array([[1,3,5],[2,0,4],[0,0,2]])

print('Example 1:')

print(A.dot(B))
#Matrix 2D Example 2
C = np.array([[1,3],[0,4]])
D = np.array([[5,2],[1,0]])

print()
print('Example 2:')
print(C.dot(D))

#Matrix 3D Example 3:
E = np.array([[2,0,4],[1,5,0],[2,0,2]])
F = np.array([[1,5,2],[0,2,1],[3,2,1]])


print()
print('Example 3:')
print(E.dot(F))


'''
an example using tensorflow matmul method.
 '''
# 2-D tensor `a`
# [[1, 2, 3],
#  [4, 5, 6]]
A = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])

# 2-D tensor `b`
# [[ 7,  8],
#  [ 9, 10],
#  [11, 12]]
B = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2])

# `a` * `b`
# [[ 58,  64],
#  [139, 154]]
C = tf.matmul(A, B)
print("Solution")
sess = tf.Session()
with sess.as_default():

   C.eval()
print(sess.run(C))







