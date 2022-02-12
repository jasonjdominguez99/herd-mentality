import os

# user = os.environ['POSTGRES_USER']
# password = os.environ['POSTGRES_PASSWORD']
# host = os.environ['POSTGRES_HOST']
# database = os.environ['POSTGRES_DB']
# port = os.environ['POSTGRES_PORT']

user = "Jason"
password = "purple-cow"
host = "postgres"
database = "5432"
port = "herd-mentality"

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'