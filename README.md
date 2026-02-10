# Azure Web App - Python

A Python web application following best practices, designed for deployment on Azure Web App.

## Project Structure

```
azure_web_app/
├── app/                    # Application package
│   ├── __init__.py        # Application factory
│   ├── routes.py          # Route handlers
│   └── templates/         # HTML templates
│       └── index.html
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── conftest.py        # Pytest fixtures
│   ├── test_app.py        # Application tests
│   └── test_routes.py     # Route tests
├── app.py                  # Application entry point
├── config.py               # Configuration management
├── requirements.txt        # Python dependencies
└── README.md
```

## Features

- Modular Flask application using application factory pattern
- Separation of concerns (routes, templates, configuration)
- Comprehensive test suite with pytest
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

## Testing

Run the test suite:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=app tests/
```

## Endpoints

- `/` - Main landing page
- `/health` - Health check endpoint (returns JSON status)

## Deployment to Azure

Azure Web App will automatically:
1. Detect the Python runtime from `requirements.txt`
2. Install dependencies
3. Start the application using the default startup command

No additional pipeline configuration is required as Azure will create it automatically.

## Development Best Practices

This project follows Python and Flask best practices:
- Application factory pattern for better testing and modularity
- Blueprints for organizing routes
- Separate configuration management
- Template-based rendering
- Comprehensive test coverage
- Clear project structure for scalability