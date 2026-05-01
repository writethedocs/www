FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# Remove broken yarn apt source whose GPG key is expired (devcontainers/images#1752)
# Install Ruby for htmlproofer (link checking in CI and locally)
RUN rm -f /etc/apt/sources.list.d/yarn.list \
    && apt-get update && apt-get install -y --no-install-recommends \
    ruby ruby-dev build-essential zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*
