# Запуск
**В консоли**

git clone https://github.com/RudyKhabib/Wb5.git

gdown "https://drive.google.com/uc?id=1g4sgW8Eja7QSxjQjIqfefvxlc-Kg5UEq" && unzip -d ./ weights.zip

docker build . --tag fastapi

docker compose -d 

**Обращение к эндпоинту**
Представлено в request_template.py

# О решении

Итоговое решение представляет собой композицию алгоритмов: эмбеддинги из дообученного Visual Transformer конкатенируются с эмбеддингами с Word2Vec (BERT показал себя хуже) после easyOCR и отправляются в catboost, который и возвращает результат
