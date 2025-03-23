import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from TrainTest import trainTestSplit

X_train, X_test, y_train, y_test = trainTestSplit()

models = [
        ('Naive Bayes', GaussianNB()),
        ('Linear SVM', SVC(kernel='linear')),
        ('RBF SVM', SVC(kernel='rbf')),
        ('Random Forest', RandomForestClassifier(n_estimators=250)),
        ('Gradient Boosting', GradientBoostingClassifier(n_estimators=250))
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

