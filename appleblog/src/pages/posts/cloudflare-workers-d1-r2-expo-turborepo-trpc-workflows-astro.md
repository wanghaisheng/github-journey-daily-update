---
author: Bob Johnson
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734780385806_lkq64d
  url: https://fluxapi.borninsea.com/image/image_1734780385806_lkq64d
description: 'Create an expo mobile app powered by Cloudflare Workers, Workers AI, R2, D1, Workflows, and Pages. Contains Clerk auth, tRPC, and Drizzle integrations with Turborepo.'
featured: true
keywords: cloudflare-workers,expo,turborepo,trpc,workflows,astro,clerk-auth,d1,r2,workers-ai,turbo-stack,tailwind,drizzle,typescript,cloudflare-pages,mobile-app-template,edge-computing,serverless-compute,mobile-app,landing-page,secure-user-management,type-safe-api-communication,edge-ai-processing,image-storage,edge-database,orm,prerequisites,nodejs,pnpm,cloudflare-account,wrangler-cli,clerk-account,production-environment,development-environment,database-migrations,monorepo,turborepo-efficiency
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Bob Johnson
  name: author
- content: cloudflare-workers,expo,turborepo,trpc,workflows,astro,clerk-auth,d1,r2,workers-ai,turbo-stack,tailwind,drizzle,typescript,cloudflare-pages,mobile-app-template,edge-computing,serverless-compute,mobile-app,landing-page,secure-user-management,type-safe-api-communication,edge-ai-processing,image-storage,edge-database,orm,prerequisites,nodejs,pnpm,cloudflare-account,wrangler-cli,clerk-account,production-environment,development-environment,database-migrations,monorepo,turborepo-efficiency
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- cloudflare-workers,expo,turbo-stack,astro,clerk-auth,trpc,r2,d1,workflows,pages,database,edge-compute,serverless
theme: light
title: cloudflare-workers-d1-r2-expo-turborepo-trpc-workflows-astro
---

# cloudflare-workers-d1-r2-expo-turborepo-trpc-workflows-astro

## Repository URL: 
[https://github.com/wanghaisheng/cloudflare-workers-d1-r2-expo-turborepo-trpc-workflows-astro](https://github.com/wanghaisheng/cloudflare-workers-d1-r2-expo-turborepo-trpc-workflows-astro)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Create an expo mobile app powered by Cloudflare Workers, Workers AI, R2, D1, Workflows, and Pages. Contains Clerk auth, tRPC, and Drizzle integrations with Turborepo.

## README Content: 
# Cloudflare Turbo Stack

A full-stack mobile application template powered by Cloudflare's edge platform. This template provides a foundation for building AI-powered mobile apps with a web landing page, using modern tools and best practices.

## 🚀 Features

- 📱 **Expo Mobile App**: Cross-platform mobile application
- 🌐 **Astro Landing Page**: Fast, modern web presence
- 🔒 **Clerk Authentication**: Secure user management
- 🔄 **tRPC API**: Type-safe API communication
- 🤖 **Workers AI**: Edge AI processing
- 📦 **R2 Storage**: Image and asset storage
- 💾 **D1 Database**: Edge SQLite database with Drizzle ORM
- 🏗️ **Cloudflare Workers**: Serverless compute
- 🔄 **Workflows**: Durable AI task processing

## 📦 Project Structure

```
.
├── apps/
│   ├── apiservice/    # Cloudflare Worker API
│   └── astro/         # Landing page
├── packages/
│   ├── db/           # Database schema and utilities
│   └── trpc/         # tRPC router definitions
└── tooling/          # Shared development tools
```

## 🛠️ Prerequisites

- Node.js >= 20.16.0
- pnpm >= 9.6.0
- Cloudflare account
- Wrangler CLI (`npm install -g wrangler`)
- Clerk account

## 🚀 Getting Started

Note: In a production app, you'll want to properly set up secrets and proper dev/prod environments using wrangler, but this will get you up and running quickly.

1. **Clone the repository**

```bash
git clone <repository-url>
cd cloudflare-turbo
```

2. **Install dependencies**

```bash
pnpm install
```

3. **Configure Cloudflare**

Login to Cloudflare CLI:
```bash
wrangler login
```

Update the following `wrangler.toml` files with your Cloudflare settings:
- `apps/apiservice/wrangler.toml`
- `packages/db/wrangler.toml`

4. **Environment Setup**

Create `.env` files based on the provided examples and update with your credentials:
```bash
cp apps/expo/.env.example apps/expo/.env
```

5. **Start Development**

```bash
pnpm dev
```

## 🔧 Configuration

### Cloudflare Setup

1. Create a D1 Database:
```bash
wrangler d1 create <your-database-name>
```

2. Create an R2 Bucket:
```bash
wrangler r2 bucket create <your-bucket-name>
```

3. Update the respective `wrangler.toml` files with the created resource IDs

### Clerk Setup

1. Create a Clerk application at https://clerk.dev
2. Add the Clerk keys to your `.env` files

## 📝 Development Notes

- Use `pnpm dev` to start all services in development mode
- Database migrations can be run with `pnpm db:generate`
- The project uses a monorepo structure with Turborepo for efficient builds

## 🚀 Deployment

1. **Deploy API Service**
```bash
cd apps/apiservice
pnpm run deploy
```

2. **Deploy Landing Page**
```bash
cd apps/astro
pnpm run deploy
```

3. **Deploy Workflows**
```bash
cd apps/workflows
pnpm run deploy
```

## 📚 Tech Stack

- **Frontend**: React Native (Expo), Astro
- **Backend**: Cloudflare Workers, Workers AI
- **Database**: Cloudflare D1 (SQLite)
- **Storage**: Cloudflare R2
- **Authentication**: Clerk
- **API**: tRPC
- **Build Tool**: Turborepo
- **Package Manager**: pnpm

## 🤝 Contributing

Contributions are welcome! Please read our contributing guidelines before submitting PRs.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

