import tensorflow as tf
import numpy as np
x = np.asarray([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
y = [1,2,3,4]
y = tf.square(y)
# print(x)
# x_p = tf.placeholder(tf.int32,[2,2,3])
# y =  tf.reduce_sum(x_p,3) #修改这里
# with tf.Session() as sess:
#     y = sess.run(y,feed_dict={x_p:x})
#     print(y)
with tf.Session() as sess:
    print(sess.run(y))