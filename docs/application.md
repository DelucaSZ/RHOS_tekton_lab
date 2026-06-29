# Aplicação Flask

Este projeto utiliza uma aplicação simples em Flask como workload principal do laboratório de CI/CD com OpenShift e Tekton.

A aplicação está localizada no diretório `app/` e serve como base para validar o fluxo completo de build, publicação de imagem e deploy automatizado no OpenShift.

## Objetivo da aplicação

O objetivo da aplicação é fornecer um serviço HTTP simples para demonstrar, de forma prática, o funcionamento de uma esteira CI/CD em ambiente Kubernetes/OpenShift.

A aplicação permite validar:

- Build de imagem container.
- Execução da aplicação em Pod.
- Exposição interna via Service.
- Exposição externa via Route.
- Deploy manual via manifests YAML.
- Deploy automatizado via Tekton Pipeline.

## Estrutura da aplicação

```bash
app/
├── app.py
├── requirements.txt
└── Dockerfile
```

## Arquivos principais

### `app.py`

Arquivo principal da aplicação Flask.

Ele contém a lógica da aplicação web, define as rotas HTTP e inicia o servidor Flask dentro do container.

### `requirements.txt`

Arquivo responsável por listar as dependências Python necessárias para executar a aplicação.

Exemplo:

```txt
flask
```

### `Dockerfile`

Arquivo utilizado para construir a imagem container da aplicação.

Ele define a imagem base, copia os arquivos da aplicação, instala as dependências e configura o comando de inicialização do Flask.

## Fluxo básico da aplicação

Após o deploy no OpenShift, a aplicação funciona no seguinte fluxo:

```text
Usuário
  ↓
OpenShift Route
  ↓
Service
  ↓
Pod
  ↓
Container Flask
```

## Exposição da aplicação

A aplicação é executada dentro de um Pod no OpenShift.

Para permitir o acesso, são utilizados três recursos principais:

- `Deployment`: controla a criação e atualização dos Pods.
- `Service`: expõe os Pods internamente no cluster.
- `Route`: expõe a aplicação externamente para acesso via navegador ou `curl`.

## Objetivo dentro do laboratório

Dentro deste laboratório, a aplicação Flask não tem como foco a regra de negócio em si, mas sim servir como uma aplicação simples e funcional para demonstrar práticas de DevOps, CI/CD e automação de deploy em OpenShift.

Ela representa uma aplicação real em formato reduzido, permitindo testar o ciclo completo:

```text
Código-fonte → Build da imagem → Push no registry → Deploy no OpenShift → Acesso via Route
```

## Validação esperada

Após o deploy, a aplicação deve estar acessível pela Route criada no OpenShift.

Exemplo de teste:

```bash
curl http://$(oc get route flask-app -o jsonpath='{.spec.host}')
```

Exemplo de retorno esperado:

```text
Hello from Flask running on OpenShift!
```
