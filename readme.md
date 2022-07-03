# Creating an API for the Herd Mentality board game

## To create the virtual environment...
Linux or MacOS:


    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requiements.txt


Windows:


    > virtualenv venv
    > .\venv\Scripts\activate
    > pip install -r requiements.txt


After creating the virtual environment you only need
to run the activation line for future use...
Linux or MacOS:


    $ source venv/bin/activate


Windows:


    > .\venv\Scripts\activate


To deactiate the virtual environment at any time run
'deactivate'.


## Running the server

Before starting the Flask server, ensure that the `FLASK_APP` environment variable is set to `main.py`:
Linux or MacOS:


    $ export FLASK_APP=main.py


Windows command prompt:


    > set FLASK_APP=main.py


Windows PowerShell:


    > $env:FLASK_APP = "main.py"


To start the Flask server run `flask run`.


## GraphQL playground

To use the graphql playground for development, visit http://127.0.0.1:5000/graphql while the server is running.

