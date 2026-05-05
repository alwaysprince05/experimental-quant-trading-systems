import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from scipy.interpolate import griddata
from scipy.spatial import cKDTree

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="QuantLab Pro | Prince Maurya",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PREMIUM CSS STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono&display=swap');
    
    :root {
        --primary-color: #00d4ff;
        --bg-color: #0e1117;
        --card-bg: #161b22;
        --border-color: #30363d;
    }

    .stApp {
        background-color: var(--bg-color);
        font-family: 'Inter', sans-serif;
    }

    .main-title {
        font-size: 3rem !important;
        font-weight: 700 !important;
        background: linear-gradient(90deg, #00d4ff, #0055ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem !important;
    }

    .sub-title {
        color: #8b949e;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* Card Styling */
    div[data-testid="stVerticalBlock"] > div:has(div.card) {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .metric-card {
        background: #1c2128;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0d1117;
        border-right: 1px solid var(--border-color);
    }

    /* Plotly Customization */
    .js-plotly-plot {
        border-radius: 12px;
        overflow: hidden;
    }

    /* Streamlit overrides */
    .stSlider > label { font-weight: 600; color: #c9d1d9; }
    .stSelectbox > label { font-weight: 600; color: #c9d1d9; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/crystal-diamond.png", width=80)
    st.markdown("# QuantLab **Pro**")
    st.markdown("---")
    
    app_mode = st.selectbox(
        "⚡ Select Analytical Module",
        ["Volatility Surface Model", "Order Flow Pressure Model", "Alpha Factor Explorer"],
        index=0
    )
    
    st.markdown("---")
    st.markdown("### 🛠️ Global Settings")
    dark_mode = st.toggle("Cinema Mode", value=True)
    precision = st.select_slider("Calculation Precision", options=["Low", "Medium", "High"], value="Medium")
    
    st.markdown("---")
    st.info("Created by **Prince Maurya**\n\nExperimental Quant Systems v2.0")

# --- MAIN HEADER ---
st.markdown('<h1 class="main-title">Quant Trading Analytics</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Advanced Quantitative Modeling & Algorithmic Visualization Engine</p>', unsafe_allow_html=True)

# --- DATA GENERATION UTILITIES ---
@st.cache_data
def get_vol_surface_data(n, t_max, seed):
    np.random.seed(seed)
    time = np.linspace(0, t_max, n)
    volatility = np.abs(np.random.normal(0.2, 0.05, n))
    price = np.zeros(n); price[0] = 100
    for i in range(1, n):
        drift = 0.05 * (t_max / n)
        shock = volatility[i] * np.random.normal(0, 1)
        price[i] = price[i-1] * np.exp(drift - 0.5 * volatility[i]**2 + shock * np.sqrt(t_max/n))
    return time, volatility, price

# --- APP MODES ---
if app_mode == "Volatility Surface Model":
    # --- VOLATILITY SURFACE UI ---
    st.subheader("📈 Volatility Surface Analysis")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        n_points = st.number_input("Sample Size", 50, 1000, 250)
    with c2:
        t_max = st.slider("Time Horizon (Days)", 10, 250, 100)
    with c3:
        degree = st.slider("Surface Complexity", 1, 6, 3)
    with c4:
        seed = st.number_input("Random Seed", 1, 9999, 42)

    time, vol, price = get_vol_surface_data(n_points, t_max, seed)
    
    # Modeling
    X = np.column_stack((time, vol))
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)
    reg = LinearRegression().fit(X_poly, price)

    grid_t = np.linspace(time.min(), time.max(), 50)
    grid_v = np.linspace(vol.min(), vol.max(), 50)
    T_grid, V_grid = np.meshgrid(grid_t, grid_v)
    X_grid = np.column_stack((T_grid.ravel(), V_grid.ravel()))
    P_grid = reg.predict(poly.transform(X_grid)).reshape(T_grid.shape)

    # Visualization
    col_plot, col_stats = st.columns([3, 1])
    
    with col_plot:
        fig = go.Figure(data=[go.Surface(
            z=P_grid, x=grid_t, y=grid_v, 
            colorscale='IceFire', 
            showscale=True,
            colorbar=dict(title="Price", thickness=15)
        )])
        fig.update_layout(
            title='Interactive Volatility Surface (Price Prediction)',
            template="plotly_dark",
            scene=dict(
                xaxis_title='Time',
                yaxis_title='Vol',
                zaxis_title='Price',
                camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))
            ),
            margin=dict(l=0, r=0, b=0, t=40),
            height=600
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_stats:
        st.markdown("### 📊 Metrics")
        st.metric("Avg Price", f"${price.mean():.2f}", delta=f"{((price[-1]/price[0])-1)*100:.1f}%")
        st.metric("Avg Volatility", f"{vol.mean()*100:.2f}%")
        st.metric("Model R² Score", f"{reg.score(X_poly, price):.4f}")
        
        st.markdown("---")
        st.markdown("**Insights:** The surface indicates how asset pricing shifts relative to time-decay and volatility expansion.")

    # Performance
    st.markdown("### ⚡ Strategy Performance Simulation")
    dP_dt, _ = np.gradient(P_grid, grid_t, grid_v)
    kdtree = cKDTree(np.column_stack((T_grid.ravel(), V_grid.ravel())))
    _, idxs = kdtree.query(np.column_stack((time, vol)))
    slope = dP_dt.ravel()[idxs]
    signals = np.where(slope > 0, 1, -1)
    
    pnl = np.zeros(len(time)); pos = 0
    for i in range(1, len(time)):
        if signals[i] != signals[i-1]: pos = signals[i]
        pnl[i] = pnl[i-1] + pos * (price[i] - price[i-1])

    perf_fig = go.Figure()
    perf_fig.add_trace(go.Scatter(x=time, y=price, name="Asset Price", line=dict(color='#00d4ff', width=1.5)))
    perf_fig.add_trace(go.Scatter(x=time, y=pnl+100, name="Strategy Equity", line=dict(color='#00ff88', width=2, dash='dot')))
    perf_fig.update_layout(template="plotly_dark", height=400, margin=dict(t=20), hovermode="x unified")
    st.plotly_chart(perf_fig, use_container_width=True)

elif app_mode == "Order Flow Pressure Model":
    # --- ORDER FLOW UI ---
    st.subheader("🌊 Order Flow Microstructure Analysis")
    
    col_settings, col_display = st.columns([1, 3])
    
    with col_settings:
        st.markdown("#### Config")
        steps = st.slider("Simulation steps", 100, 1000, 400)
        noise_level = st.slider("Market Noise", 0.1, 2.0, 0.5)
        thresh_pct = st.slider("Imbalance Threshold", 50, 99, 85)
        
    # Logic
    np.random.seed(42)
    time = np.arange(steps)
    buy = np.abs(np.random.normal(100, 20, steps))
    sell = np.abs(np.random.normal(100, 20, steps))
    imbalance = buy - sell
    
    price = [100.0]
    for i in range(1, steps):
        price.append(price[-1] + 0.02 * np.tanh(imbalance[i-1]/50) + np.random.normal(0, noise_level))
    price = np.array(price)
    
    threshold = np.percentile(np.abs(imbalance), thresh_pct)
    pos = np.where(imbalance > threshold, 1, np.where(imbalance < -threshold, -1, 0))
    pnl = np.cumsum(np.concatenate([[0], pos[:-1] * np.diff(price)]))

    with col_display:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time, y=price, name="Market Price", line=dict(color='#00d4ff')))
        fig.add_trace(go.Bar(x=time, y=imbalance, name="Order Imbalance", yaxis="y2", 
                             marker_color=np.where(imbalance > 0, '#00ff88', '#ff4b4b'), opacity=0.3))
        fig.update_layout(
            template="plotly_dark",
            yaxis=dict(title="Price"),
            yaxis2=dict(title="Imbalance", overlaying="y", side="right"),
            height=500, margin=dict(t=30)
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### 💹 Equity Growth")
    st.area_chart(pd.DataFrame({'Cumulative PnL': pnl}, index=time), color="#00ff88")

elif app_mode == "Alpha Factor Explorer":
    # --- ALPHA FACTOR UI ---
    st.subheader("🔍 Alpha Generation & Factor Discovery")
    
    np.random.seed(42)
    N = 300
    prices = [100]
    for _ in range(N): prices.append(prices[-1] * np.exp(np.random.normal(0.0005, 0.01)))
    df = pd.DataFrame({'price': prices})
    df['returns'] = df['price'].pct_change()
    df['momentum'] = df['returns'].rolling(10).mean()
    df['mean_reversion'] = df['price'] - df['price'].rolling(20).mean()
    df['vol'] = df['returns'].rolling(20).std()
    df['future_ret'] = df['returns'].shift(-1)
    df = df.dropna()

    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("#### Factor Interaction")
        fig = px.scatter(df, x="momentum", y="mean_reversion", color="future_ret",
                         size=df['vol'].abs()*100,
                         color_continuous_scale="RdYlGn",
                         title="Momentum vs Mean Reversion Matrix")
        fig.update_layout(template="plotly_dark", height=450)
        st.plotly_chart(fig, use_container_width=True)
        
    with c2:
        st.markdown("#### Return Distribution")
        fig = px.violin(df, y="returns", box=True, points="all", color_discrete_sequence=['#00d4ff'])
        fig.update_layout(template="plotly_dark", height=450)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### 🧠 Prediction Model (Factor Importance)")
    X = df[['momentum', 'mean_reversion', 'vol']].values
    y = df['future_ret'].values
    model = LinearRegression().fit(X, y)
    
    importance = pd.DataFrame({
        'Factor': ['Momentum', 'Mean Reversion', 'Volatility'],
        'Weight': np.abs(model.coef_)
    }).sort_values('Weight', ascending=False)
    
    st.bar_chart(importance.set_index('Factor'), color="#00d4ff")

st.markdown("---")
st.caption("⚠️ **Disclaimer:** All data is synthetically generated for research purposes. This dashboard does not provide financial advice.")
