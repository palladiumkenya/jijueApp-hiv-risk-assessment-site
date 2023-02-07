FROM python:3.11-slim-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /jijueapp

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "127.0.0.1:8000"]