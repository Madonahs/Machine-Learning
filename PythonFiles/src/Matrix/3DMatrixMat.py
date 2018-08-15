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
