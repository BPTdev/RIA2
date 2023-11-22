import base64
class Image:
    def __init__(self, image_path):
        self.image_path = image_path

    def load_image(self):
        try:
            with open(self.image_path, 'rb') as image_file:
                return image_file.read()
        except FileNotFoundError:
            print(f"Error: The file '{self.image_path}' was not found.")
            return None

    def convert_image_to_base64(self, image_bytes):
        if image_bytes is not None:
            base64_bytes = base64.b64encode(image_bytes)
            base64_string = base64_bytes.decode()
            return base64_string
        else:
            return None
