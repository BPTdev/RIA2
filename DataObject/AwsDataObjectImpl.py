import os
from dotenv import load_dotenv
from IDataObject import IDataObject
import boto3


class AwsDataObjectImpl(IDataObject):
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # Retrieve credentials from environment variables
        aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        region_name = os.getenv("AWS_REGION")

        # Set up AWS session and create a S3 client
        self.session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
        )
        self.s3 = self.session.client("s3")

    def doseExist(self, remoteFilePath: str) -> bool:
        if "/" not in remoteFilePath:
            raise ValueError("Invalid remote file path format. Expected format: 'bucket_name/object_name'")
        
        bucket_name, object_name = remoteFilePath.split("/", 1)
        try:
            self.s3.head_object(Bucket=bucket_name, Key=object_name)
            return True
        except boto3.exceptions.botocore.exceptions.ClientError as e:
            if e.response["Error"]["Code"] == "404":
                print("Object does not exist")
                return False
            else:
                raise

    def upload(self, file_path: str, remote_file_path: str) -> None:
        if "/" not in remote_file_path:
            raise ValueError("Invalid remote file path format. Expected format: 'bucket_name/object_name' : "+remote_file_path + " End of thing")
        bucket_name, object_name = remote_file_path.split("/", 1)
        self.s3.upload_file(file_path, bucket_name, object_name)

    def download(self, remote_file_path: str, local_file_path: str) -> None:
        if "/" not in remote_file_path:
            raise ValueError("Invalid remote file path format. Expected format: 'bucket_name/object_name'")
        bucket_name, object_name = remote_file_path.split("/", 1)
        self.s3.download_file(bucket_name, object_name, local_file_path)

    def publish(self, remote_file_path: str, expiration_time: int = 90) -> str:
        if "/" not in remote_file_path:
            raise ValueError("Invalid remote file path format. Expected format: 'bucket_name/object_name'")
        bucket_name, object_name = remote_file_path.split("/", 1)
        response = self.s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket_name, "Key": object_name},
            ExpiresIn=expiration_time * 60,
        )
        print(response)
        return response

    def remove(self, remote_file_path: str, recursive: bool = False) -> None:
        if "/" not in remote_file_path:
            raise ValueError("Invalid remote file path format. Expected format: 'bucket_name/object_name'")
        bucket_name, object_name = remote_file_path.split("/", 1)

        if recursive:
            bucket = self.session.resource("s3").Bucket(bucket_name)
            bucket.objects.filter(Prefix=object_name).delete()
        else:
            self.s3.delete_object(Bucket=bucket_name, Key=object_name)


class AwsDataObjectImplException(Exception):
    pass

class ObjectAlreadyExistsException(AwsDataObjectImplException):
    def __init__(self, message="The specified object already exists in S3"):
        self.message = message
        super().__init__(self.message)

class ObjectNotFoundException(AwsDataObjectImplException):
    def __init__(self, message="The specified object was not found in S3"):
        self.message = message
        super().__init__(self.message)

class NotEmptyObjectException(AwsDataObjectImplException):
    def __init__(self, message="The specified object is not empty"):
        self.message = message
        super().__init__(self.message)

try:
    # Code that may raise the ObjectNotFoundException
    raise ObjectNotFoundException("This is a custom ObjectNotFoundException")
except ObjectNotFoundException as e:
    print(f"Caught ObjectNotFoundException: {e}")

