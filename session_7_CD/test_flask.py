import pytest

from hello import pancakes


@pytest.fixture
def client():
	return pancakes.test_client()


def test_put_any_name_here(client):
	response = client.get('/hello')
	assert response.status_code == 200
	#assert response.data == {"message": "Hello, World!"}
	assert response.json == {"message": "Hello, World!"}
	


def test_predict(client):

	payload1 = { "Gender": "Male", "Married": "Unmarried", "Credit_History": "Cleared Debts", "ApplicantIncome": 50000, "LoanAmount": 500000000 }

	response = client.post('/predict', json=payload1)

	assert response.status_code == 200
	assert response.json == {"loan_approval_status": "Loan Rejected"}, "payload1 failed"

	payload2 = { "Gender": "Male", "Married": "Unmarried", "Credit_History": "Cleared Debts", "ApplicantIncome": 50000, "LoanAmount": 5 }

	response = client.post('/predict', json=payload2)
	assert response.status_code == 200
	assert response.json == {"loan_approval_status": "Loan Approved"}, "payload2 failed"


# Why this issue?? X does not have valid feature names, but LogisticRegression was fitted with feature names warnings