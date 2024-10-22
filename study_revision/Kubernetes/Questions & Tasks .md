Here’s a set of questions and tasks based on your notebook to help with spaced repetition:

### **Questions:**
1. What command would you use to check the Kubernetes version installed on your system?
2. How would you get a list of all Pods in your current namespace?
3. What is the difference between `kubectl apply -f` and `kubectl create -f` when working with YAML files?
4. How do you view logs for a specific Pod in Kubernetes?
5. Describe the role of the **API Server** in the control plane.
6. What is **etcd**, and what role does it play in a Kubernetes cluster?
7. Explain the responsibilities of the **Controller Manager**.
8. What is the purpose of the **Kubelet** on worker nodes?
9. Define the role of **Kube Proxy**.
10. What is a **Pod** in Kubernetes, and how is it different from a container?
11. Name three types of **Services** and their use cases.
12. What is the difference between a **ConfigMap** and a **Secret** in Kubernetes?
13. Explain the purpose of a **Persistent Volume Claim (PVC)**.
14. What does **Ingress** provide in Kubernetes?
15. What is the role of **StorageClass** in Kubernetes?

## Few more 

Here are more Kubernetes commands to reinforce your learning:

### **Commands Questions:**

1. How do you get the status of all the resources in a specific namespace?
2. What is the command to delete a namespace?
3. How would you scale a deployment to 5 replicas?
4. What is the command to view all Services in a cluster?
5. How would you restart all Pods in a deployment without deleting them?
6. How do you expose a deployment as a service?
7. What is the command to edit a running resource (e.g., a Pod or deployment)?
8. How would you label a node as "production"?
9. How do you view the events in a Kubernetes cluster?
10. What command would you use to execute a command inside a running Pod (e.g., checking the file system or running a shell)?
11. How would you roll back a deployment to a previous version?
12. How do you list all the Persistent Volumes (PVs) in your cluster?
13. How would you drain a node to prepare it for maintenance (without disrupting workloads)?
14. How do you patch an existing resource, like adding labels or annotations to a Pod?

Answer these to test your familiarity with various kubectl commands!

### **Tasks:**
1. **Deploy a Pod using `kubectl run` and a YAML file.**  
   Create an NGINX Pod using both the `kubectl run` command and by applying a YAML manifest.

2. **Set up Namespaces.**  
   Create a new namespace, then deploy a Pod into that namespace. Use `kubectl get pods --namespace=<namespace>` to verify its deployment.

3. **Work with ConfigMaps and Secrets.**  
   Create a ConfigMap and a Secret. Use them in a Pod by mounting them as volumes or environment variables.

4. **Service Setup.**  
   Deploy a multi-container Pod, expose it using a **ClusterIP** and a **NodePort** service, and verify its access.

5. **Persistent Volume Task.**  
   Create a Persistent Volume and Persistent Volume Claim, then use it in a Pod to ensure that the storage is persistent.

These questions and tasks will cover most of the core components from your notes and help you retain the knowledge effectively.