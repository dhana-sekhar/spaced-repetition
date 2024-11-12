Here are some essential Helm commands to help you get started with managing charts, releases, and configurations in Kubernetes:

### 1. **Basic Commands for Helm Installation and Setup**

- **Initialize Helm (Helm v2 only)**: Helm v3 doesn’t require server-side components (`tiller`) like Helm v2 did.
  ```bash
  helm init
  ```

- **Add a Helm Repository**: Add a repository to pull charts from (e.g., the stable repository for commonly used charts).
  ```bash
  helm repo add [repo_name] [repo_url]
  # Example: helm repo add bitnami https://charts.bitnami.com/bitnami
  ```

- **Update Repositories**: Updates your local Helm repository cache with the latest charts.
  ```bash
  helm repo update
  ```

- **List Repositories**: Shows all repositories currently added to Helm.
  ```bash
  helm repo list
  ```

### 2. **Installing and Managing Releases**

- **Install a Chart**: Install a chart from a repository, creating a new release.
  ```bash
  helm install [release_name] [repo_name/chart_name] --values values.yaml
  # Example: helm install myapp bitnami/nginx --values custom-values.yaml
  ```

- **List Releases**: View all releases installed in the Kubernetes cluster.
  ```bash
  helm list
  ```

- **View Release Status**: Check the status of a specific release.
  ```bash
  helm status [release_name]
  ```

- **Uninstall a Release**: Deletes a release from the Kubernetes cluster.
  ```bash
  helm uninstall [release_name]
  ```

### 3. **Upgrading and Rolling Back Releases**

- **Upgrade a Release**: Apply changes to an existing release, useful for updating configuration or the chart version.
  ```bash
  helm upgrade [release_name] [repo_name/chart_name] --values updated-values.yaml
  # Example: helm upgrade myapp bitnami/nginx --values new-values.yaml
  ```

- **Rollback a Release**: Roll back to a previous release version if something goes wrong.
  ```bash
  helm rollback [release_name] [revision_number]
  # Example: helm rollback myapp 1
  ```

### 4. **Working with Helm Charts**

- **Create a New Helm Chart**: Generates the structure of a new Helm chart in the specified directory.
  ```bash
  helm create [chart_name]
  # Example: helm create mychart
  ```

- **Inspect a Chart**: View information about a chart before installing it, including values and chart details.
  ```bash
  helm show chart [repo_name/chart_name]
  helm show values [repo_name/chart_name]
  ```

- **Template Rendering**: Preview a chart by rendering templates with the specified values (useful for debugging).
  ```bash
  helm template [chart_name] --values values.yaml
  # Example: helm template mychart --values values.yaml
  ```

### 5. **Helm Repositories and Search**

- **Search for a Chart**: Find charts in repositories added to Helm.
  ```bash
  helm search repo [search_term]
  # Example: helm search repo nginx
  ```

### 6. **Helm History**

- **View Release History**: See the history of updates (revisions) made to a release.
  ```bash
  helm history [release_name]
  ```

### Summary Cheat Sheet

| Command                            | Description                                              |
|------------------------------------|----------------------------------------------------------|
| `helm repo add [name] [url]`       | Add a new Helm chart repository                          |
| `helm repo update`                 | Update local cache of chart repositories                 |
| `helm install [release] [chart]`   | Install a chart as a release                            |
| `helm list`                        | List all installed releases                             |
| `helm status [release]`            | Check the status of a specific release                  |
| `helm upgrade [release] [chart]`   | Upgrade a release with updated values or chart version  |
| `helm rollback [release] [rev]`    | Roll back to a previous release revision                |
| `helm uninstall [release]`         | Uninstall a release                                     |
| `helm create [chart]`              | Create a new Helm chart                                 |
| `helm template [chart]`            | Render templates locally to preview changes             |

These commands cover the basic usage of Helm for managing charts and releases.