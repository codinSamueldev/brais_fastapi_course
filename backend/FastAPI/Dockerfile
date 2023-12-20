FROM python:3.10

WORKDIR /Brais_API

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . /Brais_API

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80",]
