import pandas as pd
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
def load_dataset(file_path):
    """Load the dataset from a CSV file."""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
# Fungsi untuk membaca CSV dan memfilter ulasan berdasarkan sentimen
def get_reviews_by_sentiment(file_path, sentiment):
    df = load_dataset(file_path)
    if df is not None:
        if sentiment.lower() == "positif":
            return df[df['sentiment_label'] == 'positif']['snippet_baku'].tolist()
        elif sentiment.lower() == "negatif":
            return df[df['sentiment_label'] == 'negatif']['snippet_baku'].tolist()
        else:
            return []
    else:
        return []

# Fungsi untuk memuat dataset
def load_dataset(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Fungsi untuk melatih model sentimen
class SentimentAnalyzer:
    def __init__(self):
        self.model = None

    def train(self, file_path):
        df = load_dataset(file_path)
        if df is not None:
            try:
                # Pastikan kolom memiliki nama yang benar
                if 'snippet_baku' in df.columns and 'sentiment_label' in df.columns:
                    X = df['snippet_baku']
                    y = df['sentiment_label']

                    # Pipeline untuk fitur ekstraksi dan model
                    self.model = make_pipeline(CountVectorizer(), MultinomialNB())
                    self.model.fit(X, y)
                    print("Model berhasil dilatih.")
                else:
                    print("Dataset tidak memiliki kolom yang sesuai.")
            except Exception as e:
                print(f"Terjadi kesalahan saat melatih model: {e}")
        else:
            print("Dataset tidak ditemukan atau error saat dimuat.")

    def predict(self, review_text):
        if self.model:
            return self.model.predict([review_text])[0]
        else:
            print("Model belum dilatih.")
            return "Error"

# Contoh penggunaan jika diintegrasikan
if __name__ == "__main__":
    file_path = "sentimenricheese.csv"  # Path dataset Anda
    analyzer = SentimentAnalyzer()
    analyzer.train(file_path)

    # Contoh ulasan baru
    review_text = "Pelayanan sangat buruk dan lama."
    sentiment = analyzer.predict(review_text)
    print(f"Sentimen ulasan: {sentiment}")
def load_dataset(file_path):
    """Load the dataset from a CSV file."""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
# Fungsi untuk membaca CSV dan memfilter ulasan berdasarkan sentimen
def get_reviews_by_sentiment(file_path, sentiment):
    df = load_dataset(file_path)
    if df is not None:
        if sentiment.lower() == "positif":
            return df[df['sentiment_label'] == 'positif']['snippet_baku'].tolist()
        elif sentiment.lower() == "negatif":
            return df[df['sentiment_label'] == 'negatif']['snippet_baku'].tolist()
        else:
            return []
    else:
        return []
