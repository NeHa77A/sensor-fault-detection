FROM python:3.8.5-slim-buster
RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt
# Expose the port the application will run on

CMD ["python3", "main.py"]
