Helm is a powerful tool for managing Kubernetes applications by using charts, which are like templates for Kubernetes resources.

### Here's a basic plan to get you started with Helm:

#### 1. **What is Helm?**
Helm is a package manager for Kubernetes, allowing you to define, install, and upgrade complex Kubernetes applications. It organizes Kubernetes YAML manifests into reusable "charts," which makes deployments more efficient and scalable.

#### 2. **Helm Components**
- **Chart**: A Helm package that contains all the Kubernetes manifest files.
- **Release**: A running instance of a Helm chart in a Kubernetes cluster.
- **Repository**: Where Helm charts are stored and shared.

#### 3. **Creating a Helm Chart**
You can create your first Helm chart to start learning. Here’s a step-by-step guide to creating a simple chart.

##### Step 1: Create a Helm Chart
Run the following command to create a new chart:
```bash
helm create my-first-chart
```

This will generate a directory structure that includes:
- `Chart.yaml`: Metadata about the chart (name, version, etc.).
- `values.yaml`: Default values that are passed to the templates.
- `templates/`: Contains your Kubernetes YAML templates.

##### Step 2: Understand the Files
- **Chart.yaml**: 
   It defines metadata for your chart.
   ```yaml
   apiVersion: v2
   name: my-first-chart
   version: 0.1.0
   ```
- **values.yaml**: 
   It stores default configuration values, which will be used in your templates.
   ```yaml
   replicaCount: 1
   image:
     repository: nginx
     tag: latest
   ```

- **templates/**: Contains your Kubernetes manifests. Helm will inject values from `values.yaml` or from command-line overrides into these templates.

##### Step 3: Customize Your Chart
Let’s modify the default deployment in `templates/deployment.yaml`. In the YAML, you’ll find placeholders like this:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}-deployment
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
```

These placeholders (`{{ }}`) are using the Go templating language. Helm injects values from `values.yaml` or command-line arguments when deploying.

#### 4. **Installing the Chart**
To install the Helm chart into your Kubernetes cluster:

```bash
helm install my-release ./my-first-chart
```

Here:
- `my-release` is the name of the Helm release.
- `./my-first-chart` points to the chart directory you just created.

Helm will generate Kubernetes resources based on the templates and deploy them to your cluster.

#### 5. **Working with Values**
You can override `values.yaml` defaults by passing values via the command line:

```bash
helm install my-release ./my-first-chart --set replicaCount=3
```

This overrides the replica count from 1 to 3, making the deployment scale with 3 replicas.

#### 6. **Upgrading a Release**
If you make changes to your chart or its values, you can upgrade the running release:
```bash
helm upgrade my-release ./my-first-chart --set image.tag=v2
```
This upgrades the application to use the new image version (`v2`).

#### 7. **Uninstalling a Release**
To uninstall a release and clean up all resources created by Helm:
```bash
helm uninstall my-release
```

#### 8. **Helm Repositories**
You can add public repositories to install pre-packaged charts, for example:
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm search repo bitnami
```

This will give you access to a wide range of pre-built charts you can install or use as references.

### Next Steps
- Play around with the Helm chart values and templates.
- Explore how Helm can manage multiple environments (e.g., dev, staging, prod) using different values files.
- Dive into Helm hooks, testing, and chart dependencies.

### Moving on 
Helm can manage multiple environments (e.g., dev, staging, prod) by using different `values.yaml` files for each environment. The idea is to provide environment-specific configurations (like replica count, image tags, etc.) that override the default values during installation or upgrade. Let’s go step by step:

### 1. **Managing Multiple Environments with Helm**
Each environment (like dev, staging, and prod) usually has different requirements such as replica counts, resource limits, and image versions. You can manage these differences in separate values files for each environment.

#### Example Structure:
```
my-first-chart/
  ├── charts/
  ├── templates/
  ├── Chart.yaml
  ├── values.yaml        # Default values
  ├── values-dev.yaml    # Dev-specific values
  ├── values-staging.yaml # Staging-specific values
  └── values-prod.yaml   # Prod-specific values
```

#### Step-by-Step Example

1. **Define the default `values.yaml`:**
   This is the base configuration, and it applies if no specific environment values are provided.
   ```yaml
   replicaCount: 1
   image:
     repository: nginx
     tag: latest
   ```

2. **Create an environment-specific values file, e.g., `values-dev.yaml`:**
   Here, you might want to scale down or use a different image version for development.
   ```yaml
   replicaCount: 1
   image:
     repository: nginx
     tag: dev
   ```

3. **Create a staging-specific `values-staging.yaml`:**
   This file can have configurations suited for a testing environment.
   ```yaml
   replicaCount: 2
   image:
     repository: nginx
     tag: staging
   ```

4. **Create a production-specific `values-prod.yaml`:**
   This is typically the final configuration, ready for production deployment.
   ```yaml
   replicaCount: 5
   image:
     repository: nginx
     tag: prod
   ```

#### Step 1: Deploying to Development
You can install the Helm chart in the dev environment by specifying `values-dev.yaml`:
```bash
helm install my-release-dev ./my-first-chart -f values-dev.yaml
```

This will use the configurations in `values-dev.yaml` (1 replica, dev image).

#### Step 2: Deploying to Staging
For staging, use the `values-staging.yaml` file:
```bash
helm install my-release-staging ./my-first-chart -f values-staging.yaml
```

This would create a deployment with 2 replicas, using the `staging` tag of the image.

#### Step 3: Deploying to Production
For production, use the `values-prod.yaml` file:
```bash
helm install my-release-prod ./my-first-chart -f values-prod.yaml
```

This will create a deployment with 5 replicas using the `prod` image.

### 2. **Upgrading Releases for Specific Environments**
When you want to make changes or upgrade a specific environment, you can pass the corresponding values file again during the upgrade.

For example, upgrading the production environment to use a new image tag:
```bash
helm upgrade my-release-prod ./my-first-chart -f values-prod.yaml --set image.tag=prod-v2
```

This upgrades the production deployment to use `prod-v2` without affecting other environments.

### 3. **Listing Installed Helm Releases**
To list all the installed Helm releases across your Kubernetes cluster, you can use the following command:

```bash
helm list
```

This will show details like the release name, namespace, revision, status, and the time it was last updated. By default, it lists releases from the current namespace. You can list releases from all namespaces using:
```bash
helm list --all-namespaces
```

### 4. **Using Multiple Values Files Together**
You can even combine multiple values files in one Helm install or upgrade. Helm merges the values from the specified files, with later files overriding earlier ones.

For example, if you want to combine `values.yaml` with `values-prod.yaml`, you can do:
```bash
helm install my-release-prod ./my-first-chart -f values.yaml -f values-prod.yaml
```

Helm will first apply the default `values.yaml`, then override any settings specified in `values-prod.yaml`.

### Recap:
- **Different values files** (`values-dev.yaml`, `values-prod.yaml`, etc.) let you manage environment-specific configurations.
- Use the `-f` flag to point Helm to a specific values file during installation/upgrade.
- **`helm list`** gives you a list of all installed Helm releases, allowing you to see what’s deployed where.

