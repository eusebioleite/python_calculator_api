# pycalc

This is a simple Flask API calculator that evaluates a mathematical formula sent as JSON in a POST request.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/python_calculator_api.git
   cd python_calculator_api
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

   The API will be running at `http://localhost:5000`.

## API Endpoint

- **POST** `/`

  This endpoint expects a JSON object with a key `formula` containing the mathematical formula to evaluate. It returns the result of the evaluation as a JSON response.

  Example request:

  ```json
  {
    "formula": "2 + 2 * 3"
  }
  ```

  Example response:

  ```json
  {
    "result": 8
  }
  ```

## Docker

You can also run the application in a Docker container. Simply build the Docker image and run the container:

```bash
docker build -t pycalc_api .
docker run -p 8080:5000 pycalc_api
```

The API will be accessible at `http://localhost:8080`.

## Files

- `app.py`: Contains the Flask application code.
- `requirements.txt`: Specifies the Python dependencies.
- `Dockerfile`: Defines the Docker container configuration.
