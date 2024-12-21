---
author: John Doe
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Swish, more like a song wish service built on top of Cloudflare Workers, Cloudflare Pages, PostgreSQL, Lavalink using Pants, TypeScript, Go and Astro for GKŠM'
featured: true
keywords: {"id":"0193e86a6711e0c8d097933636ad8dfa","object":"chat.completion","created":1734771107,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags\n\n1. **Swish**\n2. **Song Wish**\n3. **Web Application**\n4. **Queue System**\n5. **Cloudflare Workers**\n6. **Cloudflare Pages**\n7. **PostgreSQL**\n8. **Lavalink**\n9. **Pants Build Tool**\n10. **TypeScript**\n11. **Go Programming Language**\n12. **Astro Framework**\n13. **Computer Application**\n14. **Build Tools**\n15. **Deployment**\n16. **Queue Management**\n17. **Node.js**\n18. **pnpm**\n19. **golang**\n20. **Web Development**\n21. **Serverless**\n22. **Database Management**\n23. **Realtime Audio Processing**\n24. **Dynamic Web Pages**\n25. **API Development**\n\n### Tags\n- Web Application\n- Serverless\n- Cloud Infrastructure\n- Realtime Audio\n- Database Integration\n- Build Tools\n- Deployment Scripts\n- Dynamic Web Pages\n- Queue Management\n- Real-time Processing"},"finish_reason":"stop"}],"usage":{"prompt_tokens":350,"completion_tokens":225,"total_tokens":575},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: {"id":"0193e86a6711e0c8d097933636ad8dfa","object":"chat.completion","created":1734771107,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags\n\n1. **Swish**\n2. **Song Wish**\n3. **Web Application**\n4. **Queue System**\n5. **Cloudflare Workers**\n6. **Cloudflare Pages**\n7. **PostgreSQL**\n8. **Lavalink**\n9. **Pants Build Tool**\n10. **TypeScript**\n11. **Go Programming Language**\n12. **Astro Framework**\n13. **Computer Application**\n14. **Build Tools**\n15. **Deployment**\n16. **Queue Management**\n17. **Node.js**\n18. **pnpm**\n19. **golang**\n20. **Web Development**\n21. **Serverless**\n22. **Database Management**\n23. **Realtime Audio Processing**\n24. **Dynamic Web Pages**\n25. **API Development**\n\n### Tags\n- Web Application\n- Serverless\n- Cloud Infrastructure\n- Realtime Audio\n- Database Integration\n- Build Tools\n- Deployment Scripts\n- Dynamic Web Pages\n- Queue Management\n- Real-time Processing"},"finish_reason":"stop"}],"usage":{"prompt_tokens":350,"completion_tokens":225,"total_tokens":575},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86a6711e0c8d097933636ad8dfa","object":"chat.completion","created":1734771107,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags\n\n1. **Swish**\n2. **Song Wish**\n3. **Web Application**\n4. **Queue System**\n5. **Cloudflare Workers**\n6. **Cloudflare Pages**\n7. **PostgreSQL**\n8. **Lavalink**\n9. **Pants Build Tool**\n10. **TypeScript**\n11. **Go Programming Language**\n12. **Astro Framework**\n13. **Computer Application**\n14. **Build Tools**\n15. **Deployment**\n16. **Queue Management**\n17. **Node.js**\n18. **pnpm**\n19. **golang**\n20. **Web Development**\n21. **Serverless**\n22. **Database Management**\n23. **Realtime Audio Processing**\n24. **Dynamic Web Pages**\n25. **API Development**\n\n### Tags\n- Web Application\n- Serverless\n- Cloud Infrastructure\n- Realtime Audio\n- Database Integration\n- Build Tools\n- Deployment Scripts\n- Dynamic Web Pages\n- Queue Management\n- Real-time Processing"},"finish_reason":"stop"}],"usage":{"prompt_tokens":350,"completion_tokens":225,"total_tokens":575},"system_fingerprint":""}
theme: light
title: swish
---

# swish

## Repository URL: 
[https://github.com/wanghaisheng/swish](https://github.com/wanghaisheng/swish)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Swish, more like a song wish service built on top of Cloudflare Workers, Cloudflare Pages, PostgreSQL, Lavalink using Pants, TypeScript, Go and Astro for GKŠM

## README Content: 
update

**Swish** stands for **Song Wish**, it's a web application that allows users to search for songs and submit them to a queue. The queue is handled by an app that runs on a computer.

Built on top of [Cloudflare Workers](https://workers.cloudflare.com/), [Cloudflare Pages](https://pages.cloudflare.com/), [PostgreSQL](https://www.postgresql.org/), [Lavalink](https://lavalink.dev/) using [Pants](https://www.pantsbuild.org/), [TypeScript](https://www.typescriptlang.org/), [Go](https://golang.org/) and [Astro](https://astro.build/) for GKŠM.

## Requirements

- [pants](https://www.pantsbuild.org/)
- [node.js](https://nodejs.org/)
- [pnpm](https://pnpm.js.org/)
- [golang](https://golang.org/)

## Structure

- `page/` contains the web application, written in Astro.
- `api/` contains the worker that handles requests from the web application and adds them to the queue, written in TypeScript.
- `app/` contains the app that handles the queue, written in Go.
- `scripts/` contains scripts to build, deploy and run easily.

