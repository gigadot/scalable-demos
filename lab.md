### The Kubernetes Lab
```
kubectl run nginx --image=nginx --port=80; watch kubectl get pods -o wide
kubectl expose pod/nginx --type=LoadBalancer
kubectl get pods -o wide
kubectl port-forward svc/nginx 8080:80
kubectl exec -it nginx -- bash

kubectl delete po/nginx
kubectl delete svc/nginx
```
**Exercise:** try changing the content of the html page while the pod is running.

```
kubectl run alpine --image=alpine --restart=Never --rm -it -- /bin/sh
```

**Pause container case study:** creating a combined mysql and wordpress docker containers -
```
docker run --rm -d --ipc=shareable --name pause -p 8080:80 registry.k8s.io/pause:3.9
docker run --rm -d --name mysql -e MYSQL_DATABASE=wp -e MYSQL_USER=wp -e MYSQL_PASSWORD=pass -e MYSQL_RANDOM_ROOT_PASSWORD=1 --net=container:pause --ipc=container:pause --pid=container:pause mysql:8
docker run --rm -d --name wordpress -e WORDPRESS_DB_HOST="127.0.0.1" -e WORDPRESS_DB_USER=wp -e WORDPRESS_DB_PASSWORD=pass -e WORDPRESS_DB_NAME=wp --net=container:pause --ipc=container:pause --pid=container:pause wordpress:6.1.1
```
Connect to http://localhost:8080

To clean up:
```
docker stop pause mysql wordpress
```
