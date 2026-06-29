# Comandos `oc` utilizados no laboratório

Este documento centraliza os principais comandos `oc` utilizados durante o laboratório de OpenShift com Tekton Pipelines.

O objetivo é manter um guia operacional simples para consulta, validação e troubleshooting do ambiente.

## Verificar projeto atual

```bash
oc project
```

Este comando mostra em qual projeto/namespace o usuário está trabalhando no momento.

## Listar projetos disponíveis

```bash
oc get projects
```

## Selecionar um projeto

```bash
oc project <nome-do-projeto>
```

Exemplo:

```bash
oc project tekton-lab
```

## Listar todos os recursos principais

```bash
oc get all
```

## Aplicar manifests do OpenShift

```bash
oc apply -f openshift/
```

Também é possível aplicar arquivos específicos:

```bash
oc apply -f openshift/deployment.yaml
oc apply -f openshift/service.yaml
oc apply -f openshift/route.yaml
```

## Remover manifests do OpenShift

```bash
oc delete -f openshift/
```

## Listar Deployments

```bash
oc get deployment
```

## Descrever um Deployment

```bash
oc describe deployment flask-app
```

## Acompanhar rollout do Deployment

```bash
oc rollout status deployment/flask-app
```

## Reiniciar rollout do Deployment

```bash
oc rollout restart deployment/flask-app
```

## Listar Pods

```bash
oc get pods
```

## Listar Pods com mais detalhes

```bash
oc get pods -o wide
```

## Descrever um Pod

```bash
oc describe pod <nome-do-pod>
```

## Ver logs da aplicação

```bash
oc logs deployment/flask-app
```

Ou diretamente pelo Pod:

```bash
oc logs <nome-do-pod>
```

## Acompanhar logs em tempo real

```bash
oc logs deployment/flask-app -f
```

## Listar Services

```bash
oc get svc
```

## Descrever um Service

```bash
oc describe svc flask-app
```

## Listar Routes

```bash
oc get route
```

## Descrever uma Route

```bash
oc describe route flask-app
```

## Obter somente o host da Route

```bash
oc get route flask-app -o jsonpath='{.spec.host}'
```

## Testar aplicação via curl

```bash
curl http://$(oc get route flask-app -o jsonpath='{.spec.host}')
```

## Listar Tasks Tekton

```bash
oc get tasks
```

## Listar Pipelines Tekton

```bash
oc get pipelines
```

## Listar PipelineRuns

```bash
oc get pipelineruns
```

## Listar TaskRuns

```bash
oc get taskruns
```

## Criar uma PipelineRun

```bash
oc create -f tekton/pipelineruns/pipelinerun.yaml
```

## Aplicar definição da Pipeline

```bash
oc apply -f tekton/pipelines/pipeline.yaml
```

## Aplicar Tasks

```bash
oc apply -f tekton/tasks/
```

## Ver detalhes de uma PipelineRun

```bash
oc describe pipelinerun <nome-da-pipelinerun>
```

## Ver detalhes de uma TaskRun

```bash
oc describe taskrun <nome-da-taskrun>
```

## Ver Pods criados pela pipeline

```bash
oc get pods
```

Exemplo de Pods relacionados à execução da pipeline:

```bash
NAME                                                   READY   STATUS      RESTARTS   AGE
flask-build-run-xxxxx-clone-repository-pod             0/1     Completed   0          4m
flask-build-run-xxxxx-build-and-push-pod               0/1     Completed   0          3m
flask-app-xxxxxxxxxx-xxxxx                             1/1     Running     0          2m
```

## Ver logs de um Pod da pipeline

```bash
oc logs <nome-do-pod>
```

## Ver logs da PipelineRun usando Tekton CLI

```bash
tkn pipelinerun logs <nome-da-pipelinerun> -f
```

Exemplo:

```bash
tkn pipelinerun logs flask-build-run -f
```

## Remover uma PipelineRun

```bash
oc delete pipelinerun <nome-da-pipelinerun>
```

## Remover todas as PipelineRuns

```bash
oc delete pipelinerun --all
```

## Remover todas as TaskRuns

```bash
oc delete taskrun --all
```

## Ver eventos do namespace

```bash
oc get events --sort-by=.metadata.creationTimestamp
```

## Ver informações do usuário logado

```bash
oc whoami
```

## Ver URL da console web

```bash
oc whoami --show-console
```

## Resultado esperado

Com estes comandos é possível:

- Aplicar os manifests da aplicação.
- Validar recursos criados no OpenShift.
- Acompanhar Pods, Services e Routes.
- Executar e validar PipelineRuns.
- Consultar logs para troubleshooting.
- Remover recursos quando necessário.
