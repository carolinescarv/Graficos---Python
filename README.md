# E-commerce Data Visualization
## Overview

This project analyzes e-commerce datasets and visualizes key patterns using Python. It helps understand product ratings, prices, sales, and trends.

The project now includes **two parts**:

1. **Static analysis of `ecommerce_estatistica.csv`** – original visualizations using Python and Plotly/Matplotlib.  
2. **Interactive dashboard of the same dataset** – built with Dash, with dynamic charts that update based on season selection.

## Dataset

File: `ecommerce_estatistica.csv`

Contains columns such as:  
- Price (Preço)  
- Quantity Sold (Qtd_Vendidos)  
- Rating (Nota)  
- Number of Reviews (N_Avaliações)  
- Discount (Desconto)  
- Brand (Marca)  
- Material  
- Gender (Gênero)  
- Season (Temporada)  

## Visualizations

### Static Visualizations (Original)
- Histogram – Distribution of ratings.  
- Scatter Plot – Price vs. Number of Reviews.  
- Heatmap – Correlation between numeric variables.  
- Bar Chart – Number of products per season.  
- Pie Chart – Product distribution by gender.  
- Density Plot – Price distribution.  
- Regression Plot – Quantity sold vs. ratings.

### Interactive Dashboard (New)
- Bar Chart – Number of products per season, dynamically updated based on the season(s) selected in the checklist.  
- Fixed charts included in the dashboard: Histogram, Scatter Plot, Heatmap, Pie Chart, Density Plot, and Regression Plot.

## How to Run

**Clone the repository:**

```bash
git clone https://github.com/yourusername/your-repo.git
Install dependencies:

bash
Copy code
pip install pandas matplotlib plotly dash
Run the interactive dashboard:

bash
Copy code
python dash_ecommerce.py
Then open your browser at http://127.0.0.1:8050/ to access the dashboard.

