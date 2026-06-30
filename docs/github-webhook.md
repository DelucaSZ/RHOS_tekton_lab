# Fase 6 — Configurar GitHub Webhook

Nesta fase foi configurada a integração entre o GitHub e o OpenShift por meio de um Webhook apontando para o Tekton EventListener.

Como o ambiente utilizado é local, a Route do EventListener não fica acessível diretamente pela internet. Para permitir que o GitHub enviasse eventos para o laboratório, foi utilizado o ngrok como túnel público temporário, encaminhando as requisições para o Service do EventListener via `oc port-forward`.

## Configuração realizada

- Webhook criado no repositório GitHub.
- Evento configurado: `push`.
- Content type configurado como `application/json`.
- Secret configurado no GitHub e no OpenShift.
- EventListener exposto localmente via `oc port-forward`.
- URL pública temporária criada com ngrok.
- Entrega do webhook validada com sucesso.

## Fluxo validado

1. Um push foi realizado na branch `main`.
2. O GitHub enviou o evento para a URL pública do ngrok.
3. O ngrok encaminhou a requisição para o EventListener no OpenShift local.
4. O EventListener processou o evento.
5. O TriggerTemplate criou automaticamente um PipelineRun.
6. A pipeline executou o build e deploy da aplicação.

## Evidência

PipelineRun criado automaticamente pelo webhook:

```text
flask-app-github-run-sw5cb   True   Succeeded
