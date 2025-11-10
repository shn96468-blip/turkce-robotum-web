# admin_panel.py
# admin_panel.py

import streamlit as st

st.set_page_config(page_title="Yönetici Paneli")

# Varsayılan (default) kullanıcı adı ve şifre
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "123" 

# Yönetici oturumu başlatılmadıysa
if "admin_logged_in" not in st.session_state:
    st.session_state["admin_logged_in"] = False

# --- YÖNETİCİ GİRİŞİ FORMU ---
if st.session_state["admin_logged_in"] == False:
    st.title("🛡️ Yönetici Girişi")

    # Form oluşturma
    with st.form("admin_login"):
        username = st.text_input("Kullanıcı Adı")
        password = st.text_input("Şifre", type="password")
        submitted = st.form_submit_button("Giriş Yap")

        if submitted:
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                st.success("Giriş başarılı! Yönetici Paneli açıldı.")
                st.session_state["admin_logged_in"] = True
                st.rerun() # Sayfayı yenile ve paneli göster
            else:
                st.error("Kullanıcı adı veya şifre hatalı.")

# --- YÖNETİCİ PANELİ İÇERİĞİ ---
if st.session_state["admin_logged_in"] == True:
    st.title("🛠️ Admin Panel")
    st.write("Burada konuları düzenleme, yeni konu ekleme gibi işlemler yapılabilir.")
    st.markdown("---")

    # Çıkış Düğmesi
    if st.button("Çıkış Yap"):
        st.session_state["admin_logged_in"] = False
        st.rerun()
