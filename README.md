# EcoWatt

MVP acadêmico para a disciplina Gestão de Projetos da UniFAP. O EcoWatt registra consumos simulados de energia em salas, compara cada leitura com a meta cadastrada, gera alertas e apresenta economia potencial no dashboard.

## Tecnologias

- Backend: Python e FastAPI
- Frontend: JavaScript, React e Chart.js
- Banco: PostgreSQL e SQLAlchemy
- Interface: HTML e CSS
- Ambiente: Docker Compose

## Como executar

1. Instale Docker Desktop.
2. Na raiz do projeto, execute `docker compose up --build`.
3. Abra `http://localhost:5173` para o dashboard.
4. Abra `http://localhost:8000/docs` para a documentação interativa da API.

Para execução sem Docker, instale as dependências de `backend/requirements.txt`, defina `DATABASE_URL` e rode `uvicorn app.main:app --reload` dentro de `backend`. No front-end, rode `npm install` e `npm run dev` dentro de `frontend`.

## Testes

```bash
cd backend
pytest
```

Os testes cobrem cadastro de sala, consumo excessivo, alerta, consumo normal, validação, filtros, consulta de alerta e atualização de sala.

## Entregáveis da disciplina

O documento de iniciação, planejamento, monitoramento, testes, ODS e encerramento está em [docs/PROJETO.md](docs/PROJETO.md). O roteiro de apresentação está em [docs/ROTEIRO_APRESENTACAO.md](docs/ROTEIRO_APRESENTACAO.md) e o modelo para evidências em [docs/EVIDENCIAS_EQUIPE.md](docs/EVIDENCIAS_EQUIPE.md). Antes da entrega, a equipe deve preencher seus nomes e anexar evidências reais de participação, como histórico de commits e registros de reuniões.

## Contexto do projeto

O EcoWatt é um projeto acadêmico de Tecnologia da Informação da disciplina
Gestão de Projetos da UniFAP.

O projeto busca solucionar o problema do desperdício de energia em salas,
setores e prédios.

O sistema deverá permitir o monitoramento do consumo de energia, identificar
consumo acima do esperado, gerar alertas e apresentar informações em um
dashboard.

## Problema

Em universidades, escolas, empresas e prédios públicos existem situações em
que ar-condicionado, iluminação, computadores e outros equipamentos permanecem
ligados sem necessidade.

Isso pode gerar desperdício de energia e aumento dos custos.

## Solução

Criar um sistema web chamado EcoWatt capaz de:

- cadastrar salas ou setores;
- registrar consumo de energia;
- consultar consumo;
- definir consumo esperado;
- comparar consumo esperado com consumo registrado;
- identificar consumo excessivo;
- gerar alertas;
- disponibilizar dados para dashboard;
- gerar relatórios;
- calcular economia estimada.

## Exemplo principal

Uma sala normalmente consome 5 kWh por dia.

Em determinado dia foi registrado consumo de 12 kWh.

O sistema deve identificar que o consumo está acima do esperado e gerar um
alerta para o responsável.

## ODS

ODS 7 — Energia Limpa e Acessível.

O projeto está relacionado principalmente à melhoria da eficiência energética.

A meta relacionada é a ODS 7.3.

## MVP

O MVP deve ser simples e funcional.

Não é necessário implementar sensores físicos reais nesta primeira versão.

Pode utilizar dados simulados de consumo.

O MVP deve conter:

1. cadastro de salas;
2. cadastro/registro de consumo;
3. consumo esperado;
4. comparação esperado x realizado;
5. identificação de consumo excessivo;
6. alertas;
7. dashboard;
8. relatório básico.

## Escopo fora do MVP

Não implementar inicialmente:

- sensores físicos reais;
- controle automático de ar-condicionado;
- desligamento automático de equipamentos;
- integração com concessionária de energia;
- aplicativo mobile completo.

## Backend

O backend deve ser desenvolvido como uma API REST.

Tecnologia preferencial:

- Python
- FastAPI
- PostgreSQL

Utilizar arquitetura organizada e simples, adequada a um projeto acadêmico.

## Funcionalidades da API

A API deverá possuir inicialmente:

### Salas

- criar sala;
- listar salas;
- consultar sala;
- atualizar sala;
- remover sala.

### Consumo

- registrar consumo;
- listar consumo;
- consultar consumo por sala;
- consultar consumo por período.

### Análise

- calcular/comparar consumo esperado;
- identificar consumo excessivo;
- classificar situação como NORMAL ou EXCESSIVO.

### Alertas

- gerar alerta automaticamente quando o consumo ultrapassar
  o limite definido;
- listar alertas;
- consultar alerta.

### Relatórios

- consumo por sala;
- consumo por período;
- consumo total;
- consumo excessivo;
- economia estimada.

## Regras de negócio

Exemplo:

consumo esperado = 5 kWh

consumo registrado = 12 kWh

O sistema deve marcar o consumo como EXCESSIVO.

As regras de negócio devem ficar isoladas e ser fáceis de testar.

## Qualidade

Priorizar:

- código simples;
- organização;
- validação dos dados;
- tratamento de erros;
- documentação da API;
- testes automatizados;
- README atualizado.

## Processo

Antes de implementar grandes funcionalidades:

1. analisar a estrutura atual do projeto;
2. verificar arquivos existentes;
3. propor alterações;
4. implementar;
5. executar testes;
6. corrigir problemas;
7. documentar o que foi feito.

Não criar funcionalidades fora do escopo sem necessidade.
