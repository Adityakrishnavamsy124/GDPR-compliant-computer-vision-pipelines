# Real-Time AI-Based GDPR Anonymization for Mobility & Robotics Data

An intelligent Computer Vision application that automatically detects and blurs faces and vehicle license plates in images and videos in real-time using OpenCV.

This project delivers a fully Dockerized lightweight FastAPI service for real-time anonymization of images, offering a robust and scalable solution across various applications. It is  optimized to comply with data privacy regulations such as the General Data Protection Regulation (GDPR) and HIPAA giving results in realtime.


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
## Results

### Input Image  
![People](https://github.com/user-attachments/assets/c1bbdb78-7059-48e5-a39c-a8db46389aaa)

---

### Processed Output  
<img width="1917" height="911" alt="project_people_masking" src="https://github.com/user-attachments/assets/cf04b2d1-1e60-4336-b061-74a20865ce5d" />

---

## Process Overview

1. **Working on Local Project**  
   Developed and tested the anonymization app locally to ensure functionality.
   <img width="1919" height="829" alt="project_work_local_run" src="https://github.com/user-attachments/assets/f5915c39-d580-4566-884c-375e4a2cd19f" />


3. **Docker Image Creation**  
   Built a lightweight Docker image packaging the FastAPI service and all dependencies.
   <img width="1567" height="493" alt="docker_image_building" src="https://github.com/user-attachments/assets/3791d8ce-fa86-4f64-854f-436fc9621b25" />


5. **Docker Image Identified by Docker Engine**  
   Verified the Docker image was successfully created and listed by the Docker Engine.
   <img width="1915" height="777" alt="image_identify_by_docker" src="https://github.com/user-attachments/assets/5f26b144-fc5b-4ff9-8046-eac2b0541bd2" />


7. **Application Demo**  
   Ran the containerized app, demonstrating real-time face and license plate anonymization.
   <img width="1907" height="907" alt="app_demo" src="https://github.com/user-attachments/assets/0bca5812-7471-4557-8b19-4dda17d43176" />


9. **Docker Container Run**  
   Launched the Docker container exposing the app via a local port.
   <img width="1561" height="211" alt="run_docker_container" src="https://github.com/user-attachments/assets/89a1cb9a-2d8a-42fd-b4c0-e3283868ba94" />


11. **Container Activation in Docker Engine**  
   Confirmed the container was active and serving requests inside Docker Desktop.
   <img width="1911" height="549" alt="docker_container_running_at_docker_engine" src="https://github.com/user-attachments/assets/a56f91ac-4295-4a2a-a58e-85847572e150" />


### Extra outputs
<img width="1891" height="919" alt="project_liscense_plate_masking" src="https://github.com/user-attachments/assets/bf228a3f-a5a2-42f8-b1a2-6573e534777a" />
<img width="1899" height="913" alt="flowers_no_blur" src="https://github.com/user-attachments/assets/1700ed65-0070-40ee-8733-728e106bc196" />

## Project Structure

```bash
cv-anonymizer/
├── app.py              # Main FastAPI application backend
├── requirements.txt    # Python dependencies for the project
├── Dockerfile          # Docker instructions for building the container
├── .dockerignore       # Files to ignore when building the Docker image
└── static/
    └── index.html      # Frontend UI for uploading and viewing anonymized media



