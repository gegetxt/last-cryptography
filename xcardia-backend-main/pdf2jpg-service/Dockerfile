FROM python:3.9-slim

WORKDIR /app

COPY . /app
COPY wait-for-it.sh /wait-for-it.sh

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x /wait-for-it.sh

ENTRYPOINT ["/wait-for-it.sh", "db:5432", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]