FROM python:3.9.7

WORKDIR /usr/src/app

RUN python --version

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry --version

COPY . .
RUN poetry install

CMD poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
