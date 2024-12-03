FROM python:latest

# Install git to clone the repository
RUN apt update && apt install -y git

RUN pip install Django 

# Clone the repository directly from GitHub

WORKDIR /tssdata

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
