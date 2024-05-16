FROM python:3.11

COPY . .

RUN apt-get update && apt-get install libgl1 -y

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
