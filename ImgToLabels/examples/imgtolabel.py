import boto3
import botocore

def detect_labels(photo, bucket):
    try:
        session = boto3.Session(profile_name='profile-name')
        client = session.client('rekognition')

        # Rest of your code for label detection...

        return len(response['Labels'])

    except botocore.exceptions.ProfileNotFound as e:
        return f"Error: {e}. Please check your AWS CLI profile configuration."

def main():
    photo = 'photo-name'
    bucket = 'bucket-name'
    label_count = detect_labels(photo, bucket)
    print("Labels detected: " + str(label_count))

if __name__ == "__main__":
    main()
