---
author: Jane Smith
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734781735718_a3rxl
  url: https://fluxapi.borninsea.com/image/image_1734781735718_a3rxl
description: 'Use Cloudflare Workers to provide a WebDav interface for Cloudflare R2.'
featured: true
keywords: Cloudflare_Workers,WebDAV,Cloudflare_R2,文献管理,r2-webdav,部署,wrangler,开发,测试
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: Cloudflare_Workers,WebDAV,Cloudflare_R2,文献管理,r2-webdav,部署,wrangler,开发,测试
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- paper-webdav-cloudflare,r2-webdav,cloudflare-workers,webdav,cloudflare-r2,文献管理
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

