# Deploy Manual no OpenShift

Este documento descreve como realizar o deploy manual da aplicação Flask no OpenShift utilizando os manifests YAML versionados no repositório.

O deploy manual representa a forma mais básica de publicar a aplicação no cluster, sem depender da execução da pipeline Tekton.

## Objetivo

O objetivo do deploy manual é validar se os manifests da aplicação estão corretos e se o OpenShift consegue criar todos os recursos necessários para executar e expor a aplicação.

Este processo é importante antes da automação via pipeline, pois garante que a base do deploy está funcionando corretamente.

## Estrutura dos manifests

Os arquivos utilizados no deploy manual estão localizados no diretório `openshift/`:

```bash
openshift/
├── deployment.yaml
├── service.yaml
└── route.yaml
```

## Recursos criados

### Deployment

O `Deployment` é responsável por criar e manter os Pods da aplicação Flask.

Ele define informações como:

- Nome da aplicação.
- Imagem container utilizada.
- Quantidade de réplicas.
- Porta exposta pelo container.
- Labels usadas para associação com o Service.

### Service

O `Service` expõe os Pods internamente dentro do cluster OpenShift.

Ele permite que outros recursos acessem a aplicação usando um endpoint interno estável, mesmo que os Pods sejam recriados.

### Route

A `Route` expõe a aplicação externamente.

Com ela, é possível acessar a aplicação pelo navegador ou via `curl`, utilizando uma URL gerada pelo OpenShift.

## Fluxo do deploy manual

```text
Manifests YAML
  ↓
oc apply
  ↓
Deployment
  ↓
Pod
  ↓
Service
  ↓
Route
  ↓
Aplicação acessível externamente
```

## Aplicando os manifests

Para aplicar todos os manifests do diretório `openshift/`, execute:

```bash
oc apply -f openshift/
```

Também é possível aplicar os arquivos individualmente:

```bash
oc apply -f openshift/deployment.yaml
oc apply -f openshift/service.yaml
oc apply -f openshift/route.yaml
```

## Validando o Deployment

```bash
oc get deployment
```

Exemplo de saída esperada:

```bash
NAME        READY   UP-TO-DATE   AVAILABLE   AGE
flask-app   1/1     1            1           2m
```

Para visualizar mais detalhes:

```bash
oc describe deployment flask-app
```

## Validando os Pods

```bash
oc get pods
```

Exemplo de saída esperada:

```bash
NAME                         READY   STATUS    RESTARTS   AGE
flask-app-xxxxxxxxxx-xxxxx    1/1     Running   0          1m
```

Caso o Pod ainda esteja subindo, o status pode aparecer como:

```bash
ContainerCreating
```

Caso ocorra algum erro, os status mais comuns são:

```bash
ImagePullBackOff
CrashLoopBackOff
Error
```

## Validando os logs da aplicação

```bash
oc logs deployment/flask-app
```

Ou diretamente pelo nome do Pod:

```bash
oc logs <nome-do-pod>
```

## Validando o Service

```bash
oc get svc
```

Exemplo de saída esperada:

```bash
NAME        TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
flask-app   ClusterIP   172.30.x.x      <none>        8080/TCP   2m
```

## Validando a Route

```bash
oc get route
```

Exemplo de saída esperada:

```bash
NAME        HOST/PORT                                      PATH   SERVICES    PORT   TERMINATION   WILDCARD
flask-app   flask-app-namespace.apps.cluster.example.com          flask-app   8080                 None
```

## Obtendo a URL da aplicação

```bash
oc get route flask-app -o jsonpath='{.spec.host}'
```

## Testando a aplicação

```bash
curl http://$(oc get route flask-app -o jsonpath='{.spec.host}')
```

Exemplo de retorno esperado:

```text
Hello from Flask running on OpenShift!
```

## Removendo os recursos

Caso seja necessário remover os recursos criados manualmente:

```bash
oc delete -f openshift/
```

## Resultado esperado

Ao final do deploy manual, a aplicação Flask deve estar:

- Com Pod em status `Running`.
- Com Service criado.
- Com Route criada.
- Acessível externamente pela URL gerada pelo OpenShift.

Este fluxo valida que a aplicação e os manifests estão funcionando antes da automação com Tekton Pipeline.
