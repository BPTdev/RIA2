# AwsImgToLabel 



## Description

This project is designed to convert an image to labels and the main features are upload an image to aws and get a sql file back filled with labels returned from aws's Rekognition model.

## Getting Started

### Prerequisites

List all dependencies and their version needed by the project as :

* Language : Python 3.11.6
* Package : boto3, dotenv, unittest

### Configuration

Sensitive data like aws credentials, are stored in a .env file

## Deployment

### On dev environment

To get the dependencies you must install them with pip3
To run the tests, open a terminal at root of repo and write `python3 DataObjectTest.py` or `python3 LabelDetectorTest.py`

### On integration environment


## Directory structure

```shell
├── 1.png
├── 2.png
├── DataObject
│   ├── AwsDataObjectImpl.py
│   ├── IDataObject.py
│   └── __pycache__
│       ├── AwsDataObjectImpl.cpython-311.pyc
│       └── IDataObject.cpython-311.pyc
├── DataObjectTest.py
├── LabelDetector
│   ├── AwsLabelDetectorImpl.py
│   ├── ILabelDetector.py
│   ├── RekognitionClient.py
│   ├── __pycache__
│   │   ├── AwsLabelDetectorImpl.cpython-311.pyc
│   │   ├── ILabelDetector.cpython-311.pyc
│   │   └── RekognitionClient.cpython-311.pyc
│   ├── image.png
│   └── keys.json
├── LabelDetectorTest.py
├── main.py
├── sql
└── tmp
```

## Collaborate


## License

* [glp-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Contact

* Issue GitHub, Teams, Mail
