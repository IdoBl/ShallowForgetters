import tensorflow as tf
from tensorflow.python.keras import layers, Sequential
import numpy as np
import pandas as pd
pd.
print(tf.VERSION)
# print(tf.keras.__version__)
#
# model = Sequential([
# # Adds a densely-connected layer with 64 units to the model:
# layers.Dense(64, activation='relu', input_shape=(32,)),
# # Add another:
# layers.Dense(64, activation='relu'),
# # Add a softmax layer with 10 output units:
# layers.Dense(10, activation='softmax')])
#
# model.compile(optimizer=tf.train.AdamOptimizer(0.001),
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])
#
data = np.random.random((1000, 32))
labels = np.random.random((1000, 10))
#
# val_data = np.random.random((100, 32))
# val_labels = np.random.random((100, 10))
#
# dataset = tf.data.Dataset.from_tensor_slices((data, labels))
# dataset = dataset.batch(32).repeat()
#
# val_dataset = tf.data.Dataset.from_tensor_slices((val_data, val_labels))
# val_dataset = val_dataset.batch(32).repeat()
#
# model.fit(dataset, epochs=10, steps_per_epoch=30,
#           validation_data=val_dataset,
#           validation_steps=3)
#
# model.evaluate(data, labels, batch_size=32)
#
# model.evaluate(dataset, steps=30)

inputs = tf.keras.Input(shape=(32,))  # Returns a placeholder tensor

# A layer instance is callable on a tensor, and returns a tensor.
x = layers.Dense(64, activation='relu')(inputs)
x = layers.Dense(64, activation='relu')(x)
predictions = layers.Dense(10, activation='softmax')(x)
model = tf.keras.Model(inputs=inputs, outputs=predictions)

# The compile step specifies the training configuration.
model.compile(optimizer=tf.train.RMSPropOptimizer(0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Trains for 5 epochs
model.fit(data, labels, batch_size=32, epochs=5)
model.summary()
