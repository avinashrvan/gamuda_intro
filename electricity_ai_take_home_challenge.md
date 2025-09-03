# Take-Home AI Challenge: Electricity Consumption Forecasting

**Role:** AI Engineer (Fresh Graduate)  
**Duration:** Approx. 2 Days  
**Keyword:** Electricity

## 🧠 Overview

Create a machine learning pipeline that forecasts **electricity consumption** over time based on past usage and contextual features. This challenge evaluates your ability to handle time series data, build forecasting models, and deploy them in a usable format.

## 📌 Objectives

1. **Data Preparation**
   - Use or simulate a time series dataset with hourly or daily electricity consumption.
   - Fields can include: `timestamp`, `consumption_kWh`, `temperature`, `day_of_week`, `hour`, `is_holiday`.

2. **Modeling**
   - Train a forecasting model (e.g., Linear Regression, XGBoost, Prophet, or LSTM) to predict future consumption.
   - Include preprocessing (e.g., feature engineering, normalization) and evaluate using RMSE, MAE, or MAPE.

3. **Deployment**
   - Build a minimal web interface or API where users can input parameters (e.g., date/time, weather) and view the forecast.
   - Tools: Flask, Streamlit, FastAPI, or Gradio.

4. **Bonus (Optional)**
   - Visualize historical and predicted consumption.
   - Deploy online (e.g., Hugging Face Spaces, Render, or Railway).

## 🧪 Deliverables

- Complete code (GitHub or zip).
- A `README.md` including:
  - Dataset details and modeling approach.
  - Setup and usage instructions.
  - Screenshot or hosted demo (if available).
- Short write-up: how would you scale this to a national or smart grid level?

## ✅ Evaluation Criteria

- Quality of data preprocessing and modeling.
- Forecast accuracy and clarity of analysis.
- Simplicity and effectiveness of the interface.
- Code structure and documentation.

---

**Tip:** You can simulate your own dataset in Python if needed. Emphasize modular pipeline design, reproducibility, and ease of use over model complexity.
