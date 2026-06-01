import streamlit as st
import numpy as np

# Sayfa Yapısı ve Tema
st.set_page_config(page_title="Podcast Dinleme Süresi Analizi", page_icon="🎙️")

st.title("🎙️ PodAI: Yapay Zeka Podcast Dinleme Süresi Tahmini")
st.write("Podcast ve bölüm özelliklerini girerek tahmini dinleme süresini anlık hesaplayın.")

# Kullanıcı Giriş Alanları (En kritik medya parametreleri)
col1, col2 = st.columns(2)
with col1:
    episode_length = st.slider("Bölüm Süresi (Dakika)", 5, 120, 45)
    host_pop = st.slider("Sunucu Popülerliği (%)", 0, 100, 70)
with col2:
    number_of_ads = st.slider("Bölümdeki Reklam Sayısı", 0, 15, 3)
    sentiment = st.selectbox("Bölümün Genel Duygu Tonu", ["Positive", "Neutral", "Negative"])

st.write("---")

if st.button("🚀 DİNLEME SÜRESİNİ TAHMİN ET", use_container_width=True):
    # Keras modelimizin dijital medya mantığını simüle eden formülümüz
    base_retention = 0.50 # Kullanıcıların ortalama dinleme oranı (%50)
    
    # 1. Sunucu etkisi ve içerik tonu çarpanları
    if host_pop > 80: base_retention += 0.15
    if sentiment == "Positive": base_retention += 0.05
    elif sentiment == "Negative": base_retention -= 0.10
        
    # 2. Reklam yoğunluğu cezası (Çok reklam kullanıcıyı kaçırır)
    ad_density = number_of_ads / episode_length
    if ad_density > 0.15: base_retention -= 0.15
    
    # Oranı mantıksal sınırlara çekme (%10 ile %95 arası)
    final_retention = min(max(base_retention, 0.10), 0.95)
    predicted_time = episode_length * final_retention
    
    # Sonuç ekranı tasarımı
    st.subheader("📊 Yapay Zeka Tüketim Öngörüsü:")
    st.success(f"🤖 Tahmini Dinleme Süresi: **{predicted_time:.1f} Dakika** (Toplam bölümün %{final_retention*100:.0f}'i)")
    
    # Medya ve Reklam Stratejisi Yorumu
    if final_retention >= 0.70:
        st.info("📈 **Yüksek Kullanıcı Bağlılığı (High Retention):** Dinleyici kitle bölüme yüksek sadakat gösteriyor. Sunucu popülerliği ve içerik tonu reklam yükünü başarıyla dengeliyor.")
    elif final_retention >= 0.40:
        st.info("🟡 **Ortalama Dinleme Oranı:** Standart bir içerik performansı. Dinleyici kayıplarını azaltmak için reklam yerleşimleri (mid-roll) optimize edilebilir.")
    else:
        st.info("📉 **Hızlı Dinleyici Terki (Churining):** Reklam yoğunluğu veya içerik tonu dinleyiciyi sıkmış durumda. Reklam sayısının azaltılması veya sürelerinin kısaltılması önerilir.")
