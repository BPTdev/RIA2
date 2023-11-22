import sys
from RekognitionClient import RekognitionClient 

def main():
    default_image_path = "images/big.png"  
    user_input = input(f"Enter the image path (leave blank for default '{default_image_path}'): ").strip()


    image_path = user_input if user_input else default_image_path

    # Create a Rekognition client instance
    client = RekognitionClient('keys.json')
    response = client.detect_labels(image_path)
    print(response)

if __name__ == "__main__":
    main()
