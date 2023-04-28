FROM python:latest

COPY . /opt/app/
WORKDIR /opt/app
RUN python -m pip install -r requirements.txt
CMD ["python", "main.py"]