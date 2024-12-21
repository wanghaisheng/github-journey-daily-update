---
author: John Doe
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734779923485_szem3w
  url: https://fluxapi.borninsea.com/image/image_1734779923485_szem3w
description: '姓氏  属相相关'
featured: true
keywords: aicover,姓氏,属相,2024-12-06,aicover.design,README_CN.md,demo,aicover.design,quick,start,clone,project,dependencies,init,database,sql,.env.local,OPENAI_API_KEY,POSTGRES_URL,AWS_AK,AWS_SK,AWS_REGION,AWS_BUCKET,NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY,NEXT_PUBLIC_CLERK_SIGN_IN_URL,NEXT_PUBLIC_CLERK_SIGN_UP_URL,NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL,NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL,STRIPE_PUBLIC_KEY,STRIPE_PRIVATE_KEY,WEB_BASE_URI,aiwallpaper,nextjs,clerk,aws,s3,stripe,node-postgres,tailwindcss,pnm.dev,localhost
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: aicover,姓氏,属相,2024-12-06,aicover.design,README_CN.md,demo,aicover.design,quick,start,clone,project,dependencies,init,database,sql,.env.local,OPENAI_API_KEY,POSTGRES_URL,AWS_AK,AWS_SK,AWS_REGION,AWS_BUCKET,NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY,NEXT_PUBLIC_CLERK_SIGN_IN_URL,NEXT_PUBLIC_CLERK_SIGN_UP_URL,NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL,NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL,STRIPE_PUBLIC_KEY,STRIPE_PRIVATE_KEY,WEB_BASE_URI,aiwallpaper,nextjs,clerk,aws,s3,stripe,node-postgres,tailwindcss,pnm.dev,localhost
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
-  aicover, 属相, 2024-12-06, AI Cover Generator, GitHub, PostgreSQL, Vercel, Supabase, OpenAI, AWS, Next.js, Clerk, Stripe, AWS S3, node-postgres, tailwindcss, full-stack development, user authentication, image storage, payment processing, data processing, page building, Twitter, Buy Me A Coffee
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

