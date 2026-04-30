# 🚀 Flask Monitoring App with CI/CD, Prometheus & Grafana

A complete **DevOps project** demonstrating:

* Flask web application
* Monitoring with Prometheus & Grafana
* Docker containerization
* CI/CD using GitHub Actions
* Deployment on AWS EC2

---

## Architecture

![Architecture flowchart showing GitHub source repository triggering a CI CD pipeline with GitHub Actions building and testing, Docker Hub hosting container images, AWS EC2 deployment running containers, and a monitoring stack with Flask app metrics scraped by Prometheus and visualized by Grafana](assets/image.png)

---

## 🧱 Tech Stack

* Python (Flask)
* Docker & Docker Compose
* Prometheus
* Grafana
* GitHub Actions (CI/CD)
* AWS EC2

---

## 📁 Project Structure

```text
project/
│
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── templates/
│
├── monitoring/
│   └── prometheus.yml
│
├── Dockerfile
├── docker-compose.yml
└── .github/workflows/deploy.yml
```

---

## ⚙️ Features

* User Registration & Login System
* Login Success & Failure Tracking
* Real-time Monitoring Dashboard
* Automated CI/CD Deployment

---

## 🐳 Docker Setup

### Build & Run locally

```bash
docker-compose up --build
```

---

## 📊 Monitoring Setup

### Prometheus

* Scrapes metrics from Flask app (`/metrics` endpoint)

### Grafana

* Visualizes metrics using dashboards

---

## 🌐 Access URLs

| Service    | URL                             |
|------------|---------------------------------|
| Flask App  | http://<EC2_Public_IP>:5000     |
| Prometheus | http://<EC2_Public_IP>:9090     |
| Grafana    | http://<EC2_Public_IP>:3000     |

---

## 🔐 Grafana Login

* Username: `admin`
* Password: `admin`

---

## 📥 Import Grafana Dashboard

1. Open Grafana
2. Go to **Create → Import**
3. Paste dashboard JSON
4. Select Prometheus data source

---

## 🔄 CI/CD Pipeline

Using GitHub Actions:

```text
Push Code → Build Docker Image → Push to Docker Hub → Deploy to EC2 → Run Containers
```

---

## ☁️ AWS EC2 Deployment

### Steps: 1

1. Launch EC2 instance (Ubuntu)
2. Install Docker & Docker Compose
3. Configure Security Groups (ports 22, 3000, 5000, 9090)
4. Connect via SSH
5. CI/CD handles deployment automatically

---

## 🔑 Environment Variables / Secrets

Set in GitHub:

* DOCKER_USERNAME
* DOCKER_PASSWORD
* EC2_HOST
* EC2_USER
* EC2_SSH_KEY

---

## 📸 Screenshots

### 🔹 1. Application UI

![Login page showing a Flask app login form with username hk entered and a masked password field, orange Login button, Register link, and browser address bar displaying 15.206.173.125:5000 on a blue background](<assets/Screenshot 2026-04-29 144843.png>)

![Flask dashboard page showing a welcome message for user hk, login count 1, last login 2026-04-29 09:15:26.079402, password strength 1, and a Logout link in a browser window at URL 15.206.173.125:5000/dashboard](<assets/Screenshot 2026-04-29 144708.png>)

### 🔹 2. Prometheus Targets

![Prometheus targets page showing flask-app endpoint health status indicating 1 of 1 target up with endpoint http://flask-app:5000/metrics and labels instance="flask-app:5000" job="flask-app" in a browser window at 15.206.173.125:9090](<assets/Screenshot 2026-04-29 144657.png>)

### 🔹 3. Grafana Dashboard

![Grafana dashboard displaying two line charts for Login Success and Login Failures in a dark browser interface with side navigation and toolbar showing Last 6 hours, Refresh, Share, and Edit controls](<assets/Screenshot 2026-04-29 145004.png>)

### 🔹 4. CI/CD Pipeline (GitHub Actions)

![GitHub Actions workflow summary showing a successful build and deploy pipeline with steps Set up job, Checkout code, Login to Docker Hub, Build and Push Image, Setup SSH, Deploy to EC2, Post Login to Docker Hub, Post Checkout code, and Complete job displayed in a dark browser interface](<assets/Screenshot 2026-04-29 144721.png>)

### 🔹 5. AWS EC2

![AWS EC2 console showing one running EC2 instance named CI_CD_AWS with instance ID i-0eeb038ddf9437f97, instance type t3.micro, public IPv4 address 15.206.173.125, and 3 of 3 status checks passed](<assets/Screenshot 2026-04-29 144730.png>)

## 🧪 Testing

Trigger login events:

* Register a user
* Login multiple times
* Check metrics in Grafana

---

## 🚀 Future Improvements

* Add alerting (Email/Slack)
* Add Nginx + HTTPS
* Kubernetes deployment
* Blue-Green deployment strategy

---

## 🧠 Learning Outcomes

* End-to-end DevOps pipeline
* Monitoring & observability
* Cloud deployment
* CI/CD automation

---

## 🙌 Author

Himanshu Joshi

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
