---
author: Bob Johnson
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: '自建企业邮箱，构建你自己的域名邮箱，无需服务器 / Self built email / Build your own domain email without the need for a server'
featured: true
keywords: {"id":"0193e85d60621cf36da1c1b5c8711250","object":"chat.completion","created":1734770253,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- 自建企业邮箱\n- 域名邮箱\n- Cloudflare\n- 无需服务器\n- 一键部署\n- 手动部署\n- 待办清单\n- 邮件详情\n- 权限设计\n- 用户状态\n- 富文本编辑器\n- API 接口\n- 移动端支持\n\n### Tags\n- Email\n- Cloudflare\n- Self-Hosted\n- Serverless\n- Tutorial\n- Tutorial Documentation\n- Feature List\n- Deployment Methods\n- API\n- UI\n- Database"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1636,"completion_tokens":122,"total_tokens":1758},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Bob Johnson
  name: author
- content: {"id":"0193e85d60621cf36da1c1b5c8711250","object":"chat.completion","created":1734770253,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- 自建企业邮箱\n- 域名邮箱\n- Cloudflare\n- 无需服务器\n- 一键部署\n- 手动部署\n- 待办清单\n- 邮件详情\n- 权限设计\n- 用户状态\n- 富文本编辑器\n- API 接口\n- 移动端支持\n\n### Tags\n- Email\n- Cloudflare\n- Self-Hosted\n- Serverless\n- Tutorial\n- Tutorial Documentation\n- Feature List\n- Deployment Methods\n- API\n- UI\n- Database"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1636,"completion_tokens":122,"total_tokens":1758},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e85d60621cf36da1c1b5c8711250","object":"chat.completion","created":1734770253,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- 自建企业邮箱\n- 域名邮箱\n- Cloudflare\n- 无需服务器\n- 一键部署\n- 手动部署\n- 待办清单\n- 邮件详情\n- 权限设计\n- 用户状态\n- 富文本编辑器\n- API 接口\n- 移动端支持\n\n### Tags\n- Email\n- Cloudflare\n- Self-Hosted\n- Serverless\n- Tutorial\n- Tutorial Documentation\n- Feature List\n- Deployment Methods\n- API\n- UI\n- Database"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1636,"completion_tokens":122,"total_tokens":1758},"system_fingerprint":""}
theme: light
title: domain-email-on-cloudflare
---

# domain-email-on-cloudflare

## Repository URL: 
[https://github.com/wanghaisheng/domain-email-on-cloudflare](https://github.com/wanghaisheng/domain-email-on-cloudflare)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
自建企业邮箱，构建你自己的域名邮箱，无需服务器 / Self built email / Build your own domain email without the need for a server

## README Content: 
1206

<div align="center">
  <img src="https://raw.githubusercontent.com/hocgin/yourself-email/main/docs/logo.svg" alt="onedrive-cf-index-ng" width="250px" />
  <h3><a href="/">yourself-email</a></h3>
  <p><em>使用 Cloudflare 来构建你自己的邮件系统，无需服务器</em></p>

  <a href="https://deploy.workers.cloudflare.com/?url=https://github.com/hocgin/yourself-email">
    <img height="20" src="https://deploy.workers.cloudflare.com/button" alt="Deploy" />
  </a>
  <img src="https://img.shields.io/badge/Cloudflare-f38020?style=flat&logo=Cloudflare&logoColor=white" alt="Cloudflare" />
  <a href="https://github.com/hocgin/yourself-email/blob/main/docs/lang/zh-CN/README.md"><img src="https://img.shields.io/badge/中文-black?title=en&style=flat&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABmJLR0QA/wD/AP+gvaeTAAABeUlEQVRIie2VwUrDQBCGZ5ZubNmS0Ba9tF6CUqTHpg+g+AhCn8R30DfpM3jRezdHoZJroaBJQ2qgsIEdD7YSsCtJVBTxP87u/t/u7M4swDcLTQNSSseyLFbERCmlPc9LCgF83z/jnE9s294vvk+AJEmesiwbe553awQEQbCXZVnY7/ebjBXa/Ju01jCbzVIA6AwGA7WN1/KT4jg+6vV6TcYYpGlKq9UKiQgAAOr1OnU6HWNKGWPQarWa8/n8GADudwIQ0UJ89QjDEKMoOiEitRm7tm37gnNuPAUiAiJa+VjNNJmIYDgcPiAiAQD4vh9tT1NG5RJdQT8PkFKak/5ZgJTyUgjxPJ1Ob4josArAeMmWZYHrulftdhvX6/X5YrEwPtFKgG63C7ApxEajga7rVvH/BZf8D/hjACJSVRpabj1su+9OgBAiiOM41VqXNtdaw3K5TIUQQT7+rjqllKec84njOAdlAEmSPCqlxqPR6O5DQA70JZ/+t+sFAb2R22dSZ7wAAAAASUVORK5CYII=" alt="Documentation" /></a>
  <a href="https://github.com/hocgin/yourself-email/blob/main/docs/lang/en/README.md"><img src="https://img.shields.io/badge/English-black?title=en&style=flat&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABmJLR0QA/wD/AP+gvaeTAAABeUlEQVRIie2VwUrDQBCGZ5ZubNmS0Ba9tF6CUqTHpg+g+AhCn8R30DfpM3jRezdHoZJroaBJQ2qgsIEdD7YSsCtJVBTxP87u/t/u7M4swDcLTQNSSseyLFbERCmlPc9LCgF83z/jnE9s294vvk+AJEmesiwbe553awQEQbCXZVnY7/ebjBXa/Ju01jCbzVIA6AwGA7WN1/KT4jg+6vV6TcYYpGlKq9UKiQgAAOr1OnU6HWNKGWPQarWa8/n8GADudwIQ0UJ89QjDEKMoOiEitRm7tm37gnNuPAUiAiJa+VjNNJmIYDgcPiAiAQD4vh9tT1NG5RJdQT8PkFKak/5ZgJTyUgjxPJ1Ob4josArAeMmWZYHrulftdhvX6/X5YrEwPtFKgG63C7ApxEajga7rVvH/BZf8D/hjACJSVRpabj1su+9OgBAiiOM41VqXNtdaw3K5TIUQQT7+rjqllKec84njOAdlAEmSPCqlxqPR6O5DQA70JZ/+t+sFAb2R22dSZ7wAAAAASUVORK5CYII=" alt="Documentation" /></a>
</div>

### 效果展示

> 演示地址: http://mail.hocg.in, 使用你的任意邮箱登录。
>
> 目前已配置默认权限，登录后可以可读/发邮箱: test@hocg.in 和 test2@hocg.in

<div style="display:inline-block">
  <img src="docs/tutorial/demo.c1.png" width="45%"/>
  <img src="docs/tutorial/demo.c2.png" width="45%"/>
</div>

### 部署方式

**方式一** [一键部署(≈5分钟)](./docs/lang/zh-CN/One-ClickDeployment.md)

**方式二** [手动部署(≈30分钟)](./docs/lang/zh-CN/ManualTutorial.md)

### 待办清单

<details>

<summary>待办清单</summary>

- [x] 标记已读
- [x] 归档
- [x] 回收站
- [ ] 回收站、彻底删除
- [ ] 邮件添加标签
- [ ] 邮件详情，发送者显示邮件头部信息
- [x] 邮件详情，查询与X用户沟通历史
- [x] 权限设计实现
- [x] 用户状态，查询未读数量、权限账号列表
- [ ] 支持富文本编辑器
- [ ] 整理/开发 API 接口
- [x] 移动端支持

</details>

----

### 相关资料

- [Shadcn UI](https://ui.shadcn.com/)
- [Prisma](https://www.prisma.io)
- [Cloudflare D1](https://developers.cloudflare.com/d1/build-with-d1)
- [MailChannels API](https://api.mailchannels.net/tx/v1/documentation)


