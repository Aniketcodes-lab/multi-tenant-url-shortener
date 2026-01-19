FROM python:3.12-slim

#Preventing python to create pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

# copy project code
COPY . .

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]