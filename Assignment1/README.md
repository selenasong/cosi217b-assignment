# Assignment 1 

### FastAPI

To run:

```bash
uvicorn app_fastapi:app --reload
```

Then enter files/texts to process in another terminal. 

Accessing the dependency parser:

```bash
curl http:/127.0.0.1:8000
curl -X POST http://127.0.0.1:8000/dep \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d@input.json
```


Accessing the NER:

```bash
curl http:/127.0.0.1:8000
curl -X POST http://127.0.0.1:8000/ner \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d@input.json
```

You should then see the results showing up in the terminal. 


### Flask server

To run:

```bash
python app_flask.py
```


### Streamlit

To run:

```bash
streamlit run app_streamlit.py
```
