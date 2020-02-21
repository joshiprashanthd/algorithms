import unittest
import test

if __name__ == "__main__":
    loader = unittest.loader.defaultTestLoader
    suite = loader.loadTestsFromModule(test)
    g = None
    suite.run(g)