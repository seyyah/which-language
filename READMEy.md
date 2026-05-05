# Mini Notes Project 📝

Bu proje, komut satırı üzerinden çalışan basit bir not alma uygulamasıdır.

## V1 Geliştirmeleri (V0 -> V1 Farkları)
Ödevin V1 aşaması kapsamında aşağıdaki güncellemeler yapılmıştır:

1. **Dil Güncellemesi:** Tüm kullanıcı mesajları ve hata bildirimleri Türkçeleştirilerek kullanım kolaylığı sağlandı.
2. **Öncelik Sistemi:** Not oluştururken artık `Düşük`, `Orta` veya `Yüksek` gibi öncelik seviyeleri eklenebiliyor.
3. **Veri Doğrulama:** Başlık veya içerik boş bırakıldığında uygulamanın hata vermesi ve kullanıcıyı uyarması sağlandı.
4. **Dil Desteği:** Kullanıcı deneyimini artırmak amacıyla tüm hata ve bilgilendirme mesajları Türkçeleştirildi.
5. **Yeni Veri Alanı:** Notlara "Öncelik" (Priority) özelliği eklendi. Artık notlar oluşturulurken önem seviyesi belirtilebiliyor.
6. **Hata Denetimi:** Kullanıcının yanlışlıkla boş başlık veya içerik girmesini engelleyen bir kontrol mekanizması eklendi.

"""
V2 GÖREV LİSTESİ:
1. 'list' komutunu ekle: Tüm notları döngü kullanarak alt alta listele.
2. 'search' komutunu ekle: Kullanıcının girdiği kelimeyi not başlıklarında ara.
3. 'filter' komutunu ekle: Sadece seçilen öncelik seviyesindeki (Düşük/Orta/Yüksek) notları göster.

"""
V1 → V2 Değişiklik Özeti:

Dinamik Listeleme: Statik yapıdan döngüsel yapıya geçildi; artık tüm notlar dosyadan okunup listelenebiliyor.

Arama Kabiliyeti: Büyük/küçük harf duyarsız arama özelliği ile notlar arasında hızlı erişim sağlandı.

Gelişmiş Filtreleme: Notlar, V1'de eklenen "Öncelik" seviyelerine göre süzülebilecek şekilde geliştirildi.

## Kurulum ve Kullanım
Uygulamayı başlatmak için:
`python solution_v1.py init`

Not eklemek için:
`python solution_v1.py create "Başlık" "İçerik" "Yüksek"`
