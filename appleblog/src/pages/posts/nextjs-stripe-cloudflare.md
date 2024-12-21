---
author: Bob Johnson
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'No description provided.'
featured: true
keywords: {"id":"0193e8650466de4ec57749c23d8ba3a5","object":"chat.completion","created":1734770754,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- Next.js\n- Stripe\n- Cloudflare\n- c3\n- Cloudflare Pages\n- Wrangler\n- KV Binding\n- Development\n- Preview\n- Deployment\n- Next-on-Pages\n- Dev Scripts\n- Function Bindings\n\n### Tags\n- Next.js Project\n- Cloud Integration\n- Development Server\n- Cloudflare Integration\n- Wrangler CLI\n- Local Preview\n- Deployment Workflow\n- Function Binding Examples\n- Cloudflare Pages Environment\n- KV Store Binding\n- Next-on-Pages CLI"},"finish_reason":"stop"}],"usage":{"prompt_tokens":865,"completion_tokens":111,"total_tokens":976},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Bob Johnson
  name: author
- content: {"id":"0193e8650466de4ec57749c23d8ba3a5","object":"chat.completion","created":1734770754,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- Next.js\n- Stripe\n- Cloudflare\n- c3\n- Cloudflare Pages\n- Wrangler\n- KV Binding\n- Development\n- Preview\n- Deployment\n- Next-on-Pages\n- Dev Scripts\n- Function Bindings\n\n### Tags\n- Next.js Project\n- Cloud Integration\n- Development Server\n- Cloudflare Integration\n- Wrangler CLI\n- Local Preview\n- Deployment Workflow\n- Function Binding Examples\n- Cloudflare Pages Environment\n- KV Store Binding\n- Next-on-Pages CLI"},"finish_reason":"stop"}],"usage":{"prompt_tokens":865,"completion_tokens":111,"total_tokens":976},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e8650466de4ec57749c23d8ba3a5","object":"chat.completion","created":1734770754,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- Next.js\n- Stripe\n- Cloudflare\n- c3\n- Cloudflare Pages\n- Wrangler\n- KV Binding\n- Development\n- Preview\n- Deployment\n- Next-on-Pages\n- Dev Scripts\n- Function Bindings\n\n### Tags\n- Next.js Project\n- Cloud Integration\n- Development Server\n- Cloudflare Integration\n- Wrangler CLI\n- Local Preview\n- Deployment Workflow\n- Function Binding Examples\n- Cloudflare Pages Environment\n- KV Store Binding\n- Next-on-Pages CLI"},"finish_reason":"stop"}],"usage":{"prompt_tokens":865,"completion_tokens":111,"total_tokens":976},"system_fingerprint":""}
theme: light
title: nextjs-stripe-cloudflare
---

# nextjs-stripe-cloudflare

## Repository URL: 
[https://github.com/wanghaisheng/nextjs-stripe-cloudflare](https://github.com/wanghaisheng/nextjs-stripe-cloudflare)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
No description provided.

## README Content: 
2024-12-06

This is a [Next.js](https://nextjs.org/) project bootstrapped with [`c3`](https://developers.cloudflare.com/pages/get-started/c3).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Cloudflare integration

Besides the `dev` script mentioned above `c3` has added a few extra scripts that allow you to integrate the application with the [Cloudflare Pages](https://pages.cloudflare.com/) environment, these are:
  - `pages:build` to build the application for Pages using the [`@cloudflare/next-on-pages`](https://github.com/cloudflare/next-on-pages) CLI
  - `preview` to locally preview your Pages application using the [Wrangler](https://developers.cloudflare.com/workers/wrangler/) CLI
  - `deploy` to deploy your Pages application using the [Wrangler](https://developers.cloudflare.com/workers/wrangler/) CLI

> __Note:__ while the `dev` script is optimal for local development you should preview your Pages application as well (periodically or before deployments) in order to make sure that it can properly work in the Pages environment (for more details see the [`@cloudflare/next-on-pages` recommended workflow](https://github.com/cloudflare/next-on-pages/blob/05b6256/internal-packages/next-dev/README.md#recommended-workflow))

### Bindings

Cloudflare [Bindings](https://developers.cloudflare.com/pages/functions/bindings/) are what allows you to interact with resources available in the Cloudflare Platform.

You can use bindings during development, when previewing locally your application and of course in the deployed application:

- To use bindings in dev mode you need to define them in the `next.config.js` file under `setupDevBindings`, this mode uses the `next-dev` `@cloudflare/next-on-pages` submodule. For more details see its [documentation](https://github.com/cloudflare/next-on-pages/blob/05b6256/internal-packages/next-dev/README.md).

- To use bindings in the preview mode you need to add them to the `pages:preview` script accordingly to the `wrangler pages dev` command. For more details see its [documentation](https://developers.cloudflare.com/workers/wrangler/commands/#dev-1) or the [Pages Bindings documentation](https://developers.cloudflare.com/pages/functions/bindings/).

- To use bindings in the deployed application you will need to configure them in the Cloudflare [dashboard](https://dash.cloudflare.com/). For more details see the  [Pages Bindings documentation](https://developers.cloudflare.com/pages/functions/bindings/).

#### KV Example

`c3` has added for you an example showing how you can use a KV binding.

In order to enable the example:
- Search for javascript/typescript lines containing the following comment:
  ```ts
  // KV Example:
  ```
  and uncomment the commented lines below it.
- Do the same in the `wrangler.toml` file, where
  the comment is:
  ```
  # KV Example:
  ```

After doing this you can run the `dev` or `preview` script and visit the `/api/hello` route to see the example in action.

Finally, if you also want to see the example work in the deployed application make sure to add a `MY_KV` binding to your Pages application in its [dashboard kv bindings settings section](https://dash.cloudflare.com/?to=/:account/pages/view/:pages-project/settings/functions#kv_namespace_bindings_section). After having configured it make sure to re-deploy your application.

