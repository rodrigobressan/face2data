import unittest
import os

os.chdir('../')
from app import app


class ApiEndpointsTests(unittest.TestCase):
    """
    Used to perform integration tests on our Flask application. It does check if each endpoints is properly behaving
    for valid and invalid inputs, and how it also behaves on each scenario.
    """

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False

        self.app = app.test_client()

        # TODO load image

        self.assertEqual(app.debug, False)

    def test_prediction_page(self):
        """
        Test if our prediction page is being properly rendered on the screen
        :return:
        """
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_prediction_json_bad_request(self):
        """
        Given a POST call on the predict endpoint
        When an invalid json body is sent
        Then check if the response is BAD_REQUEST (400)
        """
        response = self.app.post('/predict', data=dict(var1='a', var2='b'), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    #
    # def test_prediction_json_good_request(self):
    #     """
    #     Given a POST call on the predict endpoint
    #     When a valid json body is sent
    #     Then check if the response is OK (200) AND if it contains some required fields
    #     """
    #     response = self.app.post('/predict', data=self.features[0:1].to_json(orient='records')[1:-1],
    #                              content_type='application/json')
    #
    #     self.assertEqual(response.status_code, 200)
    #
    #     self.assertTrue('summary_plot_bar' in response.json)
    #     self.assertTrue('summary_plot_full' in response.json)
    #     self.assertTrue('force_plot' in response.json)
    #     self.assertTrue('probas' in response.json)
    #
    #     self.assertTrue(isinstance(response.json['probas'], list))
    #     self.assertEqual(len(response.json['probas'][0]), 2)
    #
    # def test_prediction_form_bad_request(self):
    #     """
    #     Given a POST call on the predict endpoint
    #     When the form body is invalid
    #     Then check if the response is BAD_REQUEST (400)
    #     """
    #     response = self.app.post('/predict', data=dict(n_tp_ocorrencia=1),
    #                              content_type='application/x-www-form-urlencoded')
    #     self.assertEqual(response.status_code, 400)
    #
    # def test_prediction_form_good_request(self):
    #     """
    #     Given a POST call on the predict endpoint
    #     When the form body is a valid one
    #     Then check if the response is OK (200)
    #     """
    #     response = self.app.post('/predict', data=self.features[0:1].to_dict(orient='record')[0],
    #                              content_type='application/x-www-form-urlencoded')
    #     self.assertEqual(response.status_code, 200)
    #


if __name__ == "__main__":
    unittest.main()
