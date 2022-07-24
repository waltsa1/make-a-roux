from flask import Flask, render_template, request
import requests as req

app = Flask(__name__)

api_key = '5599045a4c71eb8bb5aa46beb2d053ee04355ad2'
api_url = 'https://www.giantbomb.com/api'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search_page():
    return render_template('search_page.html')


@app.route('/checkout')
def checkout_page():
    return render_template('checkout_page.html')


@app.route('/results', methods=['POST', 'GET'])
def results():
    if request.method == 'POST':
        game_name = request.form.get('game_name')
        search_url = '{url}/search/?api_key={key}&format=json' \
                     '&query={query}&resources=game&field_list=name,image'\
            .format(url=api_url, key=api_key, query=game_name)
        search_results = req.get(search_url)
        if search_results.status_code != 200:
            return render_template('search_results.html', results=search_results.status_code)
        return render_template('search_results.html', results=search_results)


if __name__ == '__main__':
    app.run()