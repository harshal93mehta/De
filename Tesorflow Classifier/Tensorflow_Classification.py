import pandas as pd 
import numpy as np 
import tensorflow as tf 
import matplotlib.pyplot as plt 

dataframe = pd.read_csv('data.csv')
dataframe = dataframe.drop(['index', 'price', 'sq_price'], axis =1)
dataframe = dataframe[0:10]


dataframe.loc[:, ('y1')] = [1,1,1,0,0,1,0,1,1,1]
dataframe.loc[:, ('y2')] = dataframe['y1'] == 0
dataframe.loc[:, ('y2')] = dataframe['y2'].astype(int)

inputX = dataframe.loc[:, ['area', 'bathrooms']].as_matrix()
inputY = dataframe.loc[:, ['y1','y2']].as_matrix()

learning_rate = 0.000001
training_ephocs = 2000
display_step = 50
n_samples = inputY.size

x = tf.placeholder(tf.float32, [None,2])

W = tf.Variable(tf.zeros([2,2]))

b = tf.Variable(tf.zeros([2]))

y_values = tf.add(tf.matmul(x, W), b)

y = tf.nn.softmax(y_values)

y_ = tf.placeholder(tf.float32, [None,2])

cost = tf.reduce_sum(tf.pow(y_ - y, 2))/(2*n_samples)

optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for i in range(training_ephocs):
	sess.run(optimizer, feed_dict={x:inputX, y_:inputY})

	if (i) % display_step == 0:
		cc = sess.run(cost, feed_dict={x:inputX, y_:inputY})
		print ("Training step:", '%04d' %(i), "cost=","{:.9f}".format(cc))

