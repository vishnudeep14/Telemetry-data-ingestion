# Telemetry-data-ingestion
Use of AWS services (Lambda, Glue, S3, Athena)  Event-driven architecture  Cost optimization with Parquet  Real-world analytics use case

# 📊 Serverless Telemetry Ingestion Pipeline using AWS

This project implements a **cost-effective, serverless data ingestion pipeline** to process and analyze telemetry data from multiple sources. It leverages key AWS services to handle JSON-based telemetry data, transforming it into a query-optimized format for business intelligence.

---

## ⚙️ Architecture Overview

- **AWS S3**: Stores raw telemetry JSON files and processed Parquet/Avro files.
- **AWS Lambda**: Automatically triggers on S3 uploads to orchestrate ETL flow.
- **AWS Glue**: Performs schema inference and transformation (nested JSON ➝ flat structure ➝ Parquet).
- **AWS Athena**: Enables serverless querying and analysis of processed data.
- **AWS CloudWatch**: Monitors pipeline performance and errors.

---

## 📂 Folder Structure
📁 telemetry-ingestion-pipeline/
├── lambda/
│ └── trigger_glue_job.py # Lambda function code
├── glue/
│ └── transform_job.py # Glue ETL script (Spark)
├── sample-data/
│ └── telemetry_sample.json # Sample raw JSON file
└── README.md
