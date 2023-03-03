FROM python:3.10-slim as base

WORKDIR /home/app

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS python-deps
WORKDIR /home/app

RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Create and switch to a new user
WORKDIR /home/app

# Install application into container
COPY . .

# Run the application
EXPOSE 5000
CMD ["pipenv", "run start"]