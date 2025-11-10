import streamlit as st
import pandas as pd

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="TR Türkçe Robotum (Nihai ve Kapsamlı)",
    layout="wide"
)

# --- NİHAİ VE KAPSAMLI KONULAR SÖZLÜĞÜ (Tüm 40+ Konu Düzeltildi) ---
KONULAR = {
    # 1.1. Sözcükte Anlam
    "gerçek anlam": "⭐ **Gerçek Anlam (Kelimenin Temeli):** Bir kelimenin söylendiğinde akla gelen ilk ve temel anlamıdır. Kelimenin somut ve en masum halidir. Örnek: 'Gözüm **ağrıyor**' (Gerçek ağrı).",
    "mecaz anlam": "Sözcüğün gerçek anlamından tamamen uzaklaşarak kazandığı soyut anlamdır. Yeni, hayali bir anlam taşır. Örnek: 'Bu olay kalbimi **kırdı**' (Gerçek kırılma yok, üzülme var).",
    "terim anlam": "Bilim, sanat, spor gibi özel alanlara ait kavramları karşılayan ve sadece o alanda kullanılan kelimelerdir. Örnek: 'Matematikte **açı**', 'Tiyatroda **perde**'.",
    "eş ve yakın anlamlı kelimeler": "Yazılışları farklı, anlamları aynı olanlar **(Eş Anlamlı: Kırmızı-Al)** ve tam olarak aynı olmasa da birbirinin yerine geçebilenler **(Yakın Anlamlı: Basmak-Çiğnemek)**.",
    "zıt karşıt anlamlı sözcükler": "Anlamca birbirinin tam tersi olan kelimelerdir. Olumsuzluk (gelmek-gelmemek) zıt anlam değildir. Örnek: '**İyi** - **Kötü**'.",
    "eş sesli sesteş sözcükler": "Yazılışları ve okunuşları aynı, anlamları tamamen farklı olan kelimelerdir. Örnek: '**Yüz**' (surat) ve '**yüzmek**' (eylem).",
    "deyimler": "Genellikle mecaz anlamlı, kalıplaşmış ve bir durumu daha etkileyici anlatmayı amaçlayan söz gruplarıdır. **Öğüt vermez.** Örnek: '**Etekleri zil çalmak**' (çok sevinmek).",
    "atasözleri": "Uzun gözlemler sonucu oluşmuş, genellikle toplumun ortak deneyimini yansıtan ve **öğüt/kural bildiren** kalıplaşmış özlü cümlelerdir. Örnek: '**Ağaç yaşken eğilir**'.",

    # 1.2. Cümlede Anlam
    "neden sonuç cümleleri": "Bir eylemin hangi sebeple (nedenle) yapıldığını bildiren cümlelerdir. **Kesinleşmiş bir sebep** vardır. Örnek: 'Hava soğuk **olduğu için** kalın giyindi.'",
    "amaç sonuç cümleleri": "Bir eylemin hangi **amaca ulaşmak için** yapıldığını bildiren cümlelerdir. Amaç henüz gerçekleşmemiştir. Örnek: 'Sınavı geçmek **için** çok çalışıyor.'",
    "koşul sonuç cümleleri": "Bir eylemin gerçekleşmesinin bir şarta (koşula) bağlı olduğunu bildiren cümlelerdir. Şart gerçekleşirse sonuç da gerçekleşir. Örnek: '**Erken gelirsen** sana yardım ederim.'",
    "karşılaştırma cümleleri": "Birden fazla varlık, kavram veya durum arasındaki benzerlik ya da farklılıkları ortaya koyan cümlelerdir ('Daha, gibi, en, kadar' gibi sözcükler kullanılır).",
    "öznel yargılı cümleler": "Kişiden kişiye değişen, **kişisel görüş** içeren ve kanıtlanamayan yargılardır.",
    "nesnel yargılı cümleler": "Doğruluğu herkes tarafından kabul edilen, **kanıtlanabilir** ve kişisel görüş içermeyen yargılardır.",
    "örtülü anlam": "Cümlede açıkça söylenmeyen ancak cümlenin tamamından çıkarılabilen, üstü kapalı ikinci bir anlamdır. Örnek: 'Ali **de** geldi' $\rightarrow$ Ali'den başka gelenler de var.",
    "geçiş ve bağlantı ifadeleri": "Cümleler arası anlam bütünlüğünü sağlayan, **düşüncenin yönünü değiştiren** (ama, fakat, lakin) veya **destekleyen** (ayrıca, dahası) sözcüklerdir.",
    "cümlede anlam ilişkileri": "Cümlelerin Eş, Yakın ve Zıt Anlam taşıma durumlarıdır. **Yakın Anlamlı Cümleler** tam aynı olmasa da benzer mesajı verir.",
    "cümle yorumlama": "**Cümlenin Konusu, Ana Fikri, Çıkarılabilecek / Çıkarılamayacak Yargılar, Cümle Tamamlama / Oluşturma** gibi cümlenin anlamsal yapısını inceleyen tüm becerileri kapsar.",

    # 1.3. Parçada Anlam
    "anlatım biçimleri": "**Betimleme** (Fotoğraf çekme), **Öyküleme** (Film çekme), **Açıklama** (Bilgi verme), **Tartışma** (Fikir savunma ve çürütme) yöntemleridir.",
    "düşünceyi geliştirme yolları": "**Tanımlama**, **Karşılaştırma**, **Örnekleme**, **Tanık Gösterme** (Alıntı yapma), **Benzetme** ve **Sayısal Verilerden Yararlanma** (İstatistikler) yöntemleridir.",
    "anlatıcı türleri": "**Birinci Kişi Ağzıyla Anlatım** (Ben/Biz: Olayın Kahramanı) ve **Üçüncü Kişi Ağzıyla Anlatım** (O/Onlar: Gözlemci) olarak ikiye ayrılır.",
    "paragrafın anlam yönü": "**Ana Düşünce** (Temel Mesaj), **Yardımcı Düşünceler** (Ana Fikri destekleyenler), **Konu**, **Başlık**, **Anahtar Kelimeler**, **Olay**, **Zaman**, **Yer ve Varlık Kadrosu**, **Duygular ve Duyular** gibi metnin içeriğiyle ilgili tüm unsurları kapsar.",
    "paragrafın yapı yönü": "**Giriş**, **Gelişme** ve **Sonuç** bölümlerinin düzenlenmesi, **Paragraf Oluşturma ve Tamamlama**, **Paragrafı İkiye Bölme**, **Akışı Bozan Cümleyi** bulma ve **Cümlelerin Yerini Değiştirme** gibi paragrafın mantıksal ve biçimsel yapısını kapsar.",
    "tablo ve grafik inceleme": "Verilerin tablo veya grafik üzerinden analiz edilerek yorumlanmasıdır. Verilen bilgiden **doğru yorumları ve sonuçları** çıkarma becerisidir.",
    "görsel yorumlama": "Verilen bir resim, fotoğraf veya görsel üzerinden çıkarım yapma, ana fikri bulma veya detayları analiz etme becerisidir.",

    # 2. Yazım Bilgisi
    "yazım imla kuralları": "Kelimelerin doğru yazılışını (Büyük Harf, Sayı, Birleşik Kelime, Kısaltma Yazımı) ve **Bazı Bağlaç ve Eklerin Yazımı** (de/da, ki) ile **Yazımı Karıştırılan Sözcükleri** kapsayan dil kurallarıdır.",
    "noktalama işaretleri": "**Nokta**, **Virgül**, **İki Nokta**, **Noktalı Virgül**, **Üç Nokta**, **Soru İşareti**, **Ünlem İşareti**, **Tırnak İşareti**, **Kesme İşareti**, **Yay Ayraç**, **Kısa Çizgi**, **Uzun Çizgi** ve **Eğik Çizgi** gibi anlamı netleştiren tüm simgelerdir.",

    # 3. Dil Bilgisi
    "fiiller": "🚀 **Fiiller (Cümlenin Turbo Motoru):** İş, oluş, hareket bildiren sözcüklerdir. Cümlede kip (zaman) ve kişi (şahıs) ekleri alırlar.",
    "anlamlarına göre fiiller": "**İş (Kılış)** (Nesne alan), **Durum** (Nesne almayan), **Oluş** (Kendiliğinden değişen) fiillerdir.",
    "yapılarına göre fiiller": "**Basit Fiil** (Ek almamış), **Türemiş Fiil** (Yapım eki almış), **Birleşik Fiil** (İki kelimeden oluşan) fiillerdir.",
    # DÜZELTME BURADA YAPILDI: Artık 'ek fiil' ve 'ek eylem' aramaları ayrı ayrı çalışacak.
    "ek fiil": "İsim soylu sözcükleri yüklem yapan veya basit zamanlı fiili birleşik zamanlı fiil yapan ektir. Bu eylem **'idi, imiş, ise, -dir'** şekillerinde karşımıza çıkar. İsimleri yüklem yapma ve fiilleri birleşik zamanlı yapma olmak üzere iki temel görevi vardır.",
    "ek eylem": "Ek fiilin diğer adıdır. İsim soylu sözcükleri yüklem yapan veya basit zamanlı fiili birleşik zamanlı fiil yapan ektir. Bu eylem **'idi, imiş, ise, -dir'** şekillerinde karşımıza çıkar. İsimleri yüklem yapma ve fiilleri birleşik zamanlı yapma olmak üzere iki temel görevi vardır.",
    "birleşik zamanlı fiiller": "Basit zamanlı bir fiilin ek fiil alarak ikinci bir kip eki kazanmasıdır (Örn: 'gel-iyor-du' → Şimdiki Zamanın Hikayesi).",
    "fiil çekimi": "Fiillerde **Kip, Kişi, Olumsuzluk ve Soru** eklerinin kullanılmasıdır.",
    "fiillerde anlam kayması": "Bir kipin (zamanın) başka bir kipin yerine kullanılmasıdır. Örnek: 'Yarın sinemaya **giderim**' (Geniş zaman, Gelecek zaman yerine kullanılmış).",
    "zarflar": "Fiilleri, fiilimsileri, sıfatları veya kendi türünden sözcükleri etkileyen sözcüklerdir (**Durum, Zaman, Yer-Yön, Miktar, Soru** zarfları).",
    "anlatım bozuklukları": "Cümlelerin anlam (Örn: Gereksiz sözcük, mantık hatası) veya yapı (Örn: Ek/fiil eksikliği) bakımından tutarsız olmasıdır.",
    
    # 4. Edebi Türler ve Söz Sanatları
    "söz sanatları": "**Abartma**, **Benzetme**, **Kişileştirme**, **Konuşturma** ve **Karşıtlık** (Tezat) gibi ifadeleri daha etkili hale getiren sanatlardır.",
    "yazı metin türleri": "**Söyleşi**, **Biyografi**, **Otobiyografi**, **Günlük** ve **Mektup** gibi metinlerin amaçlarına göre ayrıldığı biçimlerdir."
}

# --- YARDIMCI FONKSİYONLAR ---
def konuyu_bul(arama_terimi):
    arama_terimi = arama_terimi.lower().strip()
    if arama_terimi in KONULAR:
        return KONULAR[arama_terimi]
    else:
        return "Üzgünüm, aradığınız konuyu tam olarak bulamadım. Lütfen listenin sağ tarafındaki konulardan tam adını girin (Örn: 'ek fiil', 'gerçek anlam' veya 'noktalama işaretleri')."

def soru_cozumu_yap(arama_terimi):
    # Soru çözümü modunda (Yapay zeka simülasyonu)
    arama_terimi = arama_terimi.lower().strip()
    
    if "fiil" in arama_terimi or "çekim" in arama_terimi:
        return "❓ **Örnek Soru Çözümü (Fiiller/Ek Fiil):** Sorunuzdaki eylemin yapısını, zamanını ve ek fiil alıp almadığını kontrol etmeliyiz. Eğer isim soylu bir sözcük yüklem olmuşsa, orada mutlaka Ek Fiil vardır. **Cevap:** Ek Fiil kullanılarak türetilmiş birleşik zamanlı fiil."
    elif "zarf" in arama_terimi:
        return "❓ **Örnek Soru Çözümü (Zarflar):** Bir kelimenin zarf olması için bir eylemi, sıfatı ya da başka bir zarfı nitelemesi gerekir. Fiile 'Nasıl?' 'Ne zaman?' sorularını sorarak doğru zarf türünü buluruz. **Cevap:** Miktar zarfı."
    elif "anlam" in arama_terimi or "sanat" in arama_terimi:
        return "❓ **Örnek Soru Çözümü (Anlam ve Sanatlar):** Söz sanatı sorulduğunda insana ait bir özelliğin insan dışı bir varlığa verilip verilmediğine bakmalıyız. 'Güneş bugün bize **gülümsüyordu**' cümlesinde Kişileştirme sanatı vardır. **Cevap:** Söz sanatı kullanılmıştır."
    else:
        return "Şu an sadece **Fiiller**, **Zarflar** ve **Söz Sanatları** ile ilgili örnek soruları çözebilirim. Lütfen bu konulardan birini deneyin."

# --- YÖNETİCİ GİRİŞİ KONTROLÜ ---
query_params = st.query_params
if "p" in query_params and query_params["p"] == "admin_panel":
    import admin_panel 
    st.stop()

# --- ANA ROBOT EKRANI ---
st.title("🇹🇷 TR Türkçe Robotum: Konu Anlatım ve Soru Çözüm Asistanı")
st.markdown("Merhaba! Hangi konuda bilgi istersin ya da hangi konuyla ilgili **örnek soru çözümü** yapmamı istersin? Artık daha eğlenceli ve detaylı anlatıyorum! 😉")

# Mod Seçimi
islem_modu = st.radio(
    "Lütfen yapmak istediğiniz işlemi seçin:",
    ("Konu Anlatımı", "Soru Çözümü"),
    horizontal=True
)

konu_adi = st.text_input(f"İstediğiniz Konu Adını Giriniz (Örn: **gerçek anlam** veya **ek fiil**):")

# Sesli Konuşma Kontrolü (YENİ EK ÖZELLİK)
konusma_acik = st.checkbox("Robotun Konuyu Sesli Anlatmasını İster misiniz?")

# Yanıt düğmesi
if st.button("Başlat"):
    if konu_adi:
        if islem_modu == "Konu Anlatımı":
            konu_icerigi = konuyu_bul(konu_adi)
            
            # Konu Anlatımı İşlemi
            if konu_icerigi and "Üzgünüm" not in konu_icerigi:
                st.success(f"İşte '{konu_adi.upper()}' konusu ile ilgili bilmen gerekenler:")
                st.markdown(konu_icerigi)

                # Konuşma Özelliği (Kontrol edildi)
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

            elif "Üzgünüm" in konu_icerigi:
                st.warning(konu_icerigi)
            
            else:
                st.error("Lütfen bir konu adı giriniz.")
                
        elif islem_modu == "Soru Çözümü":
            
            # Soru Çözümü İşlemi
            soru_cevabi = soru_cozumu_yap(konu_adi)
            st.info(f"'{konu_adi.upper()}' konusu için bir örnek soru çözümü:")
            st.markdown(soru_cevabi)

            # Konuşma Özelliği (Soru çözümü için, kontrol edildi)
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
    **Sözc
