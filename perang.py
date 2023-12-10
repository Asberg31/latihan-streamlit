import streamlit as st
from streamlit_folium import folium_static
import folium

def main():
    st.title("Peta Posisi Pasukan")

    # Membuat peta
    m = folium.Map(location=[-4.2692, 138.0804], zoom_start=8)

    # Menambahkan marker untuk setiap posisi pasukan dengan informasi tambahan
    folium.Marker(
        location=[-4.1234, 138.5678],
        popup=folium.Popup('Posisi Pasukan A<br>'
                           'Kondisi Geografis: Pegunungan<br>'
                           'Sumber Daya: Terbatas<br>'
                           'Ancaman: Rintangan alami<br>'
                           'Jaringan Komunikasi: Terbatas<br>'
                           'Pergerakan Pasukan: Melalui jalur timur', max_width=250),
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

    folium.Marker(
        location=[-4.5678, 138.1234],
        popup=folium.Popup('Posisi Pasukan B<br>'
                           'Kondisi Geografis: Dataran rendah<br>'
                           'Sumber Daya: Melimpah<br>'
                           'Ancaman: Sedikit<br>'
                           'Jaringan Komunikasi: Kuat<br>'
                           'Pergerakan Pasukan: Melalui jalur utara', max_width=250),
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

    folium.Marker(
        location=[-4.546759, 136.883721],
        popup=folium.Popup('Posisi Pasukan B<br>'
                           'Kondisi Geografis: Dataran rendah<br>'
                           'Sumber Daya: Melimpah<br>'
                           'Ancaman: Sedikit<br>'
                           'Jaringan Komunikasi: Kuat<br>'
                           'Pergerakan Pasukan: Melalui jalur utara', max_width=250),
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

    # Menampilkan peta di Streamlit menggunakan streamlit-folium
    folium_static(m)

if __name__ == '__main__':
    main()
