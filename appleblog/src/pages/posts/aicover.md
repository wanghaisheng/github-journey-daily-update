---
author: Bob Johnson
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: '姓氏  属相相关'
featured: true
keywords: {"id":"0193e859059d3506fe002e6b8c12292b","object":"chat.completion","created":1734769968,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- aicover\n- AI Cover Generator\n- 姓氏\n- 属相\n- 2024-12-06\n- AI Cover\n- AI Wallpaper\n- code reference\n- full-stack development\n- user authentication\n- image storage\n- payment\n- data processing\n- page building\n- PostgreSQL\n- Vercel PostgreSQL\n- Supabase\n- open source project\n- Twitter\n- Buy Me A Coffee\n\n### Tags:\n- #AI\n- #Coding\n- #FullStackDevelopment\n- #UserAuthentication\n- #ImageStorage\n- #Payment\n- #DataProcessing\n- #PageBuilding\n- #PostgreSQL\n- #VercelPostgreSQL\n- #Supabase\n- #OpenSource\n- #Twitter\n- #BuyMeACoffee"},"finish_reason":"stop"}],"usage":{"prompt_tokens":607,"completion_tokens":174,"total_tokens":781},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Bob Johnson
  name: author
- content: {"id":"0193e859059d3506fe002e6b8c12292b","object":"chat.completion","created":1734769968,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- aicover\n- AI Cover Generator\n- 姓氏\n- 属相\n- 2024-12-06\n- AI Cover\n- AI Wallpaper\n- code reference\n- full-stack development\n- user authentication\n- image storage\n- payment\n- data processing\n- page building\n- PostgreSQL\n- Vercel PostgreSQL\n- Supabase\n- open source project\n- Twitter\n- Buy Me A Coffee\n\n### Tags:\n- #AI\n- #Coding\n- #FullStackDevelopment\n- #UserAuthentication\n- #ImageStorage\n- #Payment\n- #DataProcessing\n- #PageBuilding\n- #PostgreSQL\n- #VercelPostgreSQL\n- #Supabase\n- #OpenSource\n- #Twitter\n- #BuyMeACoffee"},"finish_reason":"stop"}],"usage":{"prompt_tokens":607,"completion_tokens":174,"total_tokens":781},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e859059d3506fe002e6b8c12292b","object":"chat.completion","created":1734769968,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- aicover\n- AI Cover Generator\n- 姓氏\n- 属相\n- 2024-12-06\n- AI Cover\n- AI Wallpaper\n- code reference\n- full-stack development\n- user authentication\n- image storage\n- payment\n- data processing\n- page building\n- PostgreSQL\n- Vercel PostgreSQL\n- Supabase\n- open source project\n- Twitter\n- Buy Me A Coffee\n\n### Tags:\n- #AI\n- #Coding\n- #FullStackDevelopment\n- #UserAuthentication\n- #ImageStorage\n- #Payment\n- #DataProcessing\n- #PageBuilding\n- #PostgreSQL\n- #VercelPostgreSQL\n- #Supabase\n- #OpenSource\n- #Twitter\n- #BuyMeACoffee"},"finish_reason":"stop"}],"usage":{"prompt_tokens":607,"completion_tokens":174,"total_tokens":781},"system_fingerprint":""}
theme: light
title: aicover
---

# aicover

## Repository URL: 
[https://github.com/wanghaisheng/aicover](https://github.com/wanghaisheng/aicover)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
姓氏  属相相关

## README Content: 
2024-12-06

# AI Cover

AI Cover Generator by [aicover.design](https://aicover.design)

[中文说明](/README_CN.md)

## Live Demo

[https://aicover.design](https://aicover.design)

![demo](./preview.png)

## Quick Start

1. clone project

```shell
git clone https://github.com/all-in-aigc/aicover
```

2. install dependencies

```shell
cd aicover
pnpm install
```

3. init database

create your database use [local postgres](https://wiki.postgresql.org/wiki/Homebrew) or [vercel-postgres](https://vercel.com/docs/storage/vercel-postgres) or [supabase](https://supabase.com/)

create tables from sql at `data/install.sql`

4. set environmental values

put `.env.local` under `aicover` root dir with values list below

```
OPENAI_API_KEY=""

POSTGRES_URL=""

AWS_AK=""
AWS_SK=""
AWS_REGION=""
AWS_BUCKET=""

NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=""
NEXT_PUBLIC_CLERK_SIGN_IN_URL=/sign-in
NEXT_PUBLIC_CLERK_SIGN_UP_URL=/sign-up
NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL=/
NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL=/

STRIPE_PUBLIC_KEY=""
STRIPE_PRIVATE_KEY=""

WEB_BASE_URI=""
```

5. local development

```shell
pnpm dev
```

open `http://localhost:3000` for preview

## Credit to

- [aiwallpaper](https://aiwallpaper.shop) for code reference
- [nextjs](https://nextjs.org/docs) for full-stack development
- [clerk](https://clerk.com/docs/quickstarts/nextjs) for user auth
- [aws s3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) for image storage
- [stripe](https://stripe.com/docs/development) for payment
- [node-postgres](https://node-postgres.com/) for data processing
- [tailwindcss](https://tailwindcss.com/) for page building

## Other Things

you can contact me at Twitter: https://twitter.com/idoubicc

if this project is helpful to you, buy me a coffee.

<a href="https://www.buymeacoffee.com/idoubi" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

