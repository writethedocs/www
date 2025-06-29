FROM python:3.9.22

RUN mkdir /www
WORKDIR /www
COPY . .

# Update the Linux environment/Operating System
RUN apt-get update
RUN apt-get autoremove -y 
RUN apt-get autoclean -y
RUN apt-get upgrade -y

# Download the Python3 dependencies
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

WORKDIR /www/docs

RUN chmod +x make.bat

# The following CMD is run every time the Container starts
CMD ["make", "dockerhtml"]