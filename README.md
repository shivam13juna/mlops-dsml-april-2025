# MLOps – April 2025

This repository contains code, notebooks, and resources from the MLOps held in April 2025. It demonstrates end-to-end workflows for model training, deployment, and serving using various tools and frameworks.

## Repository Structure

- `cars24-car-price-model.joblib` : Pre-trained car price prediction model.
- `scaler.pkl`               : Standard scaler used in preprocessing.
- `session_1_github/`        : Intro to GitHub and basic Python models
  - `conv_network.py`, `neural_network_mnist.py`, `rnn.py`, etc.
- `session_2_streamlit/`     : Building interactive apps with Streamlit
  - `cars_24_streamlit.py`, sample dataset and `requirements.txt`.
- `session_3_flask_intro/`   : Serving models via Flask API
  - `hello.py`, trained classifier, and sample data.
- `session_4_docker_container/`: Containerizing your ML apps with Docker
  - `Dockerfile`, Flask service, and `artefacts/requirements.txt`.

## Prerequisites

- Python 3.8+ installed
- pip package manager
- Docker (for session 4)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/mlops-dsml-april-2025.git
   cd mlops-dsml-april-2025
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

## Usage by Session

### Session 1 – GitHub & Python Models

```bash
pip install -r session_1_github/requirements.txt  # if provided
python session_1_github/run.py  # explore scripts and neural network examples
```
#### Common Git Commands
```bash
# Clone this repository
git clone https://github.com/your-repo/mlops-dsml-april-2025.git

# Check repository status
git status

# Stage changes for commit
git add .

# Commit changes with message
git commit -m "Your descriptive message"

# Push commits to remote (main branch)
git push origin main

# Pull latest changes from remote
git pull

# Create a new branch
git branch feature/your-feature-name

# Switch to a branch
git checkout feature/your-feature-name

# Merge a branch into main
git checkout main
git merge feature/your-feature-name

# View commit history
git log

# Show remote URLs
git remote -v
```


### Session 2 – Streamlit App

```bash
pip install -r session_2_streamlit/requirements.txt
streamlit run session_2_streamlit/cars_24_streamlit.py
```
- Step 1: Examine `cars24-car-price.csv` and load it via `cars_24_streamlit.py` to see preprocessing steps.
- Step 2: Interact with Streamlit widgets (sliders, dropdowns) to adjust feature values and observe real-time price predictions.
- Step 3: Inspect the underlying model file (`cars24-car-price-model.joblib`) and `scaler.pkl` to understand the inference pipeline.
- Step 4: Modify UI components in `cars_24_streamlit.py` and re-run to experiment with additional features.

### Session 3 – Flask API

```bash
pip install -r session_3_flask_intro/requirements.txt
flask --app hello.py run --host=0.0.0 --port=5000
```
curl http://localhost:5000/predict?feature1=value1&...
```
- Step 1: Open `train_ml.ipynb` to retrain or fine-tune the classifier on `train_flask.csv` and save to `classifier.pkl`.
- Step 2: Run `hello.py` to start the Flask server with the trained model.
- Step 3: Use `curl` or Postman to send GET/POST requests to `/predict` endpoint, passing feature values and verifying JSON responses.
- Step 4: Check logs printed in terminal for request handling and prediction details.
```

### Session 4 – Docker Container

```bash
# Build the Docker image
$ docker build -t mlops-dsml-app session_4_docker_container/
$ docker image ls

# Run the container in foreground
$ docker run -p 8000:8000 mlops-dsml-app

# Run with a custom container name
$ docker run -p 8000:8000 --name mlops-dsml-container mlops-dsml-app

# Run in detached mode
$ docker run -d -p 8000:8000 mlops-dsml-app

# Access an interactive shell inside the container
$ docker run -it -p 8000:8000 mlops-dsml-app bash

# List all containers
docker container ls --all

# Tag and push the image to Docker Hub
$ docker image tag mlops-dsml-app:latest your-dockerhub-username/mlops-dsml-app:latest
$ docker push your-dockerhub-username/mlops-dsml-app:latest
```
- Step 1: Review the `Dockerfile` and `artefacts/requirements.txt` to understand the build context and dependencies.
- Step 2: Build and inspect the image locally (`docker image ls`).
- Step 3: Run the container (foreground, named, detached or interactive) and verify that the Flask API is available at `http://localhost:8000/predict`.
- Step 4: Use `docker logs <container_id>` or `docker container ls --all` to debug issues and inspect runtime behavior.

## Contributing

Contributions, issues, and feature requests are welcome. Please review `CONTRIBUTING.md` and open a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Miscellaneous
### Git Aliases
```
gs() {
    git status
}

gp() {
    git pull
}

gl() {
    git log --oneline --all
}


gu() {
    # First argument as commit message
    local commit_msg="$1"
    # Determine branch: use second argument if provided, otherwise use current branch
    local branch="${2:-$(git rev-parse --abbrev-ref HEAD)}"

    git add .
    git commit -m "$commit_msg"
    git push --set-upstream origin "$branch"
}
```


### Jmeter 

#### BeanShell Preprocessor
```java
import java.util.Random;

Random random = new Random();

// Define arrays for choices
String[] genders = new String[]{"Male", "Female", "Confused"};
String[] marrieds = new String[]{"Married", "Un-Married"};
String[] credit_histories = new String[]{"Unclear Debts", "Clear Debts"};

// Select random values
String selectedGender = genders[random.nextInt(genders.length)];
String selectedMarried = marrieds[random.nextInt(marrieds.length)];
int applicantIncome = random.nextInt(1000000000);
int loanAmount = random.nextInt(1000000000);
String selectedCreditHistory = credit_histories[random.nextInt(credit_histories.length)];

// Store values in JMeter variables
vars.put("gender", selectedGender);
vars.put("married", selectedMarried);
vars.put("applicant_income", Integer.toString(applicantIncome));
vars.put("loan_amount", Integer.toString(loanAmount));
vars.put("credit_history", selectedCreditHistory);
```

#### Post request body-data
```
{
    "Gender": "${gender}",
    "Married": "${married}",
    "ApplicantIncome": ${applicant_income},
    "LoanAmount": ${loan_amount},
    "Credit_History": "${credit_history}"
}
```

### Steps for connecting to EC2


1. **SSH into EC2 Instance**:
   ```bash
   chmod 600 mlops-key-pair-april25.pem 
   ssh -i "your-key.pem" ubuntu@your-ec2-public-dns
   ```
explain usage of chmod 600
    - The `chmod 600` command sets the permissions of the key file to be read/write for the owner only. This is important for security reasons, as SSH will refuse to use a key file that is accessible by others.

2. **Install Docker**:

  https://docs.docker.com/engine/install/ubuntu/


  If you want to run Docker as a non-root user, then you need to add your user to the docker group.

  sudo usermod -aG docker $USER

