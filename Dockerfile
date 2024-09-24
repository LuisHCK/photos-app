FROM python:alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /opt/app
WORKDIR /opt/app
RUN pip install --upgrade pip
COPY requirements.txt /opt/app

RUN pip install -r requirements.txt
COPY . /opt/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
