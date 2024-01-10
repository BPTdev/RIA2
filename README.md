# AwsImgToLabel 



## Description

This project is designed to convert an image to labels and the main features are upload an image to aws and get a sql file back filled with labels returned from aws's Rekognition model.

## Getting Started

### Prerequisites

List all dependencies and their version needed by the project as :

* Language : Python 3.11.6
* Package : boto3, dotenv, unittest

### Configuration

Sensitive data like aws creds, are stored in a .env file

## Directory structure

```shell
├── DataObject
│   ├── 4.png
│   ├── AwsDataObjectImpl.py
│   ├── DataObjectTest.py
│   ├── IDataObject.py
│   ├── __pycache__
│   │   ├── AwsDataObjectImpl.cpython-311.pyc
│   │   └── IDataObject.cpython-311.pyc
│   └── image.png
├── LabelDetector
│   ├── AwsLabelDetectorImpl.py
│   ├── ILabelDetector.py
│   ├── LabelDetectorTest.py
│   ├── RekognitionClient.py
│   ├── __pycache__
│   │   ├── AwsLabelDetectorImpl.cpython-311.pyc
│   │   ├── ILabelDetector.cpython-311.pyc
│   │   └── RekognitionClient.cpython-311.pyc
│   ├── image.png
│   └── keys.json
├── keys.json
├── keys.json.example
└── main.py
```

## Collaborate


## License

* [glp-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Contact

* Issue GitHub, Teams, Mail
