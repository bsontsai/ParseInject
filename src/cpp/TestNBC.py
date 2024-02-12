import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Define the functions
def linear(x): return x
def quadratic(x): return x**2
def cubic(x): return x**3
def log2(x): return np.log2(x)
def ln(x): return np.log(x)
def exp(x): return np.exp(x)

# Create a dictionary of the functions
tags = {'linear': linear, 'quadratic': quadratic, 'cubic': cubic, 'log2': log2, 'ln': ln, 'exp': exp}

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Initialize the Logistic Regression and Naive Bayes models
lr = LogisticRegression()
gnb = GaussianNB()



if __name__ == '__main__':
    # Generate the training data
    X_train = []
    y_train = []
    for _ in range(50):
        X = np.array(range(1, 11)).reshape(-1, 1)
        tag = np.random.choice(list(tags.keys()))
        Y = np.array(tags[tag for x in X])
        X_train.append(scaler.fit_transform(X))
        y_train.append(tag)

    # Fit the models
    lr.fit(X_train, y_train)
    gnb.fit(X_train, y_train)

    # Generate the validation data
    X_val = []
    y_val = []
    for _ in range(10):
        X = np.array(range(1, 11)).reshape(-1, 1)
        tag = np.random.choice(list(tags.keys()))
        Y = tags[tag]
        X_val.append(scaler.transform(X))
        y_val.append(tag)

    # Predict the tags
    y_pred_lr = lr.predict(X_val)
    y_pred_gnb = gnb.predict(X_val)

    # Output the accuracies
    print('Logistic Regression Accuracy:', accuracy_score(y_val, y_pred_lr))
    print('Naive Bayes Accuracy:', accuracy_score(y_val, y_pred_gnb))