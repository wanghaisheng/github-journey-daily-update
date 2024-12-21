---
author: Jane Smith
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734782330540_7kwp1
  url: https://fluxapi.borninsea.com/image/image_1734782330540_7kwp1
description: 'No description provided.'
featured: true
keywords: automation,script,serv00,maintenance,30 days,WeChat Enterprise Robot,secret configuration,account key,enterprise微信机器人
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: automation,script,serv00,maintenance,30 days,WeChat Enterprise Robot,secret configuration,account key,enterprise微信机器人
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- spyfu-research,serv00-autologin,自动化运行,企业微信机器人,secrets配置
theme: light
title: spyfu-research
---

# spyfu-research

## Repository URL: 
[https://github.com/wanghaisheng/spyfu-research](https://github.com/wanghaisheng/spyfu-research)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
No description provided.

## README Content: 
# serv00-autologin

自动化运行脚本实现 serv00 保活，默认每 30 天运行一次，并通过企业微信机器人进行消息推送


## secrets 配置方式
Settings -> Secrets and variables -> Repository secrets -> New Repository secrets

### 账号密钥
- Name 设置为 ACCOUNT            
- Secret 格式如下

```json
[
    {
        "username": "test",
        "password": "test",
        "url": "http://xxxx/login"
    },
    {
        "username": "test2",
        "password": "test2",
        "url": "http://xxxx/login"
    }
]

```
### 企业微信机器人
- Name 设置为 WX_URL
Secret 设置为 完整的url
```
https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxx
```
