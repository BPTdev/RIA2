import boto3
import json

class RekognitionClient:
    def __init__(self, credentials_file):
        # Load credentials from JSON file
        with open(credentials_file, 'r') as file:
            credentials = json.load(file)

        # Set up AWS session and create a Rekognition client
        self.session = boto3.Session(
            aws_access_key_id=credentials['aws_access_key_id'],
            aws_secret_access_key=credentials['aws_secret_access_key'],
            region_name=credentials['region_name']
        )
        self.rekognition = self.session.client('rekognition')

    def detect_labels(self, image_path):
        # Open the image file
        with open(image_path, 'rb') as image_file:
            image_bytes = image_file.read()

        # Call Amazon Rekognition to detect labels in the image
        response = self.rekognition.detect_labels(
            Image={
                'Bytes': image_bytes
            }
        )

        # Return the detected labels
        return response

