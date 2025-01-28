from flask import Flask, jsonify
from natscraper import Scraper

app = Flask(__name__)

# Initialize the scraper
scraper = Scraper()

@app.route("/scrape_tweets", methods=["GET"])
def scrape_tweets():
    try:
        # Scrape the latest 10 tweets with the keyword "story protocol"
        tweets = scraper.search("story protocol", limit=10)
        
        # Return tweets in JSON format
        return jsonify(tweets)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# This is necessary for Vercel's serverless function handler
def handler(request):
    return app(request)
