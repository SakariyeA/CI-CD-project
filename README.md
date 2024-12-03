CI/CD DevOps Project: Customer Contact Data Pipeline

Project Objective
To build a fully automated CI/CD pipeline for producing and deploying a web application that displays customer contact data.
Steps Completed

    Web Application Setup:
    A simple HTML+JavaScript web app was created, which fetches customer data from a data.json file.

    Data Transformation:
        Built csvtojson.py to convert profiles1.csv into a JSON file (data.json).
        Added validations to ensure the CSV file:
            Contains 12 columns.
            Has 900+ rows.
        Verified that the generated JSON file:
            Includes the required properties.
            Contains 900+ rows.

    Unit Testing:
        Created a suite of unit tests to validate CSV-to-JSON transformation logic.
        Tests ensure data integrity, correct column mapping, and JSON compliance.

    GitHub Actions CI/CD Pipeline:
        Configured a pipeline to:
            Run unit tests and halt on failure.
            Execute generate.py and csvtojson.py scripts.
            Deploy index.html, script.js, and data.json to GitHub Pages.

    Testing Pipeline Resilience:
        Simulated test failures to verify the pipeline aborts on unsuccessful test execution.
        Ensured the pipeline automatically retries and passes when errors are resolved.

    Deployment:
        Successfully deployed the web app on GitHub Pages, making the site accessible for displaying customer data dynamically.

This project automated the entire data pipeline for producing customer contact data, from transformation to deployment, ensuring data accuracy and seamless CI/CD functionality. 🚀
