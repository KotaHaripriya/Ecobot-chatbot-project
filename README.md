
# 🌿 EcoBot – AI-Powered Eco-Friendly Product Recommender

EcoBot is an intelligent chatbot built using Python and Streamlit that helps users discover eco-friendly products from online platforms like Amazon and Flipkart. It combines voice and text-based search, eco-impact scoring, sentiment analysis, and a beautiful chat-style interface to assist consumers in making greener choices.

---

## 🚀 Features

- 🔍 **Voice + Text Input**: Search for products using voice or text in a seamless chat-like UI.
- 🛒 **Live Web Scraping**: Fetches real-time product data from Amazon and Flipkart.
- 🟢 **Eco Confidence Score**: Calculates a climate score (0%–100%) using NLP analysis of reviews, product description, and keywords.
- 😀 **Sentiment Indicators**: Uses emoji-based sentiment analysis of product reviews.
- 📊 **Pie Chart Visualization**: Visual breakdown of eco-friendliness scores across all results.
- 🖼️ **Product Images & Links**: Clickable product previews to shop directly.
- 🕹️ **Search History Sidebar**: Structured and clickable search query history.
- 📱 **Responsive UI**: Optimized for both mobile and desktop with a modern, dark-mode-free aesthetic.

---

## 📁 Project Structure

```
├── app.py
├── analyzer.py
├── storage.py
├── scraper/
│   ├── __init__.py
│   ├── scrape_amazon.py
│   └── scrape_flipkart.py
├── assets/
│   └── (icons, styles, voice scripts)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/KotaHaripriya/ecobot.git
   cd ecobot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # Windows: myenv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## 🌍 Deployment

You can deploy EcoBot on:
- [Streamlit Cloud](https://streamlit.io/cloud)
- Render, Heroku, or any cloud server

Need help deploying? Ask in the issues tab or contact the maintainer.

---

---

## 🧠 Technologies Used

- Python
- Streamlit
- Selenium
- NLTK
- Matplotlib
- HTML/CSS/JS (for voice & layout)

---



---

## 👤 Author

**Bugslayers** – [GitHub](https://github.com/KotaHaripriya)
Haripriya Kota
Nidaharmain Maigeri
Sanskruti Joshi
Sejal Mote

---

## 💡 Contributing

Feel free to fork, improve, or suggest features via pull requests or issues.
