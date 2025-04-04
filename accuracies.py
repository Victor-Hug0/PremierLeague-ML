from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from TrainTest import trainTestSplit
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def calculate_rps(y_true, y_pred_proba):
    
    encoder = OneHotEncoder(sparse_output=False)
    y_true_encoded = encoder.fit_transform(np.array(y_true).reshape(-1, 1))

    y_true_cumsum = np.cumsum(y_true_encoded, axis=1)
    y_pred_cumsum = np.cumsum(y_pred_proba, axis=1)

    rps_per_sample = np.mean((y_true_cumsum - y_pred_cumsum) ** 2, axis=1)
    
    return np.mean(rps_per_sample)

def getAccuracies():
    
    X_train, X_test, y_train, y_test = trainTestSplit()

    models = [
            ('Naive Bayes', GaussianNB()),
            ('Linear SVM', SVC(kernel='linear', probability=True)),
            ('RBF SVM', SVC(kernel='rbf', probability=True)),
            ('Random Forest', RandomForestClassifier(n_estimators=250)),
            ('Gradient Boosting', GradientBoostingClassifier(n_estimators=250))
        ]
    
    labels = ["H", "A", "D"]

    results = {}

    for name, model in models:
        try:
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            y_pred_proba = model.predict_proba(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            rps = calculate_rps(y_test, y_pred_proba)
            cMatrix = confusion_matrix(y_test, y_pred, labels=labels)
            cReport = classification_report(y_test, y_pred, labels=labels)
            results[name] = accuracy
            print(f'{name}: {accuracy:.2%}')
            print(f'RPS: {rps:.4f}')
            print(cMatrix)
            print(cReport)
            print('-' * 50)
        except Exception as e:
            print(f'Erro em {name}: {str(e)}')
            
    return results

getAccuracies()
