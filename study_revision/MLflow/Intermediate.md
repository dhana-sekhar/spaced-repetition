### **MLflow: From Basics to Advanced**

#### **Multiple Runs in MLflow**
MLflow allows you to run multiple experiments (or "runs") to compare their outcomes and optimize the performance of machine learning models. Each run records parameters, metrics, artifacts, and models.

---

#### **1. Hyperparameter Tuning**
Hyperparameter tuning involves experimenting with different configurations of a model’s hyperparameters to improve performance. In MLflow, you can track hyperparameter tuning across multiple runs.

**Example:**
```python
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Start multiple runs to test hyperparameters
for max_depth in [5, 10, 15]:
    with mlflow.start_run():
        clf = RandomForestClassifier(max_depth=max_depth)
        clf.fit(X_train, y_train)
        
        # Log hyperparameters and metrics
        mlflow.log_param('max_depth', max_depth)
        accuracy = clf.score(X_test, y_test)
        mlflow.log_metric('accuracy', accuracy)
```

---

#### **2. Testing with Different Datasets**
MLflow allows you to compare how models perform on different datasets. You can track these runs to understand the generalizability of the model.

**Example:**
```python
datasets = [dataset1, dataset2]
for data in datasets:
    with mlflow.start_run():
        clf = RandomForestClassifier()
        clf.fit(data['train'], data['target'])
        mlflow.log_metric('accuracy', clf.score(data['test'], data['target_test']))
```

---

#### **3. Incremental Training**
Incremental training refers to training a model in stages, rather than on the whole dataset at once. This is helpful when dealing with large datasets that don’t fit in memory or in online learning.

**Example:**
```python
from sklearn.linear_model import SGDClassifier
clf = SGDClassifier()

for data_chunk in data_chunks:
    with mlflow.start_run():
        clf.partial_fit(data_chunk['train'], data_chunk['target'])
        mlflow.log_metric('accuracy', clf.score(data_chunk['test'], data_chunk['target_test']))
```

---

#### **4. Model Checkpointing**
MLflow supports checkpointing to save intermediate models during long-running experiments. This is helpful for resuming training or tracking progress.

**Example:**
```python
with mlflow.start_run():
    for epoch in range(epochs):
        # Training code
        mlflow.log_artifact("model_checkpoint.pth")  # Save checkpoints
```

---

#### **5. Feature Engineering**
Feature engineering involves creating new features or modifying existing ones to improve model performance. MLflow can track these modifications across runs to identify their impact.

**Example:**
```python
with mlflow.start_run():
    # Feature engineering step
    new_feature = data['col1'] * data['col2']
    mlflow.log_param("feature_engineering", "col1 * col2")
    clf.fit(data, labels)
```

---

### **Autologging**
Autologging automates the logging of parameters, metrics, and models, reducing the need for manual logging.

#### **1. MLflow.autolog()**
This function enables autologging for supported machine learning libraries, such as scikit-learn, TensorFlow, and PyTorch.

**Example:**
```python
mlflow.autolog()
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
```

#### **2. MLflow.<lib>.autolog()**
For specific libraries, MLflow offers tailored autologging functions.

**Example:**
```python
mlflow.tensorflow.autolog()  # Enables TensorFlow-specific autologging
```

#### **3. MLflow.sklearn.autolog()**
This function enables autologging for scikit-learn models.

**Example:**
```python
mlflow.sklearn.autolog()
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
```

---

### **Tracking Server**

#### **1. Storage**
The MLflow tracking server allows you to log data and models to various storage backends. You can configure both the backend store and artifact store.

##### **Backend Store**
Stores metadata like parameters, metrics, and run information.

- **DB Store**: Supports `sqlite`, `mysql`, and `postgresql`.
  - Example: 
    - SQLite: `sqlite:///mlflow.db`
    - MySQL: `mysql+pymysql://username:password@host/db`
    - PostgreSQL: `postgresql://username:password@host/db`

##### **Artifact Store**
Stores large files like models, images, and other artifacts.
- Example stores: 
  - **AWS S3**: `s3://bucket-name/artifacts/`
  - **Azure Blob Storage**: `azure://container-name/artifacts/`
  - **Google Cloud Storage (GCS)**: `gs://bucket-name/artifacts/`



### **Starting the MLflow Tracking Server with MySQL, SQLite, PostgreSQL, and Artifact Stores**

#### **1. Setting up the Tracking Server with MySQL, SQLite, or PostgreSQL**

To start an MLflow tracking server using a specific backend store (MySQL, SQLite, or PostgreSQL), you need to specify the database connection details in the command.

##### **1a. SQLite Example**
SQLite is a simple file-based database, and it's a good choice for local development or small-scale experimentation.

**Start the tracking server with SQLite:**
```bash
mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./mlruns \
    --host 0.0.0.0 --port 5000
```
In this case:
- `--backend-store-uri` is the location where the tracking data will be stored.
- `--default-artifact-root` defines where the model artifacts will be stored.

##### **1b. MySQL Example**
MySQL is more suitable for production use and multi-user setups.

**Start the tracking server with MySQL:**
```bash
mlflow server \
    --backend-store-uri mysql+pymysql://username:password@host:port/dbname \
    --default-artifact-root s3://your-bucket/mlflow-artifacts \
    --host 0.0.0.0 --port 5000
```
- `mysql+pymysql://username:password@host:port/dbname` is the MySQL database connection URI.

##### **1c. PostgreSQL Example**
PostgreSQL is another robust choice for scalable, production-grade tracking servers.

**Start the tracking server with PostgreSQL:**
```bash
mlflow server \
    --backend-store-uri postgresql://username:password@host:port/dbname \
    --default-artifact-root gs://your-bucket/mlflow-artifacts \
    --host 0.0.0.0 --port 5000
```
- `postgresql://username:password@host:port/dbname` is the PostgreSQL database connection URI.

---

#### **2. Setting up the Artifact Store**

In addition to the backend store (which tracks metadata like parameters and metrics), you need an artifact store for storing model artifacts, logs, and other large files.

##### **Artifact Store Example with AWS S3:**
```bash
mlflow server \
    --backend-store-uri mysql+pymysql://username:password@host:port/dbname \
    --default-artifact-root s3://your-bucket/mlflow-artifacts \
    --host 0.0.0.0 --port 5000
```
- `s3://your-bucket/mlflow-artifacts` refers to an S3 bucket that stores artifacts.

##### **Artifact Store Example with Azure Blob Storage:**
```bash
mlflow server \
    --backend-store-uri postgresql://username:password@host:port/dbname \
    --default-artifact-root azure://your-container/mlflow-artifacts \
    --host 0.0.0.0 --port 5000
```
- `azure://your-container/mlflow-artifacts` refers to an Azure Blob Storage container.

##### **Artifact Store Example with Google Cloud Storage (GCS):**
```bash
mlflow server \
    --backend-store-uri postgresql://username:password@host:port/dbname \
    --default-artifact-root gs://your-bucket/mlflow-artifacts \
    --host 0.0.0.0 --port 5000
```
- `gs://your-bucket/mlflow-artifacts` is a Google Cloud Storage (GCS) bucket that will store your MLflow artifacts.

---


#### **2. Networking**

##### **REST API**
MLflow’s REST API allows communication between the client and the tracking server. You can use this API to log parameters, metrics, and models programmatically.

##### **Proxy Access**
A proxy can be set up to access the tracking server behind firewalls.

##### **RPC (gRPC)**
MLflow uses gRPC for remote procedure calls, enhancing communication efficiency between distributed systems.

---

### **ML Model Components**

#### **1. Storage Format**
MLflow stores models in a standardized format, making it easy to reload and serve them.

#### **2. Model, Signature**
Model signatures capture input and output data shapes and types, ensuring consistent data processing when the model is deployed.

#### **3. Model API**

##### **Signature Enforcement**
- **Name Ordering Enforcement**: Ensures that input features are provided in the order expected by the model.
- **Input Type Enforcement**: Validates the types of inputs (e.g., floats, integers) before feeding them into the model.

##### **Log Signature and Input Example** (without autologging)
To log a model signature manually:
1. Create a list of dictionaries for input data.
2. Create output data and define a schema with `ColumnSpec`.

**Example:**
```python
from mlflow.models.signature import infer_signature
input_example = X_test[:5]  # Example input data
signature = infer_signature(X_train, y_train)

with mlflow.start_run():
    mlflow.sklearn.log_model(clf, "model", signature=signature, input_example=input_example)
```

---

#### **Model API**

##### **1. save_model()**
Saves the trained model to disk.

##### **2. load_model()**
Loads a saved model for inference or further training.

**Example:**
```python
# Save model
mlflow.sklearn.save_model(clf, "my_model")

# Load model
model = mlflow.sklearn.load_model("my_model")
```

### **Logging Signature and Input Examples in MLflow (Without Autologging)**

In MLflow, model signatures capture the schema of the input and output data. Logging a signature ensures that future predictions use the correct data format. Here's a detailed example of how to create and log a signature manually:

#### **Steps for Logging Signature and Input Example:**

1. **Create a List of Dictionaries for Input Data**
   - This step represents the data format used for predictions, often as a Pandas DataFrame or NumPy array.

**Example:**
```python
import pandas as pd

input_example = pd.DataFrame({
    "age": [25, 30, 35],
    "salary": [50000, 60000, 70000]
})
```

2. **Create Output Data**
   - This represents the target variable or predictions that the model will output.

**Example:**
```python
output_example = pd.DataFrame({
    "predicted_salary": [52000, 61000, 73000]
})
```

3. **Create a Schema Using `mlflow.models.signature.infer_signature()`**
   - The signature captures the schema (data types, column names) of the input and output.

**Example:**
```python
from mlflow.models.signature import infer_signature

# Infer the input-output signature from the training data and model predictions
signature = infer_signature(input_example, output_example)
```

4. **Log the Model with Signature and Input Example**
   - When saving the model, you can log both the signature and an example of the input.

**Example:**
```python
from sklearn.ensemble import RandomForestRegressor
import mlflow
import mlflow.sklearn

# Train a model
X_train = input_example
y_train = output_example['predicted_salary']
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Start a new run in MLflow
with mlflow.start_run():
    # Log the model with signature and input example
    mlflow.sklearn.log_model(
        sk_model=model, 
        artifact_path="random_forest_model",
        signature=signature, 
        input_example=input_example
    )
```

In this example:
- `input_example` provides an actual sample of input data.
- `signature` ensures that the correct input and output types are logged for model inference.

---

### **Advanced Signature Enforcement**

MLflow uses signature enforcement to ensure that inputs conform to the expected format when the model is deployed. This can include:

1. **Name Ordering Enforcement**: Ensures that the input data columns are provided in the exact order as expected.
2. **Input Type Enforcement**: Enforces data types such as `float`, `integer`, or `string` to prevent incorrect input formats.
3. **Output Type Enforcement**: Ensures the output data is of the expected type.

**Example:**
```python
from mlflow.models import ModelSignature
from mlflow.types import DataType, Schema, ColSpec

# Define input and output schemas manually
input_schema = Schema([ColSpec(DataType.integer, "age"), ColSpec(DataType.double, "salary")])
output_schema = Schema([ColSpec(DataType.double, "predicted_salary")])

# Create a signature using these schemas
signature = ModelSignature(inputs=input_schema, outputs=output_schema)

# Log the model with the manually defined signature
with mlflow.start_run():
    mlflow.sklearn.log_model(model, "model_with_signature", signature=signature)
```

In this case, the input schema specifies that "age" should be an integer, while "salary" should be a floating-point number. The output is expected to be a floating-point number (`double`).

---

These additions cover the process of starting the MLflow multiple runs to model tracking, logging, and storage configuration, tracking server with various backend stores (MySQL, SQLite, PostgreSQL) and artifact stores (AWS S3, Azure Blob, GCS). Moreover, the detailed example for logging signatures should provide clarity on how to enforce and log model signatures manually.
