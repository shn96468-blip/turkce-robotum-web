import streamlit as st
import pandas as pd

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="TR Türkçe Robotum (Nihai)",
    layout="wide"
)

# --- NİHAİ VE KAPSAMLI KONULAR SÖZLÜĞÜ (Tüm 40+ Konu) ---
KONULAR = {
    # 1.1. Sözcükte Anlam (Eğlenceli ve Detaylı İçerikler)
    "gerçek anlam": "⭐ **Gerçek Anlam (Sözcüğün 'Kimlik Kartı' Adı):** Gerçek Anlam'a, bir kelimenin nüfus cüzdanındaki adı diyebiliriz. Bu, kelimenin herkesin bildiği, sözlükte ilk sırada yazan, en masum halidir. Akla gelen ilk anlamı temsil eder ve çoğunlukla somut bir şeyi ifade eder. **Eğlenceli Örnek:** 'Çocuğun **dişleri** bembeyazdı.' Burada 'diş', gerçekten ağzımızdaki kemiksi yapıyı ifade eder. Eğer 'Kapının **dişleri** kırıldı' deseydik, kapının gerçek bir dişi olmadığı için anlam değişmiş olurdu!",
    "mecaz anlam": "Sözcüğün gerçek anlamından tamamen uzaklaşarak kazandığı soyut anlamdır. Artık kelime, ilk anlamıyla hiçbir bağ kurmaz ve yeni, hayali bir anlam kazanır (Örnek: 'Bize karşı çok **soğuk** davrandı' — Soğuk kelimesi burada 'ilgisiz, sevgisiz' anlamında mecazlaşmıştır).",
    "terim anlam": "Bilim, sanat, spor gibi özel alanlara ait kavramları karşılayan ve sadece o alanda geçerli olan kelimelerdir (Örnek: Matematikte 'Üçgenin **açısı**', Tiyatroda '**Perde**' kelimesi).",
    "eş anlamlı kelimeler": "Yazılışları farklı, anlamları tamamen aynı olan ve cümlede birbirinin yerine kullanılabilen sözcüklerdir (Örnek: '**Siyah** - **Kara**', '**Okul** - **Mektep**').",
    "zıt anlamlı sözcükler": "Anlamca birbirinin tam tersi olan kelimelerdir (Örnek: '**İyi** - **Kötü**', '**Gelmek** - **Gitmek**').",
    "eş sesli kelimeler": "Yazılışları ve okunuşları aynı olmasına rağmen, anlamları tamamen farklı olan kelimelerdir (Örnek: '**Gül**' (çiçek) ve '**gülmek**' (eylem)).",
    "deyimler": "Genellikle mecaz anlamlı, kalıplaşmış, en az iki sözcükten oluşan söz gruplarıdır (Örnek: '**Ateş püskürmek**' $\rightarrow$ çok sinirlenmek anlamında kullanılır).",
    "atasözleri": "Uzun deneyimler sonucu oluşmuş, öğüt veren, anonim ve kalıplaşmış özlü sözlerdir (Örnek: '**Ağaç yaşken eğilir**' $\rightarrow$ Çocukların küçük yaşta eğitilmesi gerektiğini anlatır).",

    # 1.2. Cümlede Anlam
    "neden sonuç cümleleri": "Bir eylemin hangi sebeple (nedenle) yapıldığını bildiren cümlelerdir. İki bölümden oluşur: Eylem ve bu eylemin sebebi ('... için, ... olduğundan' gibi ekler kullanılır).",
    "amaç sonuç cümleleri": "Bir eylemin hangi amaca ulaşmak için yapıldığını bildiren cümlelerdir. Amaç henüz gerçekleşmemiştir ve genellikle 'diye, amacıyla, -mek için' gibi ifadelerle kurulur.",
    "koşul sonuç cümleleri": "Bir eylemin gerçekleşmesinin bir şarta (koşula) bağlı olduğunu bildiren cümlelerdir. Şart gerçekleşirse sonuç da gerçekleşir ('-se, -sa' eki veya 'üzere, ama' gibi sözcükler kullanılır).",
    "karşılaştırma cümleleri": "Birden fazla varlık, kavram veya durum arasındaki benzerlik ya da farklılıkları ortaya koyan cümlelerdir ('Daha, gibi, en, kadar' gibi sözcükler kullanılır).",
    "öznel yargılı cümleler": "Kişiden kişiye değişen, doğruluğu veya yanlışlığı kanıtlanamayan, kişisel görüş ve duygu içeren yargılardır.",
    "nesnel yargılı cümleler": "Doğruluğu herkes tarafından kabul edilen, kanıtlanabilir, kişisel görüş içermeyen, kanıtlanabilir yargılardır.",
    "örtülü anlam": "Cümlede açıkça söylenmeyen ancak cümlenin tamamından çıkarılabilen, üstü kapalı ikinci bir anlamdır (Örnek: 'Ali **de** tatile gitti' $\rightarrow$ Ali'den başka gidenler de varmış).",
    "geçiş ve bağlantı ifadeleri": "Cümleler veya paragraflar arası anlam bütünlüğünü sağlayan, düşüncenin yönünü değiştiren sözcüklerdir ('Oysa, fakat, ilk olarak, özetle' gibi).",
    "cümle yorumlama": "Verilen bir cümlenin konusunu, ana fikrini veya bu cümleden çıkarılabilecek yargıları bulma işlemidir. Cümlenin mantığını anlamayı gerektirir.",

    # 1.3. Parçada Anlam (Eğlenceli ve Detaylı İçerikler)
    "anlatım biçimleri": "🎨 **Anlatım Biçimleri (Yazarın Kamera Açısı):** Yazarın derdini, düşüncesini veya olayını anlatırken seçtiği yöntemdir. Sanki yazar, bir film yönetmeni gibi, hangi kamera açısını kullanacağını seçer. **Betimleme (Resim Çizme):** Okuyucunun gözünde bir fotoğraf karesi oluşturmaktır. Varlıkların tüm detayları (renk, şekil, koku, ses) ayrıntılı verilir. **Öyküleme (Film Çekme):** Bir olayı, olay örgüsüne bağlı kalarak, zaman ve mekan belirterek anlatmaktır. **Açıklama (Öğretmen Modu):** Bilgi verme ve öğretme esastır. **Tartışma (Münazara):** Yazarın kendi görüşünü savunarak karşı görüşü çürütmeye çalıştığı anlatım biçimidir.",
    "düşünceyi geliştirme yolları": "**Tanımlama:** Kavramın ne olduğunu belirtme. **Karşılaştırma:** Farklılık veya benzerlikleri belirtme. **Örnekleme:** Soyut bir düşünceyi somutlaştırma. **Tanık Gösterme:** Ünlü birinin sözünü kullanma. **Benzetme:** Bir şeyi başkasına benzeterek anlatma.",
    "anlatıcı türleri": "**Birinci Kişi Ağzıyla Anlatım:** Yazarın, olayın kahramanı olduğu ve '-dım, -dik' gibi ekler kullandığı anlatım. **Üçüncü Kişi Ağzıyla Anlatım:** Yazarın olayın gözlemcisi olduğu ve '-dı, -du' gibi ekler kullandığı anlatım.",
    "paragrafta ana düşünce": "Yazarın paragraf aracılığıyla okuyucuya iletmek istediği temel mesaj veya asıl fikirdir. Genellikle paragrafın giriş veya sonuç cümlesinde saklıdır.",
    "paragrafın yapı yönü": "Paragrafın Giriş (Genel yargı), Gelişme (Detaylar) ve Sonuç (Özet/Ana düşünce) bölümlerinin düzenlenmesidir.",
    "tablo ve grafik inceleme": "Verilerin tablo veya grafik üzerinden analiz edilerek yorumlanmasıdır. Ana amaç, sunulan sayısal bilgiden doğru yorumları ve sonuçları çıkarmaktır.",
    "görsel yorumlama": "Verilen bir resim, fotoğraf veya görsel üzerinden çıkarım yapma, ana fikri bulma veya detayları analiz etme becerisidir.",

    # 2. Yazım Bilgisi
    "yazım kuralları": "Büyük Harflerin Kullanıldığı Yerler, Sayıların Yazımı, Birleşik Kelimelerin Yazımı, Kısaltmaların Yazımı gibi dilin doğru kullanımını sağlayan kurallar bütünüdür.",
    "noktalama işaretleri": "Cümlelerin anlamını netleştirmek ve okumayı kolaylaştırmak için kullanılan simgelerdir (Nokta, Virgül, Soru İşareti, vb.).",

    # 3. Dil Bilgisi (Eğlenceli ve Detaylı İçerikler)
    "fiiller": "🚀 **Fiiller (Cümlenin Turbo Motoru):** Fiiller, cümlenin aksiyon merkezidir! Onlar olmadan cümle hareket edemez, bir olay, durum ya da oluş gerçekleşmez. Fiiller, bir cümlenin ne zaman (kip) ve kim tarafından (kişi) yapıldığını bize anında söylerler. **Detaylı İnceleme:** 'Gel-iyor-um' fiilinde '-iyor' kipi, '-um' ise kişiyi gösterir.",
    "anlamlarına göre fiiller": "**İş (Kılış) Fiilleri:** Nesne alabilen fiillerdir. **Durum Fiilleri:** Nesne alamayan, öznenin içinde bulunduğu durumu bildiren fiillerdir. **Oluş Fiilleri:** Kendiliğinden gerçekleşen, zamana bağlı değişim bildiren fiillerdir.",
    "yapılarına göre fiiller": "**Basit Fiil:** Yapım eki almamış fiil. **Türemiş Fiil:** Yapım eki almış fiil. **Birleşik Fiil:** En az iki kelimeden oluşan fiillerdir.",
    "fiil çekimi": "Fiillerde kip (zaman), kişi (şahıs), olumsuzluk ve soru eklerinin kullanılmasıdır.",
    "fiillerde anlam kayması": "Bir kipin başka bir kipin yerine kullanılması durumudur (Örnek: 'Yarın sinemaya giderim' – Geniş zaman yerine Gelecek zaman kipi kullanılması).",
    "ek fiil": "İsim soylu sözcükleri yüklem yapan veya basit zamanlı fiili birleşik zamanlı fiil yapan ektir (Örn: 'İdi, imiş, ise, -dir').",
    "birleşik zamanlı fiiller": "Basit zamanlı bir fiilin ek fiil alarak ikinci bir kip eki kazanmasıdır (Örn: 'gel-iyor-du').",
    "zarflar": "Fiilleri, fiilimsileri, sıfatları veya kendi türünden sözcükleri etkileyen sözcüklerdir (Durum, Zaman, Yer-Yön, Miktar, Soru zarfları).",
    "anlatım bozuklukları": "Cümlelerin anlam veya yapı bakımından tutarsız olmasıdır (Örn: Gereksiz sözcük, mantık hatası).",
    
    # 4. Edebi Türler ve Söz Sanatları
    "söz sanatları": "**Abartma:** Bir şeyi olduğundan çok gösterme. **Benzetme:** Bir şeyi başkasına benzeterek anlatma. **Kişileştirme:** İnsan dışındaki varlıklara insan özelliği verme. **Konuşturma:** İnsan dışındaki varlıkları konuşturma. **Karşıtlık:** Zıt kavramları bir arada kullanma.",
    "yazı metin türleri": "**Söyleşi (Sohbet):** Samimi bir dille, karşılıklı konuşma havasında yazılan tür. **Biyografi:** Ünlü birinin hayatını başkasının yazdığı yazı. **Otobiyografi:** Bir kişinin kendi hayatını anlattığı yazı. **Günlük:** Günü gününe, tarih atılarak yazılan kişisel notlar."
}

# --- YARDIMCI FONKSİYONLAR ---
def konuyu_bul(arama_terimi):
    arama_terimi = arama_terimi.lower().strip()
    if arama_terimi in KONULAR:
        return KONULAR[arama_terimi]
    else:
        return "Üzgünüm, aradığınız konuyu tam olarak bulamadım. Lütfen listenin sağ tarafındaki konulardan tam adını girin (Örn: 'gerçek anlam' veya 'anlatıcı türleri')."

def soru_cozumu_yap(arama_terimi):
    arama_terimi = arama_terimi.lower().strip()
    
    if "fiil" in arama_terimi or "çekim" in arama_terimi:
        return "❓ **Örnek Soru Çözümü (Fiiller):** Sorunuzdaki eylemin basit, türemiş veya birleşik yapıda olduğunu belirlemek için öncelikle fiilin kökünü bulmalıyız. Kökten sonraki yapım eklerini kontrol ederek doğru cevaba ulaşabiliriz. Unutmayın, birleşik fiil en az iki kelimeden oluşur. **Cevap:** Türemiş yapılı fiil örneği."
    elif "zarf" in arama_terimi:
        return "❓ **Örnek Soru Çözümü (Zarflar):** Bir kelimenin zarf olması için bir eylemi, sıfatı ya da başka bir zarfı nitelemesi gerekir. Fiile 'Nasıl?' 'Ne zaman?' sorularını sorarak doğru zarf türünü buluruz. 'Çok hızlı koştu' cümlesinde 'çok', 'hızlı' zarfını etkilemiştir. **Cevap:** Miktar zarfı."
    elif "anlam" in arama_terimi or "sanat" in arama_terimi:
        return "❓ **Örnek Soru Çözümü (Anlam ve Sanatlar):** Söz sanatı sorulduğunda insana ait bir özelliğin insan dışı bir varlığa verilip verilmediğine bakmalıyız. 'Güneş bugün bize **gülümsüyordu**' cümlesinde Kişileştirme sanatı vardır, çünkü güneşin gülümsemesi insana özgüdür. **Cevap:** Söz sanatı kullanılmıştır."
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

konu_adi = st.text_input(f"İstediğiniz Konu Adını Giriniz (Örn: **gerçek anlam** veya **fiiller**):")

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
