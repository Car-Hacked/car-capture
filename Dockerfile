FROM python:3.10-slim as base

WORKDIR /home/app

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS python-deps
WORKDIR /home/app

RUN apt-get update && apt-get install -y gcc, build-essentials
COPY Pipfile .
COPY Pipfile.lock .
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

FROM base AS runtime
# Create and switch to a new user
WORKDIR /home/app
# Install application into container
COPY . .
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser ./
USER appuser

# Run the application
EXPOSE 5000
CMD ["pipenv", "run", "start"]