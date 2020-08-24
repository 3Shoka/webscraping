from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detik-populer')
def detik_populer():
    url = 'https://www.detik.com/terpopuler'
    content = requests.get(url)

    soup = BeautifulSoup(content.text, 'html.parser')
    populer = soup.find(attrs={'class': 'list-content'})

    titles = populer.findAll(attrs={'class': 'media__title'})
    images = populer.findAll(attrs={'class': 'media__image'})

    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)