# Azure Web App - Python

A simple Python web application designed for deployment on Azure Web App.

## Features

- Simple Flask web application
- Health check endpoint for monitoring
- Responsive HTML interface
- Ready for Azure Web App deployment

## Azure Web App Configuration

This application is configured for Azure Web App with the following settings:

- **Publishing model**: Code
- **Runtime Stack**: Python 3.14
- **Operating System**: Linux

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Access the application at `http://localhost:8000`

## Endpoints

- `/` - Main landing page
- `/health` - Health check endpoint (returns JSON status)

## Deployment to Azure

Azure Web App will automatically:
1. Detect the Python runtime from `requirements.txt`
2. Install dependencies
3. Start the application using the default startup command

No additional pipeline configuration is required as Azure will create it automatically.