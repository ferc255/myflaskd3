'''
Application unit tests
'''

import unittest
import myflaskd3


class FlaskrTestCase(unittest.TestCase):
    '''
    Service class unittest's library
    '''

    def setUp(self):
        '''
        Initialization
        '''
        self.app = myflaskd3.APP.test_client()

    def tearDown(self):
        '''
        The last actions
        '''

        pass

    def test_404(self):
        '''
        Check if the server returns 404 for '/' route.
        '''

        response = self.app.get('/')
        assert b'404 Not Found' in response.data

    def test_graph_response(self):
        '''
        Check if the server returns 200 for '/graph' route.
        '''

        response = self.app.get('/graph',
                                headers={'Content-Type': 'text/html'})
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
