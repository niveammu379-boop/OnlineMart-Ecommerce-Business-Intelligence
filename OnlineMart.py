import pandas as pd
# -----------------------------
# CUSTOMERS DATA
# -----------------------------
customers_data = {
    "customer_id": ["C001", "C002", "C003", "C004", "C005",
                    "C006", "C007", "C008", "C009", "C010",
                    "C011", "C012", "C013", "C014", "C015"],
    "customer_name": ["Arjun Kumar", "Priya Sharma", "Rahul Verma", "Divya Raj", "Karthik S",
                      "Ananya Singh", "Vijay Kumar", "Sneha R", "Rohit Mehta", "Meena Devi",
                      "Sanjay Patel", "Keerthana M", "Naveen R", "Aishwarya K", "Mohammed Ali"],
    "customer_age": [28, 32, 25, 29, 35,
                     27, 41, 24, 38, 31,
                     45, 26, 33, 30, 37],
    "customer_gender": ["Male", "Female", "Male", "Female", "Male",
                        "Female", "Male", "Female", "Male", "Female",
                        "Male", "Female", "Male", "Female", "Male"],
    "customer_city": ["Chennai", "Bengaluru", "Mumbai", "Coimbatore", "Hyderabad",
                      "Delhi", "Salem", "Kochi", "Pune", "Madurai",
                      "Ahmedabad", "Tiruchirappalli", "Mysuru", "Bengaluru", "Kolkata"],
    "customer_state": ["Tamil Nadu", "Karnataka", "Maharashtra", "Tamil Nadu", "Telangana",
                       "Delhi", "Tamil Nadu", "Kerala", "Maharashtra", "Tamil Nadu",
                       "Gujarat", "Tamil Nadu", "Karnataka", "Karnataka", "West Bengal"],
    "customer_segment": ["Regular", "Premium", "Regular", "Premium", "Regular",
                         "Premium", "Regular", "New", "Premium", "Regular",
                         "Premium", "New", "Regular", "Premium", "Regular"],
    "registration_date": ["2025-01-15", "2025-02-10", "2025-02-22", "2025-03-05", "2025-03-18",
                          "2025-04-02", "2025-04-15", "2025-05-01", "2025-05-20", "2025-06-08",
                          "2025-06-21", "2025-07-04", "2025-07-19", "2025-08-03", "2025-08-17"]}
customers = pd.DataFrame(customers_data)
# -----------------------------
# PRODUCTS DATA
# -----------------------------
products_data = {
    "product_id": ["P001", "P002", "P003", "P004", "P005",
                   "P006", "P007", "P008", "P009", "P010",
                   "P011", "P012", "P013", "P014", "P015"],
    "product_name": ["Laptop", "Smartphone", "Wireless Mouse", "Keyboard", "Headphones",
                     "Smart Watch", "T-Shirt", "Jeans", "Running Shoes", "Backpack",
                     "Coffee Maker", "Mixer Grinder", "Office Chair", "Table Lamp",
                     "Bluetooth Speaker"],
    "category": ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics",
                 "Electronics", "Fashion", "Fashion", "Fashion", "Fashion",
                 "Home", "Home", "Furniture", "Home", "Electronics"],
    "subcategory": ["Computers", "Mobile", "Accessories", "Accessories", "Audio",
                    "Wearables", "Clothing", "Clothing", "Footwear", "Bags",
                    "Kitchen", "Kitchen", "Chairs", "Lighting", "Audio"],
    "brand": ["Dell", "Samsung", "Logitech", "HP", "Sony",
              "Noise", "Puma", "Levi's", "Adidas", "Skybags",
              "Philips", "Preethi", "FeatherLite", "Wipro", "JBL"],
    "unit_price": [55000, 28000, 1200, 1800, 3500,
                   2500, 1200, 2500, 4500, 1800,
                   4500, 3800, 8500, 1500, 4200],
    "cost_price": [47000, 23000, 700, 1100, 2400,
                   1600, 650, 1500, 2800, 1000,
                   3000, 2500, 6000, 850, 2900],
    "supplier": ["TechSupply", "MobileHub", "TechSupply", "TechSupply", "AudioWorld",
                 "WearTech", "FashionHub", "FashionHub", "ShoeWorld", "BagWorld",
                 "HomeSupply", "HomeSupply", "FurnitureHub", "HomeSupply", "AudioWorld"]}
products = pd.DataFrame(products_data)
print("Customers Data:")
print(customers.head())
print("\nCustomers Shape:")
print(customers.shape)
print("\nProducts Data:")
print(products.head())
print("\nProducts Shape:")
print(products.shape)
# -----------------------------
# ORDERS DATA
# -----------------------------
orders_data = {
    "order_id": ["ORD10001", "ORD10002", "ORD10003", "ORD10004", "ORD10005",
                 "ORD10006", "ORD10007", "ORD10008", "ORD10009", "ORD10010",
                 "ORD10011", "ORD10012", "ORD10013", "ORD10014", "ORD10015"],
    "customer_id": ["C001", "C002", "C003", "C004", "C005",
                    "C006", "C007", "C008", "C009", "C010",
                    "C011", "C012", "C013", "C014", "C015"],
    "order_date": ["2026-01-05", "2026-01-08", "2026-01-12", "2026-01-15", "2026-01-20",
                   "2026-01-24", "2026-02-02", "2026-02-07", "2026-02-14", "2026-02-20",
                   "2026-02-25", "2026-03-03", "2026-03-08", "2026-03-15", "2026-03-22"],
    "product_id": ["P001", "P003", "P008", "P011", "P002",
                   "P009", "P013", "P007", "P005", "P014",
                   "P006", "P012", "P010", "P015", "P004"],
    "product_name": ["Laptop", "Wireless Mouse", "Jeans", "Coffee Maker", "Smartphone",
                     "Running Shoes", "Office Chair", "T-Shirt", "Headphones", "Table Lamp",
                     "Smart Watch", "Mixer Grinder", "Backpack", "Bluetooth Speaker", "Keyboard"],
    "category": ["Electronics", "Electronics", "Fashion", "Home", "Electronics",
                 "Fashion", "Furniture", "Fashion", "Electronics", "Home",
                 "Electronics", "Home", "Fashion", "Electronics", "Electronics"],
    "subcategory": ["Computers", "Accessories", "Clothing", "Kitchen", "Mobile",
                    "Footwear", "Chairs", "Clothing", "Audio", "Lighting",
                    "Wearables", "Kitchen", "Bags", "Audio", "Accessories"],
    "quantity": [1, 2, 1, 1, 1,
                 2, 1, 3, 1, 2,
                 1, 1, 2, 1, 1],
    "unit_price": [55000, 1200, 2500, 4500, 28000,
                   4500, 8500, 1200, 3500, 1500,
                   2500, 3800, 1800, 4200, 1800],
    "discount": [5, 10, 0, 8, 12,
                 5, 10, 0, 15, 5,
                 5, 10, 0, 8, 5],
    "shipping_cost": [500, 100, 150, 250, 300,
                      200, 600, 150, 100, 120,
                      100, 250, 150, 200, 100],
    "payment_method": ["UPI", "Card", "UPI", "Card", "Net Banking",
                       "UPI", "Card", "UPI", "Card", "UPI",
                       "UPI", "Card", "UPI", "Net Banking", "Card"],
    "order_status": ["Delivered", "Delivered", "Delivered", "Delivered", "Delivered",
                     "Delivered", "Delivered", "Delivered", "Delivered", "Cancelled",
                     "Delivered", "Delivered", "Delivered", "Delivered", "Delivered"],
    "return_status": ["No", "No", "No", "No", "No",
                      "No", "No", "No", "Returned", "No",
                      "No", "No", "No", "No", "No"],
    "customer_city": ["Chennai", "Bengaluru", "Mumbai", "Coimbatore", "Hyderabad",
                      "Delhi", "Salem", "Kochi", "Pune", "Madurai",
                      "Ahmedabad", "Tiruchirappalli", "Mysuru", "Bengaluru", "Kolkata"],
    "customer_state": ["Tamil Nadu", "Karnataka", "Maharashtra", "Tamil Nadu", "Telangana",
                       "Delhi", "Tamil Nadu", "Kerala", "Maharashtra", "Tamil Nadu",
                       "Gujarat", "Tamil Nadu", "Karnataka", "Karnataka", "West Bengal"]}
orders = pd.DataFrame(orders_data)
print("\nOrders Data:")
print(orders.head())
print("\nOrders Shape:")
print(orders.shape)
# -----------------------------
# SAVE DATA TO EXCEL
# -----------------------------
with pd.ExcelWriter("OnlineMart_Ecommerce_Data.xlsx", engine="openpyxl") as writer:
    customers.to_excel(writer,sheet_name="Customers",index=False)
    products.to_excel(writer,sheet_name="Products",index=False)
    orders.to_excel(writer,sheet_name="Orders",index=False)
print("\nExcel file created successfully!")
print("File: OnlineMart_Ecommerce_Data.xlsx")
# ============================================================
# STEP 6 - GENERATE 500 REALISTIC E-COMMERCE ORDERS
# ============================================================
import random
from datetime import datetime, timedelta
# Number of new orders
num_orders = 500
# Starting Order ID
start_order_id = 10016
# Date range
start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 8, 31)
# Lists for random selection
payment_methods = ["UPI", "Card", "Net Banking", "Cash on Delivery"]
order_statuses = ["Delivered", "Delivered", "Delivered",
                  "Delivered", "Cancelled", "Returned"]
return_statuses = ["No", "No", "No", "No", "Yes"]
# Store generated orders
generated_orders = []
for i in range(num_orders):
    # Generate Order ID
    order_id = f"ORD{start_order_id + i}"
    # Random customer
    customer = customers.sample(1).iloc[0]
    # Random product
    product = products.sample(1).iloc[0]
    # Random order date
    random_days = random.randint(0,(end_date - start_date).days)
    order_date = start_date + timedelta(days=random_days)
    # Random quantity
    quantity = random.randint(1, 5)
    # Product price
    unit_price = product["unit_price"]
    # Random discount percentage
    discount_percent = random.choice([0, 5, 10, 15, 20])
    # Calculate gross amount
    gross_amount = quantity * unit_price
    # Calculate discount
    discount_amount = gross_amount * discount_percent / 100
    # Final amount
    final_amount = gross_amount - discount_amount
    # Random shipping cost
    shipping_cost = random.choice([50, 75, 100, 150, 200, 250, 300, 500])
    # Payment method
    payment_method = random.choice(payment_methods)
    # Order status
    order_status = random.choice(order_statuses)
    # Return status
    if order_status == "Returned":
        return_status = "Yes"
    else:
        return_status = "No"
    # Create order record    
    order = {
        "order_id": order_id,
        "customer_id": customer["customer_id"],
        "order_date": order_date.strftime("%Y-%m-%d"),
        "product_id": product["product_id"],
        "product_name": product["product_name"],
        "category": product["category"],
        "subcategory": product["subcategory"],
        "brand": product["brand"],
        "quantity": quantity,
        "unit_price": unit_price,
        "discount_percent": discount_percent,
        "discount_amount": discount_amount,
        "gross_amount": gross_amount,
        "final_amount": final_amount,
        "shipping_cost": shipping_cost,
        "payment_method": payment_method,
        "order_status": order_status,
        "return_status": return_status,
        "customer_city": customer["customer_city"],
        "customer_state": customer["customer_state"]}
    generated_orders.append(order)
# Convert generated orders into DataFrame
generated_orders_df = pd.DataFrame(generated_orders)
# Display generated data
print("\nGenerated Orders Data:")
print(generated_orders_df.head())
print("\nGenerated Orders Shape:")
print(generated_orders_df.shape)
# Save generated orders separately
generated_orders_df.to_excel("OnlineMart_Generated_Orders.xlsx",index=False)
print("\n500 new orders generated successfully!")
print("File: OnlineMart_Generated_Orders.xlsx")
# ============================================================
# STEP 7 - COMBINE SEED ORDERS + GENERATED ORDERS
# ============================================================
all_orders = pd.concat([orders, generated_orders_df],ignore_index=True,sort=False)
print("\nCombined Orders Data:")
print(all_orders.head())
print("\nCombined Orders Shape:")
print(all_orders.shape)
print("\nMissing Values in Combined Orders:")
print(all_orders.isnull().sum())
print("\nLast 5 Orders:")
print(all_orders.tail())
# Save raw combined dataset
all_orders.to_excel("OnlineMart_All_Orders_Raw.xlsx",index=False)
print("\nAll orders combined successfully!")
print("File: OnlineMart_All_Orders_Raw.xlsx")
# ============================================================
# STEP 8 - DATA INSPECTION
# ============================================================
print("\n" + "=" * 60)
print("STEP 8 - DATA INSPECTION")
print("=" * 60)
# Check column names
print("\nColumn Names:")
print(all_orders.columns.tolist())
# Check data types
print("\nData Types:")
print(all_orders.dtypes)
# Check missing values
print("\nMissing Values:")
print(all_orders.isnull().sum())
# Check duplicate rows
print("\nDuplicate Rows:")
print(all_orders.duplicated().sum())
# Check unique values in important columns
print("\nOrder Status:")
print(all_orders["order_status"].value_counts())
print("\nReturn Status:")
print(all_orders["return_status"].value_counts())
print("\nPayment Method:")
print(all_orders["payment_method"].value_counts())
print("\nCategory:")
print(all_orders["category"].value_counts())
# Basic numerical statistics
print("\nNumerical Summary:")
print(all_orders.describe())
# ============================================================
# STEP 9 - DATA CLEANING
# ============================================================
print("\n" + "=" * 60)
print("STEP 9 - DATA CLEANING")
print("=" * 60)
# 1. Remove duplicate rows
all_orders = all_orders.drop_duplicates()
# 2. Remove the old discount column
all_orders = all_orders.drop(columns=["discount"])
# 3. Convert order_date to datetime
all_orders["order_date"] = pd.to_datetime(all_orders["order_date"])
# 4. Fill missing brand using product information
brand_mapping = products.set_index("product_id")["brand"]
all_orders["brand"] = all_orders["brand"].fillna(all_orders["product_id"].map(brand_mapping))
# 5. Fill missing discount percentage with 0
all_orders["discount_percent"] = all_orders["discount_percent"].fillna(0)
# 6. Calculate gross amount for missing rows
all_orders["gross_amount"] = all_orders["gross_amount"].fillna(all_orders["quantity"] * all_orders["unit_price"])
# 7. Calculate discount amount
all_orders["discount_amount"] = (all_orders["gross_amount"]* all_orders["discount_percent"]/ 100)
# 8. Calculate final amount
all_orders["final_amount"] = (all_orders["gross_amount"]- all_orders["discount_amount"])
# 9. Standardize return status
all_orders["return_status"] = all_orders["return_status"].replace({"Returned": "Yes"})
# 10. Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(all_orders.isnull().sum())
# 11. Check data types after cleaning
print("\nData Types After Cleaning:")
print(all_orders.dtypes)
# 12. Check final shape
print("\nCleaned Orders Shape:")
print(all_orders.shape)
# 13. Save cleaned dataset
all_orders.to_excel("OnlineMart_Cleaned_Orders.xlsx",index=False)
print("\nData cleaning completed successfully!")
print("File: OnlineMart_Cleaned_Orders.xlsx")
# ============================================================
# STEP 10 - DATA VALIDATION
# ============================================================
print("\n" + "=" * 60)
print("STEP 10 - DATA VALIDATION")
print("=" * 60)
# 1. Check duplicate Order IDs
print("\nDuplicate Order IDs:")
print(all_orders["order_id"].duplicated().sum())
# 2. Check duplicate Customer IDs
print("\nUnique Customers:")
print(all_orders["customer_id"].nunique())
# 3. Check invalid quantity
print("\nInvalid Quantity Records:")
print((all_orders["quantity"] <= 0).sum())
# 4. Check invalid unit price
print("\nInvalid Unit Price Records:")
print((all_orders["unit_price"] <= 0).sum())
# 5. Check invalid discount percentage
print("\nInvalid Discount Percentage Records:")
print(((all_orders["discount_percent"] < 0)|(all_orders["discount_percent"] > 100)).sum())
# 6. Check amount calculation
calculated_gross = (all_orders["quantity"] * all_orders["unit_price"])
print("\nIncorrect Gross Amount Records:")
print((all_orders["gross_amount"] != calculated_gross).sum())
# 7. Check final amount calculation
calculated_final = (all_orders["gross_amount"] - all_orders["discount_amount"])
print("\nIncorrect Final Amount Records:")
print((all_orders["final_amount"] != calculated_final).sum())
# 8. Check order status values
print("\nValid Order Status Values:")
print(all_orders["order_status"].unique())
# 9. Check return status values
print("\nValid Return Status Values:")
print(all_orders["return_status"].unique())
# 10. Final validation message
print("\nData validation completed successfully!")
# ============================================================
# STEP 11 - BASIC BUSINESS EDA
# ============================================================
print("\n" + "=" * 60)
print("STEP 11 - BASIC BUSINESS EDA")
print("=" * 60)
# Total transactions
total_orders = all_orders["order_id"].nunique()
# Total customers
total_customers = all_orders["customer_id"].nunique()
# Total quantity sold
total_quantity = all_orders["quantity"].sum()
# Total gross sales
total_gross_sales = all_orders["gross_amount"].sum()
# Total discount
total_discount = all_orders["discount_amount"].sum()
# Total final sales
total_final_sales = all_orders["final_amount"].sum()
# Average order value
average_order_value = all_orders["final_amount"].mean()
print("\nTotal Orders:")
print(total_orders)
print("\nTotal Customers:")
print(total_customers)
print("\nTotal Quantity Sold:")
print(total_quantity)
print("\nTotal Gross Sales:")
print(total_gross_sales)
print("\nTotal Discount:")
print(total_discount)
print("\nTotal Final Sales:")
print(total_final_sales)
print("\nAverage Order Value:")
print(average_order_value)
print("\nOrder Status Summary:")
print(all_orders["order_status"].value_counts())
# ============================================================
# STEP 12 - CATEGORY & PRODUCT EDA
# ============================================================
print("\n" + "=" * 60)
print("STEP 12 - CATEGORY & PRODUCT EDA")
print("=" * 60)
# 1. Category-wise sales
category_sales = (all_orders.groupby("category")["final_amount"].sum().sort_values(ascending=False))
print("\nCategory-wise Final Sales:")
print(category_sales)
# 2. Category-wise quantity
category_quantity = (all_orders.groupby("category")["quantity"].sum().sort_values(ascending=False))
print("\nCategory-wise Quantity Sold:")
print(category_quantity)
# 3. Product-wise sales
product_sales = (all_orders.groupby("product_name")["final_amount"].sum().sort_values(ascending=False))
print("\nProduct-wise Final Sales:")
print(product_sales)
# 4. Top 5 products
print("\nTop 5 Products by Sales:")
print(product_sales.head(5))
# 5. Product-wise quantity
product_quantity = (all_orders.groupby("product_name")["quantity"].sum().sort_values(ascending=False))
print("\nTop 5 Products by Quantity Sold:")
print(product_quantity.head(5))
# 6. Category-wise average order value
category_aov = (all_orders.groupby("category")["final_amount"].mean().sort_values(ascending=False))
print("\nCategory-wise Average Order Value:")
print(category_aov)
# ============================================================
# STEP 13 - CUSTOMER EDA
# ============================================================
print("\n" + "=" * 60)
print("STEP 13 - CUSTOMER EDA")
print("=" * 60)
# 1. Customer-wise order count
customer_orders = (all_orders.groupby("customer_id")["order_id"].nunique().sort_values(ascending=False))
print("\nCustomer-wise Order Count:")
print(customer_orders)
# 2. Customer-wise total quantity
customer_quantity = (all_orders.groupby("customer_id")["quantity"].sum().sort_values(ascending=False))
print("\nCustomer-wise Quantity:")
print(customer_quantity)
# 3. Customer-wise total sales
customer_sales = (all_orders.groupby("customer_id")["final_amount"].sum().sort_values(ascending=False))
print("\nCustomer-wise Final Sales:")
print(customer_sales)
# 4. Top 5 customers by sales
print("\nTop 5 Customers by Sales:")
print(customer_sales.head(5))
# 5. Customer-wise average order value
customer_aov = (all_orders.groupby("customer_id")["final_amount"].mean().sort_values(ascending=False))
print("\nCustomer-wise Average Order Value:")
print(customer_aov)
# 6. Top 5 customers by order frequency
print("\nTop 5 Customers by Order Frequency:")
print(customer_orders.head(5))
# ============================================================
# STEP 14 - CUSTOMER DEMOGRAPHIC ANALYSIS
# ============================================================
print("\n" + "=" * 60)
print("STEP 14 - CUSTOMER DEMOGRAPHIC ANALYSIS")
print("=" * 60)
# Merge customer details with order data
customer_analysis = all_orders.merge(customers[["customer_id","customer_name","customer_age","customer_gender","customer_segment"]],on="customer_id",how="left")
# 1. Segment-wise sales
segment_sales = (customer_analysis.groupby("customer_segment")["final_amount"].sum().sort_values(ascending=False))
print("\nCustomer Segment-wise Final Sales:")
print(segment_sales)
# 2. Segment-wise order count
segment_orders = (customer_analysis.groupby("customer_segment")["order_id"].nunique().sort_values(ascending=False))
print("\nCustomer Segment-wise Order Count:")
print(segment_orders)
# 3. City-wise sales
city_sales = (customer_analysis.groupby("customer_city")["final_amount"].sum().sort_values(ascending=False))
print("\nCity-wise Final Sales:")
print(city_sales)
# 4. State-wise sales
state_sales = (customer_analysis.groupby("customer_state")["final_amount"].sum().sort_values(ascending=False))
print("\nState-wise Final Sales:")
print(state_sales)
# 5. Gender-wise sales
gender_sales = (customer_analysis.groupby("customer_gender")["final_amount"].sum().sort_values(ascending=False))
print("\nGender-wise Final Sales:")
print(gender_sales)
# 6. Age group analysis
customer_analysis["age_group"] = pd.cut(customer_analysis["customer_age"],bins=[0, 25, 35, 50, 100],labels=["18-25", "26-35", "36-50", "51+"])
age_group_sales = (customer_analysis.groupby("age_group", observed=True)["final_amount"].sum().sort_values(ascending=False))
print("\nAge Group-wise Final Sales:")
print(age_group_sales)
# ============================================================
# STEP 15 - ORDER & PAYMENT ANALYSIS
# ============================================================
print("\n" + "=" * 60)
print("STEP 15 - ORDER & PAYMENT ANALYSIS")
print("=" * 60)
# 1. Payment method-wise order count
payment_orders = (all_orders.groupby("payment_method")["order_id"].nunique().sort_values(ascending=False))
print("\nPayment Method-wise Order Count:")
print(payment_orders)
# 2. Payment method-wise final sales
payment_sales = (all_orders.groupby("payment_method")["final_amount"].sum().sort_values(ascending=False))
print("\nPayment Method-wise Final Sales:")
print(payment_sales)
# 3. Order status-wise final sales
status_sales = (all_orders.groupby("order_status")["final_amount"].sum().sort_values(ascending=False))
print("\nOrder Status-wise Final Sales:")
print(status_sales)
# 4. Return count
return_count = (all_orders["return_status"].eq("Yes").sum())
print("\nTotal Returned Orders:")
print(return_count)
# 5. Return rate
return_rate = (return_count / len(all_orders) * 100)
print("\nReturn Rate:")
print(round(return_rate, 2), "%")
# 6. Cancellation count
cancelled_count = (all_orders["order_status"].eq("Cancelled").sum())
print("\nTotal Cancelled Orders:")
print(cancelled_count)
# 7. Cancellation rate
cancellation_rate = (cancelled_count / len(all_orders) * 100)
print("\nCancellation Rate:")
print(round(cancellation_rate, 2), "%")
# 8. Payment method vs order status
payment_status = pd.crosstab(all_orders["payment_method"],all_orders["order_status"])
print("\nPayment Method vs Order Status:")
print(payment_status)
# 9. Payment method-wise average order value
payment_aov = (all_orders.groupby("payment_method")["final_amount"].mean().sort_values(ascending=False))
print("\nPayment Method-wise Average Order Value:")
print(payment_aov)
print("\nOrder & payment analysis completed successfully!")
# ============================================================
# STEP 16 - TIME-BASED SALES ANALYSIS
# ============================================================
print("\n" + "=" * 60)
print("STEP 16 - TIME-BASED SALES ANALYSIS")
print("=" * 60)
# 1. Create month column
all_orders["order_month"] = (all_orders["order_date"].dt.to_period("M"))
# 2. Monthly order count
monthly_orders = (all_orders.groupby("order_month")["order_id"].nunique())
print("\nMonthly Order Count:")
print(monthly_orders)
# 3. Monthly sales
monthly_sales = (all_orders.groupby("order_month")["final_amount"].sum())
print("\nMonthly Sales:")
print(monthly_sales)
# 4. Monthly quantity sold
monthly_quantity = (all_orders.groupby("order_month")["quantity"].sum())
print("\nMonthly Quantity Sold:")
print(monthly_quantity)
# 5. Monthly AOV
monthly_aov = (monthly_sales / monthly_orders)
print("\nMonthly Average Order Value:")
print(monthly_aov.round(2))
# 6. Highest sales month
highest_sales_month = monthly_sales.idxmax()
highest_sales_value = monthly_sales.max()
print("\nHighest Sales Month:")
print(highest_sales_month)
print("Sales:", highest_sales_value)
# 7. Lowest sales month
lowest_sales_month = monthly_sales.idxmin()
lowest_sales_value = monthly_sales.min()
print("\nLowest Sales Month:")
print(lowest_sales_month)
print("Sales:", lowest_sales_value)
print("\nTime-based sales analysis completed successfully!")
# Step 16.1: Monthly Performance Status
monthly_analysis = pd.DataFrame({"sales": monthly_sales,"quantity": monthly_quantity,"order_count": monthly_orders,"AOV": monthly_aov})
monthly_analysis["sales_change_%"] = (monthly_analysis["sales"].pct_change().mul(100).round(2))
monthly_analysis["sales_status"] = monthly_analysis["sales_change_%"].apply(lambda x: "Growth" if x > 0 else "Decline" if x < 0 else "No Change")
print("\nMonthly Performance Status:")
print(monthly_analysis)
# Step 16.2: Monthly Trend Summary
growth_months = (monthly_analysis["sales_status"] == "Growth").sum()
decline_months = (monthly_analysis["sales_status"] == "Decline").sum()
best_growth_month = monthly_analysis["sales_change_%"].idxmax()
best_growth_rate = monthly_analysis["sales_change_%"].max()
worst_decline_month = monthly_analysis["sales_change_%"].idxmin()
worst_decline_rate = monthly_analysis["sales_change_%"].min()
print("\n" + "=" * 60)
print("STEP 16.2 - MONTHLY TREND SUMMARY")
print("=" * 60)
print("\nTotal Growth Months:", growth_months)
print("Total Decline Months:", decline_months)
print("\nBest Growth Month:")
print(best_growth_month)
print("Growth Rate:", best_growth_rate, "%")
print("\nWorst Decline Month:")
print(worst_decline_month)
print("Decline Rate:", worst_decline_rate, "%")
if growth_months > decline_months:
    overall_trend = "Positive Growth Trend"
elif decline_months > growth_months:
    overall_trend = "Declining Trend"
else:
    overall_trend = "Mixed / Stable Trend"
print("\nOverall Sales Trend:")
print(overall_trend)
print("\nMonthly trend summary completed successfully!")
# ============================================================
# STEP 17.1 - DESCRIPTIVE STATISTICAL ANALYSIS
# ============================================================
print("\n" + "=" * 60)
print("STEP 17.1 - DESCRIPTIVE STATISTICAL ANALYSIS")
print("=" * 60)
# 1. Select important numerical columns
stat_columns = ["quantity","unit_price","shipping_cost","discount_percent","discount_amount","gross_amount","final_amount"]
# 2. Calculate descriptive statistics
statistical_summary = pd.DataFrame({"Mean": all_orders[stat_columns].mean(),"Median": all_orders[stat_columns].median(),"Mode": all_orders[stat_columns].mode().iloc[0],"Minimum": all_orders[stat_columns].min(),"Maximum": all_orders[stat_columns].max(),"Range": all_orders[stat_columns].max() - all_orders[stat_columns].min(),"Variance": all_orders[stat_columns].var(),"Standard_Deviation": all_orders[stat_columns].std()})
# 3. Round the values
statistical_summary = statistical_summary.round(2)
print("\nDescriptive Statistical Summary:")
print(statistical_summary)
print("\nDescriptive statistical analysis completed successfully!")
# ============================================================
# STEP 17.2 - STATISTICAL DISTRIBUTION & OUTLIER ANALYSIS
# ============================================================
print("\n" + "=" * 60)
print("STEP 17.2 - STATISTICAL DISTRIBUTION & OUTLIER ANALYSIS")
print("=" * 60)
# 1. Select important numerical columns
outlier_columns = ["quantity","unit_price","shipping_cost","discount_amount","gross_amount","final_amount"]
# 2. Calculate skewness
skewness = all_orders[outlier_columns].skew()
print("\nSkewness:")
print(skewness.round(2))
# 3. Create outlier summary
outlier_summary = []
for column in outlier_columns:
    Q1 = all_orders[column].quantile(0.25)
    Q3 = all_orders[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_limit = Q1 - (1.5 * IQR)
    upper_limit = Q3 + (1.5 * IQR)
    outliers = all_orders[(all_orders[column] < lower_limit) | (all_orders[column] > upper_limit)]
    outlier_count = len(outliers)
    outlier_summary.append({"Column": column,"Q1": Q1,"Q3": Q3,"IQR": IQR,"Lower_Limit": lower_limit,"Upper_Limit": upper_limit,"Outlier_Count": outlier_count})
# 4. Convert summary into DataFrame
outlier_summary = pd.DataFrame(outlier_summary)
# 5. Round values
outlier_summary = outlier_summary.round(2)
print("\nOutlier Analysis:")
print(outlier_summary)
print("\nStatistical distribution and outlier analysis completed successfully!")
# ============================================================
# STEP 18.1 - CUSTOMER-WISE ORDER & SALES ANALYSIS
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.1 - CUSTOMER-WISE ORDER & SALES ANALYSIS")
print("=" * 60)
# 1. Customer-wise order count
customer_order_count = (all_orders.groupby("customer_id")["order_id"].nunique())
# 2. Customer-wise total quantity
customer_quantity = (all_orders.groupby("customer_id")["quantity"].sum())
# 3. Customer-wise total sales
customer_sales = (all_orders.groupby("customer_id")["final_amount"].sum())
# 4. Customer-wise AOV
customer_aov = (customer_sales / customer_order_count)
# 5. Create customer analysis table
customer_analysis = pd.DataFrame({"order_count": customer_order_count,"total_quantity": customer_quantity,"total_sales": customer_sales,"AOV": customer_aov})
# 6. Round AOV
customer_analysis["AOV"] = customer_analysis["AOV"].round(2)
# 7. Sort by total sales
customer_analysis = customer_analysis.sort_values(by="total_sales",ascending=False)
# 8. Display result
print("\nCustomer-wise Analysis:")
print(customer_analysis)
print("\nCustomer-wise order and sales analysis completed successfully!")
# ============================================================
# STEP 18.2 - REPEAT vs ONE-TIME CUSTOMER ANALYSIS
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.2 - REPEAT vs ONE-TIME CUSTOMER ANALYSIS")
print("=" * 60)
# 1. Count orders for each customer
customer_frequency = (all_orders.groupby("customer_id")["order_id"].nunique())
# 2. Classify customers
customer_type = customer_frequency.apply(lambda x: "Repeat Customer" if x >= 2 else "One-Time Customer")
# 3. Create customer type summary
customer_type_summary = customer_type.value_counts()
print("\nCustomer Type Summary:")
print(customer_type_summary)
# 4. Calculate percentages
customer_type_percentage = (customer_type_summary / customer_type_summary.sum() * 100).round(2)
print("\nCustomer Type Percentage:")
print(customer_type_percentage)
# 5. Display individual customer classification
customer_frequency_analysis = pd.DataFrame({"order_count": customer_frequency,"customer_type": customer_type})
customer_frequency_analysis = customer_frequency_analysis.sort_values(by="order_count",ascending=False)
print("\nCustomer Frequency Analysis:")
print(customer_frequency_analysis)
print("\nRepeat vs One-Time customer analysis completed successfully!")
# ============================================================
# STEP 18.3 - CUSTOMER VALUE ANALYSIS
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.3 - CUSTOMER VALUE ANALYSIS")
print("=" * 60)
# 1. Customer-wise total orders
customer_value_orders = (all_orders.groupby("customer_id")["order_id"].nunique())
# 2. Customer-wise total quantity
customer_value_quantity = (all_orders.groupby("customer_id")["quantity"].sum())
# 3. Customer-wise total sales
customer_value_sales = (all_orders.groupby("customer_id")["final_amount"].sum())
# 4. Create customer value analysis table
customer_value = pd.DataFrame({"total_orders": customer_value_orders,"total_quantity": customer_value_quantity,"total_sales": customer_value_sales})
# 5. Calculate sales contribution percentage
customer_value["sales_percentage"] = (customer_value["total_sales"] / customer_value["total_sales"].sum()) * 100
# 6. Round percentage
customer_value["sales_percentage"] = (customer_value["sales_percentage"].round(2))
# 7. Sort customers by total sales
customer_value = customer_value.sort_values(by="total_sales",ascending=False)
# 8. Display result
print("\nCustomer Value Analysis:")
print(customer_value)
print("\nCustomer value analysis completed successfully!")
# ============================================================
# STEP 18.3.2 - CUSTOMER VALUE CLASSIFICATION
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.3.2 - CUSTOMER VALUE CLASSIFICATION")
print("=" * 60)
# Classify customers into 3 value groups
# based on their total sales
customer_value["value_segment"] = pd.qcut(customer_value["total_sales"],q=3,labels=["Low Value", "Medium Value", "High Value"])
# Display customer-wise value classification
customer_value_classification = customer_value[["total_orders","total_quantity","total_sales","sales_percentage","value_segment"]]
print("\nCustomer Value Classification:")
print(customer_value_classification)
print("\nCustomer Value Classification completed successfully!")
# ============================================================
# STEP 18.3.3 - CUSTOMER VALUE SEGMENT SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.3.3 - CUSTOMER VALUE SEGMENT SUMMARY")
print("=" * 60)
# 1. Segment-wise customer count
value_segment_customers = (customer_value.groupby("value_segment", observed=False).size())
# 2. Segment-wise total orders
value_segment_orders = (customer_value.groupby("value_segment", observed=False)["total_orders"].sum())
# 3. Segment-wise total quantity
value_segment_quantity = (customer_value.groupby("value_segment", observed=False)["total_quantity"].sum())
# 4. Segment-wise total sales
value_segment_sales = (customer_value.groupby("value_segment", observed=False)["total_sales"].sum())
# 5. Create segment summary table
value_segment_summary = pd.DataFrame({"customer_count": value_segment_customers,"total_orders": value_segment_orders,"total_quantity": value_segment_quantity,"total_sales": value_segment_sales})
# 6. Calculate sales contribution percentage
value_segment_summary["sales_percentage"] = (value_segment_summary["total_sales"] / value_segment_summary["total_sales"].sum()) * 100
# 7. Calculate average sales per customer
value_segment_summary["avg_sales_per_customer"] = (value_segment_summary["total_sales"] / value_segment_summary["customer_count"])
# 8. Round calculated values
value_segment_summary["sales_percentage"] = (value_segment_summary["sales_percentage"].round(2))
value_segment_summary["avg_sales_per_customer"] = (value_segment_summary["avg_sales_per_customer"].round(2))
# 9. Display segment summary
print("\nCustomer Value Segment Summary:")
print(value_segment_summary)
print("\nCustomer value segment summary completed successfully!")
# ============================================================
# STEP 18.3.4 - CUSTOMER VALUE BUSINESS INSIGHTS
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.3.4 - CUSTOMER VALUE BUSINESS INSIGHTS")
print("=" * 60)
highest_sales_segment = value_segment_summary["total_sales"].idxmax()
lowest_sales_segment = value_segment_summary["total_sales"].idxmin()
highest_sales_value = value_segment_summary.loc[highest_sales_segment, "total_sales"]
lowest_sales_value = value_segment_summary.loc[lowest_sales_segment, "total_sales"]
highest_sales_percentage = value_segment_summary.loc[highest_sales_segment, "sales_percentage"]
highest_avg_customer_value = value_segment_summary["avg_sales_per_customer"].idxmax()
highest_avg_value = value_segment_summary.loc[highest_avg_customer_value, "avg_sales_per_customer"]
print("\nCustomer Value Business Insights:")
print(f"1. Highest revenue segment: {highest_sales_segment}")
print(f"   Sales generated: ₹{highest_sales_value:,.2f}")
print(f"   Revenue contribution: {highest_sales_percentage:.2f}%")
print(f"\n2. Lowest revenue segment: {lowest_sales_segment}")
print(f"   Sales generated: ₹{lowest_sales_value:,.2f}")
print(f"\n3. Highest average customer value segment: " f"{highest_avg_customer_value}")
print(f"   Average sales per customer: ₹{highest_avg_value:,.2f}")
print("\n4. Business Recommendation:")
print("   Focus on retaining High Value customers, " "while developing strategies to convert Medium Value " "customers into High Value customers.")
print("\nCustomer value business insights completed successfully!")
# ============================================================
# STEP 18.4.1 - CUSTOMER REVENUE CONTRIBUTION / PARETO ANALYSIS
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.4.1 - CUSTOMER REVENUE CONTRIBUTION / PARETO ANALYSIS")
print("=" * 60)
customer_pareto = customer_value[["total_orders", "total_quantity", "total_sales"]].copy()
customer_pareto = customer_pareto.sort_values(by="total_sales",ascending=False)
customer_pareto["sales_percentage"] = (customer_pareto["total_sales"] / customer_pareto["total_sales"].sum()) * 100
customer_pareto["cumulative_sales_percentage"] = (customer_pareto["sales_percentage"].cumsum())
customer_pareto["sales_percentage"] = (customer_pareto["sales_percentage"].round(2))
customer_pareto["cumulative_sales_percentage"] = (customer_pareto["cumulative_sales_percentage"].round(2))
print("\nCustomer Revenue Contribution / Pareto Analysis:")
print(customer_pareto)
print("\nCustomer revenue contribution analysis completed successfully!")
# ============================================================
# STEP 18.4.2 - TOP 20% CUSTOMER REVENUE CONTRIBUTION
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.4.2 - TOP 20% CUSTOMER REVENUE CONTRIBUTION")
print("=" * 60)
total_customers = len(customer_pareto)
top_20_percent_count = max(1,round(total_customers * 0.20))
top_20_customers = customer_pareto.head(top_20_percent_count)
top_20_sales = top_20_customers["total_sales"].sum()
total_sales = customer_pareto["total_sales"].sum()
top_20_sales_percentage = (top_20_sales / total_sales) * 100
print("\nTop 20% Customer Analysis:")
print(f"Total Customers: {total_customers}")
print(f"Top 20% Customer Count: {top_20_percent_count}")
print(f"Top 20% Customer Sales: ₹{top_20_sales:,.2f}")
print(f"Top 20% Revenue Contribution: " f"{top_20_sales_percentage:.2f}%")
print("\nTop 20% Customers:")
print(top_20_customers[["total_orders","total_quantity","total_sales","sales_percentage"]])
print("\nTop 20% customer revenue contribution " "analysis completed successfully!")
# ============================================================
# STEP 18.4.3 - PARETO CUSTOMER CLASSIFICATION
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.4.3 - PARETO CUSTOMER CLASSIFICATION")
print("=" * 60)
pareto_customers = customer_pareto.copy()
total_customers = len(pareto_customers)
top_20_count = max(1,round(total_customers * 0.20))
top_50_count = max(top_20_count,round(total_customers * 0.50))
pareto_customers["contribution_segment"] = "Lower Contribution"
pareto_customers.iloc[:top_20_count,pareto_customers.columns.get_loc("contribution_segment")] = "Top Contribution"
pareto_customers.iloc[top_20_count:top_50_count,pareto_customers.columns.get_loc("contribution_segment")] = "Medium Contribution"
print("\nPareto Customer Classification:")
print(pareto_customers[["total_orders","total_quantity","total_sales","sales_percentage","cumulative_sales_percentage","contribution_segment"]])
print("\nContribution Segment Summary:")
print(pareto_customers["contribution_segment"].value_counts())
print("\nPareto customer classification completed successfully!")
# ============================================================
# STEP 18.4.4 - CONTRIBUTION SEGMENT SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.4.4 - CONTRIBUTION SEGMENT SUMMARY")
print("=" * 60)
contribution_customers = (pareto_customers.groupby("contribution_segment").size())
contribution_orders = (pareto_customers.groupby("contribution_segment")["total_orders"].sum())
contribution_quantity = (pareto_customers.groupby("contribution_segment")["total_quantity"].sum())
contribution_sales = (pareto_customers.groupby("contribution_segment")["total_sales"].sum())
contribution_summary = pd.DataFrame({"customer_count": contribution_customers,"total_orders": contribution_orders,"total_quantity": contribution_quantity,"total_sales": contribution_sales})
contribution_summary["sales_percentage"] = (contribution_summary["total_sales"] / contribution_summary["total_sales"].sum()) * 100
contribution_summary["avg_sales_per_customer"] = (contribution_summary["total_sales"] / contribution_summary["customer_count"])
contribution_summary["sales_percentage"] = (contribution_summary["sales_percentage"].round(2))
contribution_summary["avg_sales_per_customer"] = (contribution_summary["avg_sales_per_customer"].round(2))
print("\nContribution Segment Summary:")
print(contribution_summary)
print("\nContribution segment summary completed successfully!")
# ============================================================
# STEP 18.5.1 - CUSTOMER PURCHASE FREQUENCY
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.5.1 - CUSTOMER PURCHASE FREQUENCY")
print("=" * 60)
retention_frequency = (all_orders.groupby("customer_id")["order_id"].nunique().sort_values(ascending=False))
print("\nCustomer Purchase Frequency:")
print(retention_frequency)
total_customers = retention_frequency.shape[0]
repeat_customers = ((retention_frequency >= 2).sum())
one_time_customers = ((retention_frequency == 1).sum())
repeat_customer_percentage = (repeat_customers / total_customers) * 100
one_time_customer_percentage = (one_time_customers / total_customers) * 100
average_orders_per_customer = (retention_frequency.mean())
print("\nRetention Summary:")
print(f"Total Customers: {total_customers}")
print(f"Repeat Customers: {repeat_customers}")
print(f"Repeat Customer Percentage: " f"{repeat_customer_percentage:.2f}%")
print(f"One-Time Customers: {one_time_customers}")
print(f"One-Time Customer Percentage: " f"{one_time_customer_percentage:.2f}%")
print(f"Average Orders per Customer: " f"{average_orders_per_customer:.2f}")
print("\nCustomer purchase frequency analysis completed successfully!")
# ============================================================
# STEP 18.5.2 - PURCHASE FREQUENCY CLASSIFICATION
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.5.2 - PURCHASE FREQUENCY CLASSIFICATION")
print("=" * 60)
purchase_frequency_analysis = pd.DataFrame({"order_count": retention_frequency})
purchase_frequency_analysis["frequency_segment"] = pd.qcut(purchase_frequency_analysis["order_count"],q=3,labels=["Low Frequency","Medium Frequency","High Frequency"])
print("\nPurchase Frequency Classification:")
print(purchase_frequency_analysis)
print("\nFrequency Segment Summary:")
print(purchase_frequency_analysis["frequency_segment"].value_counts())
print("\nPurchase frequency classification completed successfully!")
# ============================================================
# STEP 18.5.3 - FREQUENCY SEGMENT SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.5.3 - FREQUENCY SEGMENT SUMMARY")
print("=" * 60)
frequency_customers = (purchase_frequency_analysis.groupby("frequency_segment",observed=False).size())
frequency_orders = (purchase_frequency_analysis.join(customer_value[["total_quantity", "total_sales"]]).groupby("frequency_segment",observed=False)["order_count"].sum())
frequency_quantity = (purchase_frequency_analysis.join(customer_value[["total_quantity", "total_sales"]]).groupby("frequency_segment",observed=False)["total_quantity"].sum())
frequency_sales = (purchase_frequency_analysis.join(customer_value[["total_quantity", "total_sales"]]).groupby("frequency_segment",observed=False)["total_sales"].sum())
frequency_summary = pd.DataFrame({"customer_count": frequency_customers,"total_orders": frequency_orders,"total_quantity": frequency_quantity,"total_sales": frequency_sales})
frequency_summary["sales_percentage"] = (frequency_summary["total_sales"] / frequency_summary["total_sales"].sum()) * 100
frequency_summary["avg_sales_per_customer"] = ( frequency_summary["total_sales"] / frequency_summary["customer_count"])
frequency_summary["sales_percentage"] = (frequency_summary["sales_percentage"].round(2))
frequency_summary["avg_sales_per_customer"] = (frequency_summary["avg_sales_per_customer"].round(2))
print("\nFrequency Segment Summary:")
print(frequency_summary)
print("\nFrequency segment summary completed successfully!")
# ============================================================
# STEP 18.5.4 - FREQUENCY VS CUSTOMER VALUE ANALYSIS
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.5.4 - FREQUENCY VS CUSTOMER VALUE ANALYSIS")
print("=" * 60)
frequency_value_analysis = (purchase_frequency_analysis.join(customer_value[["total_quantity", "total_sales", "value_segment"]]))
frequency_value_analysis = frequency_value_analysis.sort_values(by="total_sales",ascending=False)
print("\nFrequency vs Customer Value Analysis:")
print(frequency_value_analysis)
print("\nFrequency Segment vs Value Segment:")
frequency_value_cross_tab = pd.crosstab(frequency_value_analysis["frequency_segment"],frequency_value_analysis["value_segment"])
print(frequency_value_cross_tab)
print("\nFrequency vs customer value analysis completed successfully!")
# ============================================================
# STEP 18.5.5 - CUSTOMER OPPORTUNITY CLASSIFICATION
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.5.5 - CUSTOMER OPPORTUNITY CLASSIFICATION")
print("=" * 60)
customer_opportunity = frequency_value_analysis.copy()

def classify_opportunity(row):
    if (row["frequency_segment"] == "High Frequency" and row["value_segment"] == "High Value"):
        return "VIP / Loyal Customer"
    elif (row["frequency_segment"] == "Low Frequency" and row["value_segment"] == "High Value"):
        return "High Value Opportunity"
    elif (row["frequency_segment"] == "High Frequency" and row["value_segment"] == "Low Value"):
        return "Upsell Opportunity"
    elif (row["frequency_segment"] == "Low Frequency" and row["value_segment"] == "Low Value"):
        return "Reactivation Opportunity"
    elif (row["frequency_segment"] == "High Frequency" and row["value_segment"] == "Medium Value"):
        return "Loyal Growth Opportunity"
    elif row["value_segment"] == "High Value":
        return "High Value Customer"
    else:
        return "Growth Opportunity"
customer_opportunity["opportunity_type"] = (customer_opportunity.apply(classify_opportunity,axis=1))
customer_opportunity = customer_opportunity.sort_values(by="total_sales",ascending=False)
print("\nCustomer Opportunity Classification:")
print(customer_opportunity[["order_count","frequency_segment","total_quantity","total_sales","value_segment","opportunity_type"]])
print("\nOpportunity Type Summary:")
print(customer_opportunity["opportunity_type"].value_counts())
print("\nCustomer opportunity classification completed successfully!")
# ============================================================
# STEP 18.6.1 - RFM RAW METRICS
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.6.1 - RFM RAW METRICS")
print("=" * 60)
rfm_analysis = (all_orders.groupby("customer_id").agg(last_purchase_date=("order_date", "max"),frequency=("order_id", "nunique"),monetary=("final_amount", "sum")))
analysis_date = all_orders["order_date"].max()
rfm_analysis["recency"] = (analysis_date - rfm_analysis["last_purchase_date"]).dt.days
rfm_analysis = rfm_analysis[["last_purchase_date","recency","frequency","monetary"]]
rfm_analysis = rfm_analysis.sort_values(by="monetary",ascending=False)
print("\nRFM Raw Metrics:")
print(rfm_analysis)
print("\nAnalysis Date:")
print(analysis_date)
print("\nRFM raw metrics calculated successfully!")
# ============================================================
# STEP 18.6.2 - RFM SCORING
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.6.2 - RFM SCORING")
print("=" * 60)
rfm_analysis["R_score"] = pd.qcut(rfm_analysis["recency"].rank(method="first"),q=5,labels=[5, 4, 3, 2, 1])
rfm_analysis["F_score"] = pd.qcut(rfm_analysis["frequency"].rank(method="first"),q=5,labels=[1, 2, 3, 4, 5])
rfm_analysis["M_score"] = pd.qcut(rfm_analysis["monetary"].rank(method="first"),q=5,labels=[1, 2, 3, 4, 5])
rfm_analysis["R_score"] = rfm_analysis["R_score"].astype(int)
rfm_analysis["F_score"] = rfm_analysis["F_score"].astype(int)
rfm_analysis["M_score"] = rfm_analysis["M_score"].astype(int)
rfm_analysis["RFM_score"] = (rfm_analysis["R_score"] + rfm_analysis["F_score"] + rfm_analysis["M_score"])
print("\nRFM Scoring:")
print(rfm_analysis[["recency","frequency","monetary","R_score","F_score","M_score","RFM_score"]].sort_values(by="RFM_score",ascending=False))
print("\nRFM scoring completed successfully!")
# ============================================================
# STEP 18.6.3 - RFM CUSTOMER SEGMENTATION
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.6.3 - RFM CUSTOMER SEGMENTATION")
print("=" * 60)
def classify_rfm(score):
    if score >= 13:
        return "Champions"
    elif score >= 10:
        return "Loyal Customers"
    elif score >= 8:
        return "Potential Loyalists"
    elif score >= 6:
        return "At Risk"
    else:
        return "Need Attention"
rfm_analysis["rfm_segment"] = (rfm_analysis["RFM_score"].apply(classify_rfm))
rfm_analysis = rfm_analysis.sort_values(by="RFM_score",ascending=False)
print("\nRFM Customer Segmentation:")
print(rfm_analysis[["recency","frequency","monetary","R_score","F_score","M_score","RFM_score","rfm_segment"]])
print("\nRFM Segment Summary:")
print(rfm_analysis["rfm_segment"].value_counts())
print("\nRFM customer segmentation completed successfully!")
# ============================================================
# STEP 18.6.4 - RFM SEGMENT SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.6.4 - RFM SEGMENT SUMMARY")
print("=" * 60)
rfm_customers = (rfm_analysis.groupby("rfm_segment").size())
rfm_orders = (rfm_analysis.groupby("rfm_segment")["frequency"].sum())
rfm_sales = (rfm_analysis.groupby("rfm_segment")["monetary"].sum())
rfm_quantity = (customer_value.join(rfm_analysis["rfm_segment"]).groupby("rfm_segment")["total_quantity"].sum())
rfm_summary = pd.DataFrame({"customer_count": rfm_customers,"total_orders": rfm_orders,"total_quantity": rfm_quantity,"total_sales": rfm_sales})
rfm_summary["sales_percentage"] = (rfm_summary["total_sales"] / rfm_summary["total_sales"].sum()) * 100
rfm_summary["avg_sales_per_customer"] = (rfm_summary["total_sales"] / rfm_summary["customer_count"])
rfm_summary["sales_percentage"] = (rfm_summary["sales_percentage"].round(2))
rfm_summary["avg_sales_per_customer"] = (rfm_summary["avg_sales_per_customer"].round(2))
print("\nRFM Segment Summary:")
print(rfm_summary)
print("\nRFM segment summary completed successfully!")
# ============================================================
# STEP 18.6.5 - RFM BUSINESS INSIGHTS
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.6.5 - RFM BUSINESS INSIGHTS")
print("=" * 60)
highest_revenue_rfm_segment = (rfm_summary["total_sales"].idxmax())
highest_revenue_rfm_sales = (rfm_summary.loc[highest_revenue_rfm_segment,"total_sales"])
highest_revenue_rfm_percentage = (rfm_summary.loc[highest_revenue_rfm_segment,"sales_percentage"])
highest_avg_rfm_segment = (rfm_summary["avg_sales_per_customer"].idxmax())
highest_avg_rfm_value = (rfm_summary.loc[highest_avg_rfm_segment,"avg_sales_per_customer"])
largest_rfm_segment = (rfm_summary["customer_count"].idxmax())
largest_rfm_customer_count = (rfm_summary.loc[largest_rfm_segment,"customer_count"])
print("\nRFM Business Insights:")
print(f"1. Highest revenue RFM segment: " f"{highest_revenue_rfm_segment}")
print(f"   Revenue: ₹{highest_revenue_rfm_sales:,.2f}")
print(f"   Revenue contribution: " f"{highest_revenue_rfm_percentage:.2f}%")
print(f"\n2. Highest average revenue per customer: " f"{highest_avg_rfm_segment}")
print(f"   Average revenue per customer: " f"₹{highest_avg_rfm_value:,.2f}")
print(f"\n3. Largest customer segment: " f"{largest_rfm_segment}")
print(f"   Customer count: " f"{largest_rfm_customer_count}")
print("\n4. Business Recommendations:")
print("   - Retain Champions using loyalty and personalized offers.")
print("   - Develop Potential Loyalists into Loyal Customers.")
print("   - Re-engage At Risk customers with targeted campaigns.")
print("   - Reactivate Need Attention customers using relevant offers.")
print("   - Identify opportunities to increase customer value " "through upselling and cross-selling.")
print("\nRFM business insights completed successfully!")
# ============================================================
# STEP 18.7.1 - CUSTOMER x CATEGORY PURCHASE ANALYSIS
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.7.1 - CUSTOMER x CATEGORY PURCHASE ANALYSIS")
print("=" * 60)
customer_category_analysis = (all_orders.groupby(["customer_id", "category"]).agg(order_count=("order_id", "nunique"),total_quantity=("quantity", "sum"),total_sales=("final_amount", "sum")).reset_index())
customer_category_analysis = (customer_category_analysis.sort_values(by=["customer_id", "total_sales"],ascending=[True, False]))
print("\nCustomer x Category Purchase Analysis:")
print(customer_category_analysis)
print("\nCustomer x Category purchase analysis " "completed successfully!")
# ============================================================
# STEP 18.7.2 - CUSTOMER'S TOP CATEGORY IDENTIFICATION
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.7.2 - CUSTOMER'S TOP CATEGORY IDENTIFICATION")
print("=" * 60)
customer_top_category = (customer_category_analysis.loc[customer_category_analysis.groupby("customer_id")["total_sales"].idxmax()].reset_index(drop=True))
print("\nCustomer's Top Category:")
print(customer_top_category[["customer_id","category","order_count","total_quantity","total_sales"]])
print("\nCustomer's top category identification " "completed successfully!")
# ============================================================
# STEP 18.7.3 - CUSTOMER x CATEGORY SALES CONTRIBUTION
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.7.3 - CUSTOMER x CATEGORY SALES CONTRIBUTION")
print("=" * 60)
customer_category_contribution = customer_category_analysis.copy()
customer_total_sales = (customer_category_contribution.groupby("customer_id")["total_sales"].transform("sum"))
customer_category_contribution["sales_contribution_percent"] = (customer_category_contribution["total_sales"] / customer_total_sales) * 100
customer_category_contribution["sales_contribution_percent"] = (customer_category_contribution["sales_contribution_percent"].round(2))
customer_category_contribution = (customer_category_contribution.sort_values(by=["customer_id", "sales_contribution_percent"],ascending=[True, False]))
print("\nCustomer x Category Sales Contribution:")
print(customer_category_contribution[["customer_id","category","order_count","total_quantity","total_sales","sales_contribution_percent"]])
print("\nCustomer x Category sales contribution " "analysis completed successfully!")
# ============================================================
# STEP 18.7.4 - CUSTOMER CATEGORY PREFERENCE CLASSIFICATION
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.7.4 - CUSTOMER CATEGORY PREFERENCE CLASSIFICATION")
print("=" * 60)
customer_preference = (customer_category_contribution.groupby("customer_id")["sales_contribution_percent"].max().reset_index(name="top_category_contribution_percent"))
def classify_customer_preference(percent):
    if percent >= 75:
        return "Highly Concentrated"
    elif percent >= 50:
        return "Moderately Concentrated"
    else:
        return "Diversified"
customer_preference["preference_type"] = (customer_preference["top_category_contribution_percent"].apply(classify_customer_preference))
customer_preference = customer_preference.sort_values(by="top_category_contribution_percent",ascending=False)
print("\nCustomer Category Preference:")
print(customer_preference)
print("\nPreference Type Summary:")
print(customer_preference["preference_type"].value_counts())
print("\nCustomer category preference classification " "completed successfully!")
# ============================================================
# STEP 18.7.5 - CUSTOMER x CATEGORY OPPORTUNITY ANALYSIS
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.7.5 - CUSTOMER x CATEGORY OPPORTUNITY ANALYSIS")
print("=" * 60)
customer_opportunity_analysis = customer_preference.copy()
def classify_category_opportunity(percent):
    if percent >= 75:
        return "Cross-Sell Opportunity"
    elif percent >= 50:
        return "Category Expansion Opportunity"
    else:
        return "Diversification Opportunity"
customer_opportunity_analysis["opportunity_type"] = (customer_opportunity_analysis["top_category_contribution_percent"].apply(classify_category_opportunity))
print("\nCustomer Category Opportunity Analysis:")
print(customer_opportunity_analysis)
print("\nOpportunity Type Summary:")
print(customer_opportunity_analysis["opportunity_type"].value_counts())
print("\nCustomer x Category opportunity analysis " "completed successfully!")
# ============================================================
# STEP 18.7.6 - CUSTOMER CATEGORY PURCHASE MATRIX
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.7.6 - CUSTOMER CATEGORY PURCHASE MATRIX")
print("=" * 60)
customer_category_matrix = pd.pivot_table(customer_category_analysis,index="customer_id",columns="category",values="total_sales",aggfunc="sum",fill_value=0)
print("\nCustomer Category Purchase Matrix:")
print(customer_category_matrix)
print("\nCustomer category purchase matrix " "created successfully!")
# ============================================================
# STEP 18.8.1 - HIGH-VALUE CUSTOMER IDENTIFICATION
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.8.1 - HIGH-VALUE CUSTOMER IDENTIFICATION")
print("=" * 60)
high_value_customers = (customer_value.sort_values(by="total_sales", ascending=False).head(5))
print("\nTop 5 High-Value Customers:")
print(high_value_customers[["total_orders","total_quantity","total_sales","sales_percentage","value_segment"]])
print("\nHigh-value customer identification " "completed successfully!")
# ============================================================
# STEP 18.8.2 - HIGH-VALUE CUSTOMER REVENUE CONTRIBUTION
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.8.2 - HIGH-VALUE CUSTOMER REVENUE CONTRIBUTION")
print("=" * 60)
top_5_customer_sales = high_value_customers["total_sales"].sum()
total_customer_sales = customer_value["total_sales"].sum()
top_5_revenue_contribution = (top_5_customer_sales / total_customer_sales) * 100
print("\nTop 5 Customer Sales:", top_5_customer_sales)
print("Total Customer Sales:", total_customer_sales)
print("Top 5 Customer Revenue Contribution:",round(top_5_revenue_contribution, 2),"%")
print("\nHigh-value customer revenue contribution " "analysis completed successfully!")
# ============================================================
# STEP 18.8.3 - CUSTOMER REVENUE CONCENTRATION ANALYSIS
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.8.3 - CUSTOMER REVENUE CONCENTRATION ANALYSIS")
print("=" * 60)
customer_revenue_concentration = customer_value[["total_sales"]].copy()
customer_revenue_concentration = (customer_revenue_concentration.sort_values(by="total_sales", ascending=False))
total_customers = len(customer_revenue_concentration)
top_20_count = max(1, round(total_customers * 0.20))
top_50_count = max(top_20_count, round(total_customers * 0.50))
customer_revenue_concentration["revenue_group"] = "Remaining 50%"
customer_revenue_concentration.iloc[:top_20_count,customer_revenue_concentration.columns.get_loc("revenue_group")] = "Top 20%"
customer_revenue_concentration.iloc[top_20_count:top_50_count,customer_revenue_concentration.columns.get_loc("revenue_group")] = "Next 30%"
revenue_concentration_summary = (customer_revenue_concentration.groupby("revenue_group").agg(customer_count=("total_sales", "count"),total_sales=("total_sales", "sum")))
revenue_concentration_summary["sales_percentage"] = (revenue_concentration_summary["total_sales"] / revenue_concentration_summary["total_sales"].sum()) * 100
revenue_concentration_summary["sales_percentage"] = (revenue_concentration_summary["sales_percentage"].round(2))
print("\nCustomer Revenue Concentration:")
print(revenue_concentration_summary)
print("\nCustomer revenue concentration " "analysis completed successfully!")
# ============================================================
# STEP 18.8.4 - CUSTOMER RETENTION & REVENUE RISK ANALYSIS
# ============================================================
print("\n" + "=" * 60)
print("STEP 18.8.4 - CUSTOMER RETENTION & REVENUE RISK ANALYSIS")
print("=" * 60)
customer_risk_analysis = frequency_value_analysis.copy()
def classify_customer_risk(row):
    if (row["frequency_segment"] == "High Frequency" and row["value_segment"] == "High Value"):
        return "Loyal Revenue Driver"
    elif (row["frequency_segment"] == "Low Frequency" and row["value_segment"] == "High Value"):
        return "Retention Risk"
    elif (row["frequency_segment"] == "High Frequency" and row["value_segment"] == "Low Value"):
        return "Upsell Opportunity"
    else:
        return "Low Priority Customer"
customer_risk_analysis["risk_category"] = (customer_risk_analysis.apply(classify_customer_risk,axis=1))
customer_risk_analysis = customer_risk_analysis.sort_values(by="total_sales",ascending=False)
print("\nCustomer Retention & Revenue Risk Analysis:")
print(customer_risk_analysis[["order_count","frequency_segment","total_sales","value_segment","risk_category"]])
print("\nRisk Category Summary:")
print(customer_risk_analysis["risk_category"].value_counts())
print("\nCustomer retention and revenue risk analysis " "completed successfully!")

print("\n" + "=" * 60)
print("STEP 18.8.5 - REVENUE OPPORTUNITY IDENTIFICATION")
print("=" * 60)
revenue_opportunity = customer_risk_analysis.copy()
def classify_revenue_opportunity(row):
    if row["risk_category"] == "Loyal Revenue Driver":
        return "Retention & Loyalty"
    elif row["risk_category"] == "Retention Risk":
        return "Retention Campaign"
    elif row["risk_category"] == "Upsell Opportunity":
        return "Upsell Campaign"
    elif (row["value_segment"] == "High Value" and row["frequency_segment"] == "Medium Frequency"):
        return "Increase Purchase Frequency"
    elif row["value_segment"] == "Medium Value":
        return "Customer Growth"
    else:
        return "Reactivation Campaign"
revenue_opportunity["revenue_opportunity"] = (revenue_opportunity.apply(classify_revenue_opportunity,axis=1))
revenue_opportunity = revenue_opportunity.sort_values(by="total_sales",ascending=False)
print("\nCustomer Revenue Opportunity Analysis:")
print(revenue_opportunity[["order_count","frequency_segment","total_sales","value_segment","risk_category","revenue_opportunity"]])
print("\nRevenue Opportunity Summary:")
print(revenue_opportunity["revenue_opportunity"].value_counts())

print("\n" + "=" * 60)
print("STEP 18.8.6 - OPPORTUNITY REVENUE CONTRIBUTION")
print("=" * 60)
opportunity_revenue_summary = (revenue_opportunity.groupby("revenue_opportunity").agg(customer_count=("total_sales", "count"),total_sales=("total_sales", "sum"),average_sales_per_customer=("total_sales", "mean")))
opportunity_revenue_summary["revenue_percentage"] = (opportunity_revenue_summary["total_sales"] / opportunity_revenue_summary["total_sales"].sum()) * 100
opportunity_revenue_summary["revenue_percentage"] = (opportunity_revenue_summary["revenue_percentage"].round(2))
opportunity_revenue_summary["average_sales_per_customer"] = (opportunity_revenue_summary["average_sales_per_customer"].round(2))
opportunity_revenue_summary = opportunity_revenue_summary.sort_values(by="total_sales",ascending=False)
print("\nOpportunity Revenue Contribution:")
print(opportunity_revenue_summary)
print("\nOpportunity Revenue Contribution Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 18.8.7 - FINAL CUSTOMER BUSINESS PRIORITY")
print("=" * 60)
customer_business_priority = revenue_opportunity.copy()
def classify_business_priority(row):
    if row["value_segment"] == "High Value":
        return "High Priority"
    elif (row["value_segment"] == "Medium Value" and row["frequency_segment"] == "High Frequency"):
        return "High Priority"
    elif row["value_segment"] == "Medium Value":
        return "Medium Priority"
    else:
        return "Low Priority"
customer_business_priority["business_priority"] = (customer_business_priority.apply(classify_business_priority,axis=1))
customer_business_priority = customer_business_priority.sort_values(by=["business_priority", "total_sales"],ascending=[True, False])
print("\nFinal Customer Business Priority:")
print(customer_business_priority[["order_count","frequency_segment","total_sales","value_segment","revenue_opportunity","business_priority"]])
print("\nBusiness Priority Summary:")
print(customer_business_priority["business_priority"].value_counts())
print("\nStep 18.8 Advanced Business Insights Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.1 - PREPARE CLEANED DATA FOR SQL")
print("=" * 60)
sql_orders = all_orders.copy()
sql_orders.to_csv("OnlineMart_Cleaned_Orders.csv",index=False)
print("\nCleaned Orders CSV file created successfully!")
print("Rows:", sql_orders.shape[0])
print("Columns:", sql_orders.shape[1])
print("File Name: OnlineMart_Cleaned_Orders.csv")

print("\n" + "=" * 60)
print("STEP 19.2 - VERIFY SQL DATASET STRUCTURE")
print("=" * 60)
print("\nSQL Dataset Shape:")
print(sql_orders.shape)
print("\nSQL Dataset Columns:")
print(sql_orders.columns.tolist())
print("\nSQL Dataset Data Types:")
print(sql_orders.dtypes)
print("\nSQL Dataset Verification Completed Successfully!")

import sqlite3
print("\n" + "=" * 60)
print("STEP 19.3 - CREATE SQL DATABASE")
print("=" * 60)
connection = sqlite3.connect("OnlineMart.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS orders (order_id TEXT PRIMARY KEY,customer_id TEXT,order_date DATE,product_id TEXT,product_name TEXT,category TEXT,subcategory TEXT,quantity INTEGER,unit_price INTEGER,shipping_cost INTEGER,payment_method TEXT,order_status TEXT,return_status TEXT,customer_city TEXT,customer_state TEXT,brand TEXT,discount_percent REAL,discount_amount REAL,gross_amount REAL,final_amount REAL,order_month TEXT)""")
connection.commit()
print("\nOnlineMart.db database created successfully!")
print("Orders table created successfully!")


print("\n" + "=" * 60)
print("STEP 19.4 - LOAD DATA INTO SQL TABLE")
print("=" * 60)
sql_orders_for_insert = sql_orders.copy()
sql_orders_for_insert["order_date"] = (sql_orders_for_insert["order_date"].astype(str))
sql_orders_for_insert["order_month"] = (sql_orders_for_insert["order_month"].astype(str))
cursor.execute("DELETE FROM orders")
connection.commit()
sql_orders_for_insert.to_sql("orders",connection,if_exists="append",index=False)
print("\nData loaded into SQL table successfully!")
cursor.execute("SELECT COUNT(*) FROM orders")
row_count = cursor.fetchone()[0]
print("Rows loaded into orders table:", row_count)

print("\n" + "=" * 60)
print("STEP 19.5 - SQL DATA VERIFICATION")
print("=" * 60)
cursor.execute("""SELECT COUNT(*) AS total_orders,COUNT(DISTINCT customer_id) AS unique_customers,COUNT(DISTINCT product_id) AS unique_products FROM orders""")
verification_result = cursor.fetchone()
print("\nSQL Data Verification:")
print("Total Orders:", verification_result[0])
print("Unique Customers:", verification_result[1])
print("Unique Products:", verification_result[2])
print("\nFirst 5 Orders:")
cursor.execute("""SELECT order_id,customer_id,order_date,product_name,quantity,final_amount FROM orders LIMIT 5""")
for row in cursor.fetchall():
    print(row)
print("\nSQL Data Verification Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.6 - BASIC SQL SELECT QUERY")
print("=" * 60)
cursor.execute("""SELECT order_id,customer_id,product_name,category,final_amount FROM orders LIMIT 10""")
select_result = cursor.fetchall()
print("\nFirst 10 Orders using SQL SELECT:")
for row in select_result:
    print(row)
print("\nBasic SQL SELECT Query Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.7 - SQL WHERE FILTERING")
print("=" * 60)
cursor.execute("""SELECT order_id,customer_id,product_name,category,final_amount FROM orders WHERE category = 'Electronics' LIMIT 10""")
where_result = cursor.fetchall()
print("\nElectronics Orders:")
for row in where_result:
    print(row)
print("\nSQL WHERE Filtering Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.8 - SQL MULTIPLE CONDITION FILTERING")
print("=" * 60)
cursor.execute("""SELECT order_id,customer_id,product_name,category,final_amount FROM orders WHERE category = 'Electronics' AND final_amount > 10000 ORDER BY final_amount DESC LIMIT 10""")
multiple_condition_result = cursor.fetchall()
print("\nHigh-Value Electronics Orders:")
for row in multiple_condition_result:
    print(row)
print("\nSQL Multiple Condition Filtering Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.9 - SQL AGGREGATE FUNCTIONS")
print("=" * 60)
cursor.execute("""SELECT COUNT(order_id) AS total_orders,COUNT(DISTINCT customer_id) AS unique_customers,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value,MIN(final_amount) AS minimum_order_value,MAX(final_amount) AS maximum_order_value FROM orders""")
aggregate_result = cursor.fetchone()
print("\nSQL Business KPIs:")
print("Total Orders:", aggregate_result[0])
print("Unique Customers:", aggregate_result[1])
print("Total Sales:", round(aggregate_result[2], 2))
print("Average Order Value:", round(aggregate_result[3], 2))
print("Minimum Order Value:", round(aggregate_result[4], 2))
print("Maximum Order Value:", round(aggregate_result[5], 2))
print("\nSQL Aggregate Functions Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.10 - SQL GROUP BY CATEGORY ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT category,COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY category ORDER BY total_sales DESC""")
category_result = cursor.fetchall()
print("\nCategory-wise Sales Analysis:")
for row in category_result:
    print(row)
print("\nSQL GROUP BY Category Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.11 - SQL CUSTOMER-WISE SALES ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT customer_id,COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY customer_id ORDER BY total_sales DESC""")
customer_result = cursor.fetchall()
print("\nCustomer-wise Sales Analysis:")
for row in customer_result:
    print(row)
print("\nSQL Customer-wise Sales Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.12 - SQL PRODUCT-WISE SALES ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT product_id,product_name,category,COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY product_id, product_name, category ORDER BY total_sales DESC""")
product_result = cursor.fetchall()
print("\nProduct-wise Sales Analysis:")
for row in product_result:
    print(row)
print("\nSQL Product-wise Sales Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.13 - SQL MONTHLY SALES ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT order_month,COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY order_month ORDER BY order_month""")
monthly_result = cursor.fetchall()
print("\nMonthly Sales Analysis:")
for row in monthly_result:
    print(row)
print("\nSQL Monthly Sales Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.14 - SQL PAYMENT METHOD ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT payment_method,COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY payment_method ORDER BY total_sales DESC""")
payment_result = cursor.fetchall()
print("\nPayment Method Analysis:")
for row in payment_result:
    print(row)
print("\nSQL Payment Method Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.15 - SQL ORDER STATUS & RETURN ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT order_status,COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY order_status ORDER BY total_orders DESC""")
status_result = cursor.fetchall()
print("\nOrder Status Analysis:")
for row in status_result:
    print(row)
print("\nSQL Order Status Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.16 - SQL RETURN & CANCELLATION RATE ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT COUNT(order_id) AS total_orders,SUM(CASE WHEN order_status = 'Returned' THEN 1 ELSE 0 END) AS returned_orders,SUM(CASE WHEN order_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_orders,ROUND(SUM(CASE WHEN order_status = 'Returned' THEN 1 ELSE 0 END) * 100.0 / COUNT(order_id),2) AS return_rate,ROUND(SUM(CASE WHEN order_status = 'Cancelled' THEN 1 ELSE 0 END) * 100.0 / COUNT(order_id),2) AS cancellation_rate FROM orders""")
rate_result = cursor.fetchone()
print("\nReturn & Cancellation Rate Analysis:")
print("Total Orders:", rate_result[0])
print("Returned Orders:", rate_result[1])
print("Cancelled Orders:", rate_result[2])
print("Return Rate:", rate_result[3], "%")
print("Cancellation Rate:", rate_result[4], "%")
print("\nSQL Return & Cancellation Rate Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.17 - SQL PAYMENT METHOD x ORDER STATUS ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT payment_method,order_status,COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales FROM orders GROUP BY payment_method, order_status ORDER BY payment_method, total_orders DESC""")
payment_status_result = cursor.fetchall()
print("\nPayment Method x Order Status Analysis:")
for row in payment_status_result:
    print(row)
print("\nSQL Payment Method x Order Status Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.18 - CREATE CUSTOMERS TABLE")
print("=" * 60)
cursor.execute("""CREATE TABLE IF NOT EXISTS customers (customer_id TEXT PRIMARY KEY,customer_name TEXT,customer_age INTEGER,customer_gender TEXT,customer_city TEXT,customer_state TEXT,customer_segment TEXT,registration_date DATE)""")
connection.commit()
cursor.execute("DELETE FROM customers")
customers_for_sql = customers.copy()
customers_for_sql["registration_date"] = (customers_for_sql["registration_date"].astype(str))
customers_for_sql.to_sql("customers",connection,if_exists="append",index=False)
cursor.execute("SELECT COUNT(*) FROM customers")
customer_row_count = cursor.fetchone()[0]
print("\nCustomers table created successfully!")
print("Rows loaded into customers table:", customer_row_count)

print("\n" + "=" * 60)
print("STEP 19.19 - SQL JOIN ORDERS WITH CUSTOMERS")
print("=" * 60)
cursor.execute("""SELECT o.order_id,o.customer_id,c.customer_name,c.customer_city,c.customer_segment,o.product_name,o.quantity,o.final_amount FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id ORDER BY o.final_amount DESC LIMIT 15""")
join_result = cursor.fetchall()
print("\nOrders with Customer Details:")
for row in join_result:
    print(row)
print("\nSQL JOIN Orders with Customers Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.20 - CREATE PRODUCTS TABLE")
print("=" * 60)
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("""CREATE TABLE products (product_id TEXT PRIMARY KEY,product_name TEXT,category TEXT,subcategory TEXT,brand TEXT,unit_price INTEGER,cost_price INTEGER,supplier TEXT)""")
connection.commit()
products_for_sql = products.copy()
print("\nProducts DataFrame Columns:")
print(products.columns.tolist())
products_for_sql.to_sql("products",connection,if_exists="append",index=False)
cursor.execute("SELECT COUNT(*) FROM products")
product_row_count = cursor.fetchone()[0]
print("\nProducts table created successfully!")
print("Rows loaded into products table:", product_row_count)

print("\n" + "=" * 60)
print("STEP 19.20 - SQL JOIN ORDERS WITH PRODUCTS")
print("=" * 60)
cursor.execute("""SELECT o.order_id,o.customer_id,o.product_id,p.product_name,p.category,p.subcategory,p.brand,o.quantity,o.final_amount FROM orders AS o INNER JOIN products AS p ON o.product_id = p.product_id ORDER BY o.final_amount DESC LIMIT 15""")
product_join_result = cursor.fetchall()
print("\nOrders with Product Details:")
for row in product_join_result:
    print(row)
print("\nSQL JOIN Orders with Products Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.21 - SQL 3-TABLE JOIN")
print("=" * 60)
cursor.execute("""SELECT o.order_id,o.order_date,c.customer_id,c.customer_name,c.customer_city,c.customer_segment,p.product_id,p.product_name,p.category,p.brand,o.quantity,o.final_amount FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id INNER JOIN products AS p ON o.product_id = p.product_id ORDER BY o.final_amount DESC LIMIT 20""")
three_table_result = cursor.fetchall()
print("\nOrders with Customer and Product Details:")
for row in three_table_result:
    print(row)
print("\nSQL 3-Table JOIN Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.22 - CUSTOMER SEGMENT-WISE SALES ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT c.customer_segment,COUNT(o.order_id) AS total_orders,COUNT(DISTINCT o.customer_id) AS total_customers,SUM(o.quantity) AS total_quantity,SUM(o.final_amount) AS total_sales,ROUND(AVG(o.final_amount), 2) AS average_order_value FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment ORDER BY total_sales DESC""")
segment_result = cursor.fetchall()
print("\nCustomer Segment-wise Sales Analysis:")
for row in segment_result:
    print(row)
print("\nSQL Customer Segment-wise Sales Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.23 - CATEGORY x CUSTOMER SEGMENT ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT c.customer_segment,p.category,COUNT(o.order_id) AS total_orders,SUM(o.quantity) AS total_quantity,SUM(o.final_amount) AS total_sales,ROUND(AVG(o.final_amount), 2) AS average_order_value FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id INNER JOIN products AS p ON o.product_id = p.product_id GROUP BY c.customer_segment,p.category ORDER BY total_sales DESC""")
category_segment_result = cursor.fetchall()
print("\nCategory x Customer Segment Analysis:")
for row in category_segment_result:
    print(row)
print("\nSQL Category x Customer Segment Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.24 - CUSTOMER REVENUE RANKING")
print("=" * 60)
cursor.execute("""SELECT c.customer_id,c.customer_name,c.customer_segment,SUM(o.final_amount) AS total_sales,RANK() OVER (ORDER BY SUM(o.final_amount) DESC) AS sales_rank FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment ORDER BY sales_rank""")
customer_rank_result = cursor.fetchall()
print("\nCustomer Revenue Ranking:")
for row in customer_rank_result:
    print(row)
print("\nSQL Customer Revenue Ranking Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.25 - SEGMENT-WISE CUSTOMER REVENUE RANKING")
print("=" * 60)
cursor.execute("""SELECT c.customer_id,c.customer_name,c.customer_segment,SUM(o.final_amount) AS total_sales,RANK() OVER (PARTITION BY c.customer_segment ORDER BY SUM(o.final_amount) DESC) AS segment_rank FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment ORDER BY c.customer_segment,segment_rank""")
segment_rank_result = cursor.fetchall()
print("\nSegment-wise Customer Revenue Ranking:")
for row in segment_rank_result:
    print(row)
print("\nSQL Segment-wise Customer Revenue Ranking Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.26 - TOP 2 CUSTOMERS FROM EACH SEGMENT")
print("=" * 60)
cursor.execute("""WITH customer_ranking AS (SELECT c.customer_id,c.customer_name,c.customer_segment,SUM(o.final_amount) AS total_sales,RANK() OVER (PARTITION BY c.customer_segment ORDER BY SUM(o.final_amount) DESC) AS segment_rank FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment) SELECT customer_id,customer_name,customer_segment,total_sales,segment_rank FROM customer_ranking WHERE segment_rank <= 2 ORDER BY customer_segment,segment_rank""")
top_customers_result = cursor.fetchall()
print("\nTop 2 Customers from Each Segment:")
for row in top_customers_result:
    print(row)
print("\nSQL Top 2 Customers per Segment Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.27 - TOP PRODUCT BY CATEGORY")
print("=" * 60)
cursor.execute("""WITH product_ranking AS (SELECT p.product_id,p.product_name,p.category,SUM(o.final_amount) AS total_sales,RANK() OVER (PARTITION BY p.category ORDER BY SUM(o.final_amount) DESC) AS category_rank FROM orders AS o INNER JOIN products AS p ON o.product_id = p.product_id GROUP BY p.product_id,p.product_name,p.category) SELECT product_id,product_name,category,total_sales,category_rank FROM product_ranking WHERE category_rank = 1 ORDER BY total_sales DESC""")
top_product_result = cursor.fetchall()
print("\nTop Revenue Product in Each Category:")
for row in top_product_result:
    print(row)
print("\nSQL Top Product by Category Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.28 - TOP 3 PRODUCTS OVERALL")
print("=" * 60)
cursor.execute("""SELECT p.product_id,p.product_name,p.category,SUM(o.quantity) AS total_quantity,SUM(o.final_amount) AS total_sales,RANK() OVER (ORDER BY SUM(o.final_amount) DESC) AS sales_rank FROM orders AS o INNER JOIN products AS p ON o.product_id = p.product_id GROUP BY p.product_id,p.product_name,p.category ORDER BY sales_rank LIMIT 3""")
top_3_products_result = cursor.fetchall()
print("\nTop 3 Products Overall:")
for row in top_3_products_result:
    print(row)
print("\nSQL Top 3 Products Overall Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.29 - CUSTOMER PURCHASE FREQUENCY ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT c.customer_id,c.customer_name,c.customer_segment,COUNT(o.order_id) AS total_orders,SUM(o.quantity) AS total_quantity,SUM(o.final_amount) AS total_spent,ROUND(CAST(SUM(o.quantity) AS REAL) / COUNT(o.order_id),2) AS average_quantity_per_order FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment ORDER BY total_orders DESC""")
purchase_frequency_result = cursor.fetchall()
print("\nCustomer Purchase Frequency Analysis:")
for row in purchase_frequency_result:
    print(row)
print("\nSQL Customer Purchase Frequency Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.30 - CUSTOMER AVERAGE ORDER VALUE RANKING")
print("=" * 60)
cursor.execute("""SELECT c.customer_id,c.customer_name,c.customer_segment,COUNT(o.order_id) AS total_orders,SUM(o.final_amount) AS total_spent,ROUND(AVG(o.final_amount),2) AS average_order_value,RANK() OVER (ORDER BY AVG(o.final_amount) DESC) AS aov_rank FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment ORDER BY aov_rank""")
customer_aov_result = cursor.fetchall()
print("\nCustomer Average Order Value Ranking:")
for row in customer_aov_result:
    print(row)
print("\nSQL Customer Average Order Value Ranking Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.31 - CUSTOMER REVENUE CONTRIBUTION")
print("=" * 60)
cursor.execute("""WITH customer_sales AS (SELECT c.customer_id,c.customer_name,c.customer_segment,SUM(o.final_amount) AS total_sales FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment),overall_sales AS (SELECT SUM(final_amount) AS company_total_sales FROM orders)SELECT cs.customer_id,cs.customer_name,cs.customer_segment,cs.total_sales,ROUND(cs.total_sales * 100.0 / os.company_total_sales,2) AS revenue_contribution_percent FROM customer_sales AS cs CROSS JOIN overall_sales AS os ORDER BY cs.total_sales DESC""")
customer_contribution_result = cursor.fetchall()
print("\nCustomer Revenue Contribution:")
for row in customer_contribution_result:
    print(row)
print("\nSQL Customer Revenue Contribution Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.32 - TOP 20% CUSTOMERS REVENUE CONTRIBUTION")
print("=" * 60)
cursor.execute("""WITH customer_sales AS (SELECT c.customer_id,c.customer_name,c.customer_segment,SUM(o.final_amount) AS total_sales FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment),customer_ranked AS (SELECT customer_id,customer_name,customer_segment,total_sales,ROW_NUMBER() OVER (ORDER BY total_sales DESC) AS customer_rank,COUNT(*) OVER () AS total_customers FROM customer_sales),overall_sales AS (SELECT SUM(final_amount) AS company_total_sales FROM orders) SELECT cr.customer_id,cr.customer_name,cr.customer_segment,cr.total_sales,cr.customer_rank,ROUND(cr.total_sales * 100.0 / os.company_total_sales,2) AS revenue_contribution_percent FROM customer_ranked AS cr CROSS JOIN overall_sales AS os WHERE cr.customer_rank <= CEIL(cr.total_customers * 0.20) ORDER BY cr.customer_rank""")
top_20_result = cursor.fetchall()
print("\nTop 20% Customers by Revenue:")
for row in top_20_result:
    print(row)
print("\nSQL Top 20% Customer Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.33 - CUSTOMER LIFETIME VALUE PROXY")
print("=" * 60)
cursor.execute("""SELECT c.customer_id,c.customer_name,c.customer_segment,COUNT(o.order_id) AS total_orders,SUM(o.final_amount) AS historical_customer_value,ROUND(AVG(o.final_amount),2) AS average_order_value,ROUND(SUM(o.final_amount) * 1.0 / COUNT(DISTINCT o.order_date),2) AS average_daily_customer_value FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment ORDER BY historical_customer_value DESC""")
clv_proxy_result = cursor.fetchall()
print("\nCustomer Lifetime Value Proxy:")
for row in clv_proxy_result:
    print(row)
print("\nSQL Customer Lifetime Value Proxy Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.34 - CUSTOMER RECENCY ANALYSIS")
print("=" * 60)
cursor.execute("""WITH customer_recency AS (SELECT c.customer_id,c.customer_name,c.customer_segment,MAX(o.order_date) AS last_purchase_date FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment),dataset_date AS (SELECT MAX(order_date) AS latest_order_date FROM orders) SELECT cr.customer_id,cr.customer_name,cr.customer_segment,cr.last_purchase_date,CAST(JULIANDAY(dd.latest_order_date) - JULIANDAY(cr.last_purchase_date) AS INTEGER) AS recency_days FROM customer_recency AS cr CROSS JOIN dataset_date AS dd ORDER BY recency_days ASC""")
recency_result = cursor.fetchall()
print("\nCustomer Recency Analysis:")
for row in recency_result:
    print(row)
print("\nSQL Customer Recency Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.35 - RFM CUSTOMER SCORING")
print("=" * 60)
cursor.execute("""WITH rfm_base AS (SELECT c.customer_id,c.customer_name,c.customer_segment,MAX(o.order_date) AS last_purchase_date,COUNT(o.order_id) AS frequency,SUM(o.final_amount) AS monetary FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment),dataset_date AS (SELECT MAX(order_date) AS latest_order_date FROM orders),rfm_data AS (SELECT rb.customer_id,rb.customer_name,rb.customer_segment,CAST(JULIANDAY(dd.latest_order_date) - JULIANDAY(rb.last_purchase_date) AS INTEGER) AS recency,rb.frequency,rb.monetary FROM rfm_base AS rb CROSS JOIN dataset_date AS dd),rfm_scores AS (SELECT customer_id,customer_name,customer_segment,recency,frequency,monetary,NTILE(5) OVER (ORDER BY recency DESC) AS recency_score,NTILE(5) OVER (ORDER BY frequency ASC) AS frequency_score,NTILE(5) OVER (ORDER BY monetary ASC) AS monetary_score FROM rfm_data) SELECT customer_id,customer_name,customer_segment,recency,frequency,monetary,recency_score,frequency_score,monetary_score,(recency_score || frequency_score || monetary_score) AS rfm_score FROM rfm_scores ORDER BY recency_score DESC,frequency_score DESC,monetary_score DESC""")
rfm_result = cursor.fetchall()
print("\nRFM Customer Scores:")
for row in rfm_result:
    print(row)
print("\nSQL RFM Customer Scoring Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.36 - RFM CUSTOMER SEGMENTATION")
print("=" * 60)
cursor.execute("""WITH rfm_base AS (SELECT c.customer_id,c.customer_name,c.customer_segment,MAX(o.order_date) AS last_purchase_date,COUNT(o.order_id) AS frequency,SUM(o.final_amount) AS monetary FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment),dataset_date AS (SELECT MAX(order_date) AS latest_order_date FROM orders),rfm_data AS (SELECT rb.customer_id,rb.customer_name,rb.customer_segment,CAST(JULIANDAY(dd.latest_order_date) - JULIANDAY(rb.last_purchase_date) AS INTEGER) AS recency,rb.frequency,rb.monetary FROM rfm_base AS rb CROSS JOIN dataset_date AS dd),rfm_scores AS (SELECT customer_id,customer_name,customer_segment,recency,frequency,monetary,NTILE(5) OVER ( ORDER BY recency ASC) AS recency_score,NTILE(5) OVER (ORDER BY frequency ASC) AS frequency_score,NTILE(5) OVER (ORDER BY monetary ASC) AS monetary_score FROM rfm_data),rfm_segmented AS (SELECT *,(recency_score || frequency_score || monetary_score) AS rfm_score FROM rfm_scores) SELECT customer_id,customer_name,customer_segment,recency,frequency,monetary,recency_score,frequency_score,monetary_score,rfm_score,CASE WHEN recency_score >= 4 AND frequency_score >= 4 AND monetary_score >= 4 THEN 'Champions' WHEN recency_score >= 4 AND frequency_score >= 3 THEN 'Loyal Customers' WHEN recency_score >= 4 AND monetary_score >= 3 THEN 'Potential Loyalists' WHEN recency_score <= 2 AND frequency_score >= 3 AND monetary_score >= 3 THEN 'At Risk' WHEN recency_score <= 2 AND frequency_score <= 2 AND monetary_score <= 2 THEN 'Low Value' ELSE 'Regular Customers' END AS rfm_customer_segment FROM rfm_segmented ORDER BY recency_score DESC,frequency_score DESC,monetary_score DESC""")
rfm_segment_result = cursor.fetchall()
print("\nRFM Customer Segmentation:")
for row in rfm_segment_result:
    print(row)
print("\nSQL RFM Customer Segmentation Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.37 - RFM SEGMENT-WISE BUSINESS ANALYSIS")
print("=" * 60)
cursor.execute("""WITH rfm_base AS (SELECT c.customer_id,c.customer_name,c.customer_segment,MAX(o.order_date) AS last_purchase_date,COUNT(o.order_id) AS frequency,SUM(o.final_amount) AS monetary FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment),dataset_date AS (SELECT MAX(order_date) AS latest_order_date FROM orders),rfm_data AS (SELECT rb.customer_id,rb.customer_name,rb.customer_segment,CAST(JULIANDAY(dd.latest_order_date) - JULIANDAY(rb.last_purchase_date) AS INTEGER) AS recency,rb.frequency,rb.monetary FROM rfm_base AS rb CROSS JOIN dataset_date AS dd),rfm_scores AS ( SELECT *,NTILE(5) OVER (ORDER BY recency DESC) AS recency_score,NTILE(5) OVER (ORDER BY frequency ASC) AS frequency_score,NTILE(5) OVER (ORDER BY monetary ASC) AS monetary_score FROM rfm_data),rfm_segmented AS (SELECT *,CASE WHEN recency_score >= 4 AND frequency_score >= 4 AND monetary_score >= 4 THEN 'Champions' WHEN recency_score >= 4 AND frequency_score >= 3 THEN 'Loyal Customers' WHEN recency_score >= 4 AND monetary_score >= 3 THEN 'Potential Loyalists' WHEN recency_score <= 2 AND frequency_score >= 3 AND monetary_score >= 3 THEN 'At Risk' WHEN recency_score <= 2 AND frequency_score <= 2 AND monetary_score <= 2 THEN 'Low Value' ELSE 'Regular Customers' END AS rfm_customer_segment FROM rfm_scores),segment_summary AS (SELECT rfm_customer_segment,COUNT(*) AS customer_count,SUM(monetary) AS total_revenue,AVG(monetary) AS average_customer_revenue,AVG(frequency) AS average_frequency,AVG(recency) AS average_recency FROM rfm_segmented GROUP BY rfm_customer_segment),overall_revenue AS (SELECT SUM(monetary) AS company_revenue FROM rfm_segmented) SELECT ss.rfm_customer_segment,ss.customer_count,ROUND(ss.total_revenue, 2) AS total_revenue,ROUND(ss.average_customer_revenue, 2) AS average_customer_revenue,ROUND(ss.average_frequency, 2) AS average_frequency,ROUND(ss.average_recency, 2) AS average_recency,ROUND((ss.total_revenue * 100.0) / orv.company_revenue,2) AS revenue_contribution_percent FROM segment_summary AS ss CROSS JOIN overall_revenue AS orv ORDER BY ss.total_revenue DESC""")
rfm_segment_business_result = cursor.fetchall()
print("\nRFM Segment-wise Business Analysis:")
for row in rfm_segment_business_result:
    print(row)
print("\nSQL RFM Segment-wise Business Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.38 - RFM SEGMENT x CUSTOMER SEGMENT ANALYSIS")
print("=" * 60)
cursor.execute("""WITH rfm_base AS (SELECT c.customer_id,c.customer_name,c.customer_segment,MAX(o.order_date) AS last_purchase_date,COUNT(o.order_id) AS frequency,SUM(o.final_amount) AS monetary FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment),dataset_date AS (SELECT MAX(order_date) AS latest_order_date FROM orders),rfm_data AS (SELECT rb.customer_id,rb.customer_name,rb.customer_segment,CAST(JULIANDAY(dd.latest_order_date) - JULIANDAY(rb.last_purchase_date) AS INTEGER) AS recency,rb.frequency,rb.monetary FROM rfm_base AS rb CROSS JOIN dataset_date AS dd),rfm_scores AS (SELECT *,NTILE(5) OVER (ORDER BY recency DESC) AS recency_score,NTILE(5) OVER (ORDER BY frequency ASC) AS frequency_score,NTILE(5) OVER (ORDER BY monetary ASC) AS monetary_score FROM rfm_data),rfm_segmented AS (SELECT *,CASE WHEN recency_score >= 4 AND frequency_score >= 4 AND monetary_score >= 4 THEN 'Champions' WHEN recency_score >= 4 AND frequency_score >= 3 THEN 'Loyal Customers' WHEN recency_score >= 4 AND monetary_score >= 3 THEN 'Potential Loyalists' WHEN recency_score <= 2 AND frequency_score >= 3 AND monetary_score >= 3 THEN 'At Risk' WHEN recency_score <= 2 AND frequency_score <= 2 AND monetary_score <= 2 THEN 'Low Value' ELSE 'Regular Customers' END AS rfm_customer_segment FROM rfm_scores) SELECT customer_segment,rfm_customer_segment,COUNT(*) AS customer_count,ROUND(SUM(monetary), 2) AS total_revenue,ROUND(AVG(monetary), 2) AS average_customer_revenue,ROUND(AVG(frequency), 2) AS average_frequency,ROUND(AVG(recency), 2) AS average_recency FROM rfm_segmented GROUP BY customer_segment,rfm_customer_segment ORDER BY customer_segment,total_revenue DESC""")
rfm_customer_segment_result = cursor.fetchall()
print("\nRFM Segment x Customer Segment Analysis:")
for row in rfm_customer_segment_result:
    print(row)
print("\nSQL RFM Segment x Customer Segment Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.39 - RFM SEGMENT-WISE CUSTOMER & REVENUE CONTRIBUTION")
print("=" * 60)
cursor.execute("""WITH rfm_base AS (SELECT c.customer_id,c.customer_name,c.customer_segment,MAX(o.order_date) AS last_purchase_date,COUNT(o.order_id) AS frequency,SUM(o.final_amount) AS monetary FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment),dataset_date AS (SELECT MAX(order_date) AS latest_order_date FROM orders),rfm_data AS (SELECT rb.customer_id,rb.customer_name,rb.customer_segment,CAST(JULIANDAY(dd.latest_order_date) - JULIANDAY(rb.last_purchase_date) AS INTEGER) AS recency,rb.frequency,rb.monetary FROM rfm_base AS rb CROSS JOIN dataset_date AS dd),rfm_scores AS (SELECT *,NTILE(5) OVER (ORDER BY recency DESC) AS recency_score,NTILE(5) OVER (ORDER BY frequency ASC) AS frequency_score,NTILE(5) OVER (ORDER BY monetary ASC) AS monetary_score FROM rfm_data),rfm_segmented AS (SELECT *,CASE WHEN recency_score >= 4 AND frequency_score >= 4 AND monetary_score >= 4 THEN 'Champions' WHEN recency_score >= 4 AND frequency_score >= 3 THEN 'Loyal Customers' WHEN recency_score >= 4 AND monetary_score >= 3 THEN 'Potential Loyalists' WHEN recency_score <= 2 AND frequency_score >= 3 AND monetary_score >= 3 THEN 'At Risk' WHEN recency_score <= 2 AND frequency_score <= 2 AND monetary_score <= 2 THEN 'Low Value' ELSE 'Regular Customers' END AS rfm_customer_segment FROM rfm_scores),segment_summary AS (SELECT rfm_customer_segment,COUNT(*) AS customer_count,SUM(monetary) AS total_revenue FROM rfm_segmented GROUP BY rfm_customer_segment),overall_summary AS (SELECT COUNT(*) AS total_customers,SUM(monetary) AS overall_revenue FROM rfm_segmented) SELECT ss.rfm_customer_segment,ss.customer_count,ROUND(ss.customer_count * 100.0 / os.total_customers,2) AS customer_percentage,ROUND(ss.total_revenue, 2) AS total_revenue,ROUND(ss.total_revenue * 100.0 / os.overall_revenue,2) AS revenue_contribution_percentage FROM segment_summary AS ss CROSS JOIN overall_summary AS os ORDER BY ss.total_revenue DESC""")
rfm_contribution_result = cursor.fetchall()
print("\nRFM Segment-wise Customer & Revenue Contribution:")
for row in rfm_contribution_result:
    print(row)
print("\nSQL RFM Segment-wise Customer & Revenue Contribution Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.40 - RFM CUSTOMER PRIORITY ANALYSIS")
print("=" * 60)
cursor.execute("""WITH rfm_base AS (SELECT c.customer_id,c.customer_name,c.customer_segment,MAX(o.order_date) AS last_purchase_date,COUNT(o.order_id) AS frequency,SUM(o.final_amount) AS monetary FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment),dataset_date AS (SELECT MAX(order_date) AS latest_order_date FROM orders),rfm_data AS (SELECT rb.customer_id,rb.customer_name,rb.customer_segment,CAST(JULIANDAY(dd.latest_order_date) - JULIANDAY(rb.last_purchase_date) AS INTEGER) AS recency,rb.frequency,rb.monetary FROM rfm_base AS rb CROSS JOIN dataset_date AS dd),rfm_scores AS (SELECT *,NTILE(5) OVER (ORDER BY recency DESC) AS recency_score,NTILE(5) OVER (ORDER BY frequency ASC) AS frequency_score,NTILE(5) OVER (ORDER BY monetary ASC) AS monetary_score FROM rfm_data),rfm_segmented AS (SELECT *,(recency_score || frequency_score || monetary_score) AS rfm_score,CASE WHEN recency_score >= 4 AND frequency_score >= 4 AND monetary_score >= 4 THEN 'Champions' WHEN recency_score >= 4 AND frequency_score >= 3 THEN 'Loyal Customers' WHEN recency_score >= 4 AND monetary_score >= 3 THEN 'Potential Loyalists' WHEN recency_score <= 2 AND frequency_score >= 3 AND monetary_score >= 3 THEN 'At Risk' WHEN recency_score <= 2 AND frequency_score <= 2 AND monetary_score <= 2 THEN 'Low Value' ELSE 'Regular Customers' END AS rfm_customer_segment FROM rfm_scores),priority_data AS (SELECT *,CASE WHEN rfm_customer_segment = 'Champions' THEN 'High Priority' WHEN rfm_customer_segment = 'Loyal Customers' THEN 'High Priority' WHEN rfm_customer_segment = 'At Risk' THEN 'High Priority' WHEN rfm_customer_segment = 'Potential Loyalists' THEN 'Medium Priority' WHEN rfm_customer_segment = 'Regular Customers' THEN 'Medium Priority' WHEN rfm_customer_segment = 'Low Value' THEN 'Low Priority' END AS business_priority FROM rfm_segmented) SELECT customer_id,customer_name,customer_segment,recency,frequency,ROUND(monetary, 2) AS monetary,recency_score,frequency_score,monetary_score,rfm_score,rfm_customer_segment,business_priority,RANK() OVER (ORDER BY CASE business_priority WHEN 'High Priority' THEN 1 WHEN 'Medium Priority' THEN 2 WHEN 'Low Priority' THEN 3 END,monetary DESC) AS priority_rank FROM priority_data ORDER BY priority_rank""")
rfm_priority_result = cursor.fetchall()
print("\nRFM Customer Priority Analysis:")
for row in rfm_priority_result:
    print(row)
print("\nSQL RFM Customer Priority Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.41 - RFM PRIORITY-WISE REVENUE ANALYSIS")
print("=" * 60)
cursor.execute("""WITH rfm_base AS (SELECT c.customer_id,c.customer_name,c.customer_segment,MAX(o.order_date) AS last_purchase_date,COUNT(o.order_id) AS frequency,SUM(o.final_amount) AS monetary FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment),dataset_date AS (SELECT MAX(order_date) AS latest_order_date FROM orders),rfm_data AS (SELECT rb.customer_id,rb.customer_name,rb.customer_segment,CAST(JULIANDAY(dd.latest_order_date) - JULIANDAY(rb.last_purchase_date)AS INTEGER) AS recency,rb.frequency,rb.monetary FROM rfm_base AS rb CROSS JOIN dataset_date AS dd),rfm_scores AS (SELECT *,NTILE(5) OVER (ORDER BY recency DESC) AS recency_score,NTILE(5) OVER (ORDER BY frequency ASC) AS frequency_score,NTILE(5) OVER (ORDER BY monetary ASC) AS monetary_score FROM rfm_data),rfm_segmented AS (SELECT *,CASE WHEN recency_score >= 4 AND frequency_score >= 4 AND monetary_score >= 4 THEN 'Champions' WHEN recency_score >= 4 AND frequency_score >= 3 THEN 'Loyal Customers' WHEN recency_score >= 4 AND monetary_score >= 3 THEN 'Potential Loyalists' WHEN recency_score <= 2 AND frequency_score >= 3 AND monetary_score >= 3 THEN 'At Risk' WHEN recency_score <= 2 AND frequency_score <= 2 AND monetary_score <= 2 THEN 'Low Value' ELSE 'Regular Customers' END AS rfm_customer_segment FROM rfm_scores),priority_data AS (SELECT *,CASE WHEN rfm_customer_segment IN ('Champions','Loyal Customers','At Risk') THEN 'High Priority' WHEN rfm_customer_segment IN ('Potential Loyalists','Regular Customers') THEN 'Medium Priority' WHEN rfm_customer_segment = 'Low Value' THEN 'Low Priority' END AS business_priority FROM rfm_segmented),priority_summary AS (SELECT business_priority,COUNT(*) AS customer_count,SUM(monetary) AS total_revenue,AVG(monetary) AS average_customer_revenue FROM priority_data GROUP BY business_priority),overall_summary AS (SELECT COUNT(*) AS total_customers,SUM(monetary) AS overall_revenue FROM priority_data) SELECT ps.business_priority,ps.customer_count,ROUND(ps.customer_count * 100.0 / os.total_customers,2) AS customer_percentage,ROUND(ps.total_revenue,2) AS total_revenue,ROUND(ps.average_customer_revenue,2) AS average_customer_revenue,ROUND(ps.total_revenue * 100.0 / os.overall_revenue,2) AS revenue_contribution_percentage FROM priority_summary AS ps CROSS JOIN overall_summary AS os ORDER BY CASE ps.business_priority WHEN 'High Priority' THEN 1 WHEN 'Medium Priority' THEN 2 WHEN 'Low Priority' THEN 3 END""")
rfm_priority_summary_result = cursor.fetchall()
print("\nRFM Priority-wise Revenue Analysis:")
for row in rfm_priority_summary_result:
    print(row)
print("\nSQL RFM Priority-wise Revenue Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.42 - RFM SEGMENT x PRODUCT CATEGORY ANALYSIS")
print("=" * 60)
cursor.execute("""WITH rfm_base AS (SELECT c.customer_id,c.customer_name,c.customer_segment,MAX(o.order_date) AS last_purchase_date,COUNT(o.order_id) AS frequency,SUM(o.final_amount) AS monetary FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name,c.customer_segment),dataset_date AS (SELECT MAX(order_date) AS latest_order_date FROM orders),rfm_data AS (SELECT rb.customer_id,rb.customer_name,rb.customer_segment,CAST(JULIANDAY(dd.latest_order_date) - JULIANDAY(rb.last_purchase_date)AS INTEGER) AS recency,rb.frequency,rb.monetary FROM rfm_base AS rb CROSS JOIN dataset_date AS dd),rfm_scores AS (SELECT *,NTILE(5) OVER (ORDER BY recency DESC) AS recency_score,NTILE(5) OVER (ORDER BY frequency ASC) AS frequency_score,NTILE(5) OVER (ORDER BY monetary ASC) AS monetary_score FROM rfm_data),rfm_segmented AS (SELECT *,CASE WHEN recency_score >= 4 AND frequency_score >= 4 AND monetary_score >= 4 THEN 'Champions' WHEN recency_score >= 4 AND frequency_score >= 3 THEN 'Loyal Customers' WHEN recency_score >= 4 AND monetary_score >= 3 THEN 'Potential Loyalists' WHEN recency_score <= 2 AND frequency_score >= 3 AND monetary_score >= 3 THEN 'At Risk' WHEN recency_score <= 2 AND frequency_score <= 2 AND monetary_score <= 2 THEN 'Low Value' ELSE 'Regular Customers' END AS rfm_customer_segment FROM rfm_scores) SELECT rs.rfm_customer_segment,o.category,COUNT(o.order_id) AS total_orders,SUM(o.quantity) AS total_quantity,ROUND(SUM(o.final_amount), 2) AS total_revenue,ROUND(AVG(o.final_amount), 2) AS average_order_value FROM rfm_segmented AS rs INNER JOIN orders AS o ON rs.customer_id = o.customer_id GROUP BY rs.rfm_customer_segment,o.category ORDER BY rs.rfm_customer_segment,total_revenue DESC""")
rfm_category_result = cursor.fetchall()
print("\nRFM Segment x Product Category Analysis:")
for row in rfm_category_result:
    print(row)
print("\nSQL RFM Segment x Product Category Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.43 - RFM SEGMENT x CATEGORY REVENUE CONTRIBUTION")
print("=" * 60)
cursor.execute("""WITH rfm_base AS (SELECT c.customer_id,c.customer_name,MAX(o.order_date) AS last_purchase_date,COUNT(o.order_id) AS frequency,SUM(o.final_amount) AS monetary FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name),dataset_date AS (SELECT MAX(order_date) AS latest_order_date FROM orders),rfm_data AS (SELECT rb.customer_id,rb.customer_name,CAST(JULIANDAY(dd.latest_order_date) - JULIANDAY(rb.last_purchase_date)AS INTEGER) AS recency,rb.frequency,rb.monetary FROM rfm_base AS rb CROSS JOIN dataset_date AS dd),rfm_scores AS (SELECT *,NTILE(5) OVER (ORDER BY recency DESC) AS recency_score,NTILE(5) OVER (ORDER BY frequency ASC) AS frequency_score,NTILE(5) OVER (ORDER BY monetary ASC) AS monetary_score FROM rfm_data),rfm_segmented AS (SELECT *,CASE WHEN recency_score >= 4 AND frequency_score >= 4 AND monetary_score >= 4 THEN 'Champions' WHEN recency_score >= 4 AND frequency_score >= 3 THEN 'Loyal Customers' WHEN recency_score >= 4 AND monetary_score >= 3 THEN 'Potential Loyalists' WHEN recency_score <= 2 AND frequency_score >= 3 AND monetary_score >= 3 THEN 'At Risk' WHEN recency_score <= 2 AND frequency_score <= 2 AND monetary_score <= 2 THEN 'Low Value' ELSE 'Regular Customers' END AS rfm_customer_segment FROM rfm_scores),category_revenue AS (SELECT rs.rfm_customer_segment,o.category,ROUND(SUM(o.final_amount), 2) AS category_revenue FROM rfm_segmented AS rs INNER JOIN orders AS o ON rs.customer_id = o.customer_id GROUP BY rs.rfm_customer_segment,o.category),segment_revenue AS (SELECT rfm_customer_segment,SUM(category_revenue) AS total_segment_revenue FROM category_revenue GROUP BY rfm_customer_segment) SELECT cr.rfm_customer_segment,cr.category,cr.category_revenue,ROUND(cr.category_revenue * 100.0 / sr.total_segment_revenue,2) AS revenue_contribution_percent FROM category_revenue AS cr INNER JOIN segment_revenue AS sr ON cr.rfm_customer_segment = sr.rfm_customer_segment ORDER BY cr.rfm_customer_segment,revenue_contribution_percent DESC""")
rfm_category_contribution = cursor.fetchall()
print("\nRFM Segment x Category Revenue Contribution:")
for row in rfm_category_contribution:
    print(row)
print("\nSQL RFM Segment x Category Revenue Contribution Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.44 - RFM SEGMENT x PRODUCT ANALYSIS")
print("=" * 60)
cursor.execute("""WITH rfm_base AS (SELECT c.customer_id,c.customer_name,MAX(o.order_date) AS last_purchase_date,COUNT(o.order_id) AS frequency,SUM(o.final_amount) AS monetary FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name),dataset_date AS (SELECT MAX(order_date) AS latest_order_date FROM orders),rfm_data AS (SELECT rb.customer_id,rb.customer_name,CAST(JULIANDAY(dd.latest_order_date) - JULIANDAY(rb.last_purchase_date)AS INTEGER) AS recency,rb.frequency,rb.monetary FROM rfm_base AS rb CROSS JOIN dataset_date AS dd),rfm_scores AS (SELECT *,NTILE(5) OVER (ORDER BY recency DESC) AS recency_score,NTILE(5) OVER (ORDER BY frequency ASC) AS frequency_score,NTILE(5) OVER (ORDER BY monetary ASC) AS monetary_score FROM rfm_data),rfm_segmented AS (SELECT *,CASE WHEN recency_score >= 4 AND frequency_score >= 4 AND monetary_score >= 4 THEN 'Champions' WHEN recency_score >= 4 AND frequency_score >= 3 THEN 'Loyal Customers' WHEN recency_score >= 4 AND monetary_score >= 3 THEN 'Potential Loyalists' WHEN recency_score <= 2 AND frequency_score >= 3 AND monetary_score >= 3 THEN 'At Risk' WHEN recency_score <= 2 AND frequency_score <= 2 AND monetary_score <= 2 THEN 'Low Value' ELSE 'Regular Customers' END AS rfm_customer_segment FROM rfm_scores) SELECT rs.rfm_customer_segment,o.product_name,o.category,COUNT(o.order_id) AS total_orders,SUM(o.quantity) AS total_quantity,ROUND(SUM(o.final_amount), 2) AS total_revenue,ROUND(AVG(o.final_amount), 2) AS average_order_value FROM rfm_segmented AS rs INNER JOIN orders AS o ON rs.customer_id = o.customer_id GROUP BY rs.rfm_customer_segment,o.product_name,o.category ORDER BY rs.rfm_customer_segment,total_revenue DESC""")
rfm_product_result = cursor.fetchall()
print("\nRFM Segment x Product Analysis:")
for row in rfm_product_result:
    print(row)
print("\nSQL RFM Segment x Product Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.45 - TOP 3 PRODUCTS BY REVENUE WITHIN EACH RFM SEGMENT")
print("=" * 60)
cursor.execute("""WITH rfm_base AS (SELECT c.customer_id,c.customer_name,MAX(o.order_date) AS last_purchase_date,COUNT(o.order_id) AS frequency,SUM(o.final_amount) AS monetary FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id,c.customer_name),dataset_date AS (SELECT MAX(order_date) AS latest_order_date FROM orders),rfm_data AS (SELECT rb.customer_id,rb.customer_name,CAST(JULIANDAY(dd.latest_order_date) - JULIANDAY(rb.last_purchase_date)AS INTEGER) AS recency,rb.frequency,rb.monetary FROM rfm_base AS rb CROSS JOIN dataset_date AS dd),rfm_scores AS (SELECT *,NTILE(5) OVER (ORDER BY recency DESC) AS recency_score,NTILE(5) OVER (ORDER BY frequency ASC) AS frequency_score,NTILE(5) OVER (ORDER BY monetary ASC) AS monetary_score FROM rfm_data),rfm_segmented AS (SELECT *,CASE WHEN recency_score >= 4 AND frequency_score >= 4 AND monetary_score >= 4 THEN 'Champions' WHEN recency_score >= 4 AND frequency_score >= 3 THEN 'Loyal Customers' WHEN recency_score >= 4 AND monetary_score >= 3 THEN 'Potential Loyalists' WHEN recency_score <= 2 AND frequency_score >= 3 AND monetary_score >= 3 THEN 'At Risk' WHEN recency_score <= 2 AND frequency_score <= 2 AND monetary_score <= 2 THEN 'Low Value' ELSE 'Regular Customers' END AS rfm_customer_segment FROM rfm_scores),product_revenue AS (SELECT rs.rfm_customer_segment,o.product_name,o.category,SUM(o.quantity) AS total_quantity,ROUND(SUM(o.final_amount), 2) AS total_revenue FROM rfm_segmented AS rs INNER JOIN orders AS o ON rs.customer_id = o.customer_id GROUP BY rs.rfm_customer_segment,o.product_name,o.category),ranked_products AS (SELECT *,RANK() OVER (PARTITION BY rfm_customer_segment ORDER BY total_revenue DESC) AS product_rank FROM product_revenue) SELECT rfm_customer_segment,product_name,category,total_quantity,total_revenue,product_rank FROM ranked_products WHERE product_rank <= 3 ORDER BY rfm_customer_segment,product_rank;""")
top3_rfm_products = cursor.fetchall()
print("\nTop 3 Products by Revenue within Each RFM Segment:")
for row in top3_rfm_products:
    print(row)
print("\nSQL Top 3 Products by RFM Segment Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.46 - CUSTOMER SEGMENT x PRODUCT CATEGORY PERFORMANCE")
print("=" * 60)
cursor.execute("""SELECT c.customer_segment,o.category,COUNT(o.order_id) AS total_orders,SUM(o.quantity) AS total_quantity,ROUND(SUM(o.final_amount), 2) AS total_revenue,ROUND(AVG(o.final_amount), 2) AS average_order_value FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.category ORDER BY c.customer_segment,total_revenue DESC""")
customer_category_result = cursor.fetchall()
print("\nCustomer Segment x Product Category Performance:")
for row in customer_category_result:
    print(row)
print("\nSQL Customer Segment x Product Category Performance Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.47 - CUSTOMER SEGMENT x CATEGORY REVENUE CONTRIBUTION")
print("=" * 60)
cursor.execute("""WITH category_revenue AS (SELECT c.customer_segment,o.category,ROUND(SUM(o.final_amount), 2) AS category_revenue FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.category),segment_revenue AS (SELECT customer_segment,SUM(category_revenue) AS total_segment_revenue FROM category_revenue GROUP BY customer_segment)SELECT cr.customer_segment,cr.category,cr.category_revenue,ROUND(cr.category_revenue * 100.0 / sr.total_segment_revenue,2) AS revenue_contribution_percent FROM category_revenue AS cr INNER JOIN segment_revenue AS sr ON cr.customer_segment = sr.customer_segment ORDER BY cr.customer_segment,revenue_contribution_percent DESC""")
customer_category_contribution = cursor.fetchall()
print("\nCustomer Segment x Category Revenue Contribution:")
for row in customer_category_contribution:
    print(row)
print("\nSQL Customer Segment x Category Revenue Contribution Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.48 - CUSTOMER SEGMENT x PRODUCT REVENUE ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT c.customer_segment,o.product_name,o.category,COUNT(o.order_id) AS total_orders,SUM(o.quantity) AS total_quantity,ROUND(SUM(o.final_amount), 2) AS total_revenue,ROUND(AVG(o.final_amount), 2) AS average_order_value FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name,o.category ORDER BY c.customer_segment,total_revenue DESC""")
customer_product_result = cursor.fetchall()
print("\nCustomer Segment x Product Revenue Analysis:")
for row in customer_product_result:
    print(row)
print("\nSQL Customer Segment x Product Revenue Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.49 - CUSTOMER SEGMENT x PRODUCT REVENUE CONTRIBUTION")
print("=" * 60)
cursor.execute("""WITH product_revenue AS (SELECT c.customer_segment,o.product_name,ROUND(SUM(o.final_amount), 2) AS product_revenue FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name),segment_revenue AS (SELECT customer_segment,SUM(product_revenue) AS total_segment_revenue FROM product_revenue GROUP BY customer_segment) SELECT pr.customer_segment,pr.product_name,pr.product_revenue,ROUND(pr.product_revenue * 100.0 / sr.total_segment_revenue,2) AS revenue_contribution_percent FROM product_revenue AS pr INNER JOIN segment_revenue AS sr ON pr.customer_segment = sr.customer_segment ORDER BY pr.customer_segment,revenue_contribution_percent DESC""")
customer_product_contribution = cursor.fetchall()
print("\nCustomer Segment x Product Revenue Contribution:")
for row in customer_product_contribution:
    print(row)
print("\nSQL Customer Segment x Product Revenue Contribution Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.50 - CUSTOMER SEGMENT x PRODUCT TOP 3")
print("=" * 60)
cursor.execute("""WITH product_revenue AS (SELECT c.customer_segment,o.product_name,o.category,ROUND(SUM(o.final_amount), 2) AS total_revenue FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name,o.category),ranked_products AS (SELECT customer_segment,product_name,category,total_revenue,RANK() OVER (PARTITION BY customer_segment ORDER BY total_revenue DESC) AS product_rank FROM product_revenue) SELECT customer_segment,product_name,category,total_revenue,product_rank FROM ranked_products WHERE product_rank <= 3 ORDER BY customer_segment,product_rank""")
customer_segment_top3 = cursor.fetchall()
print("\nTop 3 Products by Customer Segment:")
for row in customer_segment_top3:
    print(row)
print("\nSQL Customer Segment x Product Top 3 Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.51 - CUSTOMER SEGMENT x PRODUCT QUANTITY ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT c.customer_segment,o.product_name,o.category,SUM(o.quantity) AS total_quantity,COUNT(o.order_id) AS total_orders,ROUND(SUM(o.final_amount), 2) AS total_revenue FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name,o.category ORDER BY c.customer_segment,total_quantity DESC""")
customer_product_quantity = cursor.fetchall()
print("\nCustomer Segment x Product Quantity Analysis:")
for row in customer_product_quantity:
    print(row)
print("\nSQL Customer Segment x Product Quantity Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.52 - CUSTOMER SEGMENT x PRODUCT QUANTITY RANKING")
print("=" * 60)
cursor.execute("""WITH product_quantity AS (SELECT c.customer_segment,o.product_name,o.category,SUM(o.quantity) AS total_quantity FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name,o.category),ranked_products AS (SELECT customer_segment,product_name,category,total_quantity,RANK() OVER (PARTITION BY customer_segment ORDER BY total_quantity DESC) AS quantity_rank FROM product_quantity) SELECT customer_segment,product_name,category,total_quantity,quantity_rank FROM ranked_products WHERE quantity_rank <= 3 ORDER BY customer_segment,quantity_rank""")
customer_quantity_top3 = cursor.fetchall()
print("\nTop 3 Products by Quantity within Each Customer Segment:")
for row in customer_quantity_top3:
    print(row)
print("\nSQL Customer Segment x Product Quantity Ranking Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.53 - CUSTOMER SEGMENT x PRODUCT QUANTITY CONTRIBUTION")
print("=" * 60)
cursor.execute("""WITH product_quantity AS (SELECT c.customer_segment,o.product_name,SUM(o.quantity) AS product_quantity FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name),segment_quantity AS (SELECT customer_segment,SUM(product_quantity) AS total_segment_quantity FROM product_quantity GROUP BY customer_segment) SELECT pq.customer_segment,pq.product_name,pq.product_quantity,ROUND(pq.product_quantity * 100.0 / sq.total_segment_quantity,2) AS quantity_contribution_percent FROM product_quantity AS pq INNER JOIN segment_quantity AS sq ON pq.customer_segment = sq.customer_segment ORDER BY pq.customer_segment,quantity_contribution_percent DESC""")
customer_quantity_contribution = cursor.fetchall()
print("\nCustomer Segment x Product Quantity Contribution:")
for row in customer_quantity_contribution:
    print(row)
print("\nSQL Customer Segment x Product Quantity Contribution Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.54 - CUSTOMER SEGMENT x PRODUCT AOV ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT c.customer_segment,o.product_name,o.category,COUNT(o.order_id) AS total_orders,SUM(o.quantity) AS total_quantity,ROUND(SUM(o.final_amount), 2) AS total_revenue,ROUND(AVG(o.final_amount), 2) AS average_order_value FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name,o.category ORDER BY c.customer_segment,average_order_value DESC""")
customer_product_aov = cursor.fetchall()
print("\nCustomer Segment x Product AOV Analysis:")
for row in customer_product_aov:
    print(row)
print("\nSQL Customer Segment x Product AOV Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.55 - CUSTOMER SEGMENT x PRODUCT AOV RANKING")
print("=" * 60)
cursor.execute("""WITH product_aov AS (SELECT c.customer_segment,o.product_name,o.category,COUNT(o.order_id) AS total_orders,ROUND(AVG(o.final_amount), 2) AS average_order_value FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name,o.category),ranked_products AS (SELECT customer_segment,product_name,category,total_orders,average_order_value,RANK() OVER (PARTITION BY customer_segment ORDER BY average_order_value DESC) AS aov_rank FROM product_aov) SELECT customer_segment,product_name,category,total_orders,average_order_value,aov_rank FROM ranked_products WHERE aov_rank <= 3 ORDER BY customer_segment,aov_rank""")
customer_product_aov_top3 = cursor.fetchall()
print("\nTop 3 Products by AOV within Each Customer Segment:")
for row in customer_product_aov_top3:
    print(row)
print("\nSQL Customer Segment x Product AOV Ranking Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.56 - CUSTOMER SEGMENT x PRODUCT REVENUE CONTRIBUTION")
print("=" * 60)
cursor.execute("""WITH product_revenue AS (SELECT c.customer_segment,o.product_name,ROUND(SUM(o.final_amount), 2) AS product_revenue FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name),segment_revenue AS (SELECT customer_segment,SUM(product_revenue) AS total_segment_revenue FROM product_revenue GROUP BY customer_segment) SELECT pr.customer_segment,pr.product_name,pr.product_revenue,ROUND(pr.product_revenue * 100.0 / sr.total_segment_revenue,2) AS revenue_contribution_percent FROM product_revenue AS pr INNER JOIN segment_revenue AS sr ON pr.customer_segment = sr.customer_segment ORDER BY pr.customer_segment,revenue_contribution_percent DESC""")
customer_product_revenue_contribution = cursor.fetchall()
print("\nCustomer Segment x Product Revenue Contribution:")
for row in customer_product_revenue_contribution:
    print(row)
print("\nSQL Customer Segment x Product Revenue Contribution Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.57 - CUSTOMER SEGMENT x PRODUCT REVENUE RANKING")
print("=" * 60)
cursor.execute("""WITH product_revenue AS (SELECT c.customer_segment,o.product_name,o.category,ROUND(SUM(o.final_amount), 2) AS total_revenue FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name,o.category),ranked_products AS (SELECT customer_segment,product_name,category,total_revenue,RANK() OVER (PARTITION BY customer_segment ORDER BY total_revenue DESC) AS revenue_rank FROM product_revenue) SELECT customer_segment,product_name,category,total_revenue,revenue_rank FROM ranked_products WHERE revenue_rank <= 3 ORDER BY customer_segment,revenue_rank""")
customer_product_revenue_top3 = cursor.fetchall()
print("\nTop 3 Products by Revenue within Each Customer Segment:")
for row in customer_product_revenue_top3:
    print(row)
print("\nSQL Customer Segment x Product Revenue Ranking Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.58 - CUSTOMER SEGMENT x TOP 3 PRODUCT REVENUE SHARE")
print("=" * 60)
cursor.execute("""WITH product_revenue AS (SELECT c.customer_segment,o.product_name,ROUND(SUM(o.final_amount), 2) AS product_revenue FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name),ranked_products AS (SELECT customer_segment,product_name,product_revenue,RANK() OVER (PARTITION BY customer_segment ORDER BY product_revenue DESC) AS revenue_rank FROM product_revenue),segment_revenue AS (SELECT customer_segment,SUM(product_revenue) AS total_segment_revenue FROM product_revenue GROUP BY customer_segment),top3_revenue AS (SELECT customer_segment,SUM(product_revenue) AS top3_product_revenue FROM ranked_products WHERE revenue_rank <= 3 GROUP BY customer_segment) SELECT t.customer_segment,ROUND(t.top3_product_revenue, 2) AS top3_product_revenue,ROUND(s.total_segment_revenue, 2) AS total_segment_revenue,ROUND(t.top3_product_revenue * 100.0 / s.total_segment_revenue,2) AS top3_revenue_share_percent FROM top3_revenue AS t INNER JOIN segment_revenue AS s ON t.customer_segment = s.customer_segment ORDER BY top3_revenue_share_percent DESC""")
customer_segment_top3_share = cursor.fetchall()
print("\nTop 3 Product Revenue Share by Customer Segment:")
for row in customer_segment_top3_share:
    print(row)
print("\nSQL Customer Segment x Top 3 Product Revenue Share Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.59 - CUSTOMER SEGMENT x TOP 3 PRODUCT QUANTITY SHARE")
print("=" * 60)
cursor.execute("""WITH product_quantity AS (SELECT c.customer_segment,o.product_name,SUM(o.quantity) AS product_quantity FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name),ranked_products AS (SELECT customer_segment,product_name,product_quantity,RANK() OVER (PARTITION BY customer_segment ORDER BY product_quantity DESC) AS quantity_rank FROM product_quantity),segment_quantity AS (SELECT customer_segment,SUM(product_quantity) AS total_segment_quantity FROM product_quantity GROUP BY customer_segment),top3_quantity AS (SELECT customer_segment,SUM(product_quantity) AS top3_product_quantity FROM ranked_products WHERE quantity_rank <= 3 GROUP BY customer_segment)SELECT t.customer_segment,t.top3_product_quantity,s.total_segment_quantity,ROUND(t.top3_product_quantity * 100.0 / s.total_segment_quantity,2) AS top3_quantity_share_percent FROM top3_quantity AS t INNER JOIN segment_quantity AS s ON t.customer_segment = s.customer_segment ORDER BY top3_quantity_share_percent DESC""")
customer_segment_top3_quantity_share = cursor.fetchall()
print("\nTop 3 Product Quantity Share by Customer Segment:")
for row in customer_segment_top3_quantity_share:
    print(row)
print("\nSQL Customer Segment x Top 3 Product Quantity Share Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.60 - CUSTOMER SEGMENT x TOP 3 PRODUCT REVENUE + QUANTITY")
print("=" * 60)
cursor.execute("""WITH product_performance AS (SELECT c.customer_segment,o.product_name,SUM(o.quantity) AS total_quantity,ROUND(SUM(o.final_amount), 2) AS total_revenue FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name),ranked_products AS (SELECT customer_segment,product_name,total_quantity,total_revenue,RANK() OVER (PARTITION BY customer_segment ORDER BY total_revenue DESC) AS revenue_rank FROM product_performance)SELECT customer_segment,product_name,total_quantity,total_revenue,revenue_rank FROM ranked_products WHERE revenue_rank <= 3 ORDER BY customer_segment,revenue_rank""")
customer_segment_top3_performance = cursor.fetchall()
print("\nTop 3 Products by Revenue with Quantity:")
print("")
for row in customer_segment_top3_performance:
    print(row)
print("\nSQL Customer Segment x Top 3 Product Revenue + Quantity Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.61 - CUSTOMER SEGMENT x TOP 3 PRODUCT AOV")
print("=" * 60)
cursor.execute("""WITH product_aov AS (SELECT c.customer_segment,o.product_name,o.category,COUNT(o.order_id) AS total_orders,ROUND(AVG(o.final_amount), 2) AS average_order_value FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name,o.category),ranked_products AS (SELECT customer_segment,product_name,category,total_orders,average_order_value,RANK() OVER (PARTITION BY customer_segment ORDER BY average_order_value DESC) AS aov_rank FROM product_aov)SELECT customer_segment,product_name,category,total_orders,average_order_value,aov_rank FROM ranked_products WHERE aov_rank <= 3 ORDER BY customer_segment,aov_rank""")
customer_segment_top3_aov = cursor.fetchall()
print("\nTop 3 Products by AOV within Each Customer Segment:")
for row in customer_segment_top3_aov:
    print(row)
print("\nSQL Customer Segment x Top 3 Product AOV Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.62 - CUSTOMER SEGMENT x TOP 3 PRODUCT AOV + REVENUE")
print("=" * 60)
cursor.execute("""WITH product_performance AS (SELECT c.customer_segment,o.product_name,o.category,COUNT(o.order_id) AS total_orders,ROUND(AVG(o.final_amount), 2) AS average_order_value,ROUND(SUM(o.final_amount), 2) AS total_revenue FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name,o.category),ranked_products AS (SELECT customer_segment,product_name,category,total_orders,average_order_value,total_revenue,RANK() OVER (PARTITION BY customer_segment ORDER BY average_order_value DESC) AS aov_rank FROM product_performance)SELECT customer_segment,product_name,category,total_orders,average_order_value,total_revenue,aov_rank FROM ranked_products WHERE aov_rank <= 3 ORDER BY customer_segment,aov_rank""")
customer_segment_top3_aov_revenue = cursor.fetchall()
print("\nTop 3 Products by AOV with Revenue:")
for row in customer_segment_top3_aov_revenue:
    print(row)
print("\nSQL Customer Segment x Top 3 Product AOV + Revenue Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.63 - CUSTOMER SEGMENT x PRODUCT REVENUE vs QUANTITY")
print("=" * 60)
cursor.execute("""SELECT c.customer_segment,o.product_name,o.category,SUM(o.quantity) AS total_quantity,ROUND(SUM(o.final_amount), 2) AS total_revenue,ROUND(SUM(o.final_amount) * 1.0 / SUM(o.quantity),2) AS revenue_per_unit FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name,o.category ORDER BY c.customer_segment,total_revenue DESC""")
segment_product_revenue_quantity = cursor.fetchall()
print("\nCustomer Segment x Product Revenue vs Quantity:")
for row in segment_product_revenue_quantity:
    print(row)
print("\nSQL Customer Segment x Product Revenue vs Quantity Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.64 - CUSTOMER SEGMENT x PRODUCT REVENUE PER UNIT RANKING")
print("=" * 60)
cursor.execute("""WITH product_performance AS (SELECT c.customer_segment,o.product_name,o.category,SUM(o.quantity) AS total_quantity,ROUND(SUM(o.final_amount), 2) AS total_revenue,ROUND(SUM(o.final_amount) * 1.0 / SUM(o.quantity),2) AS revenue_per_unit FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name,o.category),ranked_products AS (SELECT customer_segment,product_name,category,total_quantity,total_revenue,revenue_per_unit,RANK() OVER (PARTITION BY customer_segment ORDER BY revenue_per_unit DESC) AS revenue_per_unit_rank FROM product_performance)SELECT customer_segment,product_name,category,total_quantity,total_revenue,revenue_per_unit,revenue_per_unit_rank FROM ranked_products WHERE revenue_per_unit_rank <= 3 ORDER BY customer_segment,revenue_per_unit_rank""")
segment_product_rpu_ranking = cursor.fetchall()
print("\nTop 3 Products by Revenue per Unit within Each Customer Segment:")
for row in segment_product_rpu_ranking:
    print(row)
print("\nSQL Customer Segment x Product Revenue per Unit Ranking Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.65 - CUSTOMER SEGMENT x PRODUCT REVENUE PER UNIT CONTRIBUTION")
print("=" * 60)
cursor.execute("""WITH product_performance AS (SELECT c.customer_segment,o.product_name,o.category,SUM(o.quantity) AS total_quantity,ROUND(SUM(o.final_amount), 2) AS total_revenue,ROUND(SUM(o.final_amount) * 1.0 / SUM(o.quantity),2) AS revenue_per_unit FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.product_name,o.category),segment_performance AS (SELECT customer_segment,SUM(total_revenue) AS segment_revenue,SUM(total_quantity) AS segment_quantity FROM product_performance GROUP BY customer_segment) SELECT p.customer_segment,p.product_name,p.category,p.revenue_per_unit,ROUND(p.total_revenue * 100.0 / s.segment_revenue,2) AS revenue_contribution_percent,ROUND(p.total_quantity * 100.0 / s.segment_quantity,2) AS quantity_contribution_percent FROM product_performance AS p INNER JOIN segment_performance AS s ON p.customer_segment = s.customer_segment ORDER BY p.customer_segment,revenue_contribution_percent DESC""")
segment_product_rpu_contribution = cursor.fetchall()
print("\nProduct Revenue per Unit with Revenue and Quantity Contribution:")
for row in segment_product_rpu_contribution:
    print(row)
print("\nSQL Customer Segment x Product Revenue per Unit Contribution Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.66 - CUSTOMER SEGMENT REVENUE EFFICIENCY")
print("=" * 60)
cursor.execute("""SELECT c.customer_segment,SUM(o.quantity) AS total_quantity,ROUND(SUM(o.final_amount), 2) AS total_revenue,ROUND(SUM(o.final_amount) * 1.0 / SUM(o.quantity),2) AS revenue_per_unit FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment ORDER BY revenue_per_unit DESC""")
segment_revenue_efficiency = cursor.fetchall()
print("\nCustomer Segment Revenue Efficiency:")
for row in segment_revenue_efficiency:
    print(row)
print("\nSQL Customer Segment Revenue Efficiency Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.67 - CUSTOMER SEGMENT x ORDER STATUS ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT c.customer_segment,o.order_status,COUNT(*) AS order_count,ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY c.customer_segment),2) AS status_percentage FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.order_status ORDER BY c.customer_segment,order_count DESC""")
segment_order_status = cursor.fetchall()
print("\nCustomer Segment x Order Status:")
for row in segment_order_status:
    print(row)
print("\nSQL Customer Segment x Order Status Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.68 - CUSTOMER SEGMENT x ORDER STATUS REVENUE")
print("=" * 60)
cursor.execute("""SELECT c.customer_segment,o.order_status,COUNT(*) AS order_count,ROUND(SUM(o.final_amount), 2) AS total_revenue,ROUND(SUM(o.final_amount) * 100.0 / SUM(SUM(o.final_amount)) OVER (PARTITION BY c.customer_segment),2) AS revenue_percentage FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.order_status ORDER BY c.customer_segment,total_revenue DESC""")
segment_status_revenue = cursor.fetchall()
print("\nCustomer Segment x Order Status Revenue:")
for row in segment_status_revenue:
    print(row)
print("\nSQL Customer Segment x Order Status Revenue Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.69 - CUSTOMER SEGMENT x RETURN & CANCELLATION RATE")
print("=" * 60)
cursor.execute("""SELECT c.customer_segment,COUNT(*) AS total_orders,SUM(CASE WHEN o.order_status = 'Returned' THEN 1 ELSE 0 END) AS returned_orders,SUM(CASE WHEN o.order_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_orders,ROUND(SUM(CASE WHEN o.order_status = 'Returned' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),2) AS return_rate,ROUND(SUM(CASE WHEN o.order_status = 'Cancelled' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),2) AS cancellation_rate,ROUND(SUM(CASE WHEN o.order_status IN ('Returned', 'Cancelled') THEN 1 ELSE 0 END) * 100.0 / COUNT(*),2) AS combined_issue_rate FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment ORDER BY combined_issue_rate DESC""")
segment_issue_rate = cursor.fetchall()
print("\nCustomer Segment x Return & Cancellation Rate:")
for row in segment_issue_rate:
    print(row)
print("\nSQL Customer Segment x Return & Cancellation Rate Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.70 - CUSTOMER SEGMENT x NET SUCCESSFUL REVENUE")
print("=" * 60)
cursor.execute("""SELECT c.customer_segment,ROUND(SUM(CASE WHEN o.order_status = 'Delivered' THEN o.final_amount ELSE 0 END),2) AS delivered_revenue,ROUND(SUM(CASE WHEN o.order_status IN ('Returned', 'Cancelled') THEN o.final_amount ELSE 0 END),2) AS affected_revenue,ROUND(SUM(o.final_amount),2) AS total_revenue,ROUND(SUM(CASE WHEN o.order_status = 'Delivered' THEN o.final_amount ELSE 0 END) * 100.0 / SUM(o.final_amount),2) AS delivered_revenue_percentage FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment ORDER BY delivered_revenue DESC""")
segment_net_revenue = cursor.fetchall()
print("\nCustomer Segment x Successful vs Affected Revenue:")
for row in segment_net_revenue:
    print(row)
print("\nSQL Customer Segment x Net Successful Revenue Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.71 - CUSTOMER SEGMENT x AOV BY ORDER STATUS")
print("=" * 60)
cursor.execute("""SELECT c.customer_segment,o.order_status,COUNT(*) AS order_count,ROUND(SUM(o.final_amount),2) AS total_revenue,ROUND(AVG(o.final_amount),2) AS average_order_value FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.order_status ORDER BY c.customer_segment,average_order_value DESC""")
segment_status_aov = cursor.fetchall()
print("\nCustomer Segment x Order Status AOV:")
for row in segment_status_aov:
    print(row)
print("\nSQL Customer Segment x AOV by Order Status Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.72 - CUSTOMER SEGMENT x PAYMENT METHOD ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT c.customer_segment,o.payment_method,COUNT(*) AS order_count,ROUND(SUM(o.final_amount),2) AS total_revenue,ROUND(AVG(o.final_amount),2) AS average_order_value FROM orders AS o INNER JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_segment,o.payment_method ORDER BY c.customer_segment,total_revenue DESC""")
segment_payment_analysis = cursor.fetchall()
print("\nCustomer Segment x Payment Method:")
for row in segment_payment_analysis:
    print(row)
print("\nSQL Customer Segment x Payment Method Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.73 - PAYMENT METHOD x ORDER STATUS ANALYSIS")
print("=" * 60)
cursor.execute("""SELECT o.payment_method,o.order_status,COUNT(*) AS order_count,ROUND(SUM(o.final_amount),2) AS total_revenue,ROUND(AVG(o.final_amount),2) AS average_order_value FROM orders AS o GROUP BY o.payment_method,o.order_status ORDER BY o.payment_method,order_count DESC""")
payment_status_analysis = cursor.fetchall()
print("\nPayment Method x Order Status:")
for row in payment_status_analysis:
    print(row)
print("\nSQL Payment Method x Order Status Analysis Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.74 - PAYMENT METHOD x REVENUE CONTRIBUTION")
print("=" * 60)
cursor.execute("""SELECT payment_method,COUNT(*) AS order_count,ROUND(SUM(final_amount), 2) AS total_revenue,ROUND(SUM(final_amount) * 100.0 / SUM(SUM(final_amount)) OVER (),2) AS revenue_contribution_percentage FROM orders GROUP BY payment_method ORDER BY total_revenue DESC""")
payment_revenue_contribution = cursor.fetchall()
print("\nPayment Method Revenue Contribution:")
for row in payment_revenue_contribution:
    print(row)
print("\nSQL Payment Method x Revenue Contribution Completed Successfully!")

print("\n" + "=" * 60)
print("STEP 19.75 - FINAL SQL BUSINESS SUMMARY")
print("=" * 60)
cursor.execute("""SELECT COUNT(*) AS total_orders,COUNT(DISTINCT customer_id) AS total_customers,COUNT(DISTINCT product_id) AS total_products,ROUND(SUM(final_amount), 2) AS total_revenue,ROUND(AVG(final_amount), 2) AS average_order_value FROM orders""")
final_sql_summary = cursor.fetchone()
print("\nFinal SQL Business Summary:")
print("Total Orders:", final_sql_summary[0])
print("Total Customers:", final_sql_summary[1])
print("Total Products:", final_sql_summary[2])
print("Total Revenue:", final_sql_summary[3])
print("Average Order Value:", final_sql_summary[4])
print("\nSQL ANALYTICS PHASE COMPLETED SUCCESSFULLY!")
print("STEP 19.75 - FINAL SQL STEP COMPLETED!")

print("\n" + "=" * 60)
print("STEP 20.1 - TOTAL REVENUE KPI")
print("=" * 60)
cursor.execute("""SELECT ROUND(SUM(final_amount), 2) AS total_revenue FROM orders""")
total_revenue = cursor.fetchone()[0]
print("\nTotal Revenue KPI:")
print("₹", total_revenue)
print("\nSTEP 20.1 - TOTAL REVENUE KPI COMPLETED SUCCESSFULLY!")

print("\n" + "=" * 60)
print("STEP 20.2 - TOTAL ORDERS KPI")
print("=" * 60)
cursor.execute("""SELECT COUNT(*) AS total_orders FROM orders""")
total_orders = cursor.fetchone()[0]
print("\nTotal Orders KPI:")
print(total_orders)
print("\nSTEP 20.2 - TOTAL ORDERS KPI COMPLETED SUCCESSFULLY!")

print("\n" + "=" * 60)
print("STEP 20.3 - TOTAL CUSTOMERS KPI")
print("=" * 60)
cursor.execute("""SELECT COUNT(DISTINCT customer_id) AS total_customers FROM orders""")
total_customers = cursor.fetchone()[0]
print("\nTotal Customers KPI:")
print(total_customers)
print("\nSTEP 20.3 - TOTAL CUSTOMERS KPI COMPLETED SUCCESSFULLY!")

print("\n" + "=" * 60)
print("STEP 20.4 - AVERAGE ORDER VALUE KPI")
print("=" * 60)
cursor.execute("""SELECT ROUND(AVG(final_amount), 2) AS average_order_value FROM orders""")
average_order_value = cursor.fetchone()[0]
print("\nAverage Order Value KPI:")
print("₹", average_order_value)
print("\nSTEP 20.4 - AVERAGE ORDER VALUE KPI COMPLETED SUCCESSFULLY!")

print("\n" + "=" * 60)
print("STEP 20.5 - TOTAL QUANTITY SOLD KPI")
print("=" * 60)
cursor.execute("""SELECT SUM(quantity) AS total_quantity_sold FROM orders""")
total_quantity_sold = cursor.fetchone()[0]
print("\nTotal Quantity Sold KPI:")
print(total_quantity_sold)
print("\nSTEP 20.5 - TOTAL QUANTITY SOLD KPI COMPLETED SUCCESSFULLY!")

print("\n" + "=" * 60)
print("STEP 20.6 - ORDER STATUS KPIs")
print("=" * 60)
cursor.execute("""SELECT order_status,COUNT(*) AS order_count FROM orders GROUP BY order_status ORDER BY order_count DESC""")
order_status_kpis = cursor.fetchall()
print("\nOrder Status KPIs:")
for row in order_status_kpis:
    print(row)
print("\nSTEP 20.6 - ORDER STATUS KPIs COMPLETED SUCCESSFULLY!")

print("\n" + "=" * 60)
print("STEP 20.7 - RETURN RATE KPI")
print("=" * 60)
cursor.execute("""SELECT ROUND(SUM(CASE WHEN order_status = 'Returned' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS return_rate FROM orders""")
return_rate = cursor.fetchone()[0]
print("\nReturn Rate KPI:")
print(return_rate, "%")
print("\nSTEP 20.7 - RETURN RATE KPI COMPLETED SUCCESSFULLY!")

print("\n" + "=" * 60)
print("STEP 20.8 - CANCELLATION RATE KPI")
print("=" * 60)
cursor.execute("""SELECT ROUND(SUM(CASE WHEN order_status = 'Cancelled' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),2) AS cancellation_rate FROM orders""")
cancellation_rate = cursor.fetchone()[0]
print("\nCancellation Rate KPI:")
print(cancellation_rate, "%")
print("\nSTEP 20.8 - CANCELLATION RATE KPI COMPLETED SUCCESSFULLY!")

print("\n" + "=" * 60)
print("STEP 20.9 - REPEAT CUSTOMER RATE KPI")
print("=" * 60)
cursor.execute("""WITH customer_orders AS (SELECT customer_id,COUNT(*) AS order_count FROM orders GROUP BY customer_id),customer_summary AS (SELECT COUNT(*) AS total_customers,SUM(CASE WHEN order_count >= 2 THEN 1 ELSE 0 END) AS repeat_customers FROM customer_orders)SELECT total_customers,repeat_customers,ROUND(repeat_customers * 100.0 / total_customers,2) AS repeat_customer_rate FROM customer_summary""")
repeat_customer_kpi = cursor.fetchone()
print("\nRepeat Customer KPI:")
print("Total Customers:", repeat_customer_kpi[0])
print("Repeat Customers:", repeat_customer_kpi[1])
print("Repeat Customer Rate:", repeat_customer_kpi[2], "%")
print("\nSTEP 20.9 - REPEAT CUSTOMER RATE KPI COMPLETED SUCCESSFULLY!")

print("\n" + "=" * 60)
print("STEP 20.10 - REVENUE BY CATEGORY KPI")
print("=" * 60)
cursor.execute("""SELECT category,COUNT(*) AS order_count,ROUND(SUM(final_amount), 2) AS total_revenue,ROUND(SUM(final_amount) * 100.0 / SUM(SUM(final_amount)) OVER (),2) AS revenue_contribution_percentage FROM orders GROUP BY category ORDER BY total_revenue DESC""")
category_revenue_kpi = cursor.fetchall()
print("\nRevenue by Category:")
for row in category_revenue_kpi:
    print(row)
print("\nSTEP 20.10 - REVENUE BY CATEGORY KPI COMPLETED SUCCESSFULLY!")

print("\n" + "=" * 60)
print("STEP 20.11 - REVENUE BY CUSTOMER SEGMENT KPI")
print("=" * 60)
cursor.execute("""WITH customer_metrics AS (SELECT customer_id,COUNT(*) AS frequency,SUM(final_amount) AS monetary FROM orders GROUP BY customer_id),customer_segments AS (SELECT customer_id,frequency,monetary,CASE WHEN frequency >= 40 AND monetary >= 800000 THEN 'Premium' WHEN frequency >= 20 AND monetary >= 400000 THEN 'Regular' ELSE 'New' END AS customer_segment FROM customer_metrics)SELECT customer_segment,COUNT(DISTINCT customer_id) AS customer_count,SUM(frequency) AS order_count,ROUND(SUM(monetary), 2) AS total_revenue,ROUND(SUM(monetary) * 100.0 / SUM(SUM(monetary)) OVER (),2) AS revenue_contribution_percentage FROM customer_segments GROUP BY customer_segment ORDER BY total_revenue DESC""")
segment_revenue_kpi = cursor.fetchall()
print("\nRevenue by Customer Segment:")
for row in segment_revenue_kpi:
    print(row)
print("\nSTEP 20.11 - REVENUE BY CUSTOMER SEGMENT KPI COMPLETED SUCCESSFULLY!")

print("\n" + "=" * 60)
print("STEP 20.12 - MONTHLY REVENUE KPI")
print("=" * 60)
cursor.execute("""SELECT order_month,COUNT(*) AS order_count,ROUND(SUM(final_amount), 2) AS total_revenue,ROUND(AVG(final_amount), 2) AS average_order_value FROM orders GROUP BY order_month ORDER BY order_month""")
monthly_revenue_kpi = cursor.fetchall()
print("\nMonthly Revenue KPI:")
for row in monthly_revenue_kpi:
    print(row)
print("\nSTEP 20.12 - MONTHLY REVENUE KPI COMPLETED SUCCESSFULLY!")

print("\n" + "=" * 60)
print("STEP 20.13 - FINAL BUSINESS KPI SUMMARY")
print("=" * 60)
cursor.execute("""SELECT COUNT(*) AS total_orders,COUNT(DISTINCT customer_id) AS total_customers,COUNT(DISTINCT product_id) AS total_products,SUM(quantity) AS total_quantity_sold,ROUND(SUM(final_amount), 2) AS total_revenue,ROUND(AVG(final_amount), 2) AS average_order_value,SUM(CASE WHEN order_status = 'Delivered' THEN 1 ELSE 0 END) AS delivered_orders,SUM(CASE WHEN order_status = 'Returned' THEN 1 ELSE 0 END) AS returned_orders,SUM(CASE WHEN order_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_orders FROM orders""")
final_kpi = cursor.fetchone()
print("\nFINAL BUSINESS KPI SUMMARY:")
print("Total Orders:", final_kpi[0])
print("Total Customers:", final_kpi[1])
print("Total Products:", final_kpi[2])
print("Total Quantity Sold:", final_kpi[3])
print("Total Revenue: ₹", final_kpi[4])
print("Average Order Value: ₹", final_kpi[5])
print("Delivered Orders:", final_kpi[6])
print("Returned Orders:", final_kpi[7])
print("Cancelled Orders:", final_kpi[8])
print("\nBUSINESS KPI PHASE COMPLETED SUCCESSFULLY!")
print("STEP 20.13 - FINAL BUSINESS KPI STEP COMPLETED!")

import pandas as pd
import openpyxl

from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import BarChart, LineChart, PieChart, Reference
from openpyxl.chart.label import DataLabelList
from openpyxl.utils import get_column_letter

# ============================================================
# PHASE 21 - EXCEL BUSINESS ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("PHASE 21 - EXCEL BUSINESS ANALYSIS")
print("=" * 70)

# ============================================================
# STEP 21.1 - EXCEL DATA IMPORT
# ============================================================

print("\n" + "=" * 70)
print("STEP 21.1 - EXCEL DATA IMPORT")
print("=" * 70)
input_file = "OnlineMart_Cleaned_Orders.xlsx"
output_file = "OnlineMart_Excel_Business_Analysis.xlsx"
df = pd.read_excel(input_file)
print("\nData imported successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("\nColumns:")
print(df.columns.tolist())

# ============================================================
# STEP 21.2 - DATA SHEET PREPARATION
# ============================================================

print("\n" + "=" * 70)
print("STEP 21.2 - DATA SHEET PREPARATION")
print("=" * 70)
df["order_date"] = pd.to_datetime(df["order_date"])
df["order_month"] = df["order_date"].dt.strftime("%Y-%m")
df["gross_amount"] = pd.to_numeric(df["gross_amount"],errors="coerce")
df["discount_amount"] = pd.to_numeric(df["discount_amount"],errors="coerce")
df["final_amount"] = pd.to_numeric(df["final_amount"],errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"],errors="coerce")
df = df.drop_duplicates(subset=["order_id"])
df = df.sort_values("order_date")
print("\nData preparation completed!")
print("Rows after cleaning:", len(df))
print("Duplicate Order IDs:", df["order_id"].duplicated().sum())
print("Missing values:", df.isnull().sum().sum())

# ============================================================
# STEP 21.3 - EXCEL KPI SHEET
# ============================================================

print("\n" + "=" * 70)
print("STEP 21.3 - EXCEL KPI SHEET")
print("=" * 70)
total_orders = df["order_id"].nunique()
total_customers = df["customer_id"].nunique()
total_products = df["product_id"].nunique()
total_quantity = df["quantity"].sum()
total_revenue = df["final_amount"].sum()
average_order_value = df["final_amount"].mean()
delivered_orders = (df["order_status"] == "Delivered").sum()
returned_orders = (df["order_status"] == "Returned").sum()
cancelled_orders = (df["order_status"] == "Cancelled").sum()
return_rate = (returned_orders / total_orders) * 100
cancellation_rate = (cancelled_orders / total_orders) * 100

# ============================================================
# STEP 21.4 - PIVOT STYLE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("STEP 21.4 - PIVOT ANALYSIS")
print("=" * 70)
category_pivot = (df.groupby("category").agg(Orders=("order_id", "count"),Quantity=("quantity", "sum"),Revenue=("final_amount", "sum")).reset_index())
customer_pivot = (df.groupby("customer_id").agg(Orders=("order_id", "count"),Quantity=("quantity", "sum"),Revenue=("final_amount", "sum")).reset_index().sort_values("Revenue", ascending=False))
product_pivot = (df.groupby(["product_id", "product_name"]).agg(Orders=("order_id", "count"),Quantity=("quantity", "sum"),Revenue=("final_amount", "sum")).reset_index().sort_values("Revenue", ascending=False))

# ============================================================
# STEP 21.5 - CATEGORY ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("STEP 21.5 - CATEGORY ANALYSIS")
print("=" * 70)
category_analysis = (df.groupby("category").agg(Total_Orders=("order_id", "count"),Total_Quantity=("quantity", "sum"),Total_Revenue=("final_amount", "sum"),Average_Order_Value=("final_amount", "mean")).reset_index())
category_analysis["Revenue_Share_%"] = (category_analysis["Total_Revenue"] / total_revenue * 100)
category_analysis = category_analysis.sort_values("Total_Revenue",ascending=False)

# ============================================================
# STEP 21.6 - CUSTOMER ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("STEP 21.6 - CUSTOMER ANALYSIS")
print("=" * 70)
customer_analysis = (df.groupby("customer_id").agg(Total_Orders=("order_id", "count"),Total_Quantity=("quantity", "sum"),Total_Spending=("final_amount", "sum"),Average_Order_Value=("final_amount", "mean"),Last_Order_Date=("order_date", "max")).reset_index())
customer_analysis = customer_analysis.sort_values("Total_Spending",ascending=False)

# ============================================================
# STEP 21.7 - PRODUCT ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("STEP 21.7 - PRODUCT ANALYSIS")
print("=" * 70)
product_analysis = (df.groupby(["product_id","product_name","category"]).agg(Total_Orders=("order_id", "count"),Total_Quantity=("quantity", "sum"),Total_Revenue=("final_amount", "sum"),Average_Order_Value=("final_amount", "mean")).reset_index())
product_analysis = product_analysis.sort_values("Total_Revenue",ascending=False)

# ============================================================
# STEP 21.8 - MONTHLY SALES ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("STEP 21.8 - MONTHLY SALES ANALYSIS")
print("=" * 70)
monthly_sales = (df.groupby("order_month").agg(Total_Orders=("order_id", "count"),Total_Quantity=("quantity", "sum"),Total_Revenue=("final_amount", "sum"),Average_Order_Value=("final_amount", "mean")).reset_index())
monthly_sales = monthly_sales.sort_values("order_month")

# ============================================================
# STEP 21.9 - ORDER STATUS ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("STEP 21.9 - ORDER STATUS ANALYSIS")
print("=" * 70)
status_analysis = (df.groupby("order_status").agg(Order_Count=("order_id", "count"),Revenue=("final_amount", "sum")).reset_index())
status_analysis["Percentage"] = (status_analysis["Order_Count"] / total_orders * 100)
status_analysis = status_analysis.sort_values("Order_Count",ascending=False)

# ============================================================
# STEP 21.10 - EXCEL CHARTS
# ============================================================

print("\n" + "=" * 70)
print("STEP 21.10 - EXCEL CHARTS")
print("=" * 70)

# ============================================================
# CREATE EXCEL WORKBOOK
# ============================================================

with pd.ExcelWriter(output_file,engine="openpyxl") as writer:

# Raw / prepared data

    df.to_excel(writer,sheet_name="Data",index=False)
category_analysis.to_excel(writer,sheet_name="Category Analysis",index=False)
customer_analysis.to_excel(writer,sheet_name="Customer Analysis",index=False)
product_analysis.to_excel(writer,sheet_name="Product Analysis",index=False)
monthly_sales.to_excel(writer,sheet_name="Monthly Sales",index=False)
status_analysis.to_excel(writer,sheet_name="Order Status",index=False)
customer_pivot.to_excel(writer,sheet_name="Customer Pivot",index=False)
product_pivot.to_excel(writer,sheet_name="Product Pivot",index=False)
category_pivot.to_excel(writer,sheet_name="Category Pivot",index=False)

# ============================================================
# LOAD WORKBOOK
# ============================================================

wb = load_workbook(output_file)

# ============================================================
# COMMON STYLES
# ============================================================

header_fill = PatternFill(start_color="1F4E78",end_color="1F4E78",fill_type="solid")
header_font = Font(color="FFFFFF",bold=True)
title_font = Font(size=18,bold=True)
bold_font = Font(bold=True)
thin_border = Border(left=Side(style="thin"),right=Side(style="thin"),top=Side(style="thin"),bottom=Side(style="thin"))

# ============================================================
# FORMAT ALL DATA SHEETS
# ============================================================

for ws in wb.worksheets:
    ws.freeze_panes = "A2"
    for cell in ws[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center")
    for row in ws.iter_rows():
        for cell in row:
            cell.border = thin_border
    for column_cells in ws.columns:
        max_length = 0
        column_letter = get_column_letter(column_cells[0].column)
        for cell in column_cells:
            if cell.value is not None:
                max_length = max(max_length,len(str(cell.value)))
        ws.column_dimensions[column_letter].width = min(max_length + 2, 30)

# ============================================================
# KPI SHEET - STEP 21.3
# ============================================================

if "KPI Dashboard" in wb.sheetnames:
    del wb["KPI Dashboard"]
kpi_ws = wb.create_sheet("KPI Dashboard",0)
kpi_ws["A1"] = "ONLINE MART - BUSINESS KPI DASHBOARD"
kpi_ws["A1"].font = title_font
kpi_data = [["KPI", "Value"],["Total Orders", total_orders],["Total Customers", total_customers],["Total Products", total_products],["Total Quantity Sold", total_quantity],["Total Revenue", total_revenue],["Average Order Value", average_order_value],["Delivered Orders", delivered_orders],["Returned Orders", returned_orders],["Cancelled Orders", cancelled_orders],["Return Rate %", return_rate],["Cancellation Rate %", cancellation_rate]]
for row in kpi_data:
    kpi_ws.append(row)
for cell in kpi_ws[2]:
    cell.fill = header_fill
    cell.font = header_font
for row in kpi_ws.iter_rows(min_row=2,max_row=kpi_ws.max_row):
    for cell in row:
        cell.border = thin_border
kpi_ws.column_dimensions["A"].width = 28
kpi_ws.column_dimensions["B"].width = 20
for row in range(3, 13):
    if row in [7, 8]:
        kpi_ws[f"B{row}"].number_format = '₹#,##0.00'
    if row in [12, 13]:
        kpi_ws[f"B{row}"].number_format = '0.00%'

# ============================================================
# CREATE EXCEL WORKBOOK
# ============================================================

with pd.ExcelWriter(output_file,engine="openpyxl") as writer:
    # Data Sheet
    df.to_excel(writer,sheet_name="Data",index=False)
    # Category Analysis
    category_analysis.to_excel(writer,sheet_name="Category Analysis",index=False)
    # Customer Analysis
    customer_analysis.to_excel(writer,sheet_name="Customer Analysis",index=False)
    # Product Analysis
    product_analysis.to_excel(writer,sheet_name="Product Analysis",index=False)
    # Monthly Sales
    monthly_sales.to_excel(writer,sheet_name="Monthly Sales",index=False)
    # Order Status
    status_analysis.to_excel(writer,sheet_name="Order Status",index=False)
    # Customer Pivot
    customer_pivot.to_excel(writer,sheet_name="Customer Pivot",index=False)
    # Product Pivot
    product_pivot.to_excel(writer,sheet_name="Product Pivot",index=False)
    # Category Pivot
    category_pivot.to_excel(writer,sheet_name="Category Pivot",index=False)

# ============================================================
# LOAD CREATED EXCEL WORKBOOK
# ============================================================

wb = load_workbook(output_file)

print("\nExcel workbook created successfully!")
print("Available Excel Sheets:")
print(wb.sheetnames)

# ============================================================
# STEP 21.10 - EXCEL CHARTS
# ============================================================

print("\n" + "=" * 70)
print("STEP 21.10 - EXCEL CHARTS")
print("=" * 70)

# ============================================================
# LOAD EXCEL WORKBOOK
# ============================================================

wb = load_workbook(output_file)

# ============================================================
# CHECK REQUIRED SHEETS
# ============================================================

print("\nAvailable Excel Sheets:")
print(wb.sheetnames)

# ============================================================
# CATEGORY REVENUE CHART
# ============================================================

category_ws = wb["Category Analysis"]
bar_chart = BarChart()
bar_chart.title = "Revenue by Category"
bar_chart.y_axis.title = "Revenue"
bar_chart.x_axis.title = "Category"
data = Reference(category_ws,min_col=4,min_row=1,max_row=category_ws.max_row)
categories = Reference(category_ws,min_col=1,min_row=2,max_row=category_ws.max_row)
bar_chart.add_data(data,titles_from_data=True)
bar_chart.set_categories(categories)
bar_chart.height = 8
bar_chart.width = 14
category_ws.add_chart(bar_chart,"G2")
print("Category Revenue Chart created successfully!")

# ============================================================
# MONTHLY REVENUE CHART
# ============================================================

monthly_ws = wb["Monthly Sales"]
line_chart = LineChart()
line_chart.title = "Monthly Revenue Trend"
line_chart.y_axis.title = "Revenue"
line_chart.x_axis.title = "Month"
data = Reference(monthly_ws,min_col=4,min_row=1,max_row=monthly_ws.max_row)
categories = Reference(monthly_ws,min_col=1,min_row=2,max_row=monthly_ws.max_row)
line_chart.add_data(data,titles_from_data=True)
line_chart.set_categories(categories)
line_chart.height = 8
line_chart.width = 14
monthly_ws.add_chart(line_chart,"G2")
print("Monthly Revenue Chart created successfully!")

# ============================================================
# ORDER STATUS PIE CHART
# ============================================================

status_ws = wb["Order Status"]
pie_chart = PieChart()
pie_chart.title = "Order Status Distribution"
data = Reference(status_ws,min_col=2,min_row=1,max_row=status_ws.max_row)
labels = Reference(status_ws,min_col=1,min_row=2,max_row=status_ws.max_row)
pie_chart.add_data(data,titles_from_data=True)
pie_chart.set_categories(labels)
pie_chart.height = 8
pie_chart.width = 12
pie_chart.dataLabels = DataLabelList()
pie_chart.dataLabels.showPercent = True
status_ws.add_chart(pie_chart,"G2")
print("Order Status Pie Chart created successfully!")

# ============================================================
# SAVE CHARTS
# ============================================================

wb.save(output_file)
print("\nAll Excel Charts created successfully!")
print("STEP 21.10 - EXCEL CHARTS COMPLETED!")

# ============================================================
# STEP 21.11 - EXCEL DASHBOARD
# ============================================================

print("\n" + "=" * 70)
print("STEP 21.11 - EXCEL DASHBOARD")
print("=" * 70)
# Load the latest saved workbook
wb = load_workbook(output_file)
if "Dashboard" in wb.sheetnames:
    del wb["Dashboard"]
dashboard = wb.create_sheet("Dashboard",0)
dashboard["A1"] = "ONLINE MART"
dashboard["A1"].font = Font(size=24,bold=True)
dashboard["A2"] = ("E-Commerce Business Intelligence Dashboard")
dashboard["A2"].font = Font(size=14,bold=True)
dashboard["A4"] = "KEY BUSINESS METRICS"
dashboard["A4"].font = Font(size=16,bold=True)
dashboard_metrics = [["Total Orders", total_orders],["Total Customers", total_customers],["Total Products", total_products],["Quantity Sold", total_quantity],["Revenue", total_revenue],["Average Order Value", average_order_value],["Delivered Orders", delivered_orders],["Returned Orders", returned_orders],["Cancelled Orders", cancelled_orders]]
start_row = 6
for i, row in enumerate(dashboard_metrics,start=start_row):
    dashboard[f"A{i}"] = row[0]
    dashboard[f"B{i}"] = row[1]
    dashboard[f"A{i}"].font = bold_font
    dashboard[f"A{i}"].border = thin_border
    dashboard[f"B{i}"].border = thin_border
dashboard["B10"].number_format = '#,##0'
dashboard["B11"].number_format = '₹#,##0.00'
dashboard["B12"].number_format = '₹#,##0.00'
dashboard["D4"] = "BUSINESS HIGHLIGHTS"
dashboard["D4"].font = Font(size=16,bold=True)
top_category = category_analysis.iloc[0]["category"]
top_product = product_analysis.iloc[0]["product_name"]
top_customer = customer_analysis.iloc[0]["customer_id"]
highest_month = monthly_sales.loc[monthly_sales["Total_Revenue"].idxmax(),"order_month"]
lowest_month = monthly_sales.loc[monthly_sales["Total_Revenue"].idxmin(),"order_month"]
highlights = [["Top Revenue Category", top_category],["Top Revenue Product", top_product],["Top Customer by Spending", top_customer],["Highest Revenue Month", highest_month],["Lowest Revenue Month", lowest_month]]
for i, row in enumerate(highlights,start=6):
    dashboard[f"D{i}"] = row[0]
    dashboard[f"E{i}"] = row[1]
    dashboard[f"D{i}"].font = bold_font
    dashboard[f"D{i}"].border = thin_border
    dashboard[f"E{i}"].border = thin_border
dashboard.column_dimensions["A"].width = 28
dashboard.column_dimensions["B"].width = 20
dashboard.column_dimensions["D"].width = 30
dashboard.column_dimensions["E"].width = 25

# ============================================================
# DASHBOARD CHART - CATEGORY
# ============================================================

category_ws = wb["Category Analysis"]
bar_chart_dashboard = BarChart()
bar_chart_dashboard.title = "Revenue by Category"
bar_chart_dashboard.y_axis.title = "Revenue"
bar_chart_dashboard.x_axis.title = "Category"
data = Reference(category_ws,min_col=4,min_row=1,max_row=category_ws.max_row)
categories = Reference(category_ws,min_col=1,min_row=2,max_row=category_ws.max_row)
bar_chart_dashboard.add_data(data,titles_from_data=True)
bar_chart_dashboard.set_categories(categories)
bar_chart_dashboard.height = 8
bar_chart_dashboard.width = 14
dashboard.add_chart(bar_chart_dashboard,"A17")

# ============================================================
# DASHBOARD CHART - MONTHLY
# ============================================================

monthly_ws = wb["Monthly Sales"]
line_chart_dashboard = LineChart()
line_chart_dashboard.title = "Monthly Revenue Trend"
line_chart_dashboard.y_axis.title = "Revenue"
line_chart_dashboard.x_axis.title = "Month"
data = Reference(monthly_ws,min_col=4,min_row=1,max_row=monthly_ws.max_row)
categories = Reference(monthly_ws,min_col=1,min_row=2,max_row=monthly_ws.max_row)
line_chart_dashboard.add_data(data,titles_from_data=True)
line_chart_dashboard.set_categories(categories)
line_chart_dashboard.height = 8
line_chart_dashboard.width = 14
dashboard.add_chart(line_chart_dashboard,"J17")
wb.save(output_file)
print("Dashboard created successfully!")
print("STEP 21.11 - EXCEL DASHBOARD COMPLETED!")

# ============================================================
# STEP 21.12 - FINAL BUSINESS SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("STEP 21.12 - FINAL BUSINESS SUMMARY")
print("=" * 70)
wb = load_workbook(output_file)
if "Final Summary" in wb.sheetnames:
    del wb["Final Summary"]
summary_ws = wb.create_sheet("Final Summary")
summary_ws["A1"] = ("ONLINE MART - FINAL BUSINESS SUMMARY")
summary_ws["A1"].font = Font(size=20,bold=True)
summary_ws["A3"] = "Metric"
summary_ws["B3"] = "Result"
summary_ws["A3"].fill = header_fill
summary_ws["B3"].fill = header_fill
summary_ws["A3"].font = header_font
summary_ws["B3"].font = header_font
final_summary = [["Total Orders", total_orders],["Total Customers", total_customers],["Total Products", total_products],["Total Quantity Sold", total_quantity],["Total Revenue", total_revenue],["Average Order Value", average_order_value],["Delivered Orders", delivered_orders],["Returned Orders", returned_orders],["Cancelled Orders", cancelled_orders],["Return Rate %", return_rate],["Cancellation Rate %", cancellation_rate],["Top Revenue Category", top_category],["Top Revenue Product", top_product],["Top Customer", top_customer],["Highest Revenue Month", highest_month],["Lowest Revenue Month", lowest_month]]
for row in final_summary:
    summary_ws.append(row)
for row in summary_ws.iter_rows(min_row=3,max_row=summary_ws.max_row):
    for cell in row:
        cell.border = thin_border
summary_ws.column_dimensions["A"].width = 32
summary_ws.column_dimensions["B"].width = 28

# ============================================================
# NUMBER FORMATTING
# ============================================================

for ws in wb.worksheets:
    for row in ws.iter_rows():
        for cell in row:
            if isinstance(cell.value, float):
                if ("Revenue" in str(ws.cell(1, cell.column).value) or "Spending" in str(ws.cell(1, cell.column).value) or "Amount" in str(ws.cell(1, cell.column).value)):
                    cell.number_format = '₹#,##0.00'

# ============================================================
# SAVE FINAL WORKBOOK
# ============================================================

wb.save(output_file)
print("Final Business Summary created successfully!")
print("STEP 21.12 - FINAL BUSINESS SUMMARY COMPLETED!")

# ============================================================
# FINAL MESSAGE
# ============================================================

print("\n" + "=" * 70)
print("PHASE 21 - EXCEL COMPLETED SUCCESSFULLY!")
print("=" * 70)
print("\nExcel workbook created:")
for sheet in wb.sheetnames:
    print("-", sheet)
print("\nExcel workbook:")
print(output_file)
print("\nCompleted Steps:")
print("21.1 - Excel Data Import")
print("21.2 - Data Sheet Preparation")
print("21.3 - Excel KPI Sheet")
print("21.4 - Pivot Analysis")
print("21.5 - Category Analysis")
print("21.6 - Customer Analysis")
print("21.7 - Product Analysis")
print("21.8 - Monthly Sales Analysis")
print("21.9 - Order Status Analysis")
print("21.10 - Excel Charts")
print("21.11 - Excel Dashboard")
print("21.12 - Final Business Summary")
print("\nPHASE 21 - EXCEL BUSINESS ANALYSIS COMPLETED!")


import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",password="Nivi@23071999",database="onlinemart_db")
if connection.is_connected():
    print("MySQL connection successful!")
connection.close()
print("MySQL connection closed.")

import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
# Load cleaned Excel data
file_path = r"C:\Users\Admin\Downloads\python\OnlineMart_Cleaned_Orders.xlsx"
df = pd.read_excel(file_path)
print("Excel data loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
# Connect to MySQL
connection = mysql.connector.connect(host="localhost",user="root",password="Nivi@23071999",database="onlinemart_db")
engine = create_engine("mysql+mysqlconnector://root:Nivi%4023071999@localhost/onlinemart_db")
cursor = connection.cursor()
# Create orders table
cursor.execute("""CREATE TABLE IF NOT EXISTS orders (order_id VARCHAR(20) PRIMARY KEY,customer_id VARCHAR(20),order_date DATE,product_id VARCHAR(20),product_name VARCHAR(100),category VARCHAR(50),subcategory VARCHAR(50),quantity INT,unit_price DECIMAL(12,2),shipping_cost DECIMAL(12,2),payment_method VARCHAR(50),order_status VARCHAR(30),return_status VARCHAR(30),customer_city VARCHAR(50),customer_state VARCHAR(50),brand VARCHAR(50),discount_percent DECIMAL(5,2),discount_amount DECIMAL(12,2),gross_amount DECIMAL(12,2),final_amount DECIMAL(12,2))""")
connection.commit()
print("Orders table created successfully!")

# ============================================================
# 22.3 - INSERT CLEANED DATA INTO MYSQL
# ============================================================

insert_query = """INSERT IGNORE INTO orders (order_id,customer_id,order_date,product_id,product_name,category,subcategory,quantity,unit_price,shipping_cost,payment_method,order_status,return_status,customer_city,customer_state,brand,discount_percent,discount_amount,gross_amount,final_amount)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
for _, row in df.iterrows():
    cursor.execute(insert_query, tuple(row))
connection.commit()
print("Data inserted successfully!")
print("Rows inserted:", len(df))

# ============================================================
# 22.4 - DATA VALIDATION + BASIC SALES ANALYSIS
# ============================================================
import pandas as pd
import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",password="Nivi@23071999",database="onlinemart_db")
engine = create_engine("mysql+mysqlconnector://root:Nivi%4023071999@localhost/onlinemart_db")
print("\n22.4 - Data Validation + Basic Sales Analysis")
# Total rows
query = "SELECT COUNT(*) AS total_rows FROM orders"
result = pd.read_sql(query, engine)
print("\nTotal Rows:")
print(result)
# Duplicate Order IDs
query = """(SELECT order_id, COUNT(*) AS duplicate_count FROM orders GROUP BY order_id HAVING COUNT(*) > 1)"""
result = pd.read_sql(query, engine)
print("\nDuplicate Order IDs:")
print(result)
# Missing values check
query = """(SELECT SUM(order_id IS NULL) AS missing_order_id,SUM(customer_id IS NULL) AS missing_customer_id,SUM(product_id IS NULL) AS missing_product_id,SUM(product_name IS NULL) AS missing_product_name,SUM(category IS NULL) AS missing_category,SUM(quantity IS NULL) AS missing_quantity,SUM(final_amount IS NULL) AS missing_final_amount FROM orders)"""
result = pd.read_sql(query, engine)
print("\nMissing Values Check:")
print(result)
# Total Quantity
query = """(SELECT SUM(quantity) AS total_quantity FROM orders)"""
result = pd.read_sql(query, engine)
print("\nTotal Quantity:")
print(result)
# Gross Sales
query = """(SELECT ROUND(SUM(gross_amount), 2) AS gross_sales FROM orders)"""
result = pd.read_sql(query, engine)
print("\nGross Sales:")
print(result)
# Discount
query = """(SELECT ROUND(SUM(discount_amount), 2) AS total_discount FROM orders)"""
result = pd.read_sql(query, engine)
print("\nTotal Discount:")
print(result)
# Final Sales
query = """(SELECT ROUND(SUM(final_amount), 2) AS final_sales FROM orders)"""
result = pd.read_sql(query, engine)
print("\nFinal Sales:")
print(result)
# Average Order Value
query = """(SELECT ROUND(AVG(final_amount), 2) AS average_order_value FROM orders)"""
result = pd.read_sql(query, engine)
print("\nAverage Order Value:")
print(result)

# ============================================================
# 22.5 - CUSTOMER ANALYSIS
# ============================================================

print("\n22.5 - Customer Analysis")
# Customer order count
query = """(SELECT customer_id,COUNT(*) AS total_orders FROM orders GROUP BY customer_id ORDER BY total_orders DESC)"""
customer_orders = pd.read_sql(query, engine)
print("\nCustomer Order Count:")
print(customer_orders)
# Customer revenue
query = """(SELECT customer_id,COUNT(*) AS total_orders,SUM(quantity) AS total_quantity,ROUND(SUM(final_amount), 2) AS total_sales,ROUND(AVG(final_amount), 2) AS average_order_value FROM orders GROUP BY customer_id ORDER BY total_sales DESC)"""
customer_sales = pd.read_sql(query, engine)
print("\nCustomer Sales Analysis:")
print(customer_sales)
# Top 5 customers
query = """(SELECT customer_id, COUNT(*) AS total_orders, ROUND(SUM(final_amount), 2) AS total_sales FROM orders GROUP BY customer_id ORDER BY total_sales DESC LIMIT 5)"""
top_customers = pd.read_sql(query, engine)
print("\nTop 5 Customers:")
print(top_customers)

# ============================================================
# 22.6 - Product Analysis
# ============================================================
print("\n22.6 - Product Analysis")
# Product-wise order count, quantity and sales
query = """(SELECT product_id,product_name,COUNT(*) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY product_id, product_name ORDER BY total_sales DESC)"""
product_analysis = pd.read_sql(query, engine)
print("\nProduct Analysis:")
print(product_analysis)
# Top 5 products by sales
top_products = product_analysis.head(5)
print("\nTop 5 Products:")
print(top_products)

# ============================================================
# 22.7 - Category Analysis
# ============================================================

print("\n22.7 - Category Analysis")
# Category-wise order count, quantity and sales
query = """(SELECT category,COUNT(*) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY category ORDER BY total_sales DESC)"""
category_analysis = pd.read_sql(query, engine)
print("\nCategory Analysis:")
print(category_analysis)
# Top 3 categories by sales
top_categories = category_analysis.head(3)
print("\nTop 3 Categories:")
print(top_categories)

# ============================================================
# 22.8 - Monthly Sales Analysis
# ============================================================

print("\n22.8 - Monthly Sales Analysis")
# Monthly order count, quantity and sales
query = """(SELECT DATE_FORMAT(order_date, '%Y-%m') AS sales_month,COUNT(*) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY DATE_FORMAT(order_date, '%Y-%m') ORDER BY sales_month)"""
monthly_sales = pd.read_sql(query, engine)
print("\nMonthly Sales Analysis:")
print(monthly_sales)
# Highest sales month
highest_sales_month = monthly_sales.loc[monthly_sales["total_sales"].idxmax()]
print("\nHighest Sales Month:")
print(highest_sales_month)

# ============================================================
# 22.9 - Order Status + Payment Analysis
# ============================================================

print("\n22.9 - Order Status + Payment Analysis")
# Order status-wise analysis
query = """(SELECT order_status,COUNT(*) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY order_status ORDER BY total_orders DESC)"""
status_analysis = pd.read_sql(query, engine)
print("\nOrder Status Analysis:")
print(status_analysis)
# Payment method-wise analysis
query = """(SELECT payment_method,COUNT(*) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY payment_method ORDER BY total_orders DESC)"""
payment_analysis = pd.read_sql(query, engine)
print("\nPayment Method Analysis:")
print(payment_analysis)
# Highest sales payment method
highest_payment_sales = payment_analysis.loc[payment_analysis["total_sales"].idxmax()]
print("\nHighest Sales Payment Method:")
print(highest_payment_sales)

# ============================================================
# 22.10 - Customer Behaviour Analysis
# ============================================================

print("\n22.10 - Customer Behaviour Analysis")
# Customer behaviour summary
query = """(SELECT customer_id,COUNT(*) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_spending,AVG(final_amount) AS average_order_value FROM orders GROUP BY customer_id ORDER BY total_spending DESC)"""
customer_behaviour = pd.read_sql(query, engine)
print("\nCustomer Behaviour Summary:")
print(customer_behaviour)
# Top 5 high-value customers
high_value_customers = customer_behaviour.head(5)
print("\nTop 5 High-Value Customers:")
print(high_value_customers)
# Repeat vs one-time customer analysis
query = """(SELECT customer_id,COUNT(*) AS total_orders FROM orders GROUP BY customer_id)"""
customer_orders = pd.read_sql(query, engine)
customer_orders["customer_type"] = customer_orders["total_orders"].apply(lambda x: "One-Time Customer" if x == 1 else "Repeat Customer")
customer_type_summary = (customer_orders["customer_type"].value_counts().reset_index())
customer_type_summary.columns = ["customer_type", "customer_count"]
print("\nCustomer Type Summary:")
print(customer_type_summary)

# ============================================================
# 22.11 - JOIN + CTE Analysis
# ============================================================

print("\n22.11 - JOIN + CTE Analysis")
# Customer + Order analysis using existing orders table
query = """(SELECT customer_id,COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY customer_id ORDER BY total_sales DESC)"""
customer_order_join = pd.read_sql(query, engine)
print("\nCustomer + Order Analysis:")
print(customer_order_join)
# Customer sales analysis using CTE
query = """(WITH customer_sales AS (SELECT customer_id,COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales FROM orders GROUP BY customer_id) SELECT customer_id,total_orders,total_quantity,total_sales FROM customer_sales ORDER BY total_sales DESC)"""
customer_cte = pd.read_sql(query, engine)
print("\nCustomer Sales Analysis using CTE:")
print(customer_cte)

# ============================================================
# 22.12 - Window Functions + Advanced SQL
# ============================================================

print("\n22.12 - Window Functions + Advanced SQL")
# Customer ranking based on total sales
query = """(SELECT customer_id,total_sales,RANK() OVER (ORDER BY total_sales DESC) AS sales_rank FROM (SELECT customer_id,SUM(final_amount) AS total_sales FROM orders GROUP BY customer_id) AS customer_sales ORDER BY sales_rank)"""
customer_ranking = pd.read_sql(query, engine)
print("\nCustomer Sales Ranking:")
print(customer_ranking)
# Product ranking based on total sales
query = """(SELECT product_id,total_sales,RANK() OVER (ORDER BY total_sales DESC) AS sales_rank FROM (SELECT product_id,SUM(final_amount) AS total_sales FROM orders GROUP BY product_id) AS product_sales ORDER BY sales_rank)"""
product_ranking = pd.read_sql(query, engine)
print("\nProduct Sales Ranking:")
print(product_ranking)
# Category ranking based on total sales
query = """(SELECT category,total_sales,RANK() OVER (ORDER BY total_sales DESC) AS sales_rank FROM (SELECT category,SUM(final_amount) AS total_sales FROM orders GROUP BY category) AS category_sales ORDER BY sales_rank)"""
category_ranking = pd.read_sql(query, engine)
print("\nCategory Sales Ranking:")
print(category_ranking)

# ============================================================
# 22.13 - Business KPIs + Final SQL Insights
# ============================================================

print("\n22.13 - Business KPIs + Final SQL Insights")
# Overall Business KPIs
query = """(SELECT COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value,MIN(final_amount) AS minimum_order_value,MAX(final_amount) AS maximum_order_value FROM orders)"""
business_kpis = pd.read_sql(query, engine)
print("\nOverall Business KPIs:")
print(business_kpis)
# Order status summary
query = """(SELECT order_status,COUNT(order_id) AS total_orders,SUM(final_amount) AS total_sales FROM orders GROUP BY order_status ORDER BY total_orders DESC)"""
final_status_summary = pd.read_sql(query, engine)
print("\nFinal Order Status Summary:")
print(final_status_summary)
# Top 5 customers by total sales
query = """(SELECT customer_id,COUNT(order_id) AS total_orders,SUM(final_amount) AS total_sales FROM orders GROUP BY customer_id ORDER BY total_sales DESC LIMIT 5)"""
final_top_customers = pd.read_sql(query, engine)
print("\nFinal Top 5 Customers:")
print(final_top_customers)
# Top 5 products by total sales
query = """(SELECT product_id,COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales FROM orders GROUP BY product_id ORDER BY total_sales DESC LIMIT 5)"""
final_top_products = pd.read_sql(query, engine)
print("\nFinal Top 5 Products:")
print(final_top_products)
# Final business insight
highest_sales_product = final_top_products.iloc[0]
highest_sales_customer = final_top_customers.iloc[0]
highest_sales_status = final_status_summary.iloc[0]
print("\nFinal Business Insights:")
print(f"Top Product by Sales: {highest_sales_product['product_id']} " f"with sales of ₹{highest_sales_product['total_sales']:,.2f}")
print(f"Top Customer by Sales: {highest_sales_customer['customer_id']} " f"with sales of ₹{highest_sales_customer['total_sales']:,.2f}")
print(f"Most Frequent Order Status: {highest_sales_status['order_status']} " f"with {highest_sales_status['total_orders']} orders")

# ============================================================
# 23 - RFM ANALYSIS
# ============================================================

print("\n23 - RFM Analysis")

# ------------------------------------------------------------
# 23.1 - RFM Base Calculation
# ------------------------------------------------------------

query = """(SELECT MAX(order_date) AS latest_order_date FROM orders)"""
latest_date = pd.read_sql(query, engine)
reference_date = (pd.to_datetime(latest_date["latest_order_date"].iloc[0]) + pd.Timedelta(days=1))
print("\nReference Date:")
print(reference_date)
query = """(SELECT customer_id,DATEDIFF(%s, MAX(order_date)) AS recency,COUNT(order_id) AS frequency,SUM(final_amount) AS monetary FROM orders GROUP BY customer_id)"""
rfm_analysis = pd.read_sql(query,engine,params=(reference_date.strftime("%Y-%m-%d"),))
print("\nRFM Base Analysis:")
print(rfm_analysis)

# ------------------------------------------------------------
# 23.2 - RFM Scoring
# ------------------------------------------------------------

# Recency:
# Lower recency is better, so reverse the score
rfm_analysis["R_Score"] = pd.qcut(rfm_analysis["recency"].rank(method="first"),5,labels=[5, 4, 3, 2, 1]).astype(int)
# Frequency:
# Higher frequency is better
rfm_analysis["F_Score"] = pd.qcut(rfm_analysis["frequency"].rank(method="first"),5,labels=[1, 2, 3, 4, 5]).astype(int)
# Monetary:
# Higher monetary value is better
rfm_analysis["M_Score"] = pd.qcut(rfm_analysis["monetary"].rank(method="first"),5,labels=[1, 2, 3, 4, 5]).astype(int)
# Combined RFM Score
rfm_analysis["RFM_Score"] = (rfm_analysis["R_Score"].astype(str) + rfm_analysis["F_Score"].astype(str) + rfm_analysis["M_Score"].astype(str))
print("\nRFM Scoring:")
print(rfm_analysis)

# ------------------------------------------------------------
# 23.3 - Customer Segmentation
# ------------------------------------------------------------

def customer_segment(row):
    if row["R_Score"] >= 4 and row["F_Score"] >= 4 and row["M_Score"] >= 4:
        return "High Value Customer"
    elif row["F_Score"] >= 4 and row["M_Score"] >= 4:
        return "Loyal Customer"
    elif row["R_Score"] >= 4:
        return "Recent Customer"
    elif row["R_Score"] <= 2 and row["F_Score"] <= 2:
        return "At Risk Customer"
    else:
        return "Regular Customer"
rfm_analysis["customer_segment"] = rfm_analysis.apply(customer_segment,axis=1)
print("\nCustomer Segmentation:")
print(rfm_analysis[["customer_id","recency","frequency","monetary","RFM_Score","customer_segment"]])

# ------------------------------------------------------------
# 23.4 - RFM Segment Summary
# ------------------------------------------------------------

segment_summary = (rfm_analysis .groupby("customer_segment") .agg(customer_count=("customer_id", "count"),total_sales=("monetary", "sum"),average_spending=("monetary", "mean"),average_frequency=("frequency", "mean"),average_recency=("recency", "mean")) .reset_index() .sort_values("total_sales", ascending=False))
print("\nRFM Segment Summary:")
print(segment_summary)

# ------------------------------------------------------------
# 23.5 - RFM Business Insights
# ------------------------------------------------------------

top_rfm_customer = rfm_analysis.sort_values("monetary", ascending=False).iloc[0]
largest_segment = segment_summary.iloc[0]
print("\nRFM Business Insights:")
print(f"Top Customer by Monetary Value: " f"{top_rfm_customer['customer_id']} " f"with spending of ₹{top_rfm_customer['monetary']:,.2f}")
print(f"Largest Sales-Contributing Segment: " f"{largest_segment['customer_segment']} " f"with sales of ₹{largest_segment['total_sales']:,.2f}")
print(f"Number of Customer Segments: " f"{rfm_analysis['customer_segment'].nunique()}")

# ============================================================
# 24 - BUSINESS KPI CONSOLIDATION + DASHBOARD PREPARATION
# ============================================================

print("\n24 - Business KPI Consolidation + Dashboard Preparation")

# ------------------------------------------------------------
# 24.1 - Overall Business KPIs
# ------------------------------------------------------------

query = """(SELECT COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value,MIN(final_amount) AS minimum_order_value,MAX(final_amount) AS maximum_order_value FROM orders)"""
overall_kpis = pd.read_sql(query, engine)
print("\nOverall Business KPIs:")
print(overall_kpis)

# ------------------------------------------------------------
# 24.2 - Order Status KPIs
# ------------------------------------------------------------

query = """(SELECT order_status,COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY order_status ORDER BY total_sales DESC)"""
status_kpis = pd.read_sql(query, engine)
print("\nOrder Status KPIs:")
print(status_kpis)

# ------------------------------------------------------------
# 24.3 - Category KPIs
# ------------------------------------------------------------

query = """(SELECT category,COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY category ORDER BY total_sales DESC)"""
category_kpis = pd.read_sql(query, engine)
print("\nCategory KPIs:")
print(category_kpis)

# ------------------------------------------------------------
# 24.4 - Monthly Sales KPIs
# ------------------------------------------------------------

query = """(SELECT DATE_FORMAT(order_date, '%Y-%m') AS sales_month,COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY DATE_FORMAT(order_date, '%Y-%m') ORDER BY sales_month)"""
monthly_kpis = pd.read_sql(query, engine)
print("\nMonthly Sales KPIs:")
print(monthly_kpis)

# ------------------------------------------------------------
# 24.5 - Top Customers
# ------------------------------------------------------------

query = """(SELECT customer_id,COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY customer_id ORDER BY total_sales DESC LIMIT 5)"""
top_customers = pd.read_sql(query, engine)
print("\nTop 5 Customers:")
print(top_customers)

# ------------------------------------------------------------
# 24.6 - Top Products
# ------------------------------------------------------------

query = """(SELECT product_id,product_name,category,COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY product_id, product_name, category ORDER BY total_sales DESC LIMIT 5)"""
top_products = pd.read_sql(query, engine)
print("\nTop 5 Products:")
print(top_products)

# ------------------------------------------------------------
# 24.7 - Payment Method KPIs
# ------------------------------------------------------------

query = """(SELECT payment_method,COUNT(order_id) AS total_orders,SUM(quantity) AS total_quantity,SUM(final_amount) AS total_sales,AVG(final_amount) AS average_order_value FROM orders GROUP BY payment_method ORDER BY total_sales DESC)"""
payment_kpis = pd.read_sql(query, engine)
print("\nPayment Method KPIs:")
print(payment_kpis)

# ------------------------------------------------------------
# 24.8 - Dashboard KPI Summary
# ------------------------------------------------------------

dashboard_summary = pd.DataFrame({"KPI": ["Total Orders","Total Quantity","Total Sales","Average Order Value","Minimum Order Value","Maximum Order Value"],"Value": [overall_kpis["total_orders"].iloc[0],overall_kpis["total_quantity"].iloc[0],overall_kpis["total_sales"].iloc[0],overall_kpis["average_order_value"].iloc[0],overall_kpis["minimum_order_value"].iloc[0],overall_kpis["maximum_order_value"].iloc[0]]})
print("\nDashboard KPI Summary:")
print(dashboard_summary)

# ------------------------------------------------------------
# 24.9 - Export Dashboard Data to Excel
# ------------------------------------------------------------

dashboard_file = "OnlineMart_Dashboard_Data.xlsx"
with pd.ExcelWriter(dashboard_file, engine="openpyxl") as writer:
    dashboard_summary.to_excel(writer,sheet_name="KPI_Summary",index=False)
    status_kpis.to_excel(writer,sheet_name="Order_Status",index=False)
    category_kpis.to_excel(writer,sheet_name="Category_Analysis",index=False)
    monthly_kpis.to_excel(writer,sheet_name="Monthly_Sales",index=False)
    top_customers.to_excel(writer,sheet_name="Top_Customers",index=False)
    top_products.to_excel(writer,sheet_name="Top_Products",index=False)
    payment_kpis.to_excel(writer,sheet_name="Payment_Method",index=False)
print(f"\nDashboard data exported successfully!")
print(f"File: {dashboard_file}")

# ------------------------------------------------------------
# 24.10 - Final Dashboard Preparation Summary
# ------------------------------------------------------------

print("\nDashboard Preparation Completed!")
print("\nDatasets prepared for Dashboard:")
print("1. KPI Summary")
print("2. Order Status Analysis")
print("3. Category Analysis")
print("4. Monthly Sales Analysis")
print("5. Top Customers")
print("6. Top Products")
print("7. Payment Method Analysis")
print("\nReady for Power BI and Tableau Dashboard Development.")

