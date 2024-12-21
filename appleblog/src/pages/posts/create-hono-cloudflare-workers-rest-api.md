---
author: Jane Smith
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Lightweight Honojs rest api template for side project or micro Saas on cloudflare workers'
featured: true
keywords: {"id":"0193e85cb66973007345a98a3ab5e6a1","object":"chat.completion","created":1734770210,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- HonoJS\n- REST API\n- Cloudflare Workers\n- Side project\n- Micro Saas\n- JWT Token Authentication\n- Route Validation\n- zod\n- Testing\n- Jest\n- Eslint\n- Prettier\n- Degit\n- Bun\n- Wrangler\n- Deployment\n- Unit Tests\n- Integration Tests\n\n### Tags:\n- #HonoJS\n- #CloudflareWorkers\n- #RESTAPI\n- #MicroSaas\n- #JWT\n- #RouteValidation\n- #Testing\n- #Jest\n- #Eslint\n- #Prettier\n- #Degit\n- #Bun\n- #Deployment\n- #TestingFramework\n- #UnitTests\n- #IntegrationTests"},"finish_reason":"stop"}],"usage":{"prompt_tokens":471,"completion_tokens":161,"total_tokens":632},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: {"id":"0193e85cb66973007345a98a3ab5e6a1","object":"chat.completion","created":1734770210,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- HonoJS\n- REST API\n- Cloudflare Workers\n- Side project\n- Micro Saas\n- JWT Token Authentication\n- Route Validation\n- zod\n- Testing\n- Jest\n- Eslint\n- Prettier\n- Degit\n- Bun\n- Wrangler\n- Deployment\n- Unit Tests\n- Integration Tests\n\n### Tags:\n- #HonoJS\n- #CloudflareWorkers\n- #RESTAPI\n- #MicroSaas\n- #JWT\n- #RouteValidation\n- #Testing\n- #Jest\n- #Eslint\n- #Prettier\n- #Degit\n- #Bun\n- #Deployment\n- #TestingFramework\n- #UnitTests\n- #IntegrationTests"},"finish_reason":"stop"}],"usage":{"prompt_tokens":471,"completion_tokens":161,"total_tokens":632},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e85cb66973007345a98a3ab5e6a1","object":"chat.completion","created":1734770210,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- HonoJS\n- REST API\n- Cloudflare Workers\n- Side project\n- Micro Saas\n- JWT Token Authentication\n- Route Validation\n- zod\n- Testing\n- Jest\n- Eslint\n- Prettier\n- Degit\n- Bun\n- Wrangler\n- Deployment\n- Unit Tests\n- Integration Tests\n\n### Tags:\n- #HonoJS\n- #CloudflareWorkers\n- #RESTAPI\n- #MicroSaas\n- #JWT\n- #RouteValidation\n- #Testing\n- #Jest\n- #Eslint\n- #Prettier\n- #Degit\n- #Bun\n- #Deployment\n- #TestingFramework\n- #UnitTests\n- #IntegrationTests"},"finish_reason":"stop"}],"usage":{"prompt_tokens":471,"completion_tokens":161,"total_tokens":632},"system_fingerprint":""}
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

