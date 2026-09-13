# Capstone: Demand Forecasting System ("DFS 1.0")

Trimester 5 capstone project (early 2020) — an end-to-end demand forecasting system for a food-service business, deployed as a Flask web application. Combines several techniques in one working pipeline rather than isolated exercises.

## What it does

1. **Data aggregation** — `EXL_agg.py`, `CLEANING.py`, `d_stats.py` aggregate raw order data into monthly (`CAP_MONTHwise/`) and total (`CAP_AGGRG/`) summaries.
2. **Time-series forecasting (ARIMA)** — `forecast_arima_model_function.py`, `combi_forecast.py`, `dateind_forecast.py`, `model.py` forecast future demand from the aggregated history.
3. **Market basket analysis (Apriori)** — `mba_association.py` (using `mlxtend`'s `apriori`/`association_rules`) and `market_basket_trial.py` mine item co-occurrence patterns — which items tend to be ordered together — from `APRIORI.xlsx`.
4. **Order quantity analysis** — `orderquantity.py` analyzes most-ordered items (treemap visualization via `squarify`).
5. **Web app** — `app1.py` / `deploy.py` (Flask entry points), `layout.py` / `layout_re.py`, `templates/`, `static/` present the forecasts and analysis through a browser UI ("DFS 1.0").

## Running it

Entry point is `app1.py` (or `deploy.py` for the deployment variant). Requires the Python packages imported at the top of each file (pandas, statsmodels/ARIMA tooling, mlxtend, squarify, Flask). File paths in some scripts are hardcoded to the original local environment and would need updating to run today.
