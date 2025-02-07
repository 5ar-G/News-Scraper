from flask import Flask, render_template, jsonify
from scraper import scrape_bbc  # Import scrape_bbc from scraper.py


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['GET'])
def scrape():
    # Get scraped data from scraper.py
    articles = scrape_bbc()
    return jsonify(articles)



if __name__ == '__main__':
   app.run(debug=False)
    