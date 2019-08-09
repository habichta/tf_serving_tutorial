import json
import numpy
import requests

import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np

labels_path = tf.keras.utils.get_file('ImageNetLabels.txt','https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
imagenet_labels = np.array(open(labels_path).read().splitlines())



file = tf.keras.utils.get_file(
    "grace_hopper.jpg",
    "https://storage.googleapis.com/download.tensorflow.org/example_images/grace_hopper.jpg")
img = tf.keras.preprocessing.image.load_img(file, target_size=[224, 224])
plt.imshow(img)
plt.axis('off')
x = tf.keras.preprocessing.image.img_to_array(img)
x = tf.keras.applications.mobilenet.preprocess_input(
    x[tf.newaxis,...]
)


data = json.dumps({"signature_name": "serving_default","instances": x.tolist()})
headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/model1/versions/2:predict',data=data, headers=headers)
predictions1 = numpy.array(json.loads(json_response.text)["predictions"])



data = json.dumps({"signature_name": "serving_default","instances": x.tolist()})
headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/model2:predict',data=data, headers=headers)
predictions2 = numpy.array(json.loads(json_response.text)["predictions"])


#TODO Prometheus



decoded1 = imagenet_labels[np.argsort(predictions1)[0,::-1][:5]+1]
decoded2 = imagenet_labels[np.argsort(predictions2)[0,::-1][:5]+1]



print(decoded1,decoded2)
