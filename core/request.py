from flask import request, jsonify


def parse_request(request):
    """
    Extract all form data from the HTTP POST request.
    """
    try:
        # Extract all form fields
        form_data = {
            "name": request.form.get("name"),
            "account_number": request.form.get("account_number"),
            "gender": request.form.get("gender"),
            "married": request.form.get("married"),
            "dependents": request.form.get("dependents"),  # Can be "0", "1", "2", "3+"
            "education": request.form.get("education"),
            "self_employed": request.form.get("self_employed"),
            "applicant_income": request.form.get("applicant_income"),
            "coapplicant_income": request.form.get("coapplicant_income"),
            "loan_amount": request.form.get("loan_amount"),
            "loan_amount_term": request.form.get("loan_amount_term"),
            "credit_history": request.form.get("credit_history"),
            "property_area": request.form.get("property_area"),
        }

        # Convert numeric fields to appropriate types
        form_data["applicant_income"] = float(form_data["applicant_income"])
        form_data["coapplicant_income"] = float(form_data["coapplicant_income"])
        form_data["loan_amount"] = float(form_data["loan_amount"])
        form_data["loan_amount_term"] = float(form_data["loan_amount_term"])
        form_data["credit_history"] = int(form_data["credit_history"])

        return form_data
    except Exception as e:
        print(f"Error parsing request: {e}")
        return None


def filter_features(form_data):
    """
    Filter only the features required for the model from the form data.
    """
    try:
        # Define mappings for categorical fields
        gender_map = {"Male": 0, "Female": 1}
        married_map = {"No": 0, "Yes": 1}
        education_map = {"Not Graduate": 0, "Graduate": 1}
        self_employed_map = {"No": 0, "Yes": 1}
        property_area_map = {"Urban": 0, "Semiurban": 1, "Rural": 2}

        # Convert dependents (e.g., "3+" -> 3)
        dependents = 3 if form_data["dependents"] == "3+" else int(form_data["dependents"])

        # Prepare the required features in the correct order
        filtered_features = [
            gender_map[form_data["gender"]],
            married_map[form_data["married"]],
            dependents,  # Processed dependents value
            education_map[form_data["education"]],
            form_data["applicant_income"],
            form_data["loan_amount"],
            form_data["credit_history"],
        ]

        return filtered_features
    except Exception as e:
        print(f"Error filtering features: {e}")
        return None
