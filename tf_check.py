# Python
import tensorflow as tf
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session(config=config)
print(sess.run(hello))

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
