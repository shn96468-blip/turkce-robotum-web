import streamlit as st
import pandas as pd

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="TR Türkçe Robotum (Nihai ve Kapsamlı)",
    layout="wide"
)

# --- NİHAİ VE KAPSAMLI KONULAR SÖZLÜĞÜ (Ek Fiil Düzeltmesi Dahil) ---
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
    "cümlede anlam ilişkileri": "Cümlelerin Eş, Yakın ve Zıt Anlam taşıma durumlarıdır. **Yakın Anlamlı Cümleler** tam
