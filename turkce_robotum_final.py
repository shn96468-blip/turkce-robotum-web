import streamlit as st
import os

# --- 1. SABİT İÇERİKLER ---
GOOGLE_LINK_BASLANGIC = "https://www.google.com/search?q="
TONGUC_KANAL_LINK = "https://www.youtube.com/@tonguc7"
TESTCOZ_ONLINE_LINK = "https://www.testcoz.com/" 
GEMINI_CHAT_LINK = "https://gemini.google.com/" 


# --- 2. DERS VE KONU TANIMLARI (Sadece Türkçe) ---

SUBJECT_MAP = {
    "tr": {
        "title": "📝 Türkçe",
        "topics": ["Fiiller", "Zarflar", "Cümlede Anlam"],
    }
}


# --- 3. SAYFA AYARLARI ---

st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | Türkçe Robotum Final") 
st.markdown("## 👨‍🎓 YUSUF EFE ŞAHİN | 🤖 TÜRKÇE ROBOTUM") 
st.markdown("---")

# --- KRİTİK: İKİ ANA SÜTUN EKLEME (İçerik ve Tanıtım) ---
col_main, col_sidebar = st.columns([3, 1]) 


# --- 4. YÖNLENDİRME FONKSİYONU ---
def get_search_link(query, search_engine):
    """Verilen sorgu için arama linki oluşturur."""
    
    if search_engine == "testcoz_quiz":
        return TESTCOZ_ONLINE_LINK
    
    elif search_engine == "tonguc_kanal":
        return TONGUC_KANAL_LINK

    elif search_engine == "ai_chat":
        return GEMINI_CHAT_LINK

    else: # Google araması (Hızlı Erişim için)
        search_query = f"{query} 7. Sınıf Konu Anlatımı"
        final_query = search_query.replace(' ', '+')
        return f"{GOOGLE_LINK_BASLANGIC}{final_query}"

# Yeni Yönlendirme Fonksiyonu (st.button için ZORUNLU)
def open_url(url):
    """Tarayıcıyı verilen URL'ye yönlendirir."""
    # st.button'a basınca link açmak için kullanılır.
    st.components.v1.html(f"<script>window.open('{url}', '_blank');</script>", height=0)


# --- 5. DERS İÇERİĞİ MANTIĞI ---
def render_subject_tab(tab_context, subject_key):
    subject_data = SUBJECT_MAP[subject_key]
    
    with tab_context:
        st.header(f"✨ {subject_data['title']} Dersi")
        
        # --- ANA BUTONLAR: st.button ile değiştirildi ---
        col_notes, col_quiz, col_video = st.columns(3)

        # A. DERS NOTLARI (GOOGLE LİNKİ)
        with col_notes:
            # st.link_button yerine st.button kullanılıyor
            if st.button("📝 Detaylı Ders Notlarını Bul", key=f"notes_{subject_key}"):
                open_url(get_search_link(subject_data['title'], "google"))
        
        # B. SORU ÇÖZME (TESTCOZ)
        with col_quiz:
            # st.link_button yerine st.button kullanılıyor
            if st.button("✅ Test Çöz - Yeni Nesil Sorular", key=f"quiz_{subject_key}"):
                open_url(get_search_link("", "testcoz_quiz"))
        
        # C. VİDEO İZLE (TONGUÇ KANAL)
        with col_video:
            # st.link_button yerine st.button kullanılıyor
            if st.button("📺 Tonguç Akademi 7. Sınıf Kanalı", key=f"tonguc_{subject_key}"):
                open_url(get_search_link("", "tonguc_kanal"))
        
        st.markdown("---")

        # --- YAPAY ZEKA BUTONU (st.button ile değiştirildi) ---
        if st.button("🧠 Yapay Zeka Soru Çözdüren Arkadaşı Aç", use_container_width=True, key=f"ai_friend_{subject_key}"):
            open_url(get_search_link("", "ai_chat"))

        st.markdown("---")
        
        # KONULARA GÖRE HIZLI ERİŞİM (GOOGLE ARAMA)
        st.subheader("Konulara Göre Hızlı Erişim (Google Arama)")
        
        cols_content = st.columns(3)
        
        for i, topic in enumerate(subject_data.get('topics', [])):
            col = cols_content[i % 3]
            google_link = get_search_link(topic, "google")
            
            with col:
                st.markdown(f"**📚 {topic}**")
                # Hızlı erişim linkleri de st.button ile değiştirildi
                if st.button("Notları Google'da Bul", key=f"topic_{subject_key}_{topic}_g"):
                    open_url(google_link)
                st.markdown("---")


# --- 6. DERS İÇERİĞİNİ ANA SÜTUNA YERLEŞTİR ---
with col_main: 
    render_subject_tab(st.container(), "tr")


# --- 7. YAN KISIM (TANITIM KARTI) İÇERİĞİ ---
with col_sidebar:
    st.markdown("### 🤖 Türkçe Robotum")
    st.info(f"""
        Merhaba, ben **Yusuf Efe Şahin**!
        
        Bu **Türkçe Robotum** uygulaması, 7. Sınıf öğrencilerine özel olarak **Türkçe Dersi** konularında yardımcı olmak amacıyla tasarlanmıştır.
        
        **YENİ:** Artık bir Yapay Zeka Soru Çözücü Arkadaşınız da var!
    """)
    st.markdown("---")
    st.markdown("_Geliştirici: Yusuf Efe Şahin_")
