import sys
import Image
import RekognitionClient
def main():
    if len(sys.argv) != 2:
        print("Usage: python image_converter.py <image_path>")
        print("Example: python image_converter.py house.webp")
        return

    image_path = sys.argv[1]
    image = Image(image_path)

    # Load the image
    image_bytes = image.load_image()

    if image_bytes is not None:
        # Convert the image to base64
        base64_image = image.convert_image_to_base64(image_bytes)
        if base64_image is not None:
            print("Base64 representation of the image:")
            print(base64_image)
        else:
            print("Error: Unable to convert the image to base64.")
    
    client = RekognitionClient(access_key, secret_key, region)
    labels = client.detect_labels('image.png')
    for label in labels:
        print(label)

if __name__ == "__main__":
    main()
