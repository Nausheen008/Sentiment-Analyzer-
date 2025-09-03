📊 Social Media Sentiment Analyzer

This project is a data analysis toolkit for studying social media posts. It helps you explore how sentiments (positive, negative, neutral) influence engagement metrics such as likes and retweets, and it also highlights trending hashtags across different platforms.

📖 Overview

Perform sentiment analysis on social media text data.

Visualize sentiment distribution with plots.

Compare engagement across platforms.

Extract top hashtags driving conversations.

Work interactively through a Jupyter Notebook or use the Python module directly.

📂 Files in this Repository
File/Folder	Description
analyzer.py	Main Python script with SentimentAnalyzer class.
analyser.ipynb	Notebook for step-by-step interactive analysis.
sentimentdataset.csv	Sample dataset containing posts and engagement details.
requirements.txt	Dependencies list (pandas, matplotlib, seaborn).
.gitignore	Ignore unnecessary files when committing.
README.md	Documentation (this file).
⚙️ Installation

Clone the repository:

git clone https://github.com/<your-username>/Sentiment-Analyzer-.git
cd Sentiment-Analyzer-


Install required packages:

pip install -r requirements.txt


(Optional: set up a virtual environment for clean installs.)

🚀 How to Use
1. Python Script
from analyzer import SentimentAnalyzer

# Load dataset
analyzer = SentimentAnalyzer("sentimentdataset.csv")

# Plot charts
analyzer.plot_sentiment_distribution()
analyzer.compare_engagement_by_platform(metric="likes")
analyzer.analyze_sentiment_impact_on_engagement()

# Extract top hashtags
print(analyzer.find_top_hashtags(n=10))

2. Notebook

Open analyser.ipynb in Jupyter Lab/Notebook or VS Code and follow the cells for guided analysis.

🛠 Requirements

Python 3.6+

pandas

matplotlib

seaborn

(Automatically installed via requirements.txt.)

📊 Example Questions Answered

What proportion of posts are positive, negative, or neutral?

Which platform drives the most engagement for positive posts?

Do negative sentiments reduce or increase likes/retweets?

What are the most common hashtags across sentiments?timent impacts engagement on different social media platforms, and which hashtags drive conversations.
