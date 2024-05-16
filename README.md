# Запуск
**В консоли**

git clone https://github.com/RudyKhabib/Wb5.git

docker build . --tag fastapi

docker compose -d 

**Обращение к эндпоинту**

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

img_for_bytes = Image.open('169448187.jpg')
img_bytes = image_to_byte_array(img_for_bytes)

api_url = 'http://127.0.0.1:8000/get_answer'

data = {
  "imgbytes": img_bytes
}

response = requests.post(api_url, data=data)

print(resp.content["prob"], resp.content["verdict"])

# О решении

Итоговое решение представляет собой композицию алгоритмов: эмбеддинги из дообученного Visual Transformer конкатенируются с эмбеддингами с Word2Vec (BERT показал себя хуже) после easyOCR и отправляются в catboost, который и возвращает результат
