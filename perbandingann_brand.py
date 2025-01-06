import pandas as pd
import matplotlib.pyplot as plt

# Load dataset ulasan KFC dan Richeese
kfc_file_path = 'sentimen_KFC.csv'  # Path file ulasan KFC
richeese_file_path = 'sentimenricheese.csv'  # Path file ulasan Richeese

kfc_reviews = pd.read_csv(kfc_file_path)
richeese_reviews = pd.read_csv(richeese_file_path)

# Pastikan dataset memiliki kolom 'sentiment'
print("Contoh data KFC:")
print(kfc_reviews.head())
print("Contoh data Richeese:")
print(richeese_reviews.head())

# Cek nilai unik di kolom sentiment_label untuk memastikan konsistensi
print("\nNilai unik di kolom 'sentiment_label' untuk KFC:", kfc_reviews['sentiment_label'].unique())
print("Nilai unik di kolom 'sentiment_label' untuk Richeese:", richeese_reviews['sentiment_label'].unique())

# Normalisasi data (samakan jumlah data)
min_rows = min(len(kfc_reviews), len(richeese_reviews))
kfc_reviews_sampled = kfc_reviews.sample(n=min_rows, random_state=42)
richeese_reviews_sampled = richeese_reviews.sample(n=min_rows, random_state=42)

# Tampilkan jumlah ulasan setelah sampling
print(f"\nJumlah ulasan setelah sampling:")
print(f"KFC: {len(kfc_reviews_sampled)} ulasan")
print(f"Richeese: {len(richeese_reviews_sampled)} ulasan")

# Hitung distribusi sentimen berdasarkan proporsi
kfc_sentiment_dist = kfc_reviews_sampled['sentiment_label'].value_counts(normalize=True) * 100
richeese_sentiment_dist = richeese_reviews_sampled['sentiment_label'].value_counts(normalize=True) * 100

# Gabungkan distribusi sentimen untuk perbandingan
comparison = pd.DataFrame({
    'Sentiment': ['negatif', 'netral', 'positif'],
    'KFC (%)': [kfc_sentiment_dist.get(sentiment, 0) for sentiment in ['negatif', 'netral', 'positif']],
    'Richeese (%)': [richeese_sentiment_dist.get(sentiment, 0) for sentiment in ['negatif', 'netral', 'positif']]
}).fillna(0)

# Hitung skor keseluruhan untuk masing-masing brand
kfc_score = kfc_sentiment_dist.get('positif', 0) - kfc_sentiment_dist.get('negatif', 0)
richeese_score = richeese_sentiment_dist.get('positif', 0) - richeese_sentiment_dist.get('negatif', 0)

print("\nPerbandingan Proporsi Sentimen:")
print(comparison)
print("\nSkor Keseluruhan:")
print(f"KFC: {kfc_score}")
print(f"Richeese: {richeese_score}")

# Visualisasi perbandingan proporsi
sentiments = comparison['Sentiment']
kfc_percentage = comparison['KFC (%)']
richeese_percentage = comparison['Richeese (%)']

x = range(len(sentiments))
bar_width = 0.4

plt.bar(x, kfc_percentage, width=bar_width, label='KFC', color='blue', align='center')
plt.bar([p + bar_width for p in x], richeese_percentage, width=bar_width, label='Richeese', color='orange', align='center')

plt.xticks([p + bar_width / 2 for p in x], sentiments)
plt.xlabel('Sentiment')
plt.ylabel('Percentage')
plt.title('Sentiment Distribution: KFC vs Richeese')
plt.legend()
plt.show()

# Visualisasi skor keseluruhan
brands = ['KFC', 'Richeese']
scores = [kfc_score, richeese_score]

plt.bar(brands, scores, color=['blue', 'orange'])
plt.xlabel('Brand')
plt.ylabel('Overall Score')
plt.title('Overall Sentiment Score: KFC vs Richeese')
plt.show()
