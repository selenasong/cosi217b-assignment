from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import ner
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)

class Token_relation(db.Model):
   token = db.Column(db.String, primary_key=True)
   relation = db.Column(db.String, primary_key=True)
   count = db.Column(db.Integer, primary_key=False, default=1)

   def __init__(self, token, relation):
      self.token = token
      self.relation = relation

class Entities(db.Model):
   entity = db.Column(db.String, primary_key=True)
   token = db.Column(db.String, primary_key=True)

   def __init__(self, entity, token):
      self.entity = entity
      self.token = token

def add_relations_to_db(dependency_parse, entities):
    with app.app_context():
        db.create_all()
        for token, relation, head in dependency_parse:
            relation_entry = "{} {} {}".format(head, relation, token)
            existing_relation = Token_relation.query.filter_by(token=token, relation=relation_entry).first()
            if existing_relation:
                existing_relation.count += 1
            else:
                db.session.add(Token_relation(token=token, relation=relation_entry))
            db.session.commit()

        for _, _, _, text in entities:
            existing_entity = Entities.query.filter_by(entity=text).first()
            if not existing_entity:
                for token in text.split():
                    db.session.add(Entities(text, token))
            db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html', input=open('input.txt').read())
    else:
        text = request.form['text']
        doc = ner.SpacyDocument(text)
        dependency_parse = doc.get_dependency_parse()
        entities = doc.get_entities()
        add_relations_to_db(dependency_parse,entities)
        markup = doc.get_entities_with_markup()
        markup_paragraphed = ''
        for line in markup.split('\n'):
            if line.strip() == '':
                markup_paragraphed += '<p/>\n'
            else:
                markup_paragraphed += line
        return render_template('result.html', markup=markup_paragraphed, dependency_parse=dependency_parse, doc=doc)

# alternative where we use two resources

@app.get('/get')
def index_get():
    return render_template('form2.html', input=open('input.txt').read())

@app.post('/post')
def index_post():
    text = request.form['text']
    doc = ner.SpacyDocument(text)
    dependency_parse = doc.get_dependency_parse()
    entities = doc.get_entities()
    add_relations_to_db(dependency_parse, entities)
    markup = doc.get_entities_with_markup()
    markup_paragraphed = ''
    for line in markup.split('\n'):
        if line.strip() == '':
            markup_paragraphed += '<p/>\n'
        else:
            markup_paragraphed += line
    return render_template('result.html', markup=markup_paragraphed, dependency_parse=dependency_parse, doc=doc)


@app.route('/post')
def show_all():
    entity_relations = Token_relation.query.join(Entities, Entities.token == Token_relation.token).add_columns(
         Entities.entity, Token_relation.relation, Token_relation.count).all()

    entity_counts = {}
    for entity_relation in entity_relations:
        entity = entity_relation.entity
        count = entity_relation.count
        if entity in entity_counts:
            entity_counts[entity] += count
        else:
            entity_counts[entity] = count

    return render_template('show_all.html', entity_relations=entity_relations, entity_counts=entity_counts)


if __name__ == '__main__':
   app.run(debug=True)