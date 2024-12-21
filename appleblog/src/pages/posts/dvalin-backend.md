---
author: John Doe
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734780584215_78ft9
  url: https://fluxapi.borninsea.com/image/image_1734780584215_78ft9
description: 'Backend for dval.in. Stores user data and handles communication with Hoyoverse'
featured: true
keywords: Backend,dval.in,user data,communication,Hoyoverse,Node,20,Pnpm,9,PostgreSQL,Redis,Oauth Tokens,Github,Google,Microsoft,Clone the repository,dependencies,install dependencies,.env.example,.env,Prisma schema,Push prisma schema to database,run backend,Contributing
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: Backend,dval.in,user data,communication,Hoyoverse,Node,20,Pnpm,9,PostgreSQL,Redis,Oauth Tokens,Github,Google,Microsoft,Clone the repository,dependencies,install dependencies,.env.example,.env,Prisma schema,Push prisma schema to database,run backend,Contributing
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- backend,dval.in,user data,communication,Hoyoverse,Node.js,Pnpm,PostgreSQL,Redis,Oauth Tokens,Github,Google,Microsoft,repository,dependencies,.env,Prisma,contributing
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

