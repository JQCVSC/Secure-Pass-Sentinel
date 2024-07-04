SecurePass Sentinel is a web application designed to evaluate password strength. It provides instant feedback on password security, helping users create stronger, more secure passwords.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app/main.py`
4. Open a web browser and navigate to `http://localhost:8080`

## Running Tests

Run the tests using the following command:
python -m unittest tests/test_password_checker.py

## Docker

To build and run the Docker container:
docker build -t securepass-sentinel .
docker run -p 8080:8080 securepass-sentinel


## Deployment to Google Cloud Platform (Optional)

To deploy this application to GCP, follow these steps:

1. Create a new GCP project
2. Enable the Cloud Run API
3. Install and initialize the Google Cloud SDK on your local machine
4. Authenticate with GCP: `gcloud auth login`
5. Set your project ID: `gcloud config set project YOUR_PROJECT_ID`
6. Build and deploy the application:
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/securepass-sentinel
gcloud run deploy --image gcr.io/YOUR_PROJECT_ID/securepass-sentinel --platform managed
Copy
Replace YOUR_PROJECT_ID with your actual GCP project ID.

Note: Deploying to GCP may incur costs. Be sure to review the pricing and set up billing alerts.

## Security Considerations

This project uses a small list of common passwords for demonstration purposes. In a real-world scenario, you would want to use a more comprehensive and regularly updated list, and store it securely (e.g., in Google Cloud Storage if using GCP).

Remember, the security of passwords is crucial. This tool should not be used to store or transmit actual passwords. Always use secure, salted hashing techniques for storing passwords in production environments.

