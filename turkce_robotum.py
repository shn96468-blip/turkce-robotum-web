# turkce_robotum.py - Streamlit Web Uygulaması Versiyonu

import streamlit as st
import difflib
from konular import konular # Bilgi bankasını buradan çekiyoruz.

# --- AYARLAR ---
st.set_page_config(
    page_title="Türkçe Robotum",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CEVAP BULMA MANTIĞI ---
def cevap_bul(soru):
    temiz_soru = soru.lower().strip()
    en_iyi_eslesme = ""
    en_yuksek_benzerlik = 0.6 

    for konu_anahtari in konular.keys():
        benzerlik = difflib.SequenceMatcher(None, konu_anahtari, temiz_soru).ratio()
        if benzerlik > en_yuksek_benzerlik:
            en_yuksek_benzerlik = benzerlik
            en_iyi_eslesme = konu_anahtari

    if en_iyi_eslesme:
        return konular[en_iyi_eslesme]
    else:
        return "Üzgünüm, aradığınız konuyu bulamadım. Lütfen 12 ünite içinden bir konunun adını deneyiniz. Örn: fiiller, zarflar"

# --- WEB ARAYÜZÜ ---

st.title("🇹🇷 Türkçe Robotum: Konu Anlatım Asistanı")
st.markdown("Merhaba! Hangi konuyu öğrenmek istersin? (Örn: **fiiller**, **zarflar**, **anlatım bozuklukları**)")

soru = st.text_input("Konu Adını Giriniz:", key="user_input")

if soru:
    cevap = cevap_bul(soru)
    st.info(cevap)

# --- ALT BÖLÜM ---
st.sidebar.title("Kullanılabilir Konular")
st.sidebar.markdown(
    """
    * Fiiller, Kip ve Kişi Ekleri
    * Sözcükte Anlam, Söz Sanatları
    * Fiilde Yapı, Ek Fiiller
    * Zarflar, Zarf Türleri
    * Parçada Anlam, Ana Düşünce
    * Deyimler ve Atasözleri
    * Anlatım Bozuklukları
    * Yazım Kuralları, Noktalama İşaretleri
    * Metin Türleri
    """
)
st.sidebar.info("Robot, aradığınız konuya en yakın eşleşmeyi bulacaktır.")

st.sidebar.caption("Bu Uygulama **Yusuf Efe  Şahin ** Tarafından Geliştirilmiştir.")

st.sidebar.markdown("---")
st.sidebar.markdown("[🛡️ Yönetici Girişi](?p=admin_panel)")

# Tarayıcının konuşma özelliğini kullanmak için gerekli JavaScript kodu
if konu_icerigi:
    st.components.v1.html(f"""
        <script>
            const text = `{konu_icerigi.replace("`", "")}`; 
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'tr-TR';
            utterance.pitch = 1.0; 
            utterance.rate = 1.0; 
            speechSynthesis.speak(utterance);
        </script>
    """, height=0)
