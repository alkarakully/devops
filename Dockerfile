FROM python:latest

# Install git to clone the repository
RUN apt update && apt install -y git

# Clone the repository directly from GitHub
RUN git clone https://github.com/alkarakully/devops.git

WORKDIR /devops

CMD [ "python3", "master.py" ]
