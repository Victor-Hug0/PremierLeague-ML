import matplotlib.pyplot as plt
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score
from TrainTest import trainTestSplit

def preprocess_data(X_train, X_test):
    cat_cols = X_train.select_dtypes(include=['object']).columns
    
    X_train = X_train.drop(columns=cat_cols, errors='ignore')
    X_test = X_test.drop(columns=cat_cols, errors='ignore')
    
    X_test = X_test[X_train.columns]
    
    X_train = X_train.apply(pd.to_numeric, errors='coerce')
    X_test = X_test.apply(pd.to_numeric, errors='coerce')
    
    imputer = SimpleImputer(strategy='mean')
    X_train_imp = pd.DataFrame(imputer.fit_transform(X_train), columns=X_train.columns)
    X_test_imp = pd.DataFrame(imputer.transform(X_test), columns=X_train.columns)
    
    return X_train_imp, X_test_imp

X_train, X_test, y_train, y_test = trainTestSplit()

if X_train is not None:
    X_train, X_test = preprocess_data(X_train, X_test)
    
    le = LabelEncoder()
    y_train = le.fit_transform(y_train)
    y_test = le.transform(y_test)

    modelos = [
        ('Naive Bayes', GaussianNB()),
        ('Linear SVM', SVC(kernel='linear')),
        ('RBF SVM', SVC(kernel='rbf')),
        ('Random Forest', RandomForestClassifier(n_estimators=100)),
        ('Gradient Boosting', GradientBoostingClassifier(n_estimators=100))
    ]

    resultados = {}

    for nome, modelo in modelos:
        try:
            modelo.fit(X_train, y_train)
            y_pred = modelo.predict(X_test)
            acuracia = accuracy_score(y_test, y_pred)
            resultados[nome] = acuracia
            print(f'{nome}: {acuracia:.2%}')
        except Exception as e:
            print(f'Erro em {nome}: {str(e)}')
            resultados[nome] = 0

    plt.figure(figsize=(8, 5))
    bars = plt.bar(resultados.keys(), resultados.values(), color='#54a3e8')
    plt.ylabel('Accuracy')
    plt.ylim(0.45, 0.59)  
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='-', alpha=0.2)
    plt.tight_layout()
    plt.savefig("accuracy_comparison.png", format="png", dpi=300)  
    plt.show()

else:
    print("Erro na carga de dados!")
