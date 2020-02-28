**Command penting**
```

docker build -t happyduck/flaskapp .
docker push happyduck/flaskapp:latest


kubectl apply -f deployment.yaml
kubectl apply -f ingress-flask.yaml


kubectl get pods -n taufik-devops
kubectl get pods -n cert-manager
kubectl get svc -n taufik-devops
kubectl get deploy -n taufik-devops
kubectl get ingress -n taufik-devops


kubectl delete deployment flaskapp -n taufik-devops
kubectl delete ingress ingress-flask -n taufik-devops
```


