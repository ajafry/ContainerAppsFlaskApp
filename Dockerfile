FROM python:3.9-slim-buster

ENV LISTEN_PORT=5000
EXPOSE 5000

WORKDIR /api_app

# Copy the app contents to the image
COPY . /api_app

COPY requirements.txt /
RUN pip install --no-cache-dir -U pip
RUN pip install --no-cache-dir -r /requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "api_app.mainapp:app"]