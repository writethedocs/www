FROM python:3.12

RUN mkdir /www
WORKDIR /www
COPY . .

# Update the Linux environment/Operating System
RUN apt-get update
RUN apt-get autoremove -y
RUN apt-get autoclean -y
RUN apt-get upgrade -y

# Install uv and project dependencies
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
RUN uv sync --frozen

WORKDIR /www/docs

RUN chmod +x make.bat

# The following CMD is run every time the Container starts
CMD ["make", "dockerhtml"]