## Dummy API

### Run

```
docker build -t dummy-example .      
docker run dummy-example -p 8080:8080
```

### Push to Container Registry

```
docker tag <SOURCE_IMAGE> <HOSTNAME>/<PROJECT-ID>/<IMAGE>:<TAG>
docker push <HOSTNAME>/<PROJECT-ID>/<IMAGE>:<TAG>
```
