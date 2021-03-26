FROM python:3.7
EXPOSE 80

RUN apt-get update
RUN apt-get install build-essential libssl-dev libffi-dev python3-dev cargo --yes
<<<<<<< HEAD
=======

>>>>>>> c1d998ebfafc3aaed84831b4366003a7cdbb0cd1
RUN pip install --upgrade pip

# copy whole installation (minus dockerignore)
COPY ./app /app

# install additional dependencies (might have duplicates?)
# (was pipenv previously but had problems with alpine)
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# set workdir to have subscripts in scope
WORKDIR /app
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
