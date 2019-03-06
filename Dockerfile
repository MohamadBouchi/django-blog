FROM python:3.7.2
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
