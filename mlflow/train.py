import os
from urllib.parse import urlparse

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import mlflow

import config


# set MLFlow tracking URI - to connect to tracking server
mlflow.set_tracking_uri(config.MLFLOW_TRACKING_URI)
# mlflow.set_tracking_uri("mysql+pymysql://mlflow_user:mlflow_password@127.0.0.1:3306/mlflow")


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

# s3_bucket = "s3://bucket"  # replace this value
# mlflow.create_experiment('hello', s3_bucket)

# mlflow.set_experiment('hello')

# log fitted model and XGBClassifier parameters
with mlflow.start_run():
    print(f"tracking_uri: {mlflow.get_tracking_uri()}")
    # print(f"artifact_uri: {mlflow.get_artifact_uri()}")
    # artifact_uri = mlflow.get_artifact_uri()

    xgb_classifier.fit(X_train, Y_train)
    clf_params = xgb_classifier.get_xgb_params()
    mlflow.log_params(clf_params)

    tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

    # model_info = mlflow.xgboost.log_model(xgb_classifier, "iris-classifier")
    model_info = mlflow.xgboost.log_model(
        xgb_model=xgb_classifier,
        artifact_path="bucket",
        registered_model_name="testing"
    )

    mlflow.end_run()


# Load saved model and make predictions
# xgb_classifier_saved = mlflow.pyfunc.load_model(model_info.model_uri)
# y_pred = xgb_classifier_saved.predict(X_test)
