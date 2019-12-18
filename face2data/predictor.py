from typing import Dict

from keras import Model
from keras.models import model_from_json
import tensorflow as tf
import numpy as np

from face2data.utils import dataset_dict

graph = tf.get_default_graph()

import os

print('Current dir: ', os.getcwd())

DEFAULT_MODEL_PATH = './model/model.json'
DEFAULT_WEIGHTS_PATH = './model/weights.h5'


class PredictionResult:
    """
    Wrapper class to hold our prediction results

    :param age: prediction age (int, not float)
    :param gender: prediction gender alias
    :param race: prediction race alias
    """

    def __init__(self, age: int, gender: str, gender_confidence: float, race: str, race_confidence: float):
        self.age = age
        self.gender = gender
        self.gender_confidence = round(float(gender_confidence), 2)
        self.race = race
        self.race_confidence = round(float(race_confidence), 2)


def load_model(model_path: str = DEFAULT_MODEL_PATH,
               weights_path: str = DEFAULT_WEIGHTS_PATH) -> Model:
    model_file = open(model_path, 'r')
    model_json = model_file.read()
    model_file.close()

    loaded_model = model_from_json(model_json)
    loaded_model.load_weights(weights_path)

    return loaded_model


def predict_on_image(model: Model, image: np.ndarray) -> Dict:
    with graph.as_default():
        prediction = model.predict(image, batch_size=None)

        age = int(prediction[0].reshape(-1)[0] * 100)  # better formatting

        race_predictions = prediction[1].reshape(-1)
        gender_predictions = prediction[2].reshape(-1)

        response = {
            'race': {
                "White": float(race_predictions[0]),
                "Latino/Hispanic": float(race_predictions[1]),
                "Indian": float(race_predictions[2]),
                "East Asian": float(race_predictions[3]),
                "Black": float(race_predictions[4]),
                "Southeast Asian": float(race_predictions[5]),
                "Middle Eastern": float(race_predictions[6])
            },
            'gender': {
                'Male': float(gender_predictions[0]),
                'Female': float(gender_predictions[1])
            },
            'age': age
        }

        return response
