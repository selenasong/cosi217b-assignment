# Assignment 3

## Docker

All files that are relevant to each app is in the directory for the app, including requirements, dockerfile, and python files. 

To run all containers:

```bash
docker-compose up
```
Then visit http://localhost:8000/,  http://localhost:5000/,  http://localhost:8501/ to view the pages. 

### FastAPI 

To create a container for app_fastapi, run the following:

```bash
cd ./app_fastapi
docker build -t app_fastapi .
docker run -dp 8000:8000 my_fastapi_app
```
Then see the result at http://localhost:8000/

### Flask SQLAlchemy
```bash
cd ./app_flask
docker build -t app_flask .
docker run -dp 8080:5000 my_flask_app
```
Then see the result at http://localhost:5000/

### Streamlit 
```bash
cd ./app_streamlit
docker build -t app_streamlit .
docker run -dp 8501:8501 my_streamlit_app
```
Then see the result at http://localhost:8501/
