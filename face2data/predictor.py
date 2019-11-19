from keras import Model
from keras.models import model_from_json
import tensorflow as tf
import numpy as np

from face2data.utils import dataset_dict

graph = tf.get_default_graph()

DEFAULT_MODEL_PATH = './model/model.json'
DEFAULT_WEIGHTS_PATH = './model/weights.h5'


def load_model(model_path: str = DEFAULT_MODEL_PATH,
               weights_path: str = DEFAULT_WEIGHTS_PATH) -> Model:
    model_file = open(model_path, 'r')
    model_json = model_file.read()
    model_file.close()

    loaded_model = model_from_json(model_json)
    loaded_model.load_weights(weights_path)

    return loaded_model


def predict_on_image(model: Model, image: np.ndarray):
    with graph.as_default():
        prediction = model.predict(image, batch_size=None)

        age = prediction[0].reshape(-1)[0]
        race = prediction[1].argmax(axis=-1)[0]
        gender = prediction[2].argmax(axis=-1)[0]

        # better formatting
        age = int(age * 100)
        race = dataset_dict['race_id'][race]
        gender = dataset_dict['gender_id'][gender]

        return age, race, gender
