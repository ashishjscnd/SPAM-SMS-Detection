### Integrate HTML With Flask
### HTTP verb GET And POST

##Jinja2 template engine
'''
{%...%} conditions,for loops
{{    }} expressions to print output
{#....#} this is for comments
'''
from flask import Flask,redirect,url_for,render_template,request
import pickle
import re
import warnings
warnings.filterwarnings("ignore")
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

model = pickle.load(open('model.pkl', 'rb'))
cv = pickle.load(open('CVvectorizer.pkl', 'rb'))

app=Flask(__name__)

def texts_Cl (tx):
    ps = PorterStemmer()
    review = re.sub('[^a-zA-Z]', ' ', tx)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    return review

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        text = request.form['text_input']
        tex_cl = texts_Cl(text)
        vector_in = cv.transform([tex_cl])
        per = model.predict(vector_in)
        if per == 1:
            result = "SPAM"
        else:
            result = "HAM"

    return render_template('result.html', word=result)



if __name__=='__main__':
    app.run(debug=True)