import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        text = "I am glad this happened"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "joy",
                         msg="Expected dominant emotion to be joy")

    def test_anger(self):
        text = "I am really mad about this"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "anger",
                         msg="Expected dominant emotion to be anger")

    def test_disgust(self):
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "disgust",
                         msg="Expected dominant emotion to be disgust")

    def test_sadness(self):
        text = "I am so sad about this"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "sadness",
                         msg="Expected dominant emotion to be sadness")

    def test_fear(self):
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "fear",
                         msg="Expected dominant emotion to be fear")

if __name__ == '__main__':
    unittest.main()
