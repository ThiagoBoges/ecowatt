# Projeto EcoWatt

## Identificação

Disciplina: Gestão de Projetos - UniFAP 2026.2  
Equipe: Integrante 1, Integrante 2 e Integrante 3 (preencher antes da entrega)  
ODS: ODS 7 - Energia Limpa e Acessível, meta 7.3

## Iniciação

### Problema e justificativa

Salas de instituições de ensino podem manter iluminação, computadores e ar-condicionado ligados além do necessário. Sem registro e comparação, o desperdício passa despercebido e eleva os custos. O EcoWatt centraliza dados simulados de consumo por sala, compara cada leitura com uma meta diária e avisa quando há excesso.

### Objetivo geral e objetivos específicos

Desenvolver um MVP web para acompanhar o consumo de energia de salas e identificar desperdícios. O sistema deve cadastrar salas e metas de consumo, registrar leituras simuladas, classificá-las como NORMAL ou EXCESSIVO e exibir alertas, relatório e economia potencial.

### Stakeholders

| Stakeholder | Interesse | Participação |
|---|---|---|
| Coordenação | Reduzir desperdício e custo | Validação |
| Responsáveis pelas salas | Receber alertas | Usuários |
| Equipe do projeto | Desenvolver e demonstrar | Execução |
| Comunidade acadêmica | Uso eficiente de energia | Beneficiada |

### Termo de Abertura

O EcoWatt criará, até a apresentação da disciplina, um sistema web de monitoramento com dados simulados. A entrega abrange API REST, banco PostgreSQL, dashboard, documentação e testes. O sucesso será demonstrado ao cadastrar uma sala, registrar 12 kWh para meta de 5 kWh e visualizar classificação EXCESSIVO com alerta.

## Planejamento

### Requisitos funcionais

1. Cadastrar, listar, consultar, atualizar e remover salas.
2. Registrar e consultar consumos por sala e por período.
3. Comparar consumo com a meta e classificar a situação.
4. Gerar e listar alertas de consumo excessivo.
5. Exibir relatório de consumo, excessos e economia estimada.

### Requisitos não funcionais

- API documentada automaticamente em `/docs`.
- Validação, tratamento de erros e testes automatizados.
- Interface responsiva e execução em contêineres.
- Dados simulados, sem dependência de sensores físicos.

### Escopo

Inclui cadastro de salas, leituras manuais simuladas, análise, alertas, relatório e dashboard. Não inclui sensores físicos, automação de equipamentos, integração com concessionária ou aplicativo móvel.

### EAP

1. Gestão: iniciação, planejamento, monitoramento e encerramento.
2. Produto: modelagem PostgreSQL, API FastAPI, dashboard React e testes.
3. Entrega: evidências da equipe, apresentação e demonstração.

### Cronograma e responsabilidades

| Período | Entrega | Responsável sugerido |
|---|---|---|
| 04 a 07/09 | Iniciação e requisitos | Integrante 1 |
| 08 a 13/09 | Modelagem e API | Integrante 2 |
| 14 a 18/09 | Dashboard e integração | Integrante 3 |
| 19 a 22/09 | Testes e documentação | Equipe |
| 23 a 24/09 | Revisão, evidências e ensaio | Equipe |
| 25/09 | Entrega e apresentação | Equipe |

### Recursos, custos e riscos

| Recurso | Custo estimado |
|---|---:|
| Computadores e internet próprios | R$ 0,00 |
| Python, React, PostgreSQL e GitHub | R$ 0,00 |
| Total | R$ 0,00 |

| Risco | Probabilidade | Resposta |
|---|---|---|
| Falta de disponibilidade da equipe | Média | Dividir tarefas e registrar reuniões |
| Erro de integração front-end e API | Média | Integrar cedo e usar endpoints simples |
| Falha do banco na demonstração | Baixa | Usar Docker e roteiro de inicialização |
| Dados de teste insuficientes | Média | Preparar cenários normal e excessivo |
| Atraso na documentação | Média | Atualizar esta documentação a cada entrega |

## Execução e Monitoramento

O repositório contém API FastAPI, modelos SQLAlchemy, interface React e configuração Docker. O registro cria alerta automaticamente quando o consumo supera a meta. A equipe deve anexar antes da entrega os commits, registros de reuniões e divisão real das tarefas, pois essas são evidências individuais que não podem ser inventadas.

| Atividade | Situação | Evidência |
|---|---|---|
| Requisitos e escopo | Concluída | README e este documento |
| API e banco | Concluída | Código e testes |
| Dashboard | Concluída | Demonstração local |
| Evidências dos três integrantes | Pendente | Commits, tarefas e reunião |
| Ensaio | Pendente | Roteiro da equipe |

Mudança registrada: o MVP usa dados simulados, conforme escopo, eliminando a dependência de sensores físicos.

## Testes e Validação

| Caso | Resultado esperado | Resultado obtido | Status |
|---|---|---|---|
| Cadastrar sala válida | Sala criada | Aprovado pelo teste automatizado | Aprovado |
| Registrar 12 kWh para meta 5 | EXCESSIVO e alerta | Aprovado pelo teste automatizado | Aprovado |
| Registrar 8 kWh para meta 8 | NORMAL e sem alerta | Aprovado pelo teste automatizado | Aprovado |
| Informar consumo zero | API recusa entrada | Aprovado pelo teste automatizado | Aprovado |
| Consultar relatório | Total, excesso e economia | Aprovado pelo teste automatizado | Aprovado |

## ODS e impacto

O EcoWatt se relaciona à ODS 7, meta 7.3, pois identifica consumo acima da meta e orienta ações de eficiência. O indicador mensurável é a economia estimada em kWh, calculada pela soma dos excessos. No cenário de 12 kWh para uma meta de 5 kWh, o indicador aponta 7 kWh de economia potencial.

## Encerramento e lições aprendidas

O escopo realizado inclui as funcionalidades previstas no MVP. A equipe deve atualizar o cronograma e a divisão de responsabilidades com as datas reais. Não houve custo financeiro estimado. Lições aprendidas: definir o MVP cedo reduz retrabalho, regras de negócio isoladas facilitam testes e evidências de equipe precisam ser registradas durante o processo.
