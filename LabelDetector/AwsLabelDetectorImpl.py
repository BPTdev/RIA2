from .ILabelDetector import ILabelDetector
from .RekognitionClient import RekognitionClient


class AwsLabelDetectorImpl(ILabelDetector):
    def __init__(self):
        self.client = RekognitionClient()

    @staticmethod
    def analyze(remoteFullPath: str, maxLabels: int = 5, minConfidenceLevel: float = 90) -> str:
        # Create a Rekognition client instance
        client = RekognitionClient()

        # Set parameters using methods
        client.set_min_confidence(minConfidenceLevel)
        client.set_max_labels(maxLabels)

        response = client.detect_labels(remoteFullPath)
        return response

