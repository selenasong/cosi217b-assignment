"""Simple Web interface to spaCy entity recognition

To see the pages point your browser at http://127.0.0.1:5000.

"""


from flask import Flask, request, render_template

import ner

app = Flask(__name__)

# For the website we use the regular Flask functionality and serve up HTML pages.

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html', input=open('input.txt').read())
    else:
        text = request.form['text']
        doc = ner.SpacyDocument(text)
        dependency_parse = doc.get_dependency_parse()
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
    markup = doc.get_entities_with_markup()
    markup_paragraphed = ''
    for line in markup.split('\n'):
        if line.strip() == '':
            markup_paragraphed += '<p/>\n'
        else:
            markup_paragraphed += line
    return render_template('result.html', markup=markup_paragraphed, dependency_parse=dependency_parse, doc=doc)


if __name__ == '__main__':

    app.run(debug=True)
