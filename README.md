
**Requirement sebuah aplikasi :**
```
.
├── app.py
├── config.py
└── requirements.txt
```

## duck@duck:~$ app.py :
```
from flask import Flask

import config

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
```

## duck@duck:~$ config.py :
```
from os import environ as env
import multiprocessing

PORT = int(env.get("PORT", 8080))
DEBUG_MODE = int(env.get("DEBUG_MODE", 1))

#Gunicorn config
bind = ":" + str(PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()
```


## duck@duck:~$ nano requirements.txt :
```
Click==7.0
Flask==1.0.2
gunicorn==19.9.0
itsdangerous==1.1.0
Jinja2==2.10
MarkupSafe==1.1.0
Werkzeug==0.14.1
```


## duck@duck:~$ nano Dockerfile :
```
FROM python:3.6-jessie

RUN apt update

WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app

ENV PORT 8080
CMD ["gunicorn", "app:app", "--config=config.py"]
```

## duck@duck:~$ nano deployment.yaml :
```
apiVersion: v1
kind: Service
metadata:
  name: flaskapp
  namespace: taufik-devops
  labels:
    app: flaskapp
spec:
  type: ClusterIP
  ports:
  - port: 80
    targetPort: 8080
  selector:
    app: flaskapp
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flaskapp
  namespace: taufik-devops
  labels:
    app: flaskapp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: flaskapp
  template:
    metadata:
      name: flaskapp
      labels:
        app: flaskapp
    spec:
      containers:
        - name: flaskapp
          image: happyduck/flaskapp:latest
          ports:
            - containerPort: 8080
          resources:
            requests:
              memory: 256Mi
            limits:
              memory: 512Mi
          env:
            - name: DEBUG_MODE
              value: "1"
```

## duck@duck:~$ nano ingress-flask.yaml :
```
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ingress-flask
  namespace: taufik-devops
  annotations:
    kubernetes.io/ingress.class: nginx
    certmanager.k8s.io/cluster-issuer: letsencrypt-dev2
    #nginx.ingress.kubernetes.io/client_max_body_size: "50m"
    #ingress.kubernetes.io/client_max_body_size: "50m"
    ingress.kubernetes.io/proxy-body-size: "50m"
    #nginx.org/client-max-body-size: "50m"
    nginx.ingress.kubernetes.io/proxy-body-size: "50m"
    #nginx.ingress.kubernetes.io/configuration-snippet: |
    #more_set_headers "X‐Frame‐Options: SAMEORIGIN";
spec:
  tls:
  - hosts:
    - taufik.worklifebeyond.com
    #host nya sesuaikan dengan host/domain yang diinginkan
    secretName: letsencrypt-dev2-new-2020-2
    #secret name nya dibedakan selalu
  rules:
  - host: taufik.worklifebeyond.com
    http:
      paths:
      - backend:
          serviceName: flaskapp
          servicePort: 80
```

## Cloud Flare :
```
taufik.worklifebeyond.com point to 163.47.10.224.

Type    Name*   IPv4 address*    TTL    Proxy Status
-----|--------|---------------|------|------------------|
  A    taufik   163.47.10.224   Auto   DNS only (click)
-----|--------|---------------|------|------------------|
```


## Command Penting :
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




