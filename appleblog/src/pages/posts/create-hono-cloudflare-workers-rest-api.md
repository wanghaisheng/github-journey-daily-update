---
author: John Doe
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734780450747_b2o44o
  url: https://fluxapi.borninsea.com/image/image_1734780450747_b2o44o
description: 'Lightweight Honojs rest api template for side project or micro Saas on cloudflare workers'
featured: true
keywords: HonoJS,REST API,Cloudflare Workers,JWT token Authentication,zod,Jest, ESLint, Prettier,degit,wrangler,bun,testing,code formatting,JWT Encoder/Decoder
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: HonoJS,REST API,Cloudflare Workers,JWT token Authentication,zod,Jest, ESLint, Prettier,degit,wrangler,bun,testing,code formatting,JWT Encoder/Decoder
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- create-hono-cloudflare-workers-rest-api,HonoJS,JWT,token,Authentication,middleware,zod,jest,eslint,prettier,Cloudflare,Workers,REST-API,side-project,micro-SaaS,testing,deployment,coding,electron,bun,fixing
theme: light
title: create-hono-cloudflare-workers-rest-api
---

# create-hono-cloudflare-workers-rest-api

## Repository URL: 
[https://github.com/wanghaisheng/create-hono-cloudflare-workers-rest-api](https://github.com/wanghaisheng/create-hono-cloudflare-workers-rest-api)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Lightweight Honojs rest api template for side project or micro Saas on cloudflare workers

## README Content: 
# create-hono-cloudflare-workers-rest-api

🚀 Welcome to [HonoJS](https://hono.dev/) REST API Template 🚀

## Features

🛠️ Minimal Setup, Maximum Power

⚙️ Middleware Magic

🔐 JWT token Authentication

✅ Route validation with [zod](https://zod.dev/)

🧪 Testing with [jest](https://jestjs.io/fr/)

🦋 Beautiful code with [eslint](https://eslint.org/) and [prettier](https://prettier.io/)

## Getting Started

```sh
npx degit https://github.com/TheSmartMonkey/create-hono-cloudflare-workers-rest-api backend
```

Create a `wrangler.toml` based on `wrangler.default.toml`

Install dependancies

```sh
bun i
```

Start coding 🧑‍💻

```sh
bun start
```

Deploy to cloudflare 🚀

```sh
bun run deploy
```

## Testing

Test you code 🧪

```sh
bun run test
```

### Run Specific Tests

Run unit tests 🧪
*Test individual components or functions*

```sh
bun run unit
```

Run integration tests 🧪
*Test your code with external dependencies like databases, APIs, etc*

```sh
bun run integration
```

### Grouping Tests

Tests are grouped using Jest's `@group` annotation:

```js
/**
 * @group unit
 */
```

```js
/**
 * @group integration
 */
```

This helps in organizing and running specific groups of tests

## More Commands

Fix you code to make it Beautiful 🦋

```sh
bun run fix
```

For more commands:

```sh
bun run
```

Encode a JWT token: [JWT Encoder/Decoder](https://10015.io/tools/jwt-encoder-decoder)

Happy coding! 🎉

