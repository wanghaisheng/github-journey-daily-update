---
author: Bob Johnson
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Backend for dval.in. Stores user data and handles communication with Hoyoverse'
featured: true
keywords: {"id":"0193e85db5541e63d2a8cb19afff99dc","object":"chat.completion","created":1734770275,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Based on the provided text, here are the keywords and tags extracted:\n\n**Keywords:**\n- dval.in\n- Backend\n- User data\n- Communication\n- Hoyoverse\n- Node.js\n- Pnpm\n- PostgreSQL\n- Redis\n- Oauth Tokens\n- Github\n- Google\n- Microsoft\n- Clone the repository\n- Install dependencies\n- .env\n- Prisma\n- Database\n- Run backend\n- Contributing\n\n**Tags:**\n- Backend Development\n- Node.js\n- Pnpm\n- PostgreSQL\n- Redis\n- OAuth\n- Github\n- Dval.in\n- Prisma\n- Database Management\n- Repository Management\n- Oauth Tokens Setup\n- Backend Setup\n- Development Steps\n- Contributing Guidelines\n- Environment Variables"},"finish_reason":"stop"}],"usage":{"prompt_tokens":275,"completion_tokens":161,"total_tokens":436},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Bob Johnson
  name: author
- content: {"id":"0193e85db5541e63d2a8cb19afff99dc","object":"chat.completion","created":1734770275,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Based on the provided text, here are the keywords and tags extracted:\n\n**Keywords:**\n- dval.in\n- Backend\n- User data\n- Communication\n- Hoyoverse\n- Node.js\n- Pnpm\n- PostgreSQL\n- Redis\n- Oauth Tokens\n- Github\n- Google\n- Microsoft\n- Clone the repository\n- Install dependencies\n- .env\n- Prisma\n- Database\n- Run backend\n- Contributing\n\n**Tags:**\n- Backend Development\n- Node.js\n- Pnpm\n- PostgreSQL\n- Redis\n- OAuth\n- Github\n- Dval.in\n- Prisma\n- Database Management\n- Repository Management\n- Oauth Tokens Setup\n- Backend Setup\n- Development Steps\n- Contributing Guidelines\n- Environment Variables"},"finish_reason":"stop"}],"usage":{"prompt_tokens":275,"completion_tokens":161,"total_tokens":436},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e85db5541e63d2a8cb19afff99dc","object":"chat.completion","created":1734770275,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Based on the provided text, here are the keywords and tags extracted:\n\n**Keywords:**\n- dval.in\n- Backend\n- User data\n- Communication\n- Hoyoverse\n- Node.js\n- Pnpm\n- PostgreSQL\n- Redis\n- Oauth Tokens\n- Github\n- Google\n- Microsoft\n- Clone the repository\n- Install dependencies\n- .env\n- Prisma\n- Database\n- Run backend\n- Contributing\n\n**Tags:**\n- Backend Development\n- Node.js\n- Pnpm\n- PostgreSQL\n- Redis\n- OAuth\n- Github\n- Dval.in\n- Prisma\n- Database Management\n- Repository Management\n- Oauth Tokens Setup\n- Backend Setup\n- Development Steps\n- Contributing Guidelines\n- Environment Variables"},"finish_reason":"stop"}],"usage":{"prompt_tokens":275,"completion_tokens":161,"total_tokens":436},"system_fingerprint":""}
theme: light
title: dvalin-backend
---

# dvalin-backend

## Repository URL: 
[https://github.com/wanghaisheng/dvalin-backend](https://github.com/wanghaisheng/dvalin-backend)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Backend for dval.in. Stores user data and handles communication with Hoyoverse

## README Content: 
# Dvalin - Backend

## How to use

### Requirements

- [Node 20](https://nodejs.org/)
- [Pnpm 9](https://pnpm.io/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://www.redis.io/)
- Oauth Tokens: (Redirect URL needs to match BACKEND_URL in .env)
    - [Github](https://github.com/settings/developers)
    - Optional: Google
    - Optional: Microsoft

### Steps

1. [Clone the repository](https://docs.github.com/articles/cloning-a-repository)
2. Install dependencies (`pnpm install`)
3. Create a copy of .env.example named .env
4. Fill in all variables in .env
5. Push prisma schema to database (`prisma db push`)
6. Run backend (`pnpm run dev`)

### Contributing

See [CONTRIBUTING.md](https://github.com/dval-in/dvalin-backend/blob/main/CONTRIBUTING.md)

