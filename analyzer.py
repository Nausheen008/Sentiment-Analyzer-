# analyzer.py
# This file contains the class definitions for our social media analysis project.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

class Post:
    """
    Represents a single social media post from the dataset.
    Each instance of this class corresponds to one row of the CSV file.
    """
    def __init__(self, text, sentiment, timestamp, platform, hashtags, retweets, likes, country):
        """
        Initializes a Post object with attributes from the dataset.
        """
        self.text = text
        self.sentiment = sentiment
        # Convert timestamp string to a datetime object for easier manipulation
        self.timestamp = pd.to_datetime(timestamp)
        self.platform = platform
        # Split hashtags string into a list of clean hashtags
        self.hashtags = [tag.strip() for tag in hashtags.split('#') if tag.strip()] if isinstance(hashtags, str) else []
        self.retweets = int(retweets) if not pd.isna(retweets) else 0
        self.likes = int(likes) if not pd.isna(likes) else 0
        self.country = country

    def calculate_total_engagement(self):
        """
        Calculates the total engagement (likes + retweets) for the post.
        """
        return self.likes + self.retweets

    def __repr__(self):
        """
        Provides a developer-friendly string representation of the Post object.
        Helpful for debugging and printing.
        """
        return f"Post(Platform: {self.platform}, Sentiment: {self.sentiment}, Likes: {self.likes})"


class SentimentAnalyzer:
    """
    Manages and analyzes a collection of Post objects.
    This is the main engine for our EDA.
    """
    def __init__(self, filepath):
        """
        Initializes the analyzer by loading and processing the dataset.
        """
        self.filepath = filepath
        self.dataframe = None
        self.posts = []
        self._load_and_process_data() # Private method called on instantiation

    def _load_and_process_data(self):
        """
        Loads data from the specified CSV file, cleans it,
        and creates a list of Post objects.
        """
        try:
            df = pd.read_csv(self.filepath)
            # --- Data Cleaning ---
            # Drop unnecessary columns
            df = df.drop(columns=['Unnamed: 0'], errors='ignore')
            # Drop rows with critical missing data
            df.dropna(subset=['Text', 'Sentiment', 'Platform', 'Timestamp'], inplace=True)
            
            self.dataframe = df # Store the cleaned dataframe
            
            # --- Object Creation ---
            # Create a Post object for each row in the dataframe
            for index, row in df.iterrows():
                self.posts.append(Post(
                    text=row.get('Text'),
                    sentiment=row.get('Sentiment'),
                    timestamp=row.get('Timestamp'),
                    platform=row.get('Platform'),
                    hashtags=row.get('Hashtags'),
                    retweets=row.get('Retweets'),
                    likes=row.get('Likes'),
                    country=row.get('Country')
                ))
            print(f"✅ Successfully loaded and processed {len(self.posts)} posts.")
        except FileNotFoundError:
            print(f"❌ Error: The file at {self.filepath} was not found.")
        except Exception as e:
            print(f"❌ An error occurred during data loading: {e}")

    def plot_sentiment_distribution(self):
        """
        Visualizes the overall distribution of sentiments across all posts.
        """
        if not self.posts:
            print("No posts to analyze.")
            return
        
        sentiment_counts = self.dataframe['Sentiment'].value_counts()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='viridis')
        plt.title('Overall Sentiment Distribution', fontsize=16)
        plt.xlabel('Sentiment', fontsize=12)
        plt.ylabel('Number of Posts', fontsize=12)
        plt.show()

    def compare_engagement_by_platform(self, metric='likes'):
        """
        Compares the average engagement (likes or retweets) across different platforms.
        """
        if not self.posts:
            print("No posts to analyze.")
            return

        # Use the dataframe for efficient grouping
        if metric == 'likes':
            avg_engagement = self.dataframe.groupby('Platform')['Likes'].mean().sort_values(ascending=False)
        elif metric == 'retweets':
            avg_engagement = self.dataframe.groupby('Platform')['Retweets'].mean().sort_values(ascending=False)
        else:
            print("Invalid metric. Choose 'likes' or 'retweets'.")
            return
            
        plt.figure(figsize=(12, 7))
        sns.barplot(x=avg_engagement.index, y=avg_engagement.values, palette='mako')
        plt.title(f'Average {metric.capitalize()} per Post by Platform', fontsize=16)
        plt.xlabel('Platform', fontsize=12)
        plt.ylabel(f'Average {metric.capitalize()}', fontsize=12)
        plt.xticks(rotation=45)
        plt.show()

    def analyze_sentiment_impact_on_engagement(self):
        """
        Visualizes how sentiment affects the average number of likes and retweets.
        """
        if not self.posts:
            print("No posts to analyze.")
            return
        
        # Calculate average likes and retweets per sentiment
        sentiment_engagement = self.dataframe.groupby('Sentiment')[['Likes', 'Retweets']].mean().reset_index()
        
        # Melt the dataframe to make it suitable for a grouped bar plot
        melted_df = sentiment_engagement.melt(id_vars='Sentiment', var_name='EngagementType', value_name='AverageCount')

        plt.figure(figsize=(12, 7))
        sns.barplot(data=melted_df, x='Sentiment', y='AverageCount', hue='EngagementType', palette='rocket')
        plt.title('Impact of Sentiment on Engagement', fontsize=16)
        plt.xlabel('Sentiment', fontsize=12)
        plt.ylabel('Average Count', fontsize=12)
        plt.legend(title='Engagement Type')
        plt.show()

    def find_top_hashtags(self, n=10):
        """
        Finds and displays the most frequently used hashtags.
        """
        if not self.posts:
            print("No posts to analyze.")
            return
        
        all_hashtags = [hashtag for post in self.posts for hashtag in post.hashtags]
        hashtag_counts = Counter(all_hashtags)
        
        top_hashtags = hashtag_counts.most_common(n)
        
        print(f"🏆 Top {n} Most Popular Hashtags:")
        for i, (hashtag, count) in enumerate(top_hashtags, 1):
            print(f"{i}. #{hashtag} (used {count} times)")
        
        return top_hashtags
