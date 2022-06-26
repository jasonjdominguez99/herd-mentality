# FROM python:latest

# WORKDIR /app

# COPY . .

# RUN pip install -r requirements.txt

# RUN python3 api/main.py



FROM python:3.8

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "api/main.py"]

















# RUN python3 -m venv herd-mentality-venv
# RUN source herd-mentality-venv/bin/activate

# RUN export FLASK_APP = main

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


# CMD [ "python3", "api/main.py" ]


# COPY requirements.txt .

# RUN pip3 install -r requirements.txt

# COPY . .

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

