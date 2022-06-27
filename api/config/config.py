import os

# user = os.environ['POSTGRES_USER']
# password = os.environ['POSTGRES_PASSWORD']
# host = os.environ['POSTGRES_HOST']
# database = os.environ['POSTGRES_DB']
# port = os.environ['POSTGRES_PORT']

user = "Jason"
password = "purple-cow"
host = "sanchayata/herd-mentality:v0.1.0"
database = "herd-mentality"
port = "5432"

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'