# projetoMonitoring
Este projeto demonstra uma solução completa de observabilidade para servidores e aplicações. Ele permite monitorar tanto os recursos do servidor (CPU, RAM, disco, etc.) quanto métricas da aplicação (latência, erros de requisição) e métricas de negócio mais específicas.

Para isso, o projeto utiliza:

Node Exporter: coleta de métricas de recursos do servidor.

Prometheus: coleta e armazenamento das métricas em sua TSDB.

Prometheus Client (Python): instrumentação de uma aplicação simples para expor métricas customizadas.

Grafana: criação de dashboards variados para visualização completa do ambiente.

Alertmanager: envio de alertas via Telegram quando determinadas condições são atendidas, como alto uso de CPU ou aumento de erros na aplicação.

Docker & Docker Compose: containerização e orquestração de todos os serviços, garantindo fácil deploy e manutenção.

O resultado é um monitoramento completo, integrando métricas de infraestrutura, aplicação e negócio, com visualização intuitiva e alertas automatizados.
