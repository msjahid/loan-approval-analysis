=====================================================
LOAN EASE - LOAN PREDICTION APP
=====================================================
A Flask-based web application for predicting loan 
approval status using machine learning. The app is 
deployed on **Railway** for seamless online access.

=====================================================
FEATURES
=====================================================

1. User-friendly loan application form.
2. Predicts loan approval status using Gaussian Naive Bayes.
3. Input validation for user-provided data.
4. Error handling for invalid inputs.
5. Deployed on Railway for cloud-based access.

=====================================================
TECHNOLOGIES USED
=====================================================

- Python: Core programming language.
- Flask: Web framework for API and frontend.
- Gaussian Naive Bayes: Machine learning model.
- HTML/CSS: Frontend templates and styling.
- Railway: Cloud platform for deployment.

=====================================================
PROJECT STRUCTURE
=====================================================
.
├── Dockerfile # Deployment instructions for Docker
├── app.py # Flask application entry point
├── core
│ ├── **init**.py # Core package initializer
│ ├── model_storage
│ │ └── gnb_model.pkl # Pre-trained Gaussian Naive Bayes model
│ ├── models.py # Model loading and prediction logic
│ ├── request.py # Input parsing and validation
│ ├── routes.py # Flask app routes
│ ├── static
│ │ ├── css
│ │ │ └── style.css # Styling for the app
│ │ └── images
│ │ ├── error-dog.png # Error page illustration
│ │ └── loan.png # Home page logo
│ └── templates
│ ├── error.html # Error page template
│ ├── index.html # Loan application form
│ └── prediction.html # Prediction result display
├── data
│ ├── processed
│ │ └── data_preprocessing.py
│ └── raw
│ ├── cleaned_data.csv
│ └── loan_data.csv
├── notebooks
│ ├── loan-status-analysis.ipynb # Data analysis notebook
├── requirements.txt # Python dependencies
├── docker-compose.yml # Docker compose file for Railway
└── README.md # Project documentation

=====================================================
INSTALLATION GUIDE
=====================================================

# Step 1: Clone the repository

```bash
git clone https://github.com/msjahid/loan-approval-analysis.git
cd loan-approval-analysis
```

# Step 2: Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

# Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

# Step 4: Run the Flask app

```bash
python app.py
```

# Step 5: Open the app in your browser

```bash
http://127.0.0.1:5000/
```

=====================================================
DEPLOYMENT ON RAILWAY
=====================================================

# Step 1: Sign up or log in to Railway

Visit [https://railway.app/](https://railway.app/) and create an account.

# Step 2: Create a new project

- Click "New Project" → "Deploy from GitHub repo".
- Select your repository (e.g., `loanease-app`).

# Step 3: Configure the deployment

- Railway auto-detects the Procfile and runtime.txt.
- Ensure dependencies in requirements.txt are accurate.

# Step 4: Deploy the app

- Wait for the build and deployment to complete.

# Step 5: Access the app

Railway provides a unique URL (e.g., [https://loanease-app.up.railway.app/](https://loanease-app.up.railway.app/)).

=====================================================
INPUT VALIDATION RULES
=====================================================

1. Name: Cannot be empty or "0".
2. Account Number: Cannot be "0".
3. Applicant Income: Must be greater than 0.
4. Loan Amount: Must be greater than 0.
5. Loan Term: Must be at least 36 months.
6. Credit History: Must be valid (0 or 1).

=====================================================
PAGE PREVIEW SCREENSHOTS
=====================================================

# 1. Home Page

- Displays the loan application form.
- Includes input fields for Name, Account Number, Income, etc.

![Home Page](project_images/home.png)

# 2. Loan Prediction Page

- Displays the loan prediction result.
- Shows personalized messages based on prediction status.

![Prediction Page](project_images/prediction.png)

# 3. Error Page

- Displays descriptive error messages for invalid inputs.
- Includes a visual illustration for better UX.

![Error Page](project_images/error.png)

=====================================================
EXAMPLE WORKFLOW
=====================================================

# INPUT

Name: Hasan
Account Number: 123456
Applicant Income: 5000
Loan Amount: 150
Loan Term: 360
Credit History: 1
Property Area: Urban

# OUTPUT (Approved)

Congratulations, Hasan! Your loan has been approved.
Account Number: 123456

# OUTPUT (Not Approved)

Unfortunately, Hasan your loan has not been approved.
Account Number: 123456

=====================================================
CONTRIBUTING
=====================================================

# Steps to contribute:

1. Fork the repository.

2. Create a new branch for your feature:
   git checkout -b feature-name

3. Commit your changes:
   git commit -m "Add new feature"

4. Push to your branch:
   git push origin feature-name

5. Submit a pull request for review.

=====================================================
LICENSE
=====================================================
This project is open-source and available under the MIT License.

=====================================================
CONTACT
=====================================================

- Author: Jahid Hasan
- GitHub: [msjahid (Jahid Hasan) · GitHub](https://github.com/msjahid)
- Email: [msjahid.ai@gmail.com](mailto:msjahid.ai@gmail.com)
