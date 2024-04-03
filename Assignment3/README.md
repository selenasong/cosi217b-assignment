# Assignment 3

## Docker

All files that are relevant to each app is in the directory for the app, including requirements, dockerfile, and python files. 

### FastAPI 

To create a container for app_fastapi, first change to the corresponding directory:

```bash
cd ./app_fastapi
```

Then build the image by 

```bash
docker build -t app_fastapi .
```

Then start the app container by 
```bash
docker run -dp 8000:8000 my_fastapi_app
```

Then see the result at http://localhost:8000/

### Flask SQLAlchemy
```bash
cd ./app_flask
docker build -t app_flask .
docker run -dp 8080:5000 my_flask_app
```

### Streamlit 
```bash
cd ./app_flask
docker build -t app_streamlit .
docker run -dp 8501:8501 my_streamlit_app
```
