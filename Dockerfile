FROM python:3.12-slim-bookworm

WORKDIR /app

COPY requirements.txt ./


RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

EXPOSE 4000

CMD ["gunicorn", "-b", "0.0.0.0:4000", "app:app"]
