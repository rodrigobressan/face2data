import unittest
import os

from face2data.predictor import load_model, predict_on_image
from face2data.preprocessing import pre_process_image


class PredictorTests(unittest.TestCase):
    samples_path = './tests/samples'
    samples = [
        'female_black_29',
        'female_white_16',
        'male_black_29',
        'male_indian_39',
        'male_white_60',
    ]

    def setUp(self) -> None:
        print('Running on ', os.getcwd())

        self.model = load_model()

    def test_load_model_invalid_path(self):
        self.assertRaises(FileNotFoundError, load_model, 'invalid_path', 'invalid_path')

    def test_prediction_samples(self):
        for sample in self.samples:
            sex, race, age = sample.split('_')

            sample_path = os.path.join(self.samples_path, sample + '.png')
            with open(sample_path, "rb") as image:
                file = image.read()
                img_bytes = bytearray(file)

                preprocessed = pre_process_image(img_bytes)
                pred_age, pred_race, pred_sex = predict_on_image(self.model, preprocessed)

                age_diff = abs(int(age) - pred_age) > 20
                self.assertEqual(sex, pred_sex)
                self.assertEqual(age_diff, False)
                self.assertEqual(race, pred_race)
