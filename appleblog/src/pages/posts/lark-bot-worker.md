---
author: John Doe
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Lark/Feishu bot on Cloudflare Workers'
featured: true
keywords: {"id":"0193e8625ca40996021d2504ad99abfc","object":"chat.completion","created":1734770580,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- Lark\n- Feishu\n- Cloudflare Workers\n- bot\n- GitLab\n- webhook\n- deployment\n- environment variables\n\n### Tags\n- Lark Bot Worker\n- Node.js\n- GitLab Integration\n- Cloudflare Workers Deployment\n- Webhook Forwarding\n- Environment Configuration"},"finish_reason":"stop"}],"usage":{"prompt_tokens":455,"completion_tokens":67,"total_tokens":522},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: {"id":"0193e8625ca40996021d2504ad99abfc","object":"chat.completion","created":1734770580,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- Lark\n- Feishu\n- Cloudflare Workers\n- bot\n- GitLab\n- webhook\n- deployment\n- environment variables\n\n### Tags\n- Lark Bot Worker\n- Node.js\n- GitLab Integration\n- Cloudflare Workers Deployment\n- Webhook Forwarding\n- Environment Configuration"},"finish_reason":"stop"}],"usage":{"prompt_tokens":455,"completion_tokens":67,"total_tokens":522},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e8625ca40996021d2504ad99abfc","object":"chat.completion","created":1734770580,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- Lark\n- Feishu\n- Cloudflare Workers\n- bot\n- GitLab\n- webhook\n- deployment\n- environment variables\n\n### Tags\n- Lark Bot Worker\n- Node.js\n- GitLab Integration\n- Cloudflare Workers Deployment\n- Webhook Forwarding\n- Environment Configuration"},"finish_reason":"stop"}],"usage":{"prompt_tokens":455,"completion_tokens":67,"total_tokens":522},"system_fingerprint":""}
theme: light
title: lark-bot-worker
---

# lark-bot-worker

## Repository URL: 
[https://github.com/wanghaisheng/lark-bot-worker](https://github.com/wanghaisheng/lark-bot-worker)

## Stars: 
**1**

## Forks: 
**0**

## Description: 
Lark/Feishu bot on Cloudflare Workers

## README Content: 
# Lark Bot Worker

[![Workflow](https://github.com/lawvs/lark-bot-worker/actions/workflows/nodejs.yml/badge.svg)](https://github.com/lawvs/lark-bot-worker/actions/workflows/nodejs.yml)

[![Deploy to Cloudflare Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/lawvs/lark-bot-worker)

Lark/Feishu bot on Cloudflare Workers.

## Features

- Forward GitLab's comment to Feishu/Lark

<img width="402" alt="image" src="https://user-images.githubusercontent.com/18554747/160114855-7f253d00-8ece-40ef-8540-ade006d16edb.png">

## Usages

- Deploy bot to Cloudflare Workers

- Add Webhooks at GitLab

![image](https://user-images.githubusercontent.com/18554747/160115957-e4f56e15-4628-4c98-9cd1-dc00fb5332ad.png)

## Config

Environment variables:

```sh
CLOUDFLARE_ACCOUNT_ID=xxx
CF_API_TOKEN=xxx
# (Optional)
CF_ZONE_ID=xxx

# Lark/Feishu bot webhook
WEBHOOK=https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxxxxxx
# (Optional) Lark/Feishu bot signature secret
SIGN_SECRET=xxxxxxxxxxxx
```

## References

- [Cloudflare Workers documentation](https://developers.cloudflare.com/workers/)
- [Webhook events | GitLab](https://docs.gitlab.com/ee/user/project/integrations/webhook_events.html)

