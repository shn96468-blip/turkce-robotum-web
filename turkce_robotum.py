import streamlit as st
import pandas as pd

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="TR/ENG İki Dilli Robotum (Nihai ve Kapsamlı)",
    layout="wide"
)

# 🇹🇷 TÜRKÇE KONULAR SÖZLÜĞÜ (Mevcut Tüm Konular)
KONULAR_TR = {
    # 1.1. Sözcükte Anlam
    "gerçek anlam": "⭐ **Gerçek Anlam (Kelimenin Temeli):** Bir kelimenin söylendiğinde akla gelen ilk ve temel anlamıdır. Kelimenin somut ve en masum halidir. Örnek: 'Gözüm **ağrıyor**' (Gerçek ağrı).",
    "mecaz anlam": "Sözcüğün gerçek anlamından tamamen uzaklaşarak kazandığı soyut anlamdır. Yeni, hayali bir anlam taşır. Örnek: 'Bu olay kalbimi **kırdı**' (Gerçek kırılma yok, üzülme var).",
    "terim anlam": "Bilim, sanat, spor gibi özel alanlara ait kavramları karşılayan ve sadece o alanda kullanılan kelimelerdir. Örnek: 'Matematikte **açı**', 'Tiyatroda **perde**'.",
    "eş ve yakın anlamlı kelimeler": "Yazılışları farklı, anlamları aynı olanlar **(Eş Anlamlı: Kırmızı-Al)** ve tam olarak aynı olmasa da birbirinin yerine geçebilenler **(Yakın Anlamlı: Basmak-Çiğnemek)**.",
    "zıt karşıt anlamlı sözcükler": "Anlamca birbirinin tam tersi olan kelimelerdir. Örnek: '**İyi** - **Kötü**'.",
    "eş sesli sesteş sözcükler": "Yazılışları ve okunuşları aynı, anlamları tamamen farklı olan kelimelerdir. Örnek: '**Yüz**' (surat) ve '**yüzmek**' (eylem).",
    "deyimler": "Genellikle mecaz anlamlı, kalıplaşmış ve bir durumu daha etkileyici anlatmayı amaçlayan söz gruplarıdır. **Öğüt vermez.**",
    "atasözleri": "Uzun gözlemler sonucu oluşmuş, genellikle toplumun ortak deneyimini yansıtan ve **öğüt/kural bildiren** kalıplaşmış özlü cümlelerdir.",

    # 1.2. Cümlede Anlam
    "neden sonuç cümleleri": "Bir eylemin hangi sebeple (nedenle) yapıldığını bildiren cümlelerdir. **Kesinleşmiş bir sebep** vardır.",
    "amaç sonuç cümleleri": "Bir eylemin hangi **amaca ulaşmak için** yapıldığını bildiren cümlelerdir. Amaç henüz gerçekleşmemiştir.",
    "koşul sonuç cümleleri": "Bir eylemin gerçekleşmesinin bir şarta (koşula) bağlı olduğunu bildiren cümlelerdir.",
    "karşılaştırma cümleleri": "Birden fazla varlık arasındaki benzerlik ya da farklılıkları ortaya koyan cümlelerdir.",
    "öznel yargılı cümleler": "Kişiden kişiye değişen, **kişisel görüş** içeren ve kanıtlanamayan yargılardır.",
    "nesnel yargılı cümleler": "Doğruluğu herkes tarafından kabul edilen, **kanıtlanabilir** ve kişisel görüş içermeyen yargılardır.",
    "örtülü anlam": "Cümlede açıkça söylenmeyen ancak cümlenin tamamından çıkarılabilen, üstü kapalı ikinci bir anlamdır.",
    "geçiş ve bağlantı ifadeleri": "Cümleler arası anlam bütünlüğünü sağlayan, **düşüncenin yönünü değiştiren** veya **destekleyen** sözcüklerdir.",
    "cümlede anlam ilişkileri": "Cümlelerin Eş, Yakın ve Zıt Anlam taşıma durumlarıdır.",
    "cümle yorumlama": "**Cümlenin Konusu, Ana Fikri, Çıkarılabilecek / Çıkarılabilecek Yargılar** gibi tüm becerileri kapsar.",

    # 1.3. Parçada Anlam
    "anlatım biçimleri": "**Betimleme** (Fotoğraf çekme), **Öyküleme** (Film çekme), **Açıklama** (Bilgi verme), **Tartışma** (Fikir savunma) yöntemleridir.",
    "düşünceyi geliştirme yolları": "**Tanımlama**, **Karşılaştırma**, **Örnekleme**, **Tanık Gösterme**, **Benzetme** ve **Sayısal Verilerden Yararlanma** yöntemleridir.",
    "anlatıcı türleri": "**Birinci Kişi Ağzıyla Anlatım** ve **Üçüncü Kişi Ağzıyla Anlatım** olarak ikiye ayrılır.",
    "paragrafın anlam yönü": "**Ana Düşünce**, **Konu**, **Başlık**, **Anahtar Kelimeler** gibi metnin içeriğiyle ilgili tüm unsurları kapsar.",
    "paragrafın yapı yönü": "**Giriş**, **Gelişme** ve **Sonuç** bölümlerinin düzenlenmesi, **Akışı Bozan Cümleyi** bulma gibi yapısal öğeleri kapsar.",
    "tablo ve grafik inceleme": "Verilerin analiz edilerek yorumlanmasıdır.",
    "görsel yorumlama": "Verilen bir resim üzerinden çıkarım yapma becerisidir.",

    # 2. Yazım Bilgisi
    "yazım imla kuralları": "Kelimelerin doğru yazılışını (Büyük Harf, Sayı, Birleşik Kelime Yazımı) ve Bağlaç/Eklerin Yazımı'nı kapsar.",
    "noktalama işaretleri": "**Nokta**, **Virgül**, **İki Nokta**, **Noktalı Virgül**, **Üç Nokta**, **Soru İşareti** gibi anlamı netleştiren tüm simgelerdir.",

    # 3. Dil Bilgisi
    "fiiller": "🚀 **Fiiller:** İş, oluş, hareket bildiren sözcüklerdir.",
    "anlamlarına göre fiiller": "**İş (Kılış)**, **Durum**, **Oluş** fiilleridir.",
    "yapılarına göre fiiller": "**Basit Fiil**, **Türemiş Fiil**, **Birleşik Fiil** fiilleridir.",
    "ek fiil": "İsim soylu sözcükleri yüklem yapan veya basit zamanlı fiili birleşik zamanlı fiil yapan ektir.",
    "ek eylem": "Ek fiilin diğer adıdır.",
    "birleşik zamanlı fiiller": "Basit zamanlı bir fiilin ek fiil alarak ikinci bir kip eki kazanmasıdır.",
    "fiil çekimi": "Fiillerde **Kip, Kişi, Olumsuzluk ve Soru** eklerinin kullanılmasıdır.",
    "fiillerde anlam kayması": "Bir kipin (zamanın) başka bir kipin yerine kullanılmasıdır.",
    "zarflar": "Fiilleri, fiilimsileri, sıfatları veya kendi türünden sözcükleri etkileyen sözcüklerdir.",
    "anlatım bozuklukları": "Cümlelerin anlam veya yapı bakımından tutarsız olmasıdır.",
    
    # 4. Edebi Türler ve Söz Sanatları
    "söz sanatları": "**Abartma**, **Benzetme**, **Kişileştirme**, **Konuşturma** ve **Karşıtlık** gibi sanatlardır.",
    "yazı metin türleri": "**Söyleşi**, **Biyografi**, **Otobiyografi**, **Günlük** ve **Mektup** gibi metinlerin amaçlarına göre ayrıldığı biçimlerdir."
}

# 🇬🇧 İNGİLİZCE KONULAR SÖZLÜĞÜ (2. Sınıftan 12. Sınıfa Temel Konular)
KONULAR_ENG = {
    # Temel Gramer (2. - 5. Sınıflar)
    "to be": "⭐ **To Be (am, is, are):** İngilizcede 'olmak' fiilidir ve isim cümlelerinin olmazsa olmazıdır. Örn: 'I **am** happy.'",
    "simple present tense": "Geniş Zaman (Yaparım). Düzenli yapılan eylemleri ve genel gerçekleri anlatır. Örn: 'She **goes** to school every day.'",
    "present continuous tense": "Şimdiki Zaman (Yapıyorum). Şu anda olan, devam eden eylemleri anlatır. Örn: 'I **am reading** a book now.'",
    "simple past tense": "Geçmiş Zaman (Yaptım). Geçmişte başlayıp bitmiş olayları anlatır. Fiillerin 2. halleri (V2) kullanılır. Örn: 'He **visited** Paris last year.'",
    "adjectives and adverbs": "Sıfatlar (isimleri niteler) ve Zarflar (fiilleri niteler). Sıfatlara -ly eklenerek zarf yapılabilir (quick → quickly).",
    
    # Ortaokul ve Lise Konuları (6. - 12. Sınıflar)
    "modals": "Can, Must, Should gibi yeterlilik, zorunluluk, tavsiye bildiren yardımcı fiillerdir. Örn: 'You **should** study hard.'",
    "future tense": "Gelecek Zaman (Yapacağım). Will veya Going To ile yapılır. Will daha genel, Going To daha kesin planları belirtir.",
    "present perfect tense": "Yakın Geçmiş Zaman (Yaptım/Bulundum). Geçmişte başlayıp etkisi devam eden veya zamanı belli olmayan eylemler için kullanılır. (Have/Has + V3).",
    "conditional sentences": "Koşul Cümleleri (If Clauses). Type 0, 1, 2, 3 gibi türleri vardır. Şart ve sonuç bildirirler. Örn: 'If I study, I will pass.'",
    "comparatives and superlatives": "Sıfatların karşılaştırma (bigger, more expensive) ve en üstünlük (the biggest, the most expensive) dereceleri.",
    "regular and irregular verbs": "Düzenli (ed alan) ve Düzensiz (şekil değiştiren) fiillerin geçmiş zaman ve Perfect Tense'lerde kullanımı.",
    
    # Ünite Örnekleri (8. Sınıf)
    "friendship": "Arkadaşlık, davet etme ve kabul/reddetme ifadeleri ile ilgili kelime ve kalıplar.",
    "teen life": "Gençlik hayatı, hobiler ve günlük aktivitelerle ilgili ifadeler.",
    "tourism": "Turizm, seyahat, yerler ve tatil aktiviteleriyle ilgili ifadeler.",
}


# --- YARDIMCI FONKSİYONLAR ---
def konuyu_bul(arama_terimi):
    arama_terimi = arama_terimi.lower().strip()
    
    # 1. Önce Türkçe Sözlüğü Kontrol Et
    if arama_terimi in KONULAR_TR:
        return f"🇹🇷 TÜRKÇE KONU ANLATIMI:\n{KONULAR_TR[arama_terimi]}"
    
    # 2. Sonra İngilizce Sözlüğü Kontrol Et
    elif arama_terimi in KONULAR_ENG:
        return f"🇬🇧 İNGİLİZCE KONU ANLATIMI:\n{KONULAR_ENG[arama_terimi]}"
    
    # 3. Bulunamadı
    else:
        return "Üzgünüm, aradığınız konuyu tam olarak ne Türkçe ne de İngilizce sözlükte bulabildim. Lütfen tam adını girin (Örn: 'gerçek anlam' veya 'simple present tense')."

def soru_cozumu_yap(arama_termi):
    arama_termi = arama_termi.lower().strip()
    
    # Türkçe Kapsam
    if "fiil" in arama_termi or "zarf" in arama_termi or "anlatım" in arama_termi:
        return "❓ **Örnek Soru Çözümü (Türkçe):** Sorunuzdaki eylemin yapısını, zamanını veya zarfın türünü belirleyerek doğru cevaba ulaşırız. **Cevap:** Çözüm için Türkçe Dil Bilgisi kuralları kullanıldı."
    
    # İngilizce Kapsam
    elif "tense" in arama_termi or "modal" in arama_termi or "if" in arama_termi or "to be" in arama_termi:
        return "❓ **Örnek Soru Çözümü (İngilizce):** İngilizcede Tense soruları için öncelikle zaman zarfına (now, yesterday, every day) bakmalıyız. Bu zarf, doğru zaman (Tense) yapısını belirler. **Cevap:** Doğru zaman yapısı (Tense) kullanıldı."
    
    else:
        return "Şu an sadece **Türkçe Fiiller/Zarflar** veya **İngilizce Tense/Modal** konularıyla ilgili örnek soruları çözebilirim."

# --- YÖNETİCİ GİRİŞİ KONTROLÜ ---
query_params = st.query_params
if "p" in query_params and query_params["p"] == "admin_panel":
    import admin_panel 
    st.stop()

# --- ANA ROBOT EKRANI ---
st.title("🇹🇷🇬🇧 TR/ENG İki Dilli Robotum: Konu Anlatım ve Soru Çözüm Asistanı")
st.markdown("Merhaba! Hangi konuda bilgi istersin (Türkçe veya İngilizce) ya da hangi konuyla ilgili **örnek soru çözümü** yapmamı istersin? 😉")

# Mod Seçimi
islem_modu = st.radio(
    "Lütfen yapmak istediğiniz işlemi seçin:",
    ("Konu Anlatımı", "Soru Çözümü"),
    horizontal=True
)

konu_adi = st.text_input(f"İstediğiniz Konu Adını Giriniz (Örn: **ek fiil** veya **simple present tense**):")

# Sesli Konuşma Kontrolü
konusma_acik = st.checkbox("Robotun Konuyu Sesli Anlatmasını İster misiniz?")

# Yanıt düğmesi
if st.button("Başlat"):
    if konu_adi:
        if islem_modu == "Konu Anlatımı":
            konu_icerigi = konuyu_bul(konu_adi)
            
            # Konu Anlatımı İşlemi
            if "Üzgünüm" not in konu_icerigi:
                st.success(f"İşte '{konu_adi.upper()}' konusu ile ilgili bilmen gerekenler:")
                st.markdown(konu_icerigi)

                if konusma_acik:
                    st.components.v1.html(f"""
                        <script>
                            const text = `{konu_icerigi.replace("`", "")}`; 
                            const utterance = new SpeechSynthesisUtterance(text);
                            utterance.lang = 'tr-TR'; 
                            utterance.rate = 1.0; 
                            speechSynthesis.speak(utterance);
                        </script>
                    """, height=0)

            else:
                st.warning(konu_icerigi)
                
        elif islem_modu == "Soru Çözümü":
            
            # Soru Çözümü İşlemi
            soru_cevabi = soru_cozumu_yap(konu_adi)
            st.info(f"'{konu_adi.upper()}' konusu için bir örnek soru çözümü:")
            st.markdown(soru_cevabi)

            if konusma_acik:
                st.components.v1.html(f"""
                    <script>
                        const text = `{soru_cevabi.replace("`", "")}`; 
                        const utterance = new SpeechSynthesisUtterance(text);
                        utterance.lang = 'tr-TR'; 
                        utterance.rate = 1.0; 
                        speechSynthesis.speak(utterance);
                    </script>
                """, height=0)
    else:
        st.error("Lütfen bir konu adı giriniz.")

# --- KENAR ÇUBUĞU VE ALT BÖLÜM ---
st.sidebar.title("Kullanılabilir Konular (Nihai Liste)")
st.sidebar.markdown(
    """
    **🇹🇷 TÜRKÇE:** Sözcükte/Cümlede/Parçada Anlam, Dil Bilgisi, Yazım Kuralları, Ek Fiil.
    **🇬🇧 İNGİLİZCE:** Tenses (Simple Present, Past...), Modals (Can, Must...), To Be, Conditionals.
    """
)
st.sidebar.caption("Lütfen aradığınız konunun tam adını giriniz. (Örn: 'ek fiil' veya 'simple present tense').")
st.sidebar.markdown("---")
st.sidebar.caption("Bu Uygulama **Yusuf Efe Şahin** Tarafından Geliştirilmiştir.")
st.sidebar.markdown("---")
st.sidebar.markdown("[🛡️ Yönetici Girişi](?p=admin_panel)")
