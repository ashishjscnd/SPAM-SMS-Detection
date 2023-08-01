from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def word_counter():
    if request.method == 'POST':
        text = request.form['text_input']
        word_count = len(text.split())
        return render_template('result.html', word_count=word_count)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)