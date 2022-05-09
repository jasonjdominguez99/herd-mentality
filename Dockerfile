FROM python:latest

WORKDIR /app

COPY . .

# RUN python3 -m venv herd-mentality-venv
# RUN source herd-mentality-venv/bin/activate
RUN pip install -r requirements.txt

# RUN export FLASK_APP = main

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


CMD [ "python3", "api/main.py" ]


# COPY requirements.txt .

# RUN pip3 install -r requirements.txt

# COPY . .

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


