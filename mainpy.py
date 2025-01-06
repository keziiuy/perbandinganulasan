from tkinter import Frame, Label,Text, Button, Tk  
from tkinter import ttk 
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Scrollbar
import pandas as pd
from improve_sentiment_analysis import SentimentAnalyzer  

class MainClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Review Ulasan")
        self.root.geometry("1280x800+150+12")
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)
        self.file_path = "inti/sentimenricheese.csv"  # Path ke file CSV
        self.showReviewOptions()
        self.file_path = "inti/sentimenricheese.csv"  # Path dataset
        self.analyzer = SentimentAnalyzer()  # Inisialisasi model analisis sentimen
        self.analyzer.train(self.file_path)  # Latih model dengan dataset
        self.firstPage()


    def firstPage(self):
        # Frame utama halaman pertama
        self.mainframe = Frame(self.root, bg="white")
        self.mainframe.place(x=0, y=0, width=1280, height=800)

        # Menambahkan gambar latar belakang
        image = Image.open("inti/firstpage.png")  # Path gambar
        image = image.resize((1280, 800), Image.Resampling.LANCZOS)  # Resize gambar ke GUI
        self.img1 = ImageTk.PhotoImage(image)
        Label(self.mainframe, image=self.img1, bg="white").place(x=0, y=0)

        # Tombol Start
        self.start_button = Button(
            self.mainframe,
            text="START",
            font=("Poppins", 30, "bold"),
            bg="#fcd24f",  # Warna kuning agar menyatu dengan desain
            fg="white",  # Warna teks cokelat
            width=6,  # Lebar tombol
            height=1,  # Tinggi tombol
            border=0,
            cursor="hand2",
            activebackground="#FFC107",
            command=self.homePage,
        )
        # Tempatkan tombol di bawah tulisan "Richeese"
        self.start_button.place(x=850, y=570)  # Sesuaikan posisi dengan area kuning

    def homePage(self):
        # Frame utama halaman utama
        self.mainframe = Frame(self.root, bg="white")
        self.mainframe.place(x=0, y=0, width=1280, height=800)

        # Menambahkan gambar latar belakang
        image = Image.open("inti/homepage.png")  # Path gambar
        image = image.resize((1280, 800), Image.Resampling.LANCZOS)  # Resize gambar ke GUI
        self.bg_image = ImageTk.PhotoImage(image)
        Label(self.mainframe, image=self.bg_image, bg="white").place(x=0, y=0)

        # Tombol Presentase Ulasan
        self.percentage_button = Button(
            self.mainframe,
            text="Presentase Ulasan",
            font=("Poppins", 26, "bold"),
            bg="#fcd24f",
            fg="white",
            width=17,
            height=1,
            border=0,
            cursor="hand2",
            activebackground="#FFC107",
            command=self.showPercentageOptions
        )
        self.percentage_button.place(x=484, y=264)  # Sesuaikan posisi dengan label kuning

        # Tombol Perbandingan Brand
        self.comparison_button = Button(
            self.mainframe,
            text="Perbandingan Brand",
            font=("Poppins", 24, "bold"),
            bg="#fcd24f",
            fg="white",
            width=17,
            height=1,
            border=0,
            cursor="hand2",
            activebackground="#FFC107",
            command=self.perbandinganBrandPage
        )
        self.comparison_button.place(x=500, y=430)  # Sesuaikan posisi dengan label kuning
        

        # Tombol Review Ulasan
        self.review_button = Button(
            self.mainframe,
            text="Review Ulasan",
            font=("Poppins", 30, "bold"),
            bg="#fcd24f",
            fg="white",
            width=13,
            height=1,
            border=0,
            cursor="hand2",
            activebackground="#FFC107",
            command=self.showReviewOptions
        )
        self.review_button.place(x=505, y=580)  # Sesuaikan posisi dengan label kuning

    def showPercentageOptions(self):
    # Membuat style untuk combobox agar sesuai dengan desain
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "Custom.TCombobox",
            fieldbackground="#fcd24f",  # Warna latar belakang kuning
            background="#fcd24f",      # Warna latar belakang dropdown
            foreground="white",        # Warna teks
            font=("Poppins", 30, "bold"),      # Font teks
            padding=(10, 5),           # Padding internal untuk memperbesar combobox
        )
        style.map(
            "Custom.TCombobox",
            fieldbackground=[("readonly", "#fcd24f")],  # Warna latar saat readonly
            foreground=[("readonly", "white")]         # Warna teks saat readonly
        )

        # Frame untuk combobox Presentase Ulasan
        self.clearOptions()
        options = ["KFC", "RICHEESE"]
        self.percentage_combo = ttk.Combobox(
            self.mainframe,
            values=options,
            state="readonly",
            style="Custom.TCombobox",  # Terapkan style khusus
            width=50                   # Lebar combobox
        )
        self.percentage_combo.place(x=493, y=315)  # Sesuaikan posisi agar sejajar dengan tombol
        self.percentage_combo.set("Pilih Brand")
        self.percentage_combo.bind("<<ComboboxSelected>>", self.navigatePercentagePage)

    def navigatePercentagePage(self, event):
        if self.percentage_combo.get() == "KFC":
            self.presentaseKFCPage()
        elif self.percentage_combo.get() == "RICHEESE":
            self.presentaseRicheesePage()

    def presentaseKFCPage(self):
        # Frame utama halaman Presentase KFC
        self.mainframe = Frame(self.root, bg="white")
        self.mainframe.place(x=0, y=0, width=1280, height=800)

        # Menambahkan gambar latar belakang
        image = Image.open("inti/presentasekfc.png")  # Path gambar
        image = image.resize((1280, 800), Image.Resampling.LANCZOS)  # Resize gambar ke GUI
        self.bg_image = ImageTk.PhotoImage(image)
        Label(self.mainframe, image=self.bg_image, bg="white").place(x=0, y=0)
    
        # Tombol Back untuk kembali ke homepage
        self.back_button = Button(
            self.mainframe,
            text="Back",
            font=("Poppins", 16, "bold"),
            bg="#f7d08d",
            fg="white",
            width=5,
            height=0,
            border=0,
            cursor="hand2",
            activebackground="#FFC107",
            command=self.homePage
        )
        self.back_button.place(x=1085, y=20)  # Posisi tombol back di pojok kiri atas

    def presentaseRicheesePage(self):
        # Frame utama halaman Presentase Richeese
        self.mainframe = Frame(self.root, bg="white")
        self.mainframe.place(x=0, y=0, width=1280, height=800)

        # Menambahkan gambar latar belakang
        image = Image.open("inti/presentasericheese.png")  # Path gambar
        image = image.resize((1280, 800), Image.Resampling.LANCZOS)  # Resize gambar ke GUI
        self.bg_image = ImageTk.PhotoImage(image)
        Label(self.mainframe, image=self.bg_image, bg="white").place(x=0, y=0)
    
        # Tombol Back untuk kembali ke homepage
        self.back_button = Button(
            self.mainframe,
            text="Back",
            font=("Poppins", 16, "bold"),
            bg="#f7d08d",
            fg="white",
            width=5,
            height=0,
            border=0,
            cursor="hand2",
            activebackground="#FFC107",
            command=self.homePage
        )
        self.back_button.place(x=1085, y=20)  # Posisi tombol back di pojok kiri atas

    def perbandinganBrandPage(self):
    # Frame utama halaman Perbandingan Brand
        self.mainframe = Frame(self.root, bg="white")
        self.mainframe.place(x=0, y=0, width=1280, height=800)

        # Menambahkan gambar latar belakang
        image = Image.open("inti/perbandinganbrand.png")  # Path gambar latar
        image = image.resize((1280, 800), Image.Resampling.LANCZOS)  # Resize gambar ke GUI
        self.bg_image = ImageTk.PhotoImage(image)
        Label(self.mainframe, image=self.bg_image, bg="white").place(x=0, y=0)
    
        # Tombol Next untuk menuju halaman Overal
        self.next_button = Button(
            self.mainframe,
            text="Next",
            font=("Poppins", 16, "bold"),
            bg="#fcd24f",
            fg="white",
            width=5,
            height=0,
            border=0,
            cursor="hand2",
            activebackground="#FFC107",
            command=self.overalPage
        )
        self.next_button.place(x=1085, y=20)  # Posisi tombol di pojok kanan atas

    def overalPage(self):
        # Frame utama halaman Overal
        self.mainframe = Frame(self.root, bg="white")
        self.mainframe.place(x=0, y=0, width=1280, height=800)

        # Menambahkan gambar latar belakang
        image = Image.open("inti/overall.png")  # Path gambar latar
        image = image.resize((1280, 800), Image.Resampling.LANCZOS)  # Resize gambar ke GUI
        self.bg_image = ImageTk.PhotoImage(image)
        Label(self.mainframe, image=self.bg_image, bg="white").place(x=0, y=0)

        # Tombol Back untuk kembali ke Homepage
        self.back_button = Button(
            self.mainframe,
            text="Back",
            font=("Poppins", 16, "bold"),
            bg="#fcd24f",
            fg="white",
            width=5,
            height=0,
            border=0,
            cursor="hand2",
            activebackground="#FFC107",
            command=self.homePage
        )
        self.back_button.place(x=1085, y=20)  # Posisi tombol di pojok kiri ata

    def showReviewOptions(self):
        # Bersihkan frame utama
        for widget in self.root.winfo_children():
            widget.destroy()

        # Label pilihan jenis ulasan
        tk.Label(self.root, text="Pilih Jenis Ulasan:", font=("Poppins", 20, "bold"), bg="white").pack(pady=10)
        self.mainframe = tk.Frame(self.root, bg="white")
        self.mainframe.place(x=0, y=0, width=1280, height=800)

        # Menambahkan gambar latar belakang
        image = Image.open("inti/ceksentimen.png")  # Path gambar latar
        image = image.resize((1280, 800), Image.Resampling.LANCZOS)  # Resize gambar ke GUI
        self.bg_image = ImageTk.PhotoImage(image)
        tk.Label(self.mainframe, image=self.bg_image, bg="white").place(x=0, y=0)

        self.combobox_brand = ttk.Combobox(
            self.mainframe, 
            values=["KFC", "Richeese"], 
            font=("Poppins", 14), 
            state="readonly"
        )
        self.combobox_brand.place(x=450, y=70)
        self.combobox_brand.set("Pilih Brand")

        # Membuat ComboBox untuk memilih jenis ulasan
        self.combobox_sentiment = ttk.Combobox(
            self.mainframe, 
            values=["Positif", "Negatif"], 
            font=("Poppins", 14), 
            state="readonly"
        )
        self.combobox_sentiment.place(x=550, y=70)
        self.combobox_sentiment.set("Pilih Sentimen")

        # Tombol untuk memproses pilihan
        self.process_button = tk.Button(
            self.mainframe,
            text="Tampilkan Ulasan",
            font=("Poppins", 14),
            bg='#fcd24f',
            fg="white",
            border=0,
            command=self.showSelectedReviews
        )
        self.process_button.place(x=552, y=145)

        # Label untuk input ulasan baru
        tk.Label(self.root, text="Masukkan Ulasan Baru:", font=("Poppins", 20, "bold"), bg="#9f0000").place(x=490, y=220)

        # Entry untuk input ulasan baru
        self.new_review_entry = ttk.Entry(self.root, font=("Poppins", 16), width=50)
        self.new_review_entry.place(x=330, y=287)
        self.new_review_entry.configure(background= '#fcd24f')

        # Tombol untuk mengecek sentimen ulasan baru
        tk.Button(self.root, text="Cek Sentimen", font=("Poppins", 14), background='#fcd24f', border=0, command=self.checkSentiment).place(x=565, y=360)

        # Membuat Frame untuk menampung Text widget dan Scrollbar
        self.frame = tk.Frame(self.root, width=300, height=456)
        self.frame.place(x=230, y=490)

        # Membuat Scrollbar (Vertikal dan Horizontal)
        self.v_scroll = Scrollbar(self.frame, orient="vertical")
        self.v_scroll.pack(side="right", fill="y")
        self.h_scroll = Scrollbar(self.frame, orient="horizontal")
        self.h_scroll.pack(side="bottom", fill="x")

        # Membuat Text widget untuk menampilkan hasil ulasan
        self.result_text = tk.Text(self.frame, font=("Poppins", 16), bg="#fff3dd", fg="black", wrap="word", height=22, width=50, padx=10, pady=10, state='disabled', yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)
        self.result_text.pack(side="left", fill="both", expand=True)

        # Mengonfigurasi scrollbars
        self.v_scroll.config(command=self.result_text.yview)
        self.h_scroll.config(command=self.result_text.xview)

        self.label_ulasan = tk.Label(
                self.mainframe,
                text="",
                font=("Poppins", 12),
                wraplength=300,
                justify="center",
                bg="white",
                fg="black"
            )
        self.label_ulasan.pack(pady=20)

    def tampilkanUlasan(self):
        # Membaca pilihan ComboBox
        brand = self.combobox_brand.get()
        sentiment = self.combobox_sentiment.get()

        try:
            # Memilih file berdasarkan brand
            if brand == "KFC":
                df = pd.read_csv('inti/sentimen_KFC.csv')  # Ganti dengan nama file KFC Anda
            else: 
                brand == "Richeese"
                df = pd.read_csv('inti/sentimenricheese.csv')  # Ganti dengan nama file Richeese Anda
                return

            # Filter ulasan berdasarkan sentimen
            if sentiment == "Positif":
                filtered_reviews = df[df['sentiment_label'] == "positif"]  # Ganti kolom sesuai dataset
            elif sentiment == "Negatif":
                filtered_reviews = df[df['sentiment_label'] == "negatif"]  # Ganti kolom sesuai dataset
            else:
                self.label_ulasan.config(text="Pilih sentimen terlebih dahulu.")
                return

            # Menampilkan ulasan pertama jika ada
            if not filtered_reviews.empty:
                ulasan = filtered_reviews.iloc[0]['snippet']  # Ganti 'snippet' dengan nama kolom ulasan
                self.label_ulasan.config(text=ulasan)
            else:
                self.label_ulasan.config(text="Tidak ada ulasan dengan kriteria tersebut.")

        except FileNotFoundError as e:
            self.label_ulasan.config(text=f"Error: File {e.filename} tidak ditemukan.")
        except Exception as e:
            self.label_ulasan.config(text=f"Terjadi kesalahan: {str(e)}")

    def showSelectedReviews(self):
        brand = self.combobox_brand.get()
        sentiment = self.combobox_sentiment.get()

        # Validasi input brand dan sentimen
        if brand == "Pilih Brand" or sentiment == "Pilih Sentimen":
            print("Pilih brand dan sentimen terlebih dahulu.")
            return

        try:
            # Memilih file berdasarkan brand
            if brand == "Richeese":
                df = pd.read_csv('inti/sentimenricheese.csv')
            elif brand == "KFC":
                df = pd.read_csv('inti/sentimen_KFC.csv')
            else:
                print("Brand tidak valid.")
                return

            # Cocokkan kolom sentimen
            sentiment_mapping = {"Positif": "positif", "Negatif": "negatif"}
            selected_sentiment = sentiment_mapping.get(sentiment)

            if selected_sentiment is None:
                print("Sentimen tidak valid.")
                return

            # Filter data berdasarkan sentiment_label
            filtered_reviews = df[df["sentiment_label"] == selected_sentiment]

            # Bersihkan seluruh widget dari root untuk menampilkan halaman baru
            for widget in self.root.winfo_children():
                widget.destroy()

            # Frame untuk tata letak
            main_frame = Frame(self.root, bg="#fff")
            main_frame.pack(expand=True, fill="both", padx=10, pady=10)

            # Tambahkan tombol Back di atas sebelah kiri
            back_button = Button(
                main_frame,
                text="Back to Homepage",
                font=("Poppins", 14, "bold"),
                bg="#fcd24f",
                fg="white",
                border=0,
                cursor="hand2",
                command=self.homePage  # Kembali ke homepage
            )
            back_button.pack(anchor="nw", padx=10, pady=10)  # Posisi di atas kiri

            # Buat widget Text untuk menampilkan ulasan
            review_text = Text(
                main_frame,
                wrap="word",
                font=("Poppins", 12),
                bg="#f9f9f9",
                fg="#333",
                padx=10,
                pady=10
            )
            review_text.pack(expand=True, fill="both", padx=10, pady=10)

            # Tampilkan ulasan di Text widget
            if not filtered_reviews.empty:
                for idx, row in filtered_reviews.iterrows():
                    review_text.insert("end", f"- {row['snippet']}\n\n")
            else:
                review_text.insert("end", "Tidak ada ulasan yang sesuai dengan pilihan.")

            # Nonaktifkan Text widget untuk mencegah pengeditan
            review_text.config(state="disabled")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")


    def checkSentiment(self):
        review_text = self.new_review_entry.get()  # Ambil teks ulasan dari input pengguna

        if review_text.strip():  # Pastikan ulasan tidak kosong
            # Membaca file CSV
            try:
                sentimen_kfc = pd.read_csv('inti/kata_sentimen_kfc.csv')  # File CSV untuk sentimen KFC
                sentimen_richeese = pd.read_csv('inti/kata_sentimen_richeese.csv')  # File CSV untuk sentimen Richeese
                
                # Gabungkan semua kata sentimen dari kedua file
                sentimen_dict = {
                    "positif": set(sentimen_kfc[sentimen_kfc['label'] == 'positif']['kata'].tolist() + 
                                sentimen_richeese[sentimen_richeese['label'] == 'positif']['kata'].tolist()),
                    "negatif": set(sentimen_kfc[sentimen_kfc['label'] == 'negatif']['kata'].tolist() + 
                                sentimen_richeese[sentimen_richeese['label'] == 'negatif']['kata'].tolist())
                }
                
                # Periksa setiap kata dalam ulasan
                words = review_text.lower().split()
                positif_count = sum(1 for word in words if word in sentimen_dict['positif'])
                negatif_count = sum(1 for word in words if word in sentimen_dict['negatif'])
                
                # Tentukan sentimen berdasarkan jumlah kata positif dan negatif
                if positif_count > negatif_count:
                    sentiment = "positif"
                elif negatif_count > positif_count:
                    sentiment = "negatif"
                else:
                    sentiment = "netral"
                
                # Tampilkan hasil pada GUI
                self.result_text.config(state='normal')  # Aktifkan widget teks
                self.result_text.delete(1.0, tk.END)  # Hapus teks sebelumnya
                self.result_text.insert(tk.END, f"Sentimen ulasan: {sentiment}")  # Tampilkan hasil
                self.result_text.config(state='disabled')  # Nonaktifkan widget teks
            except FileNotFoundError as e:
                # Tangani jika file tidak ditemukan
                self.result_text.config(state='normal')
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, f"Error: {str(e)}")  # Tampilkan pesan error
                self.result_text.config(state='disabled')
        else:
            # Jika input kosong, tampilkan pesan error
            self.result_text.config(state='normal')
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Masukkan ulasan terlebih dahulu!")  # Pesan error
            self.result_text.config(state='disabled')

    def clearOptions(self):
            # Membersihkan combobox jika ada
            for widget in self.mainframe.winfo_children():
                if isinstance(widget, ttk.Combobox):
                    widget.destroy()

    
# Main Program
if __name__ == "__main__":
    root = Tk()  # Gunakan Tk dari tkinter
    app = MainClass(root)
    root.mainloop()




