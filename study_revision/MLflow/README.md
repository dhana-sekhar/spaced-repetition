### **MLflow Notes**

---

### **What is MLflow?**

MLflow is an open-source platform designed to manage the entire machine learning (ML) lifecycle. It enables data scientists and machine learning engineers to track experiments, package code into reproducible runs, and share and deploy models easily. MLflow provides a suite of tools for simplifying these tasks and making them collaborative across teams. 

MLflow has four primary components that help manage machine learning workflows:

1. **Tracking**: Logs and queries experiments (code, data, parameters, metrics).
2. **Projects**: Packages ML code in a reusable, reproducible form.
3. **Models**: Manages and deploys models across different platforms.
4. **Model Registry**: Provides a centralized hub for managing model lifecycles.

---

### **Main MLflow Components**

#### **1. MLflow Tracking**
MLflow Tracking is an API and UI to log parameters, metrics, and artifacts when running machine learning code. This allows tracking and comparing different experiment runs, which helps to identify the best-performing models and configurations.

##### **Functions and Usage**

- **MLflow.start_run()**: Starts a new experiment run to log all metrics, parameters, and artifacts.
  - **Example**:
    ```python
    import mlflow
    with mlflow.start_run():
        mlflow.log_param("alpha", 0.5)
        mlflow.log_metric("accuracy", 0.95)
    ```

- **mlflow.end_run()**: Ends the active run.
  - **Example**:
    ```python
    mlflow.end_run()
    ```

#### **2. MLflow Projects**
MLflow Projects is a way to package ML code in a standardized format to enhance reproducibility and collaboration. Projects are defined by a YAML file (`MLproject`) that contains dependencies and execution steps.

- **Example**: A project could have a structure like this:
  ```
  .
  ├── MLproject
  ├── main.py
  ├── conda.yaml
  ```

#### **3. MLflow Models**
MLflow Models provides a standard format to package models, ensuring they are easily deployable across different environments.

- **Example**:
  ```bash
  mlflow models serve --model-uri models:/model_name/Production --port 1234
  ```

#### **4. MLflow Model Registry**
The Model Registry is a collaborative environment for managing the full lifecycle of machine learning models. It allows versioning, stage transitions (staging, production, archived), and annotations of models.

---

### **MLflow Tracking API Details**

#### **Basic Run Management Functions**

- **set_tracking_uri()**: Sets the URI of the tracking server where the logs will be stored.
  - **Example**:
    ```python
    mlflow.set_tracking_uri("http://localhost:5000")
    ```

- **get_tracking_uri()**: Retrieves the current tracking URI.
  - **Example**:
    ```python
    print(mlflow.get_tracking_uri())
    ```

- **create_experiment()**: Creates a new experiment where all related runs will be logged.
  - **Example**:
    ```python
    mlflow.create_experiment("experiment_name")
    ```

- **set_experiment()**: Sets the active experiment where logs will be stored.
  - **Example**:
    ```python
    mlflow.set_experiment("my_experiment")
    ```

- **start_run()**: Begins a run to track metrics and parameters.
  - **Example**:
    ```python
    mlflow.start_run()
    ```

- **end_run()**: Ends the current active run.
  - **Example**:
    ```python
    mlflow.end_run()
    ```

- **active_run()**: Returns the currently active run object.
  - **Example**:
    ```python
    run = mlflow.active_run()
    print(run.info.run_id)
    ```

- **last_active_run()**: Returns the most recent active run.
  - **Example**:
    ```python
    last_run = mlflow.last_active_run()
    print(last_run.info.run_id)
    ```

#### **Logging Functions**

- **log_param()**: Logs a single parameter associated with the run.
  - **Example**:
    ```python
    mlflow.log_param("learning_rate", 0.01)
    ```

- **log_params()**: Logs multiple parameters at once.
  - **Example**:
    ```python
    params = {"n_estimators": 100, "max_depth": 3}
    mlflow.log_params(params)
    ```

- **log_metric()**: Logs a single metric associated with the run.
  - **Example**:
    ```python
    mlflow.log_metric("accuracy", 0.95)
    ```

- **log_metrics()**: Logs multiple metrics at once.
  - **Example**:
    ```python
    metrics = {"precision": 0.90, "recall": 0.85}
    mlflow.log_metrics(metrics)
    ```

- **log_artifact()**: Logs a local file or directory as an artifact.
  - **Example**:
    ```python
    mlflow.log_artifact("model.pkl")
    ```

- **log_artifacts()**: Logs all artifacts from a given directory.
  - **Example**:
    ```python
    mlflow.log_artifacts("model_outputs/")
    ```

- **get_artifact_uri()**: Returns the artifact URI for the run.
  - **Example**:
    ```python
    print(mlflow.get_artifact_uri())
    ```

#### **Tagging Functions**

- **set_tag()**: Sets a tag for the run, which is a key-value pair.
  - **Example**:
    ```python
    mlflow.set_tag("version", "1.0")
    ```

- **set_tags()**: Sets multiple tags at once.
  - **Example**:
    ```python
    tags = {"team": "ML", "release_stage": "staging"}
    mlflow.set_tags(tags)
    ```

---

These notes cover the basics of MLflow from setting up tracking to logging parameters, metrics, and artifacts. It provides you with a solid foundation to start working with MLflow, and these concepts are essential for managing and scaling machine learning models effectively.