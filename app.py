# import streamlit as st
# import pandas as pd
# from PIL import Image
# from improve_sentiment_analysis import SentimentAnalyzer

# # Inisialisasi model analisis sentimen
# file_path = "inti/sentimenricheese.csv"
# analyzer = SentimentAnalyzer()
# analyzer.train(file_path)

# # Fungsi untuk halaman pertama
# def first_page():
#     st.title("Review Ulasan")
#     st.write("**Selamat datang di aplikasi analisis ulasan!**")

#     # Menambahkan gambar latar belakang
#     image = Image.open("inti/firstpage.png")
#     st.image(image, use_column_width=True)

#     # Tombol navigasi ke halaman utama
#     if st.button("START"):
#         st.session_state.page = "home"

# # Fungsi untuk halaman utama
# def home_page():
#     st.title("Halaman Utama")

#     # Menambahkan gambar latar belakang
#     image = Image.open("inti/homepage.png")
#     st.image(image, use_column_width=True)

#     # Tombol navigasi ke fitur-fitur
#     if st.button("Presentase Ulasan"):
#         st.session_state.page = "percentage"
#     if st.button("Perbandingan Brand"):
#         st.session_state.page = "comparison"
#     if st.button("Review Ulasan"):
#         st.session_state.page = "review"
#     if st.button("Tampilkan Ulasan"):  # Tambahkan tombol ini
#         st.session_state.page = "display_reviews" 

# # Fungsi untuk presentase ulasan
# def percentage_page():
#     st.title("Presentase Ulasan")

#     # Pilihan brand
#     brand = st.selectbox("Pilih Brand", ["KFC", "Richeese"])
#     if st.button("Tampilkan Presentase"):
#         if brand == "KFC":
#             st.session_state.page = "presentase_kfc"
#         elif brand == "Richeese":
#             st.session_state.page = "presentase_richeese"

# # Fungsi untuk perbandingan brand
# def comparison_page():
#     st.title("Perbandingan Brand")
#     st.write("Fitur ini sedang dalam pengembangan...")

# # Fungsi untuk review ulasan
# def review_page():
#     st.title("Review Ulasan")

#     # Input ulasan baru
#     review_text = st.text_input("Masukkan Ulasan Baru")
#     if st.button("Cek Sentimen"):
#         sentiment = check_sentiment(review_text)
#         st.write(f"Sentimen ulasan: {sentiment}")

# # Fungsi untuk presentase KFC
# def presentase_kfc_page():
#     st.title("Presentase Ulasan - KFC")
#     image = Image.open("inti/presentasekfc.png")
#     st.image(image, use_column_width=True)

#     # Tombol kembali ke halaman utama
#     if st.button("Kembali ke Halaman Utama"):
#         st.session_state.page = "home"

# # Fungsi untuk presentase Richeese
# def presentase_richeese_page():
#     st.title("Presentase Ulasan - Richeese")
#     image = Image.open("inti/presentasericheese.png")
#     st.image(image, use_column_width=True)

#     # Tombol kembali ke halaman utama
#     if st.button("Kembali ke Halaman Utama"):
#         st.session_state.page = "home"
# def display_reviews():
#     st.title("Tampilkan Ulasan")

#     # Pilihan brand
#     brand = st.selectbox("Pilih Brand", ["KFC", "Richeese"])

#     # Pilihan sentimen
#     sentiment = st.selectbox("Pilih Sentimen", ["Positif", "Negatif"])

#     if st.button("Tampilkan Ulasan"):
#         try:
#             # Memilih file berdasarkan brand
#             if brand == "KFC":
#                 df = pd.read_csv('inti/sentimen_KFC.csv')  # Path dataset KFC
#             elif brand == "Richeese":
#                 df = pd.read_csv('inti/sentimenricheese.csv')  # Path dataset Richeese

#             # Filter ulasan berdasarkan sentimen
#             sentiment_mapping = {"Positif": "positif", "Negatif": "negatif"}
#             selected_sentiment = sentiment_mapping.get(sentiment)

#             if selected_sentiment is None:
#                 st.warning("Sentimen tidak valid.")
#                 return

#             filtered_reviews = df[df["sentiment_label"] == selected_sentiment]

#             # Menampilkan ulasan
#             if not filtered_reviews.empty:
#                 st.write(f"Menampilkan ulasan {brand} dengan sentimen {sentiment}:")
#                 for idx, row in filtered_reviews.iterrows():
#                     st.write(f"- {row['snippet']}")
#             else:
#                 st.warning(f"Tidak ada ulasan {brand} dengan sentimen {sentiment}.")

#         except FileNotFoundError as e:
#             st.error(f"Error: File {e.filename} tidak ditemukan.")
#         except Exception as e:
#             st.error(f"Terjadi kesalahan: {str(e)}")

#     # Tombol Back
#     if st.button("Kembali ke Halaman Utama"):
#         st.session_state.page = "home"

# # Fungsi untuk mengecek sentimen
# def check_sentiment(review_text):
#     if not review_text.strip():
#         return "Masukkan ulasan terlebih dahulu!"
    
#     # Membaca dataset sentimen
#     sentimen_kfc = pd.read_csv('inti/kata_sentimen_kfc.csv')
#     sentimen_richeese = pd.read_csv('inti/kata_sentimen_richeese.csv')

#     # Gabungkan kata positif dan negatif
#     sentimen_dict = {
#         "positif": set(sentimen_kfc[sentimen_kfc['label'] == 'positif']['kata'].tolist() +
#                        sentimen_richeese[sentimen_richeese['label'] == 'positif']['kata'].tolist()),
#         "negatif": set(sentimen_kfc[sentimen_kfc['label'] == 'negatif']['kata'].tolist() +
#                        sentimen_richeese[sentimen_richeese['label'] == 'negatif']['kata'].tolist())
#     }

#     words = review_text.lower().split()
#     positif_count = sum(1 for word in words if word in sentimen_dict['positif'])
#     negatif_count = sum(1 for word in words if word in sentimen_dict['negatif'])

#     if positif_count > negatif_count:
#         return "positif"
#     elif negatif_count > positif_count:
#         return "negatif"
#     else:
#         return "netral"

# # Routing halaman berdasarkan session state
# if "page" not in st.session_state:
#     st.session_state.page = "first"

# if st.session_state.page == "first":
#     first_page()

# elif st.session_state.page == "home":
#     home_page()
# elif st.session_state.page == "percentage":
#     percentage_page()
# elif st.session_state.page == "comparison":
#     comparison_page()
# elif st.session_state.page == "review":
#     review_page()
# elif st.session_state.page == "presentase_kfc":
#     presentase_kfc_page()
# elif st.session_state.page == "presentase_richeese":
#     presentase_richeese_page()

import streamlit as st
import pandas as pd
from PIL import Image
from improve_sentiment_analysis import SentimentAnalyzer

# Inisialisasi model analisis sentimen
file_path = "inti/sentimenricheese.csv"
analyzer = SentimentAnalyzer()
analyzer.train(file_path)

# Fungsi untuk halaman pertama
def first_page():
    st.title("Review Ulasan")
    st.write("**Selamat datang di aplikasi analisis ulasan!**")

    # Menambahkan gambar latar belakang
    image = Image.open("inti/firstpage.png")
    st.image(image, use_column_width=True)

    # Tombol navigasi ke halaman utama
    if st.button("START"):
        st.session_state.page = "home"

# Fungsi untuk halaman utama
def home_page():
    st.title("Halaman Utama")

    # Menambahkan gambar latar belakang
    image = Image.open("inti/homepage.png")
    st.image(image, use_column_width=True)

    # Tombol navigasi ke fitur-fitur
    if st.button("Presentase Ulasan"):
        st.session_state.page = "percentage"
    if st.button("Perbandingan Brand"):
        st.session_state.page = "comparison"
    if st.button("Review Ulasan"):
        st.session_state.page = "review"
    if st.button("Tampilkan Ulasan"):  # Tambahkan tombol ini
        st.session_state.page = "display_reviews" 

# Fungsi untuk presentase ulasan
def percentage_page():
    st.title("Presentase Ulasan")

    # Pilihan brand
    brand = st.selectbox("Pilih Brand", ["KFC", "Richeese"])
    if st.button("Tampilkan Presentase"):
        if brand == "KFC":
            st.session_state.page = "presentase_kfc"
        elif brand == "Richeese":
            st.session_state.page = "presentase_richeese"

# Fungsi untuk perbandingan brand
def comparison_page():
    st.title("Perbandingan Brand")
    st.write("Fitur ini sedang dalam pengembangan...")

# Fungsi untuk review ulasan
def review_page():
    st.title("Review Ulasan")

    # Input ulasan baru
    review_text = st.text_input("Masukkan Ulasan Baru")
    if st.button("Cek Sentimen"):
        sentiment = check_sentiment(review_text)
        st.write(f"Sentimen ulasan: {sentiment}")

# Fungsi untuk presentase KFC
def presentase_kfc_page():
    st.title("Presentase Ulasan - KFC")
    image = Image.open("inti/presentasekfc.png")
    st.image(image, use_column_width=True)

    # Tombol kembali ke halaman utama
    if st.button("Kembali ke Halaman Utama"):
        st.session_state.page = "home"

# Fungsi untuk presentase Richeese
def presentase_richeese_page():
    st.title("Presentase Ulasan - Richeese")
    image = Image.open("inti/presentasericheese.png")
    st.image(image, use_column_width=True)

    # Tombol kembali ke halaman utama
    if st.button("Kembali ke Halaman Utama"):
        st.session_state.page = "home"

# Fungsi untuk menampilkan ulasan
def display_reviews():
    st.title("Tampilkan Ulasan")

    # Pilihan brand
    brand = st.selectbox("Pilih Brand", ["KFC", "Richeese"])

    # Pilihan sentimen
    sentiment = st.selectbox("Pilih Sentimen", ["Positif", "Negatif"])

    if st.button("Tampilkan Ulasan"):
        try:
            # Memilih file berdasarkan brand
            if brand == "KFC":
                df = pd.read_csv('inti/sentimen_KFC.csv')  # Path dataset KFC
            elif brand == "Richeese":
                df = pd.read_csv('inti/sentimenricheese.csv')  # Path dataset Richeese

            # Filter ulasan berdasarkan sentimen
            sentiment_mapping = {"Positif": "positif", "Negatif": "negatif"}
            selected_sentiment = sentiment_mapping.get(sentiment)

            if selected_sentiment is None:
                st.warning("Sentimen tidak valid.")
                return

            filtered_reviews = df[df["sentiment_label"] == selected_sentiment]

            # Menampilkan ulasan
            if not filtered_reviews.empty:
                st.write(f"Menampilkan ulasan {brand} dengan sentimen {sentiment}:")
                for idx, row in filtered_reviews.iterrows():
                    st.write(f"- {row['snippet']}")
            else:
                st.warning(f"Tidak ada ulasan {brand} dengan sentimen {sentiment}.")

        except FileNotFoundError as e:
            st.error(f"Error: File {e.filename} tidak ditemukan.")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {str(e)}")

    # Tombol Back
    if st.button("Kembali ke Halaman Utama"):
        st.session_state.page = "home"

# Fungsi untuk mengecek sentimen
def check_sentiment(review_text):
    if not review_text.strip():
        return "Masukkan ulasan terlebih dahulu!"
    
    # Membaca dataset sentimen
    sentimen_kfc = pd.read_csv('inti/kata_sentimen_kfc.csv')
    sentimen_richeese = pd.read_csv('inti/kata_sentimen_richeese.csv')

    # Gabungkan kata positif dan negatif
    sentimen_dict = {
        "positif": set(sentimen_kfc[sentimen_kfc['label'] == 'positif']['kata'].tolist() +
                       sentimen_richeese[sentimen_richeese['label'] == 'positif']['kata'].tolist()),
        "negatif": set(sentimen_kfc[sentimen_kfc['label'] == 'negatif']['kata'].tolist() +
                       sentimen_richeese[sentimen_richeese['label'] == 'negatif']['kata'].tolist())
    }

    words = review_text.lower().split()
    positif_count = sum(1 for word in words if word in sentimen_dict['positif'])
    negatif_count = sum(1 for word in words if word in sentimen_dict['negatif'])

    if positif_count > negatif_count:
        return "positif"
    elif negatif_count > positif_count:
        return "negatif"
    else:
        return "netral"

# Routing halaman berdasarkan session state
if "page" not in st.session_state:
    st.session_state.page = "first"

if st.session_state.page == "first":
    first_page()
elif st.session_state.page == "home":
    home_page()
elif st.session_state.page == "percentage":
    percentage_page()
elif st.session_state.page == "comparison":
    comparison_page()
elif st.session_state.page == "review":
    review_page()
elif st.session_state.page == "presentase_kfc":
    presentase_kfc_page()
elif st.session_state.page == "presentase_richeese":
    presentase_richeese_page()
elif st.session_state.page == "display_reviews":
    display_reviews()
