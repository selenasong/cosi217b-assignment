# Assignment 2

## Flask SQLAlchemy 

### Requirments:

Python>=3.9

en-core-web-sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl#sha256=86cc141f63942d4b2c5fcee06630fd6f904788d2f0ab005cce45aadb8fb73889

Flask==3.0.2

Flask-SQLAlchemy==3.1.1

spacy==3.7.4

SQLAlchemy==2.0.28



### To run app:

```bash
python app.py
```

### Note:
There is a .db file in this directory so that if you want to check the database without submitting any sentence the link ("Click here to look at all entities and relations") won't crash. 

If you would like to add new sentences into the database, simply type the sentence in the text box and click "submit". You should see all the entities marked up and all dependency parsings listed, which will at the same time be written into the database. Now, if you want to check the updated database, click the "back to form" below to go back to the first page, then click the "Click here to look at all entities and relations" link again. 

The database should look like this:


<img width="640" alt="Screenshot 2024-03-12 at 20 44 25" src="https://github.com/selenasong/cosi217b-assignment1/assets/127460254/b12beff6-6b87-4dc6-8e5e-f18339c6320d">
