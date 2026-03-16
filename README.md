# 🚀 Dockerized Python Flask Application

---

## 📌 Project Overview

This project demonstrates how to **containerize a Python Flask web application using Docker**.

A simple Flask web application is created and packaged inside a Docker container.
When the container runs, the application becomes accessible through a web browser.

The web page also contains a **GitHub button that redirects to the project repository**.

---

## 🧰 Technologies Used

* Python
* Flask
* Docker
* Linux
* AWS EC2

---

## 📂 Project Structure

```
Docker-Python-Flask-Project
│
├── app.py
├── Dockerfile
├── requirements.txt
├── Docker-image-and-container-build.png
├── Flask-app-browser-output.png
├── Redirected-repo.png
└── README.md
```

---

## ⚙️ Application Workflow

```
Flask Application
        │
        ▼
Dockerfile
        │
        ▼
Docker Image
        │
        ▼
Docker Container
        │
        ▼
Access Application via Browser
```

---

## 📝 Application Code

The Flask application returns a simple web page with:

* DevOps Flask App message
* Author name
* GitHub repository button

---

## 🐳 Dockerfile

Dockerfile is used to build the Docker image for the application.

```
FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```

---

## 🔨 Build Docker Image

```
docker build -t python-flask-app .
```

---

## ▶️ Run Docker Container

```
docker run -d -p 5000:5000 python-flask-app
```

---

## 🌐 Access the Application

```
http://<EC2-Public-IP>:5000
```

---

## 📸 Project Screenshots

### Docker Image Build and Container Creation

![Docker Build](Docker-image-and-container-build.png)

### Flask Application Running in Browser

![Flask App](Flask-app-browser-output.png)

### GitHub Button Redirecting to Repository

![Redirected Repo](Redirected-repo.png)

---

## 📦 Key Concepts Demonstrated

* Containerization
* Dockerfile usage
* Building Docker images
* Running containers
* Deploying a Flask application using Docker

---

## 🔗 GitHub Repository

https://github.com/nasiroddin-qatib/Docker-Python-Flask-Project

---

## 👨‍💻 Author

**Nasiroddin**
DevOps & Cloud Enthusiast
