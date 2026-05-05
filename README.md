## Dev/Creator = tubakhxn

# Experimental Quant Trading Systems

This repository contains three experimental trading systems built using synthetic data, machine learning, and quantitative modeling techniques. Each project is designed to explore how different market dynamics can be modeled and visualized using Python.

These systems focus on intuition, visualization, and research—not real trading.

---

# 1. Volatility Surface Trading System

## Overview

Models price as a function of time and volatility, creating a 3D surface representation of market behavior and generating signals based on surface gradients.

## What it does

* Generates synthetic price and volatility data
* Fits a regression model to create a volatility surface
* Visualizes a 3D surface with contour projections
* Generates buy/sell signals using slope (gradient)
* Simulates basic PnL

## How to run

pip install numpy matplotlib scikit-learn
python vol_surface_trading_system.py

---

# 2. Order Flow Pressure Model

## Overview

Simulates market behavior using synthetic buy/sell volume to model order flow imbalance and its impact on price movement.

## What it does

* Generates buy and sell volume streams
* Computes order flow imbalance
* Uses regression to model price response
* Generates trading signals from pressure shifts
* Visualizes price, imbalance, and PnL
* Includes 3D visualization of time, imbalance, and price

## How to run

pip install numpy matplotlib scikit-learn
python order_flow_pressure_model.py

---

# 3. Alpha Factor Explorer

## Overview

Explores common alpha factors like momentum, mean reversion, and volatility to understand their predictive power on future returns.

## What it does

* Generates synthetic stock price data
* Computes multiple alpha factors
* Uses regression to predict returns
* Visualizes factor relationships and importance
* Displays correlation heatmaps and trading signals

## How to run

pip install numpy pandas matplotlib seaborn scikit-learn
python main.py

---

# Disclaimer

These projects are for educational and research purposes only.
They are not intended for real trading, financial advice, or investment decisions.

---

# Notes

* All data is synthetically generated
* Runs on CPU (no GPU required)
* Built for learning quantitative finance and AI concepts

---

# License

MIT License (recommended)
