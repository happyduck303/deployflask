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


kubectl logs -f cert-manager-7d8fb9ccd7-t8t2c -n cert-manager | grep "taufik"
kubectl logs -f flaskapp-5dff57ff87-pfg9t -n taufik-devops | grep 'taufik'


kubectl describe ingress ingress-flask -n taufik-devops
kubectl describe service flaskapp -n taufik-devops
```


