from PIL import Image

import requests
import io

def image_to_byte_array(image: Image) -> bytes:
    # BytesIO is a file-like buffer stored in memory
    imgByteArr = io.BytesIO()
    # image.save expects a file-like as a argument
    image.save(imgByteArr, format=image.format)
    # Turn the BytesIO object back into a bytes object
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr
    
image_path = '169448187.jpg'
img_for_bytes = Image.open(image_path)
img_bytes = image_to_byte_array(img_for_bytes)

api_url = 'http://127.0.0.1:80/get_answer'

data = {
  "img_bytes": img_bytes.decode('latin-1')
}
response = requests.post(api_url, json=data)

print(response.text)
