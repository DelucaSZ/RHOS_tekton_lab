# OpenShift Flask CI/CD Lab

Este repositório documenta um laboratório prático de CI/CD utilizando OpenShift, Tekton Pipelines e uma aplicação simples em Python Flask.

O objetivo do projeto é demonstrar, de ponta a ponta, como uma aplicação pode ser versionada, construída em imagem container, publicada em um registry e implantada automaticamente no OpenShift.

## Objetivo

Construir um fluxo completo de CI/CD em ambiente OpenShift, evoluindo de uma execução manual com Tekton até um fluxo automatizado com GitHub Webhook, Tekton Triggers, build da imagem e deploy automático da aplicação.

## Arquitetura inicial

```text
GitHub Repository
        |
        v
Tekton Pipeline
        |
        +--> Clone do código-fonte
        |
        +--> Build da imagem container
        |
        +--> Push da imagem para registry
        |
        +--> Deploy no OpenShift
        |
        v
Aplicação Flask exposta via Route
```

## Arquitetura desejada

```text
GitHub Push
        |
        v
GitHub Webhook
        |
        v
Tekton Trigger / EventListener
        |
        v
Tekton PipelineRun
        |
        v
Build + Push + Deploy
        |
        v
Aplicação atualizada no OpenShift
```

## Estrutura do repositório

```text
.
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── openshift/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── route.yaml
│
├── tekton/
│   ├── tasks/
│   ├── pipelines/
│   ├── pipelineruns/
│   └── triggers/
│
├── docs/
│   └── architecture.md
│
└── README.md
```

## Diretórios

### app

Contém o código-fonte da aplicação Flask e os arquivos necessários para criação da imagem container.

### openshift

Contém os manifests Kubernetes/OpenShift responsáveis por criar os objetos da aplicação, como Deployment, Service e Route.

### tekton

Contém os objetos relacionados ao pipeline CI/CD, como Tasks, Pipelines, PipelineRuns e, futuramente, Triggers.

### docs

Contém documentação complementar do projeto, incluindo arquitetura, diagramas e explicações técnicas.

## Tecnologias utilizadas

- OpenShift
- Kubernetes
- Tekton Pipelines
- Tekton Triggers
- Python Flask
- GitHub Webhook
- Container Image Build
- OpenShift Route

## Fases do projeto

### Fase 1 — Organização do repositório

- Criar estrutura de pastas do projeto
- Separar aplicação Flask em `/app`
- Separar manifests Kubernetes/OpenShift em `/openshift`
- Separar objetos Tekton em `/tekton`
- Criar pasta `/docs`
- Criar README inicial

### Fase 2 — Documentação da arquitetura

- Criar diagrama da arquitetura
- Documentar o fluxo atual do pipeline
- Documentar os objetos utilizados no OpenShift e Tekton

### Fase 3 — Ajuste do pipeline

- Ajustar paths do Dockerfile e contexto de build
- Validar execução do PipelineRun
- Garantir build e deploy da aplicação

### Fase 4 — Integração com GitHub Webhook

- Criar Tekton Trigger
- Criar EventListener
- Criar TriggerTemplate
- Criar TriggerBinding
- Expor EventListener via Route

### Fase 5 — Deploy automático

- Configurar webhook no GitHub
- Executar pipeline automaticamente após push
- Validar atualização automática da aplicação no OpenShift

## Status atual

Fase atual: Fase 1 — Organização do repositório.

## Resultado esperado

Ao final deste laboratório, o repositório deverá demonstrar um fluxo CI/CD funcional com OpenShift e Tekton, permitindo que alterações realizadas no GitHub iniciem automaticamente o processo de build e deploy da aplicação.
