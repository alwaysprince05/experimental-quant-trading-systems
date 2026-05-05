---
title: QuantLab Pro
emoji: 💎
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# 💎 QuantLab Pro: Experimental Trading Systems

[![Live Demo](https://img.shields.io/badge/View%20Live-Hugging%20Face-blue?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/alwaysprince05e/experimental-quant-trading-systems)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github)](https://github.com/alwaysprince05/experimental-quant-trading-systems)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**QuantLab Pro** is a high-performance quantitative research environment designed to explore market microstructure, volatility surfaces, and alpha factor discovery. Built with Python, Scikit-Learn, and Plotly, it provides interactive 3D visualizations and real-time parameter simulation for experimental trading strategies.

---

## 🚀 [View Live Dashboard](https://huggingface.co/spaces/alwaysprince05e/experimental-quant-trading-systems)

---

## 🛠️ Analytical Modules

### 1. Volatility Surface Modeling
Models asset pricing as a dynamic function of **Time** and **Volatility** using high-degree Polynomial Regression.
*   **3D Surface Mapping**: Visualize how market conditions impact pricing.
*   **Gradient Signals**: Generate buy/sell signals based on surface slope (theta/vega proxies).
*   **PnL Simulation**: Real-time backtesting of surface-based strategies.

### 2. Order Flow Pressure Model
Simulates the impact of **Buy/Sell Volume Imbalance** on short-term price movements.
*   **Microstructure Analysis**: Models the nonlinear relationship between order flow and price drift.
*   **Imbalance Thresholds**: Strategy execution based on extreme order flow pressure.
*   **Equity Growth**: Interactive tracking of PnL relative to market imbalance.

### 3. Alpha Factor Explorer
A laboratory for discovering and validating **Predictive Alpha Factors**.
*   **Factor Matrix**: Momentum, Mean Reversion, and Volatility interaction.
*   **Factor Importance**: Machine learning weights showing which factors drive returns.
*   **Distribution Analysis**: Statistical profiling of returns and factor effectiveness.

---

## 💻 Local Installation

To run the QuantLab Pro dashboard on your local machine:

```bash
# 1. Clone the repository
git clone https://github.com/alwaysprince05/experimental-quant-trading-systems.git
cd experimental-quant-trading-systems

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the dashboard
streamlit run app.py
```

---

## 🌍 Deployment

This project is optimized for **Hugging Face Spaces** via Docker. The repository includes:
*   `app.py`: The main interactive dashboard engine.
*   `Dockerfile`: Pre-configured environment for high-performance containerized execution.
*   `requirements.txt`: Minimal, optimized dependency list.

---

## ⚠️ Disclaimer
These projects are for **educational and research purposes only**. All data is synthetically generated. They are not intended for live trading, financial advice, or professional investment decisions.

---

## 👤 Author
**Prince Maurya**
*   GitHub: [@alwaysprince05](https://github.com/alwaysprince05)
*   Hugging Face: [@alwaysprince05e](https://huggingface.co/alwaysprince05e)

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
