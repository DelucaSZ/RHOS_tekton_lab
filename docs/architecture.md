# Arquitetura do Projeto

Este documento descreve a arquitetura do laboratório de CI/CD utilizando OpenShift, Tekton e GitHub.

## Componentes

- GitHub Repository
- GitHub Webhook
- Tekton EventListener
- Tekton TriggerBinding
- Tekton TriggerTemplate
- Tekton Pipeline
- Tekton PipelineRun
- Container Registry
- OpenShift Deployment
- OpenShift Service
- OpenShift Route

## Fluxo atual

Neste primeiro momento, o pipeline é executado manualmente através de um PipelineRun.

```text
Desenvolvedor
     |
     v
PipelineRun manual
     |
     v
Tekton Pipeline
     |
     +--> Clone do repositório
     +--> Build da imagem
     +--> Push da imagem
     +--> Deploy no OpenShift
```

## Fluxo final esperado

Ao final do laboratório, o fluxo será automatizado através de webhook do GitHub.

```text
GitHub Push
     |
     v
GitHub Webhook
     |
     v
OpenShift Route do EventListener
     |
     v
Tekton EventListener
     |
     v
TriggerBinding + TriggerTemplate
     |
     v
PipelineRun automático
     |
     v
Build + Push + Deploy
```

## Objetivo arquitetural

O objetivo é demonstrar um fluxo CI/CD completo, onde uma alteração no código-fonte inicia automaticamente o processo de build e deploy da aplicação no OpenShift.
