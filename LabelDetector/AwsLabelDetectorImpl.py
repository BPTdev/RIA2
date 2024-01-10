import sys
from ImgToBucketToLabels.Interfaces.ILabelDetector import ILabelDetector
from RekognitionClient import RekognitionClient


class AwsLabelDetectorImpl(ILabelDetector):
    def __init__(self):
        self.client = RekognitionClient("keys.json")

    @staticmethod
    def analyze(remoteFullPath: str, maxLabels: int = 10, minConfidenceLevel: float = 90) -> str:
        # Create a Rekognition client instance
        client = RekognitionClient("keys.json")

        # Set parameters using methods
        client.set_min_confidence(minConfidenceLevel)
        client.set_max_labels(maxLabels)

        response = client.detect_labels(remoteFullPath)
        print(remoteFullPath)
        return response

