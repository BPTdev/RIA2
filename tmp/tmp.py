import boto3
import json

# Charger les credentials depuis le fichier JSON
with open('keys.json', "r") as file:
    credentials = json.load(file)

# Créer une session avec les credentials spécifiés
session = boto3.Session(
    aws_access_key_id=credentials["aws_access_key_id"],
    aws_secret_access_key=credentials["aws_secret_access_key"],
    region_name=credentials["region_name"],
)

# Utiliser cette session pour créer un client S3
s3 = session.client('s3')

# Vérifier l'existence du bucket
bucket_name = 'python.aws.cld.educatoin'
try:
    s3.head_bucket(Bucket=bucket_name)
    print(f"Le bucket '{bucket_name}' existe et est accessible.")
    # Téléverser le fichier si le bucket existe
    s3.upload_file('/Users/benoitpierrehumbert/Desktop/b.jpg', bucket_name, 'big.png')
    print("Fichier téléversé avec succès.")
except s3.exceptions.NoSuchBucket:
    print(f"Le bucket '{bucket_name}' n'existe pas ou n'est pas accessible.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")
