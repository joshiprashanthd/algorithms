import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    testSuite = loader.discover('test')
    runner = unittest.TextTestRunner()
    result = runner.run(testSuite)
    
    if result.wasSuccessful():
        print("TESTS ARE SUCCESSFUL")
        exit(0)
        
    else:
        exit(1)
    