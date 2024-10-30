import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from skimage import color, img_as_ubyte, io
import scipy.ndimage as ndi
from streamlit_option_menu import option_menu
import streamlit as st
from PIL import Image, ImageFilter



def resize_and_sharpen_image(image_path, width, height):
    image = Image.open(image_path)
    resized_image = image.resize((width, height), Image.LANCZOS)
    sharpened_image = resized_image.filter(ImageFilter.SHARPEN)
    return sharpened_image
# Fungsi untuk melakukan transformasi gambar dari RGB ke Grayscale dan inisialisasi kernel
def process_image(image):
    # Memotong gambar asli untuk menampilkan hanya sebagian
    img_cut = image[:, 0:580]
    
    # Transformasi dari RGB ke Grayscale
    img_gray = color.rgb2gray(img_cut)
    img_gray = img_as_ubyte(img_gray)  # Convert tipe data ke uint8
    
    # Inisialisasi kernel atau weights
    weights = np.full((3, 3), 1/9)
    
    return img_cut, img_gray, weights

# Inisialisasi variabel global untuk gambar
if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None

with st.sidebar:
    selected = option_menu("FP", ["Home", "Encyclopedia", "Pemrosesan dan Analisis Citra "], default_index=0, key="menu1")



if selected == "Home":
    st.title('Project FP Kelompok 2')
    st.subheader("Anggota kelompok")
    col1, col2 = st.columns(2)

    with col1:
        st.image("IMG_2267.jpg", caption="\nReynard Prastya Savero (5023211042)", use_column_width=True, width=150)
        st.image("Screenshot 2024-10-30 122841.png", caption="\nFrancisca Cindy Meilia Apsari (5023211021)", use_column_width=True, width=150)

    with col2:
        st.image("file.png", caption="\n Mavelyn Clarissa Tania (5023211004)", use_column_width=True, width=150)
        st.image("IMG_20240410_113029.jpg", caption="\n Narika Shinta (5023211057)", use_column_width=True, width=150)




# Konten untuk halaman "Encyclopedia"
if selected == "Encyclopedia":
    selected1 = st.sidebar.radio("", ["Penyakit", "Informasi"], index=0)
    
    if selected1 == 'Penyakit':
        st.markdown("<h1 style='text-align: center; color: red;'>🫀ENCYCLOPEDIA</h1>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Apa yang dimaksud Atopic Dermatitis?', key="button1"):
                new_title = '''<p style="font-family:Georgia; color:black; font-size: 20px; text-align: justify;">Dermatitis atopik adalah jenis eksim yang ditandai oleh peradangan kulit, sering disertai dengan kemerahan, kekeringan, dan kulit pecah-pecah. Kondisi ini bisa berlangsung dalam jangka waktu lama, bahkan bertahun-tahun. Umumnya, dermatitis atopik muncul pada area kulit seperti dahi, sekitar mata dan telinga, sisi leher, serta bagian dalam siku.</p>'''
                st.markdown(new_title, unsafe_allow_html=True)
        with col2:
            if st.button('Apa penyebab dari Atopic Dermatitis?', key="button2"):
                new_title1 = '''<p style="font-family:Georgia; color:black; font-size: 20px; text-align: Justify;">
                Penyebab atopic dermatitis meliputi beberapa faktor seperti:<br>
                1. Perubahan hormon<br>
                2. Alergi terhadap makanan, debu dan bulu hewan<br>
                3. Stres<br>
                4. Paparan udara yang dingin, kering, atau lembap
                </p>'''
                st.markdown(new_title1, unsafe_allow_html=True)

    elif selected1 == 'Informasi':
        st.markdown("<h1 style='text-align: center; color: blue;'>📖 Informasi</h1>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Gejala dari Atopic Dermatitis?', key="button3"):
                new_title = '''<p style="font-family:Georgia; color:black; font-size: 20px; text-align: justify;">
                1. Timbulnya ruam yang menonjol dan mengeluarkan cairan<br>
                2. Kulit yang kering dan bersisik.<br> 
                3. Kulit di telapak tangan atau area bawah mata tampak berkerut atau mengerut.<br> 
                4. Area kulit di sekitar mata terlihat lebih gelap.<br>
                5. Kulit pecah-pecah, mengelupas, hingga mengeluarkan darah.
                </p>'''
                st.markdown(new_title, unsafe_allow_html=True)
        with col2:
            if st.button('Video', key="button4"):
                content = """
                <iframe id='Video 1' width='400' height='315' src='https://www.youtube.com/embed/XE7sX_gzlS0' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
                """
                st.markdown(content, unsafe_allow_html=True)

# Konten untuk halaman "open data"
selected = st.sidebar.selectbox("Pilih Opsi", ["Pemrosesan dan Analisis Citra", "Opsi Lain"])

if selected == "Pemrosesan dan Analisis Citra":
        st.markdown("<h1 style='text-align: center; color: green;'>📂 Open Data</h1>", unsafe_allow_html=True)

        # Upload gambar
        uploaded_file = st.file_uploader("Upload Gambar", type=["jpeg", "jpg", "png"])

        if uploaded_file is not None:
            # Simpan file di session_state agar bisa diakses di bagian lain
            st.session_state.uploaded_image = skio.imread(uploaded_file)

            # Proses gambar: transformasi dari RGB ke grayscale
            img_cut, img_gray, weights = process_image(st.session_state.uploaded_image)

            # Menampilkan dua gambar yang dipotong: gambar asli dan hasil grayscale
            st.markdown("<h3 style='text-align: center;'>Gambar Asli </h3>", unsafe_allow_html=True)
            st.image(img_cut, caption="Gambar Asli", use_column_width=True)
            st.write("Tipe gambar asli :", img_cut.dtype)
            st.write("Ukuran gambar asli:", img_cut.shape)

            st.markdown("<h3 style='text-align: center;'>Gambar Grayscale </h3>", unsafe_allow_html=True)
            st.image(img_gray, caption="Gambar Grayscale ", use_column_width=True, clamp=True)
            st.write("Tipe gambar grayscale:", img_gray.dtype)
            st.write("Ukuran gambar grayscale:", img_gray.shape)

# Konten untuk halaman "histogram"
elif selected == "histogram":
    st.markdown("<h1 style='text-align: center; color: blue;'>📊 Histogram</h1>", unsafe_allow_html=True)

    if st.session_state.uploaded_image is not None:
        # Menghitung histogram untuk gambar grayscale
        img_cut, img_gray, _ = process_image(st.session_state.uploaded_image)
        
        histogram = ndi.histogram(img_gray, min=0, max=255, bins=256)
        
        # Plot histogram
        fig, ax = plt.subplots()
        ax.plot(histogram)
        ax.set_xlabel('Gray Value')
        ax.set_ylabel('Number of Pixels')
        ax.set_title('Histogram of Gray Values')

        st.pyplot(fig)  # Menampilkan histogram di Streamlit
