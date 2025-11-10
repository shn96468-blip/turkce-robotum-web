# turkce_robotum.py - Streamlit Web Uygulaması Versiyonu
import streamlit as st
import pandas as pd

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="TR Türkçe Robotum",
    layout="wide"
)

# --- KONULAR SÖZLÜĞÜ (Konu veri tabanınız) ---
KONULAR = {
    "fiiller": "Fiiller, varlıkların yaptığı işi, hareketi, durumu veya oluşu anlatan sözcüklerdir. Kip ve kişi ekleri alırlar.",
    "zarflar": "Zarflar, fiilleri, fiilimsileri, sıfatları veya kendi türünden sözcükleri (zarfları) anlam yönünden etkileyen sözcüklerdir.",
    "anlatım bozuklukları": "Cümlelerin anlam, yapı veya mantık açısından tutarsız olmasıdır. Gereksiz sözcük, mantık hatası veya tamlama hatası gibi nedenlerle ortaya çıkar.",
    "yazım kuralları": "Kelimelerin doğru yazılışını, kısaltmaların kullanımını ve noktalama işaretlerinin doğru yerleştirilmesini kapsar.",
    "noktalama işaretleri": "Cümlelerin anlamını netleştirmek, vurguyu belirlemek ve duraklama yerlerini göstermek için kullanılır.",
    "metin türleri": "Olay, düşünce veya bilgi aktarma amaçlarına göre ayrılan yazı biçimleridir (öyküleyici, bilgilendirici, betimleyici vb.)."
}

# --- YARDIMCI FONKSİYONLAR ---
def konuyu_bul(arama_terimi):
    # Arama terimini küçük harfe çevir
    arama_terimi = arama_terimi.lower().strip()
    
    if arama_terimi in KONULAR:
        return KONULAR[arama_terimi]
    else:
        # Yakın eşleşme yoksa
        return "Üzgünüm, aradığınız konuyu tam olarak bulamadım. Lütfen listenin sağ tarafındaki konuları deneyin."

# --- YÖNETİCİ GİRİŞİ KONTROLÜ (Çoklu Sayfa Sistemi) ---
# URL'deki ?p=admin_panel parametresini kontrol et
query_params = st.query_params
if "p" in query_params and query_params["p"] == "admin_panel":
    import admin_panel 
    # admin_panel.py dosyasını yükler ve ana akışı durdurur
    st.stop()

# --- ANA ROBOT EKRANI ---
st.title("🇹🇷 TR Türkçe Robotum: Konu Anlatım Asistanı")
st.markdown("Merhaba! Hangi konularda bilgi istersin? (Örn: **fiiller**, **zarflar**, **anlatım bozuklukları**)")

konu_adi = st.text_input("Konu Adını Giriniz:")

# Yanıt düğmesi
if st.button("Konu Anlatımını Başlat"):
    if konu_adi:
        konu_icerigi = konuyu_bul(konu_adi)
        
        # Hata vermeyen konuşma ve yazılı yanıt
        if konu_icerigi and "Üzgünüm" not in konu_icerigi:
            st.success(f"İşte '{konu_adi.upper()}' konusu ile ilgili bilmen gerekenler:")
            st.markdown(konu_icerigi)

            # --- KONUŞMA ÖZELLİĞİ (Web için uygun) ---
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
            # ---------------------------------------------

        elif "Üzgünüm" in konu_icerigi:
            st.warning(konu_icerigi)
        
        else:
            st.error("Lütfen bir konu adı giriniz.")
    else:
        st.error("Lütfen bir konu adı giriniz.")

# --- KENAR ÇUBUĞU VE ALT BÖLÜM ---
st.sidebar.title("Kullanılabilir Konular")
st.sidebar.write(", ".join(KONULAR.keys()).replace(",", " •"))
st.sidebar.markdown("---")
st.sidebar.caption("Bu Uygulama **Yusuf Efe Şahin** Tarafından Geliştirilmiştir.")
st.sidebar.markdown("---")
st.sidebar.markdown("[🛡️ Yönetici Girişi](?p=admin_panel)")

