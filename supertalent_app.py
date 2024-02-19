from flask import Flask, render_template

app = Flask(__name__)

# Contestants
contestants = [
    {'id': 1, 'name': 'Ricardo Marinello', 'talent': 'Singing'},
    {'id': 2, 'name': 'Michael Hirte', 'talent': 'Playing harmonica'},
    {'id': 3, 'name': 'Yvo Antoni & PrimaDonna', 'talent': 'Dog act'},
    {'id': 4, 'name': 'Freddy Sahin-Scholl', 'talent': 'Singing'},
    {'id': 5, 'name': 'Leo Rojas', 'talent': 'Playing panpipe'},
    {'id': 6, 'name': 'Jean-Michel Aweh', 'talent': 'Singing'},
    {'id': 7, 'name': 'Lukas Pratschker & Falco', 'talent': 'Dog act'},
    {'id': 8, 'name': 'Marcel Kaupp', 'talent': 'Singing'},
    {'id': 9, 'name': 'Jay Oh', 'talent': 'Singing'},
    {'id': 10, 'name': 'Angel Flukes', 'talent': 'Singing'},
    {'id': 11, 'name': 'Alexa Lauenburger & her mixed-breed dogs', 'talent': 'Dog act'},
    {'id': 12, 'name': 'Stevie Starr', 'talent': 'Professional regurgitator'},
    {'id': 13, 'name': 'Christian Stoinev & Percy', 'talent': 'Dog act'},
    {'id': 14, 'name': 'Nick Ferretti', 'talent': 'Singing'},
    {'id': 15, 'name': 'Elena Turcan', 'talent': 'Singing'},
    {'id': 16, 'name': 'Alexander Doghmani', 'talent': 'Singing'},
    
]

@app.route('/')
def index():
    return render_template('index.html', contestants=contestants)

@app.route('/contestant/<int:contestant_id>')
def contestant(contestant_id):
    contestant = next((c for c in contestants if c['id'] == contestant_id), None)
    if contestant:
        return render_template('contestant.html', contestant=contestant)
    else:
        return 'Contestant not found', 404

if __name__ == '__main__':
    app.run(debug=True)
