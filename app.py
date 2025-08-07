import streamlit as st
from analyzer import analyze_reviews, calculate_eco_score
from __init__ import scrape_all
from storage import save_to_history, load_history
import matplotlib.pyplot as plt
import base64
import os

st.set_page_config(page_title="EcoBot", layout="wide")

# Inject custom JS for mic
with open("mic.js") as f:
    st.components.v1.html(f"<script>{f.read()}</script>", height=0)

st.markdown("""
    <style>
        body {
            background-color: #ffffff;
            color: #000000;
        }
        .stTextInput > div > div {
            display: flex;
            align-items: center;
        }
        .mic-button {
            background: none;
            border: none;
            cursor: pointer;
            margin-left: -35px;
            margin-top: 5px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 EcoBot – Sustainable Product Recommender")

# Sidebar for search history
with st.sidebar:
    st.header("🕘 Search History")
    history = load_history()
    for i, h in enumerate(history[::-1]):
        if st.button(h["query"]):
            st.session_state["last_query"] = h["query"]

# Query input
query = st.text_input("Search for a product...", key="query_input", placeholder="e.g., eco-friendly yoga mat 🧘‍♀️")

mic_html = '''
    <button class="mic-button" onclick="startDictation()">
        🎤
    </button>
'''
st.markdown(mic_html, unsafe_allow_html=True)

if query or st.session_state.get("last_query"):
    user_query = query if query else st.session_state["last_query"]
    st.session_state["last_query"] = user_query

    with st.spinner("🔎 Searching eco-friendly products..."):
        raw_data = scrape_all(user_query)

        if not raw_data:
            st.error("❌ No products found. Try another keyword.")
        else:
            save_to_history(user_query)
            sentiments = {"Positive": 0, "Neutral": 0, "Negative": 0}
            eco_data = []

            for item in raw_data:
                sentiment = analyze_reviews(item.get("reviews", ""))
                score = calculate_eco_score(item.get("title", "") + item.get("description", ""))
                sentiments[sentiment] += 1
                item.update({
                    "sentiment": sentiment,
                    "eco_score": score
                })
                eco_data.append(item)

            # Results
            for i, item in enumerate(eco_data, 1):
                st.markdown(f"### {i}. [{item['title']}]({item['link']}) ({item['source']})")
                col1, col2 = st.columns([1, 4])
                with col1:
                    if item["image"]:
                        st.image(item["image"], width=100)
                with col2:
                    st.markdown(f"**Sentiment**: {item['sentiment']} {'✅' if item['sentiment']=='Positive' else '⚠️' if item['sentiment']=='Neutral' else '❌'}")
                    st.markdown(f"**Climate Score**: {item['eco_score']}% {'🟢' if item['eco_score']>=80 else '🟡' if item['eco_score']>=60 else '🔴'}")
                    st.markdown(f"**Description**: {item['description'][:200]}...")

            # Pie Chart
            sizes = [sentiments["Positive"], sentiments["Neutral"], sentiments["Negative"]]
            if sum(sizes) > 0:
                labels = ['Positive', 'Neutral', 'Negative']
                colors = ['green', 'orange', 'red']
                fig, ax = plt.subplots()
                ax.pie(sizes, labels=labels, colors=colors, startangle=90, autopct='%1.1f%%')
                ax.axis('equal')
                st.subheader("📊 Sentiment Analysis Distribution")
                st.pyplot(fig)



