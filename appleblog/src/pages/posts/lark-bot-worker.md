---
author: Jane Smith
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734781185845_tslg
  url: https://fluxapi.borninsea.com/image/image_1734781185845_tslg
description: 'Lark/Feishu bot on Cloudflare Workers'
featured: true
keywords: Cloudflare Workers,Lark,Feishu,gitLab,webhooks,deploy,Environment variables
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: Cloudflare Workers,Lark,Feishu,gitLab,webhooks,deploy,Environment variables
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- cloudflare,workers,lark,feishu,gitlab,webhooks
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

