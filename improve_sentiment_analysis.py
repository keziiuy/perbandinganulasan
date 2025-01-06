import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

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
                # Pastikan dataset memiliki kolom yang benar
                if 'snippet_baku' in df.columns and 'sentiment_label' in df.columns:
                    # Hapus baris dengan nilai NaN di kolom yang relevan
                    df = df.dropna(subset=['snippet_baku', 'sentiment_label'])

                    X = df['snippet_baku']
                    y = df['sentiment_label']

                    # Pipeline untuk fitur ekstraksi dan model
                    self.model = make_pipeline(TfidfVectorizer(), LogisticRegression())
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
            if isinstance(review_text, str) and review_text.strip():
                return self.model.predict([review_text])[0]
            else:
                print("Ulasan harus berupa teks non-kosong.")
                return "Error"
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
