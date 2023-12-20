FROM python:3.10

WORKDIR /Brais_API

COPY ./requirements.txt /Brais_API/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Brais_API/requirements.txt

COPY ./FastAPI /Brais_API/FastAPI

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
