import unittest
from emotion_detection import emotion_detector

class TestEmotion(unittest.TestCase):

    def test_emotion(self):
        result = emotion_detector("I am happy")
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
