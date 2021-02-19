FROM python:3.8.5
WORKDIR /code
COPY . .
RUN pip install -r /code/requirements.txt
CMD gunicorn yamdb_final.wsgi:application --bind 127.0.0.1:8000
