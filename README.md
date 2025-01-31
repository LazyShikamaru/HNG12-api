# HNG12 API Project

This is a simple API that returns the following:
- Your registered email address.
- The current date and time in ISO 8601 format (UTC).
- The URL of the project's GitHub repository.

## Setup Instructions

1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`.
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install flask flask-cors`.
5. Run the API: `python app.py`.

## API Documentation
- **Endpoint**: `/`
- **Request Method**: GET
- **Response Format**: JSON
- **Response Example**:
  ```json
  {
    "email": "joshbosseisfresh@gmail.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/LazyShikamaru/hng12-api"
  }
