# 📈 A Comparative Study of LSTM-Based Stock Price Prediction Models: Evaluating the Impact of Incorporating Sentiment Analysis on Predictive Accuracy.

Can tweets move stock prices? That's essentially what this project is trying to figure out. We took LSTM models, the go-to for anything time series related, and ran them twice: once on raw historical price data, and once with Twitter sentiment thrown into the mix. The goal was simple: does knowing what people are saying online actually make the predictions better?

---

## 🚀 Project Objectives

- Predict Tesla (TSLA) stock prices using LSTM models.
- Integrate Twitter sentiment data to examine its impact on prediction accuracy.
- Compare results of two models:
  - LSTM using only historical stock prices.
  - LSTM using both stock prices and Twitter sentiment scores.

---

## 📊 Datasets Used

- **Historical Stock Prices**: TSLA stock data (2015–2019) from Nasdaq.com.
- **Social Media Sentiment**: Twitter data for TSLA from Kaggle.

---

## 🛠️ Methodology

### Phase 1: LSTM Without Sentiment Analysis
- Clean and normalize historical stock data.
- Prepare sequences for LSTM input.
- Train and evaluate the model.

### Phase 2: LSTM With Sentiment Analysis
- Clean and process tweets (remove stop words, punctuation, etc.).
- Perform sentiment scoring using **VADER**.
- Merge sentiment scores with historical stock data.
- Retrain LSTM model and compare performance.

---

## 📈 Results

- Both models performed well in forecasting stock prices.
- Incorporating sentiment analysis slightly improved prediction accuracy.
- Pearson's correlation coefficient between sentiment and stock price: **0.26** (weak positive correlation).
- Model performance improved with optimal epochs but declined beyond a threshold.

---

## 📌 Key Technologies

- Python (Pandas, NumPy, Scikit-learn)
- Keras (LSTM)
- NLTK (VADER Sentiment Analysis)
- Matplotlib/Seaborn for visualization

---

## 🔍 Future Work

- Explore **weighted features** to give more importance to sentiment data.
- Include sentiment from news articles and analyst opinions.
- Integrate **reinforcement learning** to dynamically adjust model behavior.

---


