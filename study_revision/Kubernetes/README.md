Below is the updated version with Kubernetes objects and deployment strategies added.

---

# Kubernetes Notes

## 1. **Core Concepts**

| Concept           | Description                                                                                  |
|-------------------|----------------------------------------------------------------------------------------------|
| **Cluster**        | A set of machines (nodes) that run containerized applications.                               |
| **Node**           | A machine (VM or physical) that runs the Kubernetes components and workloads.                |
| **Pod**            | The smallest deployable unit, one or more containers that share the same network/IP.         |
| **Service**        | Exposes a set of Pods as a network service.                                                  |
| **Namespace**      | Virtual clusters inside a Kubernetes cluster.                                                |
| **ConfigMap**      | Stores configuration data as key-value pairs.                                                |
| **Secret**         | Stores sensitive data such as passwords, tokens, etc.                                        |

---

## 2. **Kubernetes Objects**

| Object            | Description                                                                                  |
|-------------------|----------------------------------------------------------------------------------------------|
| **Pod**           | A group of one or more containers, with shared storage/network resources and a specification for how to run them. |
| **ReplicaSet**     | Ensures a specified number of pod replicas are running at any given time.                    |
| **Deployment**     | Manages ReplicaSets and provides declarative updates to Pods and ReplicaSets.                |
| **DaemonSet**      | Ensures that all or some nodes run a copy of a pod.                                          |
| **StatefulSet**    | Manages stateful applications, ensuring unique, stable network identities for Pods.          |
| **Job**           | Creates one or more Pods and ensures that a specified number of them successfully terminate.  |
| **CronJob**        | Schedules jobs to run at specified times or intervals.                                       |
| **ConfigMap**      | Provides a way to inject configuration data into Pods.                                       |
| **Secret**         | Stores sensitive information such as passwords or API tokens.                                |
| **Service**        | Provides stable endpoints for Pods.                                                          |
| **Ingress**        | Manages external access to services in a cluster, typically HTTP.                            |
| **PersistentVolume (PV)** | A storage resource in the cluster.                                                     |
| **PersistentVolumeClaim (PVC)** | A user's request for storage.                                                   |
| **HorizontalPodAutoscaler (HPA)** | Automatically scales the number of pods based on observed CPU utilization or other metrics. |

---

## 3. **Kubernetes Architecture**

| Component                        | Description                                                                                     |
|----------------------------------|-------------------------------------------------------------------------------------------------|
| **Master Node**                  | Manages the Kubernetes cluster and makes decisions about scheduling and maintaining the desired state. Contains several control plane components. |
| **Kube-apiserver**               | The main entry point for the Kubernetes API, processes API requests and serves as the cluster's front-end. All communication with the cluster happens via the API server. |
| **etcd**                         | A distributed key-value store that stores all the data used to manage the cluster, such as the cluster state, configuration, and secrets. |
| **Kube-scheduler**               | Assigns newly created Pods to nodes based on resource availability and other constraints. Ensures efficient resource utilization. |
| **Kube-controller-manager**      | Manages various controllers that regulate the state of the cluster (e.g., node controller, replication controller, etc.). |
| **Cloud-controller-manager**     | Manages cloud-specific controller logic, such as creating, updating, and deleting resources in a cloud provider. |
| **Kubelet**                      | An agent that runs on each node, ensures that containers are running in a Pod, and communicates with the control plane. |
| **Kube-proxy**                   | Network proxy that maintains network rules on each node, enabling communication between Pods and services. |
| **Container Runtime**            | The software responsible for running containers, such as Docker, containerd, or CRI-O.          |
| **Node**                         | A worker machine (physical or virtual) in the Kubernetes cluster that runs the containers. Contains Kubelet, Kube-proxy, and container runtime. |
| **Control Plane**                | The set of components (API server, etcd, controller manager, scheduler) responsible for managing the state of the cluster. |
| **Add-ons**                      | Additional services that run on the cluster, such as DNS for service discovery, cluster logging, and monitoring. |
| **Ingress Controller**           | Manages access to the services in a Kubernetes cluster from external clients, typically using HTTP/HTTPS. |

---

## 4. **Pods**

| Property         | Description                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------|
| **Multi-container** | Pods can have multiple containers that share resources like storage and network.            |
| **Ephemeral**    | Pods are designed to be short-lived and are replaced when they fail.                           |
| **Lifecycle**    | Pods have various lifecycle phases (Pending, Running, Succeeded, Failed).                      |

### Pod Example (YAML)
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
    - name: my-container
      image: nginx
```

---

## 5. **Services**

| Type             | Description                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------|
| **ClusterIP**    | Exposes the service on a cluster-internal IP.                                                  |
| **NodePort**     | Exposes the service on each Node’s IP at a static port.                                        |
| **LoadBalancer** | Exposes the service externally using a cloud provider’s load balancer.                         |
| **ExternalName** | Maps a service to an external DNS name.                                                        |

---

## 6. **Deployments**

| Field            | Description                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------|
| **Replicas**     | Specifies the number of pod replicas to be running.                                            |
| **Strategy**     | Defines how updates are performed (RollingUpdate or Recreate).                                 |
| **Selector**     | Defines the label selector to identify Pods managed by this Deployment.                        |

### Deployment Example (YAML)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.14.2
          ports:
            - containerPort: 80
```

---

## 7. **Deployment Strategies**

| Strategy         | Description                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------|
| **RollingUpdate**| Default strategy. Gradually replaces old pods with new ones, ensuring minimal downtime.         |
| **Recreate**     | Terminates all existing pods before creating new ones.                                         |
| **Blue/Green**   | Runs two environments, with a switch to route traffic to the new version after testing.        |
| **Canary**       | Gradually shifts traffic to a new version by deploying a small percentage of pods initially.   |

---

## 8. **Storage**

| Type             | Description                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------|
| **PersistentVolume (PV)** | A piece of storage in the cluster. Managed by administrators.                          |
| **PersistentVolumeClaim (PVC)** | A user's request for storage. Binds to a PersistentVolume.                     |
| **StorageClass**  | Defines different storage types like SSD, HDD, etc.                                           |

---

## 9. **ConfigMap and Secrets**

| Concept          | Description                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------|
| **ConfigMap**    | Non-confidential key-value pairs used for configuration data.                                  |
| **Secret**       | Stores confidential information like passwords and tokens.                                     |

### Secret Example (YAML)
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  username: YWRtaW4=  # Base64 encoded
  password: MWYyZDFlMmU2N2Rm
```

---

## 10. **Networking**

| Concept          | Description                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------|
| **CNI**          | Container Network Interface used to set up networking between containers.                      |
| **Service**      | Provides networking for connecting Pods.                                                      |
| **Ingress**      | Exposes HTTP and HTTPS routes to services outside the cluster.                                 |

---

## 11. **Monitoring & Logging**

| Tool             | Description                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------|
| **Prometheus**   | Open-source monitoring and alerting tool.                                                     |
| **Grafana**      | Visualizes data from Prometheus or other sources.                                              |
| **Fluentd**      | A log collector that works with Kubernetes to aggregate and forward logs.                      |

---

## 12. **Helm**

| Concept          | Description                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------|
| **Chart**        | A Helm package that contains Kubernetes resource definitions.                                  |
| **Release**      | An instance of a chart deployed to the cluster.                                                |
| **Values.yaml**  | A file used to provide default configuration values for the chart.                             |

### Example Helm Commands
```bash
# Install a Helm chart
helm install my-release stable/nginx

# List installed Helm releases
helm list

# Uninstall a Helm release
helm uninstall my-release
```

---

## 13. **Advanced Topics**

| Topic            | Description                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------|
| **RBAC**         | Role-Based Access Control, controls access to Kubernetes resources.                            |
| **Taints & Tolerations** | Control which nodes can run specific Pods.                                             |
| **Affinity & Anti-affinity** | Defines rules for placing Pods based on certain conditions.                       |

---


## 14. **Useful Commands**

| Command                                       | Description                                                       |
|-----------------------------------------------|-------------------------------------------------------------------|
| `kubectl get pods`                            | List all pods in the default namespace.                           |
| `kubectl describe pod <pod>`                  | Describe details about a specific pod.                            |
| `kubectl logs <pod>`                          | Fetch logs for a container in a pod.                              |
| `kubectl exec -it <pod> -- <cmd>`             | Execute a command inside a running container.                     |
| `kubectl version`                             | Check the version of kubectl and the Kubernetes cluster.          |
| `kubectl get nodes`                           | Get information about all nodes in the cluster.                   |
| `kubectl run nginx --image=nginx`             | Start a pod with the `nginx` image.                               |
| `kubectl apply -f service.yaml`               | Start a pod or service using a YAML file.                         |
| `kubectl create -f service.yaml`              | Start a pod or service using a YAML file (alternative to `apply`).|
| `kubectl get <kind>`                          | Get resources by specifying the resource type.                    |
| `kubectl describe pods/<pod-name>`            | Describe a specific pod.                                          |
| `kubectl get pods/<pod-name> -o wide`         | Find the node on which a specific pod is running.                 |
| `kubectl delete pods/<pod-name>`              | Delete a specific pod.                                            |
| `kubectl delete all --all`                    | Delete all resources in the current namespace.                    |
| `kubectl apply -f /foldername`                | Apply all YAML files in a folder.                                 |
| `kubectl get namespace`                       | List all namespaces.                                              |
| `kubectl create namespace <namespace name>`   | Create a new namespace.                                           |

---

