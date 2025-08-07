from scraper.scrape_amazon import scrape_amazon
from scraper.scrape_flipkart import scrape_flipkart

def scrape_all(query):
    amazon = scrape_amazon(query)
    flipkart = scrape_flipkart(query)
    combined = amazon + flipkart

    # Fallback to dummy data if both sources fail
    if not combined:
        combined = [{
            "title": "Eco-Friendly Bamboo Toothbrush",
            "link": "https://example.com/toothbrush",
            "image": "https://via.placeholder.com/150",
            "description": "Made from 100% biodegradable bamboo.",
            "reviews": "Excellent product. Very sustainable!",
            "source": "Simulated"
        }, {
            "title": "Reusable Grocery Bag",
            "link": "https://example.com/grocery-bag",
            "image": "https://via.placeholder.com/150",
            "description": "Eco-conscious reusable bags for shopping.",
            "reviews": "Very durable and good for environment.",
            "source": "Simulated"
        }]
    return combined
