FROM python:3.10

WORKDIR /SecondTry

COPY ./backend/FastAPI/requirements.txt /SecondTry/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /SecondTry/requirements.txt

COPY ./backend/FastAPI /SecondTry/FastAPI

CMD ["uvicorn", "FastAPI.main:app", "--host", "0.0.0.0", "--port", "80"]
