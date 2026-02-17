# analyzer.py - Sales Data Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class SalesAnalyzer:
    """Analyzes sales data and generates a structured text report"""
    
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        self.load_data()
    
    def load_data(self):
        """Load sales data and format date columns"""
        try:
            self.df = pd.read_csv(r'C:\Users\PC World\OneDrive\Desktop\DevArena_INTERNSHIP\week7-sales-analysis\sales_data_2024_full_analysis.csv')
            if 'Order_Date' in self.df.columns:
                self.df['Order_Date'] = pd.to_datetime(self.df['Order_Date'])
            print(f"✅ Data loaded successfully. Shape: {self.df.shape}")
        except Exception as e:
            print(f"❌ Error loading data: {e}")

    def clean_data(self):
        """Standard cleaning: duplicates and missing values"""
        if self.df is None: return
        self.df = self.df.drop_duplicates()
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].median())
        categorical_cols = self.df.select_dtypes(include=['object']).columns
        self.df[categorical_cols] = self.df[categorical_cols].fillna("Unknown")

    def generate_formatted_report(self):
        """Generates the report in the specific requested format"""
        if self.df is None: return "No data loaded."
        
        # 1. Period and Basic Stats
        start_date = self.df['Order_Date'].min().strftime('%b %Y')
        end_date = self.df['Order_Date'].max().strftime('%b %Y')
        total_sales = self.df['Total_Sales'].sum()
        
        # 2. Monthly Trends
        df_monthly = self.df.copy()
        df_monthly['month_year'] = df_monthly['Order_Date'].dt.to_period('M')
        monthly_trends = df_monthly.groupby('month_year')['Total_Sales'].sum()
        avg_monthly_sales = monthly_trends.mean()
        
        # 3. Top Category
        cat_sales = self.df.groupby('Category')['Total_Sales'].sum()
        top_cat_name = cat_sales.idxmax()
        top_cat_val = cat_sales.max()
        
        # 4. Top 5 Products
        top_products = self.df.groupby('Product_Name')['Total_Sales'].sum().sort_values(ascending=False).head(5)
        
        # 5. Customer Insights
        total_customers = self.df['Customer_ID'].nunique()
        avg_order_val = self.df['Total_Sales'].mean()
        customer_counts = self.df['Customer_ID'].value_counts()
        repeat_customers_count = len(customer_counts[customer_counts > 1])
        repeat_perc = (repeat_customers_count / total_customers) * 100 if total_customers > 0 else 0
        
        # Assemble Format
        report = [
            "📊 SALES DATA ANALYSIS REPORT",
            "===============================",
            "",
            f"📅 Analysis Period: {start_date} - {end_date}",
            f"💰 Total Sales: ${total_sales:,.0f}",
            f"📈 Average Monthly Sales: ${avg_monthly_sales:,.0f}",
            f"🏆 Top Product Category: {top_cat_name} (${top_cat_val:,.0f})",
            "",
            "📈 Monthly Sales Trend:"
        ]
        
        for month, val in monthly_trends.items():
            report.append(f"- {month.strftime('%b')}: ${val:,.0f}")
        
        report.append("")
        report.append("📦 Top 5 Products:")
        for i, (name, val) in enumerate(top_products.items(), 1):
            report.append(f"{i}. {name}: ${val:,.0f}")
            
        report.append("")
        report.append("📊 Customer Insights:")
        report.append(f"- Total Customers: {total_customers:,}")
        report.append(f"- Average Order Value: ${avg_order_val:,.2f}")
        report.append(f"- Repeat Customers: {repeat_customers_count:,} ({repeat_perc:.1f}%)")
        
        return "\n".join(report)

# Execution block
if __name__ == "__main__":
    analyzer = SalesAnalyzer('sales_data_2024_full_analysis.csv')
    analyzer.clean_data()
    print("\n" + analyzer.generate_formatted_report())