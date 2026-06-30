# Troubleshooting

Este documento registra problemas encontrados durante a construção do laboratório e as ações aplicadas para correção.

---

## 1. PipelineRun com erro `InvalidWorkspaceBindings`

### Contexto

Durante o teste do fluxo automatizado via GitHub Webhook, o evento de `push` foi recebido corretamente pelo Tekton Trigger, porém o `PipelineRun` criado automaticamente falhou logo após sua criação.

A falha ocorreu no primeiro teste automatizado gerado pelo webhook:

```bash
oc get pipelinerun
```

Saída observada:

```text
NAME                         SUCCEEDED   REASON                     STARTTIME   COMPLETIONTIME
flask-app-github-run-2z7q7   False       InvalidWorkspaceBindings   12m         12m
flask-app-github-run-sw5cb   True        Succeeded                  9m29s       7m26s
flask-app-github-run-z6ch4   True        Succeeded                  3m57s       2m5s
flask-app-manual-run-77qsv   True        Succeeded                  67m         65m
flask-app-manual-run-zv6p6   True        Succeeded                  63m         60m
flask-build-run-6txwh        True        Succeeded                  4d22h       4d22h
```

Também foi validado o histórico ordenado por data de criação:

```bash
oc get pipelinerun --sort-by=.metadata.creationTimestamp
```

Saída observada:

```text
NAME                         SUCCEEDED   REASON                     STARTTIME   COMPLETIONTIME
flask-build-run-vw8hv        False       Failed                     4d22h       4d22h
flask-build-run-gk95n        False       Failed                     4d22h       4d22h
flask-build-run-kj799        False       Failed                     4d22h       4d22h
flask-build-run-6txwh        True        Succeeded                  4d22h       4d22h
flask-app-manual-run-77qsv   True        Succeeded                  66m         64m
flask-app-manual-run-zv6p6   True        Succeeded                  62m         60m
flask-app-github-run-2z7q7   False       InvalidWorkspaceBindings   11m         11m
flask-app-github-run-sw5cb   True        Succeeded                  8m49s       6m46s
flask-app-github-run-z6ch4   True        Succeeded                  3m17s       85s
```

---

### Sintoma

O `PipelineRun` era criado automaticamente pelo webhook, mas não iniciava corretamente a execução das Tasks.

O erro retornado foi:

```text
InvalidWorkspaceBindings
```

---

### Causa

A Pipeline utilizava workspace compartilhado entre as Tasks, porém o `PipelineRun` criado automaticamente pelo `TriggerTemplate` não estava com o binding de workspace corretamente definido.

Em Tekton, quando uma Pipeline declara um workspace obrigatório, todo `PipelineRun` precisa informar como esse workspace será montado, seja por `emptyDir`, `PersistentVolumeClaim`, `ConfigMap`, `Secret` ou outro tipo suportado.

Como o `PipelineRun` manual já funcionava, o problema não estava na Pipeline em si, mas sim na forma como o `TriggerTemplate` estava criando o `PipelineRun` automático.

---

### Correção aplicada

O `TriggerTemplate` foi ajustado para gerar um `PipelineRun` com o workspace esperado pela Pipeline.

Após o ajuste, o manifesto foi reaplicado:

```bash
oc apply -f tekton/triggers/triggertemplate.yaml
```

Em seguida, um novo teste foi realizado via `git push`, disparando novamente o GitHub Webhook.

---

### Validação

Após a correção, novos `PipelineRuns` automáticos foram criados e concluídos com sucesso:

```text
NAME                         SUCCEEDED   REASON
flask-app-github-run-sw5cb   True        Succeeded
flask-app-github-run-z6ch4   True        Succeeded
```

Também foram criados pods para cada etapa da Pipeline:

```text
flask-app-github-run-z6ch4-clone-repository-pod       Completed
flask-app-github-run-z6ch4-build-and-push-image-pod   Completed
flask-app-github-run-z6ch4-deploy-to-openshift-pod    Completed
```

---

### Aprendizado

O teste manual da Pipeline ajudou a isolar o problema.

Como o `PipelineRun` manual executava corretamente, foi possível identificar que a falha estava na camada de Trigger, mais especificamente no `TriggerTemplate` responsável por gerar o `PipelineRun` automático.

Esse tipo de erro reforça a importância de validar separadamente:

1. Tasks
2. Pipeline
3. PipelineRun manual
4. TriggerBinding
5. TriggerTemplate
6. EventListener
7. Webhook externo

