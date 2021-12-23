FROM python:3.9.7

WORKDIR /usr/src/app

RUN python --version

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry --version

COPY . .
RUN poetry install

CMD poetry run python deploy_model.py
