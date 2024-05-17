FROM python:3.11

COPY . .

RUN apt-get update && apt-get install libgl1 -y

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--timeout-keep-alive", "90", "--host", "0.0.0.0", "--port", "80"]
