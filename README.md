# 🧠 KNN ile Satın Alma Tahmini

Bu proje, bireylerin yaş ve maaş bilgilerine göre bir ürünü satın alıp almayacağını tahmin eden bir sınıflandırma modelini içerir.

## 📦 Veri Seti

- Kaynak: [social.csv](https://raw.githubusercontent.com/amankharwal/Website-data/master/social.csv)
- Özellikler:
  - `Age`: Kişinin yaşı
  - `EstimatedSalary`: Maaş tahmini
  - `Purchased`: Hedef değişken (1: Satın aldı, 0: Satın almadı)

## 🤖 Kullanılan Algoritmalar

- K-Nearest Neighbors (✅ En iyi sonuç)
- Decision Tree
- Logistic Regression
- Passive Aggressive Classifier

## 📈 En İyi Model

- **Model:** `KNN Classifier`
- **Doğruluk (Test Seti):** 85%
- Model dosyası: `KNN_classifier.pkl`

## 🚀 Streamlit Uygulaması

Kullanıcının yaş ve maaşını girerek ürün satın alıp almayacağını tahmin eden arayüz.

### Kullanmak için:
```bash
pip install streamlit joblib scikit-learn
streamlit run app.py


📂 Proje Dosyaları
social.csv: Eğitim verisi

KNN_classifier.pkl: Eğitilmiş model

app.py: Streamlit arayüzü

README.md: Proje açıklaması

🧪 Geliştirilebilir Özellikler
Daha fazla algoritma karşılaştırması

Skorların görselleştirilmesi

ROC, Confusion Matrix gibi metriklerle analiz


📝 Bu proje eğitim amaçlıdır.