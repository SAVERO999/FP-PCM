import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi
from skimage import io, color, img_as_ubyte
from scipy.ndimage import convolve

def process_image(image):
    # Potong gambar dari kolom 0 hingga kolom 580
    img_cut = image[:, 0:580]
    
    # Transformasi dari RGB ke Grayscale
    img_gray = color.rgb2gray(img_cut)
    img_gray = img_as_ubyte(img_gray)  # Convert tipe data ke uint8
    
    # Inisialisasi kernel atau weights (contoh kernel blur)
    weights = np.full((3, 3), 1/9)
    
    # Terapkan kernel ke gambar (convolve)
    img_convolved = convolve(img_gray, weights)
    
    return img_cut, img_gray, img_convolved, weights

# Inisialisasi variabel global untuk gambar
if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None

with st.sidebar:
    selected = option_menu("FP", ["Home", "Encyclopedia", "open data", "histogram"], default_index=0, key="menu1")

if selected == "Home":
    st.title('Project FP Kelompok 2')
    st.subheader("Anggota kelompok")
    
    # Menampilkan anggota kelompok dengan gambar
    col1, col2 = st.columns(2)
    with col1:
        st.image("IMG_2267.jpg", use_column_width=True, width=150)
        st.markdown("<p style='color:black; text-align:center;'>Reynard Prastya Savero<br>5023211042</p>", unsafe_allow_html=True)
    
        st.image("IMG_2104.JPEG", use_column_width=True, width=150)
        st.markdown("<p style='color:black; text-align:center;'>Francisca Cindy Meilia Apsari<br>5023211021</p>", unsafe_allow_html=True)
    
    with col2:
        st.image("file.png", use_column_width=True, width=150)
        st.markdown("<p style='color:black; text-align:center;'>Mavelyn Clarissa Tania<br>5023211004</p>", unsafe_allow_html=True)
    
        st.image("05keratosisPilaris020204-transformed.jpeg", use_column_width=True, width=150)
        st.markdown("<p style='color:black; text-align:center;'>Narika Shinta<br>5023211057</p>", unsafe_allow_html=True)

elif selected == "Encyclopedia":
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

elif selected == "open data":
    st.markdown("<h1 style='text-align: center; color: green;'>📂 Open Data</h1>", unsafe_allow_html=True)

    # Upload gambar
    uploaded_file = st.file_uploader("Upload Gambar", type=["jpeg", "jpg", "png"])

    if uploaded_file is not None:
        # Simpan file di session_state agar bisa diakses di bagian lain
        st.session_state.uploaded_image = io.imread(uploaded_file)

        # Proses gambar: potong, ubah ke grayscale, dan konvolusi
        img_cut, img_gray, img_convolved, weights = process_image(st.session_state.uploaded_image)
        
        # Menampilkan gambar asli yang telah dipotong dan diubah menjadi grayscale
        st.markdown("<h3 style='text-align: center;'>Gambar Grayscale dari Gambar Terpotong (0:580)</h3>", unsafe_allow_html=True)
        st.image(img_gray, caption="Gambar Grayscale setelah Pemotongan", use_column_width=True, clamp=True)
        st.write("Tipe gambar grayscale:", img_gray.dtype)
        st.write("Ukuran gambar grayscale:", img_gray.shape)
        
        # Menampilkan kernel yang digunakan
        st.write("Kernel yang digunakan:", weights)

elif selected == "histogram":
    st.markdown("<h1 style='text-align: center; color: blue;'>📊 Histogram</h1>", unsafe_allow_html=True)

    if st.session_state.uploaded_image is not None:
        # Menghitung histogram untuk gambar grayscale dari potongan
        _, img_gray, _, _ = process_image(st.session_state.uploaded_image)
        histogram = ndi.histogram(img_gray, min=0, max=255, bins=256)
        
        # Plot histogram
        fig, ax = plt.subplots()
        ax.plot(histogram)
        ax.set_xlabel('Gray Value')
        ax.set_ylabel('Number of Pixels')
        ax.set_title('Histogram of Gray Values (Gambar Terpotong)')
        st.pyplot(fig)  # Menampilkan histogram di Streamlit
