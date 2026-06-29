# Evidências do laboratório

Este diretório armazena prints e exemplos de saída utilizados para comprovar o funcionamento da aplicação Flask, do deploy no OpenShift e da pipeline Tekton.

As evidências servem para documentar visualmente o progresso do laboratório e facilitar a apresentação do projeto no GitHub e no LinkedIn.

## Objetivo

O objetivo deste diretório é centralizar prints e saídas importantes, como:

- Aplicação rodando no OpenShift.
- Pods em execução.
- Service criado.
- Route criada.
- Aplicação acessível via navegador.
- PipelineRun executada com sucesso.
- Logs da pipeline.

## Cuidados antes de publicar prints

Antes de adicionar prints no repositório público, valide se não existem informações sensíveis, como:

- Tokens.
- Senhas.
- Chaves de acesso.
- IPs privados sensíveis.
- URLs internas corporativas.
- Nome de usuário corporativo.
- Dados de registry privado.
- Informações de cluster que não devem ser expostas.

Caso necessário, edite ou oculte essas informações antes de publicar.

---

# Evidências sugeridas

## 1. Projeto/namespace utilizado

Comando:

```bash
oc project
```

Exemplo de saída:

```bash
Using project "tekton-lab" on server "https://api.cluster.example.com:6443".
```

Print sugerido:

```bash
docs/evidences/namespace.png
```

---

## 2. Recursos da aplicação criados

Comando:

```bash
oc get all
```

Exemplo de saída:

```bash
NAME                             READY   STATUS    RESTARTS   AGE
pod/flask-app-xxxxxxxxxx-xxxxx   1/1     Running   0          2m

NAME                TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/flask-app   ClusterIP   172.30.x.x      <none>        8080/TCP   2m

NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/flask-app   1/1     1            1           2m
```

Print sugerido:

```bash
docs/evidences/resources-created.png
```

---

## 3. Pod da aplicação em execução

Comando:

```bash
oc get pods
```

Exemplo de saída:

```bash
NAME                         READY   STATUS    RESTARTS   AGE
flask-app-xxxxxxxxxx-xxxxx    1/1     Running   0          1m
```

Print sugerido:

```bash
docs/evidences/app-running.png
```

---

## 4. Logs da aplicação

Comando:

```bash
oc logs deployment/flask-app
```

Exemplo de saída:

```bash
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:8080
* Running on http://10.x.x.x:8080
```

Print sugerido:

```bash
docs/evidences/app-logs.png
```

---

## 5. Service criado

Comando:

```bash
oc get svc
```

Exemplo de saída:

```bash
NAME        TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
flask-app   ClusterIP   172.30.x.x      <none>        8080/TCP   2m
```

Print sugerido:

```bash
docs/evidences/service-created.png
```

---

## 6. Route criada

Comando:

```bash
oc get route
```

Exemplo de saída:

```bash
NAME        HOST/PORT                                      PATH   SERVICES    PORT   TERMINATION   WILDCARD
flask-app   flask-app-namespace.apps.cluster.example.com          flask-app   8080                 None
```

Print sugerido:

```bash
docs/evidences/route-created.png
```

---

## 7. Aplicação acessível via navegador

Acessar a URL da Route no navegador.

Comando para obter a URL:

```bash
oc get route flask-app -o jsonpath='{.spec.host}'
```

Teste via terminal:

```bash
curl http://$(oc get route flask-app -o jsonpath='{.spec.host}')
```

Exemplo de retorno:

```bash
Hello from Flask running on OpenShift!
```

Print sugerido:

```bash
docs/evidences/route-access.png
```

---

## 8. PipelineRun criada

Comando:

```bash
oc get pipelineruns
```

Exemplo de saída:

```bash
NAME              SUCCEEDED   REASON      STARTTIME   COMPLETIONTIME
flask-build-run   True        Succeeded   5m          2m
```

Print sugerido:

```bash
docs/evidences/pipeline-run.png
```

---

## 9. TaskRuns da pipeline

Comando:

```bash
oc get taskruns
```

Exemplo de saída:

```bash
NAME                                      SUCCEEDED   REASON      STARTTIME   COMPLETIONTIME
flask-build-run-clone-repository          True        Succeeded   5m          4m
flask-build-run-build-and-push            True        Succeeded   4m          2m
```

Print sugerido:

```bash
docs/evidences/taskruns.png
```

---

## 10. Logs da PipelineRun

Comando:

```bash
tkn pipelinerun logs <nome-da-pipelinerun> -f
```

Exemplo:

```bash
tkn pipelinerun logs flask-build-run -f
```

Print sugerido:

```bash
docs/evidences/pipeline-logs.png
```

---

# Lista final de evidências recomendadas

```bash
docs/evidences/
├── namespace.png
├── resources-created.png
├── app-running.png
├── app-logs.png
├── service-created.png
├── route-created.png
├── route-access.png
├── pipeline-run.png
├── taskruns.png
└── pipeline-logs.png
```

## Resultado esperado

Com essas evidências, o repositório passa a demonstrar não apenas os arquivos YAML do laboratório, mas também a execução prática do fluxo no OpenShift.

Isso fortalece a documentação técnica e facilita a apresentação do projeto como um case real de CI/CD com OpenShift e Tekton.
