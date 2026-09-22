# Publicação no Vercel

O EcoWatt utiliza dois projetos Vercel e um PostgreSQL gerenciado. Essa estrutura elimina a necessidade de manter Docker aberto no computador.

## 1. Banco PostgreSQL

No painel da Vercel, crie uma integração de PostgreSQL pelo Marketplace, como Neon ou Supabase. Copie a URL de conexão compatível com SQLAlchemy, no formato `postgresql+psycopg://...`.

## 2. API

Importe este mesmo repositório como um novo projeto Vercel e selecione `backend` como Root Directory. Em Settings, adicione:

| Variável | Valor |
|---|---|
| `DATABASE_URL` | URL do PostgreSQL gerenciado |
| `CORS_ORIGINS` | URL final do dashboard Vercel |

O Vercel encontrará `backend/api/index.py` e publicará a API. Após o deploy, valide `https://URL-DA-API/health`.

## 3. Dashboard

Importe novamente o repositório como outro projeto Vercel e selecione `frontend` como Root Directory. Adicione:

| Variável | Valor |
|---|---|
| `VITE_API_URL` | `https://URL-DA-API.vercel.app/api/v1` |

O Vercel identifica o Vite e executa `npm run build`. Copie a URL do dashboard e atualize `CORS_ORIGINS` no projeto da API. Faça um novo deploy da API após essa alteração.

## Verificação

Abra o dashboard, cadastre uma sala e registre uma leitura. Uma leitura maior que a meta deve aparecer como `EXCESSIVO` e criar um alerta.
