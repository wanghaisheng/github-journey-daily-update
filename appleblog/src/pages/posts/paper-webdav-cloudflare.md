---
author: John Doe
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Use Cloudflare Workers to provide a WebDav interface for Cloudflare R2.'
featured: true
keywords: {"id":"0193e86615053327d9c5a4e8a829ebf8","object":"chat.completion","created":1734770824,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- WebDav\n- Cloudflare Workers\n- Cloudflare R2\n- Literature Management\n- wrangler\n- litmus\n- deployment\n- R2_buckets\n\n### Tags:\n- #r2-webdav\n- #cloudflare-workers\n- #webdav-interface\n- #literature-management\n- #cloudflare-r2\n- #deployment-guide\n- #development-tools\n- #litmus-testing"},"finish_reason":"stop"}],"usage":{"prompt_tokens":311,"completion_tokens":91,"total_tokens":402},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: {"id":"0193e86615053327d9c5a4e8a829ebf8","object":"chat.completion","created":1734770824,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- WebDav\n- Cloudflare Workers\n- Cloudflare R2\n- Literature Management\n- wrangler\n- litmus\n- deployment\n- R2_buckets\n\n### Tags:\n- #r2-webdav\n- #cloudflare-workers\n- #webdav-interface\n- #literature-management\n- #cloudflare-r2\n- #deployment-guide\n- #development-tools\n- #litmus-testing"},"finish_reason":"stop"}],"usage":{"prompt_tokens":311,"completion_tokens":91,"total_tokens":402},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86615053327d9c5a4e8a829ebf8","object":"chat.completion","created":1734770824,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- WebDav\n- Cloudflare Workers\n- Cloudflare R2\n- Literature Management\n- wrangler\n- litmus\n- deployment\n- R2_buckets\n\n### Tags:\n- #r2-webdav\n- #cloudflare-workers\n- #webdav-interface\n- #literature-management\n- #cloudflare-r2\n- #deployment-guide\n- #development-tools\n- #litmus-testing"},"finish_reason":"stop"}],"usage":{"prompt_tokens":311,"completion_tokens":91,"total_tokens":402},"system_fingerprint":""}
theme: light
title: paper-webdav-cloudflare
---

# paper-webdav-cloudflare

## Repository URL: 
[https://github.com/wanghaisheng/paper-webdav-cloudflare](https://github.com/wanghaisheng/paper-webdav-cloudflare)

## Stars: 
**1**

## Forks: 
**0**

## Description: 
Use Cloudflare Workers to provide a WebDav interface for Cloudflare R2.

## README Content: 
文献管理

# r2-webdav

[![Deploy to Cloudflare Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/wanghaisheng/paper-webdav-cloudflare)

Use Cloudflare Workers to provide a WebDav interface for Cloudflare R2.

## Usage

Change wrangler.toml to your own.

```toml
[[r2_buckets]]
binding = 'bucket' # <~ valid JavaScript variable name, don't change this
bucket_name = 'webdav'
```

Then use wrangler to deploy.

```bash
wrangler deploy

wrangler secret put USERNAME
wrangler secret put PASSWORD
```

## Development

With `wrangler`, you can build, test, and deploy your Worker with the following commands:

```sh
# run your Worker in an ideal development workflow (with a local server, file watcher & more)
$ npm run dev

# deploy your Worker globally to the Cloudflare network (update your wrangler.toml file for configuration)
$ npm run deploy
```

## Test

Use [litmus](https://github.com/notroj/litmus) to test.

