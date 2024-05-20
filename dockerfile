FROM python:3.11

COPY . .

RUN apt-get update && apt-get install libgl1 -y

RUN pip install gdown

RUN gdown "https://drive.google.com/uc?id=14el6x3rLJH_lmoiHKQ_AeMaj-c63EHPe"

RUN gdown "https://drive.google.com/uc?id=1vzN_gscr732BCnCxs67P3kM_mf7ZlsjG"

RUN gdown "https://drive.google.com/uc?id=17hayJNNG1-M96v4P8AnBoDVHbkZRqpCT"

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--timeout-keep-alive", "90", "--host", "0.0.0.0", "--port", "80"]
