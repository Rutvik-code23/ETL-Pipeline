# Real Time ETL Pipeline for Ride Booking and Analytics 

## 📌 Overview
This project implements a **real-time, metadata-driven ETL pipeline** for a ride booking system. It processes both streaming and batch data to generate analytics-ready datasets using a scalable data engineering architecture.

The pipeline is built on **Microsoft Azure** and follows the **Medallion Architecture (Bronze, Silver, Gold layers)** to ensure structured data transformation and high data quality.

---

## 🏗️ Architecture
- **Bronze Layer:** Raw data ingestion from streaming and batch sources  
- **Silver Layer:** Data cleaning, transformation, and creation of Operational Base Table (OBT)  
- **Gold Layer:** Dimensional modeling (Fact & Dimension tables) for analytics  

---

## 🔄 Data Flow
1. Streaming ride data is ingested via **Event Hubs**  
2. Static/batch data is fetched using **Azure Data Factory**  
3. Raw data is stored in **Azure Data Lake (Bronze layer)**  
4. Data is transformed in **Databricks (Silver layer)** to create OBT  
5. Final analytics tables are built in **Gold layer**  

---

## ▶️ Steps to Run the Project

### 1. Prerequisites
- Azure account  
- Databricks, Data Lake, Event Hubs, Data Factory setup  

### 2. Setup Resources
- Create Azure Data Lake, Databricks workspace, Event Hub, and Data Factory  

### 3. Ingestion
- Stream data via Event Hubs  
- Load batch data using Data Factory  

### 4. Processing (Databricks)
- **Bronze:** Store raw data  
- **Silver:** Transform data and create OBT  
- **Gold:** Build fact & dimension tables with SCD  

### 5. Orchestration
- Use Data Factory to schedule and trigger pipelines  

### 6. Validation
- Query Gold layer tables for analysis  