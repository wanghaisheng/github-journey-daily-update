---
author: Jane Smith
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'No description provided.'
featured: true
keywords: {"id":"0193e86a0c6d6844f670314326fab9ab","object":"chat.completion","created":1734771084,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### 关键词\n- 自动化运行脚本\n- serv00\n- 保活\n- 企业微信机器人\n- 消息推送\n- secrets\n- Repository secrets\n- 账号密钥\n- 企业微信url\n\n### 标签\n- serv00-autologin\n- 自动化\n- 运行脚本\n- 保活机制\n- 企业微信通知\n- secrets管理\n- Repository secrets配置"},"finish_reason":"stop"}],"usage":{"prompt_tokens":233,"completion_tokens":101,"total_tokens":334},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: {"id":"0193e86a0c6d6844f670314326fab9ab","object":"chat.completion","created":1734771084,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### 关键词\n- 自动化运行脚本\n- serv00\n- 保活\n- 企业微信机器人\n- 消息推送\n- secrets\n- Repository secrets\n- 账号密钥\n- 企业微信url\n\n### 标签\n- serv00-autologin\n- 自动化\n- 运行脚本\n- 保活机制\n- 企业微信通知\n- secrets管理\n- Repository secrets配置"},"finish_reason":"stop"}],"usage":{"prompt_tokens":233,"completion_tokens":101,"total_tokens":334},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86a0c6d6844f670314326fab9ab","object":"chat.completion","created":1734771084,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### 关键词\n- 自动化运行脚本\n- serv00\n- 保活\n- 企业微信机器人\n- 消息推送\n- secrets\n- Repository secrets\n- 账号密钥\n- 企业微信url\n\n### 标签\n- serv00-autologin\n- 自动化\n- 运行脚本\n- 保活机制\n- 企业微信通知\n- secrets管理\n- Repository secrets配置"},"finish_reason":"stop"}],"usage":{"prompt_tokens":233,"completion_tokens":101,"total_tokens":334},"system_fingerprint":""}
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
