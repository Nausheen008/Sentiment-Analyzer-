📊 Social Media Sentiment Analyzer

This project analyzes social media posts to study sentiment trends, engagement patterns, and hashtag usage across platforms. It combines Python scripts, Jupyter Notebook exploration, and data visualization to uncover insights from raw data.

🚀 Features

Sentiment Analysis → Understand distribution of positive, neutral, and negative posts.

Engagement Study → Compare likes and retweets across platforms.

Hashtag Trends → Identify top hashtags used in different sentiment categories.

Visual Insights → Generate clear plots with Matplotlib & Seaborn.

📂 Project Structure
.
├── analyzer.py          # Python module with SentimentAnalyzer class
├── analyser.ipynb       # Jupyter Notebook for step-by-step analysis
├── sentimentdataset.csv # Sample dataset
├── requirements.txt     # Required dependencies
├── .gitignore           # Ignore temp files & environments
└── README.md            # Project documentation

🔧 Installation

Clone this repository and install dependencies:

git clone https://github.com/<your-username>/Sentiment-Analyzer-.git
cd Sentiment-Analyzer-
pip install -r requirements.txt


(Optional) Use a virtual environment:

python -m venv .venv
.venv\Scripts\activate    # On Windows
source .venv/bin/activate # On macOS/Linux

📊 Usage
Using the Python module:
from analyzer import SentimentAnalyzer

# Load data
analyzer = SentimentAnalyzer("sentimentdataset.csv")

# Plot sentiment distribution
analyzer.plot_sentiment_distribution()

# Compare engagement (likes/retweets) across platforms
analyzer.compare_engagement_by_platform(metric="likes")

# Analyze sentiment impact on engagement
analyzer.analyze_sentiment_impact_on_engagement()

# Find trending hashtags
print(analyzer.find_top_hashtags(n=10))

Using the Jupyter Notebook:

Open analyser.ipynb in Jupyter Lab or VSCode to walk through the analysis step by step.

📊 Example Insights

Which platform has the highest positive sentiment rate?

Do negative posts get more or fewer likes/retweets?

Which hashtags dominate each sentiment category?

🛠 Tech Stack

Python (pandas, matplotlib, seaborn)

Jupyter Notebook for interactive exploration

CSV Dataset for sentiment and engagement analysis

⚠️ Notes

The provided dataset is small for demo purposes. For larger datasets (>100 MB), consider using Git LFS.

Ensure your dataset has these columns:

Text, Sentiment, Platform, Timestamp, Hashtags, Retweets, Likes, Country

📜 License

This project is open source under the MIT License – feel free to use and adapt it.

✨ With this project, you can quickly explore how sentiment impacts engagement on different social media platforms, and which hashtags drive conversations.
