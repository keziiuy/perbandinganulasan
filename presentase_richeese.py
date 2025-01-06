import pandas as pd
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import seaborn as sns
from wordcloud import WordCloud
# # Load dataset
df = pd.read_csv('sentimenricheese.csv')

df['brand'] = 'KFC'


# Menghitung distribusi sentimen dalam bentuk persentase
sentiment_counts = df['sentiment_label'].value_counts(normalize=True) * 100

# Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['skyblue', 'orange', 'green'])
plt.title('Distribusi Sentimen untuk Brand Richeese (Dalam Persentase)')
plt.show()