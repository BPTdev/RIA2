import sys
from RekognitionClient import RekognitionClient 

def main():
    default_image_path = "images/big.png"  
    user_input = input(f"Enter the image path (leave blank for default '{default_image_path}'): ").strip()
    image_path = user_input if user_input else default_image_path

    # Create a Rekognition client instance
    client = RekognitionClient('keys.json')

    # Set parameters using methods
    client.set_max_labels(10)
    client.add_label_inclusion("Light")
    # Set other parameters as needed

    response = client.detect_labels(image_path)
    print(response)

if __name__ == "__main__":
    main()