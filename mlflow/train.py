from urllib.parse import urlparse

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import mlflow

import config


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

# set MLFlow tracking URI - to log RUNS remotely
mlflow.set_tracking_uri(f"{config.MLFLOW_URL}:{config.MLFLOW_PORT}")

# log fitted model and XGBClassifier parameters
with mlflow.start_run():
    xgb_classifier.fit(X_train, Y_train)
    clf_params = xgb_classifier.get_xgb_params()
    mlflow.log_params(clf_params)

    tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
    print(tracking_url_type_store)
    print(mlflow.get_tracking_uri())

    # model_info = mlflow.xgboost.log_model(xgb_classifier, "iris-classifier")
    model_info = mlflow.xgboost.log_model(
        xgb_model=xgb_classifier,
        artifact_path="model",
        registered_model_name="testing"
    )


# Load saved model and make predictions
xgb_classifier_saved = mlflow.pyfunc.load_model(model_info.model_uri)
y_pred = xgb_classifier_saved.predict(X_test)
