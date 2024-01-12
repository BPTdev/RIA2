from datetime import datetime
from DataObject.AwsDataObjectImpl import AwsDataObjectImpl
from LabelDetector.AwsLabelDetectorImpl import AwsLabelDetectorImpl

awsData = AwsDataObjectImpl()
awsLabel = AwsLabelDetectorImpl()


bucket = 'python.cloud.aws.edu'
imagePath = '1.png'


#online image
imageOnline = 'https://i.imgur.com/iERTcTq.jpeg'
imagePath = '2.png'
#Uncomment the line below to use an img from the web with the link above
#imagePath = imageOnline

remoteFullPath = bucket+'/'+imagePath

remoteFullPath = awsData.apiCall(bucket, imagePath, remoteFullPath)
print(remoteFullPath)
tempUri=awsData.publish(remoteFullPath)

response = awsLabel.analyze(tempUri)



current_date = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
sql_file_name = f"sql/{remoteFullPath.split('/')[-1]}_{current_date}.sql"

# Open a file for writing the SQL statements
with open(sql_file_name, 'w') as sql_file:
    for label in response['Labels']:
        name = label['Name']
        confidence = label['Confidence']
        insert_statement = f"INSERT INTO your_table (name, confidence) VALUES ('{name}', {confidence});\n"
        sql_file.write(insert_statement)
print(response)
awsData.upload(sql_file_name, remoteFullPath)
# upload a sql file to the bucket that contain labels data