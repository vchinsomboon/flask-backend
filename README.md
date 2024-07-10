# Flask Backend Project

This repository contains a Flask backend project that serves as the backend for a web application [vchinsomboon-portfolio](https://github.com/vchinsomboon/vchinsomboon-portfolio).

## Prerequisites

Before running this project locally, ensure you have the following installed:

- Python (version 3.x)
- pip (Python package installer)
- Git (optional, if cloning via command line)

## Getting Started
Follow these steps to clone and run the Flask backend locally:

#### 1. Clone the Repository
Clone the repository:

```bash
git clone https://github.com/vchinsomboon/flask-backend.git
cd flask-backend
```

### Set Up Virtual Environment (Optional but Recommended)
#### 2. Create a virtual environment:

macOS and Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
Windows
```bash
python -m venv venv
venv\Scripts\activate
```
### Install Dependencies
#### 3. Install dependencies:
```bash
pip install -r requirements.txt
```
### Configure Environment Variables
#### 4. Set up environment variables:

Create a .env file in the root directory (if not already present) and add necessary configuration values. For example:

```plaintext
FLASK_APP=app.py
FLASK_ENV=development
```
You can also copy contents from **.env.example** file

### Run the Application Locally
#### 5. Run the Flask application:

```bash
flask run
```
This will start the Flask development server. By default, the application will be accessible at http://localhost:5000.

## Deploying to Production
To deploy your Flask backend to Google App Engine (GAE) in production, follow these steps:

### 1. Commit and Push Changes:

Ensure all your changes are committed and pushed to the main branch of your repository.
### 2. Automatic Deployment via GitHub Actions:

- GitHub Actions is set up to automatically deploy your Flask backend to Google App Engine whenever changes are pushed to the main branch.
- Details of the deployment workflow can be found in .github/workflows/deploy.yml.

### 3. Monitoring Deployment:

Monitor the deployment progress and view logs (Logging/Logs Explorer) in the [Google Cloud Console](https://console.cloud.google.com/home/dashboard?project=flask-react-portfolio).

### 4. Viewing the Production Application
To view the deployed application in a web browser, execute the following command in your terminal:

```bash
gcloud app browse
```
Ensure you have the Google Cloud SDK installed and authenticated before running this command.

