import multiprocessing
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time

# 1. Generate a dummy dataset
X, y = make_classification(n_samples=50000, n_features=20, n_informative=15, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Define a function to train and evaluate a model
def train_model(model_class_and_args):
    model_class, model_args = model_class_and_args
    model = model_class(**model_args)

    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    print(f"Model: {model_class.__name__}, Accuracy: {acc:.4f}")
    return acc

if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")

    t = time.time()

    # 3. List of models to train
    models_to_train = [
        (LogisticRegression, {"max_iter": 1000}),
        (RandomForestClassifier, {"n_estimators": 50}),
        (SVC, {"kernel": "rbf"})
    ]

    # 4. Create a multiprocessing Pool and train models
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(train_model, models_to_train)
    

    print("Total time taken:", "{:.8f}".format(time.time() - t))
    

    # train it sequentially
    
    t = time.time()
    for model_class, model_args in models_to_train:
        model = model_class(**model_args)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        print(f"Model: {model_class.__name__}, Accuracy: {acc:.4f}")
    print("Total time taken:", "{:.8f}".format(time.time() - t))
    # print("Sequential done in : ", "{:.8f}".format(time.time() - t))


#Model: LogisticRegression, Accuracy: 0.8467
#Model: RandomForestClassifier, Accuracy: 0.9628
#Model: SVC, Accuracy: 0.9845
#Total time taken: 8.50421906
#Model: LogisticRegression, Accuracy: 0.8467
#Model: RandomForestClassifier, Accuracy: 0.9613
#Model: SVC, Accuracy: 0.9845
#Total time taken: 11.67474318

# mutex and semaphore