from flask import Flask, request, jsonify, render_template
from io import BytesIO
import tensorflow as tf
from keras.models import model_from_json
from PIL import Image
import numpy as np

app = Flask(__name__)
app.debug = True

graph = tf.get_default_graph()

# TODO: move to config file
model_path = './model/model.json'
weights_path = './model/weights.h5'

model = None
IM_WIDTH = IM_HEIGHT = 198

dataset_dict = {
    'race_id': {
        0: 'white',
        1: 'black',
        2: 'asian',
        3: 'indian',
        4: 'others'
    },
    'gender_id': {
        0: 'male',
        1: 'female'
    }
}

dataset_dict['gender_alias'] = dict((g, i) for i, g in dataset_dict['gender_id'].items())
dataset_dict['race_alias'] = dict((g, i) for i, g in dataset_dict['race_id'].items())


def pre_process_image(img_bytes):
    """
    Used to perform some minor pre processing on the image before inputting into the network.
    """
    im = Image.open(BytesIO(img_bytes))

    if im.mode != 'RGB':
        im = im.convert('RGB')

    im = im.resize((IM_WIDTH, IM_HEIGHT))
    im = np.array(im) / 255.0
    im = np.expand_dims(im, axis=0)

    return im


def load_model():
    model_file = open(model_path, 'r')
    model_json = model_file.read()
    model_file.close()

    loaded_model = model_from_json(model_json)
    loaded_model.load_weights(weights_path)

    return loaded_model


def predict_on_image(image):
    with graph.as_default():
        prediction = model.predict(image, batch_size=None)

        return prediction


@app.route('/predict', methods=['POST'])
def predict():
    image = request.files['image'].read()
    image = pre_process_image(image)

    prediction = predict_on_image(image)
    age = prediction[0].reshape(-1)[0]
    race = prediction[1].argmax(axis=-1)[0]
    gender = prediction[2].argmax(axis=-1)[0]

    if age < 0:
        age = 1
    elif age > 100:
        age = 100

    # we could also just return a rendered template, but in this case I opted to just return a json object and parse it
    # on the screen
    response = {
        'age': int(age * 100),
        'race': dataset_dict['race_id'][race],
        'gender': dataset_dict['gender_id'][gender]
    }

    return jsonify(response)


@app.route('/how_it_works')
def how_it_works():
    return render_template('how.html')


@app.route('/dataset')
def dataset():
    return render_template('dataset.html')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    print('Loading Keras model')
    model = load_model()

    print('Starting Flask server')
    app.run(debug=True)

if __name__ == 'app':
    print('Loading Keras model')
    model = load_model()
