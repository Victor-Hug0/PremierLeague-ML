import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from TrainTest import trainTestSplit
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = trainTestSplit()

models = [
        ('Naive Bayes', GaussianNB()),
        ('Linear SVM', SVC(kernel='linear')),
        ('RBF SVM', SVC(kernel='rbf')),
        ('Random Forest', RandomForestClassifier(n_estimators=250)),
        ('Gradient Boosting', GradientBoostingClassifier(n_estimators=250)),
        ('MLP Classifier', MLPClassifier(activation="relu", hidden_layer_sizes=(128, 64, 32), solver="adam", max_iter=1000)),
        ('RBFN', make_pipeline(StandardScaler(), MLPClassifier(activation="relu", hidden_layer_sizes=(128, 64, 32),  solver="adam", max_iter=1000, learning_rate_init=0.001, tol=1e-4)))
    ]

results = {}

for name, model in models:
    try:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = accuracy
        print(f'{name}: {accuracy:.2%}')
    except Exception as e:
        print(f'Erro em {name}: {str(e)}')
        results[name] = 0

plt.figure(figsize=(8, 5))
bars = plt.bar(results.keys(), results.values(), color='#54a3e8')
plt.ylabel('Accuracy')
plt.ylim(0.45, 0.59)  
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='-', alpha=0.2)
plt.tight_layout()
plt.savefig("accuracy_comparison.png", format="png", dpi=300)  
plt.show()

