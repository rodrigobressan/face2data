import unittest
import os
from io import BytesIO

from face2data.app import app


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
        self.assertEqual(app.debug, False)

    def test_prediction_page(self):
        """
        Test if the prediction page is being properly rendered on the screen
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

    def test_how_it_works_page(self):
        """
        Test if the how it works page is being properly rendered on the screen
        :return:
        """
        response = self.app.get('/how_it_works', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_dataset_page(self):
        """
        Test if the dataset page is being properly rendered on the screen
        :return:
        """
        response = self.app.get('/dataset', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
