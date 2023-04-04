from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import mlflow


data = load_iris()

X_train, X_test, Y_train, Y_test = train_test_split(
    data["data"], data["target"], test_size=0.2
)

xgb_classifier = XGBClassifier(
    n_estimators=10,
    max_depth=3,
    learning_rate=1,
    objective="binary:logistic",
    random_state=123,
)

# log fitted model and XGBClassifier parameters
with mlflow.start_run():
    xgb_classifier.fit(X_train, Y_train)
    clf_params = xgb_classifier.get_xgb_params()
    mlflow.log_params(clf_params)
    model_info = mlflow.xgboost.log_model(xgb_classifier, "iris-classifier")

# Load saved model and make predictions
xgb_classifier_saved = mlflow.pyfunc.load_model(model_info.model_uri)
y_pred = xgb_classifier_saved.predict(X_test)
