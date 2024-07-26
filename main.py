
from flask import Flask, request, render_template
import random

app = Flask(__name__)

english_flashcards = [
    "She'll be right, mate",
    "Fair dinkum",
    "Chuck a U-ey",
    "G'day",
    "Barbie",
]

dutch_flashcards = [
    "Het komt wel goed, makker",
    "Echt waar",
    "Maak een U-bocht",
    "Goeiedag",
    "Barbecue",
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    english_text = request.form['english_text']
    english_list = english_text.split('\n')

    translated_list = []
    for item in english_list:
        index = random.randint(0, len(english_flashcards) - 1)
        translated_list.append(dutch_flashcards[index])

    dutch_text = '\n'.join(translated_list)
    return render_template('index.html', dutch_text=dutch_text)

if __name__ == '__main__':
    app.run(debug=True)
