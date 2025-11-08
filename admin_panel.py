# admin_panel.py

import streamlit as st

st.set_page_config(page_title="Yönetici Paneli")

# Varsayılan (default) kullanıcı adı ve şifre
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "123" 

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

            # --- YÖNETİCİ PANELİ İÇERİĞİ ---
            st.header("Admin Panel")
            st.write("Burada konular.py dosyasını düzenleme, yeni konu ekleme gibi işlemler yapılabilir.")
            # Şu an için sadece bir not gösteriyoruz.
            # Gerçek dosya düzenleme işlemleri daha karmaşık olacaktır.

        else:
            st.error("Kullanıcı adı veya şifre hatalı.")

# Eğer kullanıcı çıkış yapmak isterse
if st.session_state.get("admin_logged_in"):
    if st.button("Çıkış Yap"):
        st.session_state["admin_logged_in"] = False
        st.rerun()
st.sidebar.markdown("---")
st.sidebar.markdown("[🛡️ Yönetici Girişi](?p=admin_panel)")