# SQL Analytics — Business Insights Case Study

**Role Simulation:** Data Analyst / Analytics Consultant  
**Goal:** Demonstrate SQL querying, business KPI reporting, and Python visualization over a small relational dataset.

## Dataset
- Self-generated sample data (~1k orders) across three tables:
  - `orders(order_id, customer_id, order_date, product_id, quantity, unit_price)`
  - `customers(customer_id, name, region, join_date)`
  - `products(product_id, product_name, category)`

## Questions answered (examples)
1) What is monthly revenue and its trend?  
2) Which products drive the top 20% of revenue?  
3) New vs. repeat customer revenue mix?  
4) Revenue by region?

## Workflow
- Load CSVs → query with SQL (DuckDB/SQLite) inside a notebook
- Visualize results with Pandas/Matplotlib/Seaborn
- Summarize KPIs for stakeholders

## Files


## Next steps
- Add more dimensions (promotions, channel)
- Parameterize queries for re-use
- Export KPI tables for dashboards
