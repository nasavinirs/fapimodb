
# FastAPI with MongoDB

This is a sample CRUD program to connect FastAPI with MongoDB.

## Tech Stack

**Client:** Python

**Server:** FastAPI, MongoDB

## Installation

Python version 3 is required. Create a virtual environment inside the project folder as follows.

```bash
  > cd project_folder
  > python3 -m venv fenv
```

Once the virtual environment is created, go inside to that virual environment with following command.

```bash
  # For Windows
  project_folder> fenv/bin/activate.bat
  
  # For Mac or Linux
  project_folder> source fenv/bin/activate.csh
```

Install python project dependencies from requirements.txt file with following command.

```bash
  project_folder> pip3 install -r requirements.txt
```

    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`APP_PORT`

`SERVER`

`APP_NAME`

`DB_USERNAME`

`DB_PASSWORD`

## Run Locally

To run FastAPI locally, run the following command.

```bash
  project_folder> uvicorn main:app --reload
```

Once the server is started, hit http://127.0.0.1/8000 in your browser to see the response.

To see the docs, hit http://127.0.0.1:8000/docs to see API docs.


## Lessons Learned

How to use FastAPI with a NoSQL database (MongoDB). 
1. How to create a free MongoDB Atlas account online and create a free M0 cluster in it. 
2. Python code to connect to MongoDB Atlas to check its connection.
3. FastAPI routes to create CRUD methods to connect with MongoDB.


## Authors

- [SrinivasanS](https://www.github.com/nasavinirs)


## License

[MIT](https://choosealicense.com/licenses/mit/)

