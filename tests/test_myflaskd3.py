import myflaskd3
import unittest

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.app = myflaskd3.APP.test_client()

        
    def tearDown(self):
        pass

    
    def test_404(self):
        vm = self.app.get('/')
        print(vm.data)
        assert(b'404 Not Found' in vm.data)
        

if __name__ == '__main__':
    unittest.main()
