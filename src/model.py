from keras import Sequential
from keras import layers
from keras.preprocessing.image import ImageDataGenerator
import tensorflow_hub as hub
import tensorflow as tf
import tf2onnx
import onnx


model = Sequential([
    hub.KerasLayer("https://tfhub.dev/google/imagenet/efficientnet_v2_imagenet21k_b0/classification/2", trainable=False),
    layers.Dense(2, activation="softmax")
])
model.build([None, 224, 224, 3])
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

train_data = ImageDataGenerator(rescale=(1.0 / 255))
train_generator = train_data.flow_from_directory(
    "PetImages",
    target_size=(224, 224),
    batch_size=512
)
model.fit(train_generator, epochs=5)

input_signature = [tf.TensorSpec([3, 3], tf.float32, name='x')]
onnx_model, _ = tf2onnx.convert.from_keras(model, opset=13)
onnx.save(onnx_model, "model.onnx")
