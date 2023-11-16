import boto3

# Set up AWS credentials
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='europe-central-1'
)

# Create an Amazon Rekognition client
rekognition = session.client('rekognition')

# Open the image file
with open('image.jpg', 'rb') as image_file:
    image_bytes = image_file.read()

# Call Amazon Rekognition to detect labels in the image
response = rekognition.detect_labels(
    Image={
        'Bytes': image_bytes
    },
    MaxLabels=10,
    MinConfidence=80
)

# Print the detected labels
for label in response['Labels']:
    print(label['Name'])
