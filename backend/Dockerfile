FROM python:3.10

WORKDIR /SecondTry

COPY ./requirements.txt /SecondTry/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /SecondTry/requirements.txt

COPY ./FastAPI /SecondTry/FastAPI

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
