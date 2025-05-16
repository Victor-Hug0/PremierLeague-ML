from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from TrainTest import trainTestSplit
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from scikeras.wrappers import KerasClassifier
from tensorflow import keras

def getAccuracies():
    
    X_train, X_test, y_train, y_test = trainTestSplit()
    input_dim = X_train.shape[1]

    def create_keras_model():
        model = keras.Sequential([
            keras.layers.Input(shape=(input_dim,)), 
            keras.layers.Dense(64, activation="relu"),
            keras.layers.Dropout(0.5),
            keras.layers.Dense(3, activation="softmax")
        ])

        model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001), loss=keras.losses.SparseCategoricalCrossentropy(), metrics=["accuracy"])

        return model

    models = [
        ('Naive Bayes', GaussianNB()),
        ('Linear SVM', SVC(kernel='linear')),
        ('RBF SVM', SVC(kernel='rbf')),
        ('Random Forest', RandomForestClassifier(n_estimators=250)),
        ('Gradient Boosting', GradientBoostingClassifier(n_estimators=250)),
        ('MLP Classifier', MLPClassifier(activation="relu", hidden_layer_sizes=(256, 128, 64), solver="adam", max_iter=1000, learning_rate_init=0.001, tol=1e-4)),
        ('MLP Classifier (scaled)', make_pipeline(StandardScaler(), MLPClassifier(activation="relu", hidden_layer_sizes=(128, 64, 32),  solver="adam", max_iter=1000, learning_rate_init=0.001, tol=1e-4))),
        ('Keras MLP', KerasClassifier(model=create_keras_model, epochs=100, batch_size=32)),
        ('Keras MLP (scaled)', make_pipeline(StandardScaler(), KerasClassifier(model=create_keras_model, epochs=100, batch_size=32)))
    ]
    
    labels = ["H", "A", "D"]

    results = {}

    for name, model in models:
        try:
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            cMatrix = confusion_matrix(y_test, y_pred, labels=labels)
            cReport = classification_report(y_test, y_pred, labels=labels)
            results[name] = accuracy
            print(f'{name}: {accuracy:.2%}')
            print(cMatrix)
            print(cReport)
            print('-' * 50)
        except Exception as e:
            print(f'Erro em {name}: {str(e)}')
            
    return results

getAccuracies()
