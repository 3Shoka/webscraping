from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/detik-populer')
def detik_populer():
    url = 'https://www.detik.com/terpopuler'
    content = requests.get(url)

    soup = BeautifulSoup(content.text, 'html.parser')
    populer = soup.find(attrs={'class': 'list-content'})

    titles = populer.findAll(attrs={'class': 'media__title'})
    images = populer.findAll(attrs={'class': 'media__image'})

    return render_template('detik-populer.html', images=images)


@app.route('/idr-rates')
def idr_rates():
    source = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = source.json()
    return render_template('idr-rates.html', rates=json_data.values())


if __name__ == '__main__':
    app.run(debug=True)
