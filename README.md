# Real-Time AI-Based GDPR Anonymization for Mobility & Robotics Data

An intelligent Computer Vision application that automatically detects and blurs faces and vehicle license plates in images and videos using YOLOv8 and OpenCV.

This project provides a fully Dockerized FastAPI service for real-time anonymization on video streams, making it a robust solution for a wide range of applications. It is optimized to meet the strict data privacy requirements of the General Data Protection Regulation (GDPR) and other privacy laws like HIPAA.

---

## Relevance for German Industries

Given Germany's leading role in the automotive and manufacturing sectors and its exceptionally high standards for data privacy, this tool is of critical importance. The German Federal Data Protection Act (BDSG) supplements the GDPR, creating one of Europe's most stringent regulatory environments for handling personal data. This solution is directly applicable to key German markets:

- **Autonomous Driving:** Anonymizing data collected from vehicle cameras is essential for developing safe and compliant self-driving systems.

- **Smart Cities & Robotics:** Safeguarding the privacy of pedestrians and vehicles captured by public surveillance and smart infrastructure.

- **Industry 4.0 & Manufacturing:** Protecting employee and visitor data captured by robotics and surveillance systems on factory floors.

---

## Features

- **Face Detection & Anonymization:** Automatically detects and blurs individuals to protect personal identity in images and video streams.

- **License Plate Masking:** Precisely identifies and masks vehicle number plates to protect vehicle identity.

- **Customizable Blur Intensity:** Allows for adjustable anonymization strength to meet specific privacy and compliance needs.

---

## Project Structure

```bash
cv-anonymizer/
├── app.py              # Main FastAPI application backend
├── requirements.txt    # Python dependencies for the project
├── Dockerfile          # Docker instructions for building the container
├── .dockerignore       # Files to ignore when building the Docker image
└── static/
    └── index.html      # Frontend UI for uploading and viewing anonymized media
