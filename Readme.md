# Kubernetes for Data Engineering 

This repo contains the necessary configuration files and DAGs(Directed Acyclic Graphs) for setting up a robust data engineering enviroment using Kubernetes and Apache Airflow. it includes the setup for the Kubernetes Dashboard, which provides a user-friendly web interface for managing Kubernetes clusters, and Apache Airflow, a platform to programmatically author, schedule, and monitor workflows.

## Repository Structure
This repository is organised as follows:


## DAGs
fetch_and_preview.py - A DAG for fetching data and providign a preview.
hello.py - A simple example DAG to demonstrate basic Airflow concepts.

## Kubernetes (k8s) Configuration

dashboard-adminuser.yaml - YAML file for setting up an admin user for the Kubernetes Dashboard.
dashboard-clusterrole.yaml - YAML file defining the cluster role for the Kubernetes Dashboard.
dashboard-secret.yaml - YAML file for managing secrets used by the Kubernetes Dashboard.
Values.yaml - YAML file containing values for customising the Kubernetes setup.

# Getting Started

## Prerequisites
- A Kubernetes cluster
- kubectl installed and configured
- Helm (optional, but recommended for managing Kubernetes applications)

Setup
Deploy the Kubernetes Dashboard:

To deploy the Kubernetes Dashboard, apply the YAML files in the k8s directory:

kubectl apply -f k8s/
This will set up the Kubernetes Dashboard with the necessary roles and permissions.

Accessing the Kubernetes Dashboard:

To access the Dashboard, you may need to start a proxy server:

kubectl proxy
Then, access the Dashboard at: http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/.

Use the token generated for the admin user to log in (see dashboard-secret.yaml).

Deploy Apache Airflow:

You can deploy Apache Airflow using Helm or by applying custom YAML files. For Helm:

helm repo add apache-airflow https://airflow.apache.org
helm install airflow apache-airflow/airflow -f k8s/values.yaml
This will deploy Airflow with the settings defined in values.yaml.

Adding DAGs to Airflow:

Copy your DAG files (e.g., fetch_and_preview.py, hello.py) into the DAGs folder of your Airflow deployment. The method of copying depends on your Airflow setup (e.g., using Persistent Volume, Git-sync).

Usage
Kubernetes Dashboard: Use the Dashboard to monitor and manage the Kubernetes cluster.
Apache Airflow: Access the Airflow web UI to manage, schedule, and monitor workflows.

Useful Snippets
- Get the token to access the Kubernetes Dashboard (Windows/Bash)
kubectl -n kubernetes-dashboard create token admin-user 