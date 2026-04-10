FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# The Yarn apt repo bundled in this base image has an expired GPG key,
# which breaks any subsequent apt-get update (e.g. during feature installs).
# Remove it so downstream steps don't fail.
RUN rm -f /etc/apt/sources.list.d/yarn.list \
          /etc/apt/sources.list.d/yarn.list.save 2>/dev/null; exit 0