from flask import render_template, request, redirect, url_for
from core.models import load_model, predict
from core.request import parse_request, filter_features

# Initialize the machine learning model
model = load_model()


# Function to configure routes

def configure_routes(app):
    @app.route('/', endpoint='home')
    def index():
        """
        Render the home page with the loan approval form.
        """
        return render_template('index.html')

    @app.route('/process-loan', methods=['POST'])
    def process_loan():
        """
        Handle loan approval form submission and display the prediction result.
        """
        if not model:
            return render_template('error.html', message="Model not loaded. Please check the server setup.")

        # Step 1: Parse all form data
        form_data = parse_request(request)
        if not form_data:
            return render_template('error.html', message="Error processing input data.")

        # Step 2: Validate the input data
        try:
            # Validate account name
            if not form_data["name"] or form_data["name"].strip() == "0":
                raise ValueError("Name cannot be empty or '0'.")

            # Validate account number
            if not form_data["account_number"] or form_data["account_number"] == "0":
                raise ValueError("Account number cannot be '0'.")

            # Validate applicant income
            if form_data["applicant_income"] <= 0:
                raise ValueError("Applicant income must be greater than 0.")

            # Validate loan amount
            if form_data["loan_amount"] <= 0:
                raise ValueError("Loan amount must be greater than 0.")

            # Validate loan term
            if form_data["loan_amount_term"] < 36:
                raise ValueError("Loan term must be at least 36 months.")

        except ValueError as e:
            return render_template('error.html', message=f"Input validation error: {e}")

        # Step 3: Filter only the features required for prediction
        filtered_features = filter_features(form_data)
        if not filtered_features:
            return render_template('error.html', message="Error filtering input features.")

        # Step 4: Make a prediction
        try:
            result = model.predict([filtered_features])  # Predict using the filtered features
            status = "Approved" if result[0] == 1 else "Not Approved"
        except Exception as e:
            return render_template('error.html', message=f"Error during prediction: {e}")

        # Step 5: Render the prediction result page
        return render_template(
            'prediction.html',
            status=status,
            name=form_data["name"],
            account_number=form_data["account_number"]
        )
