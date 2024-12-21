---
author: Alice Cooper
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Use Duckduckgo AI Chat to provide an OpenAI-compatible API that can be used for free with gpt-4o-mini.'
featured: true
keywords: {"id":"0193e85da607c2cd798c9abe047a7d5c","object":"chat.completion","created":1734770271,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Duckduckgo AI Chat\n- OpenAI-compatible API\n- gpt-4o-mini\n- claude-3-haiku\n- llama3.1\n- Docker\n- Render\n- Deno Deploy\n- Deno\n- environment variables\n- request rate limiting\n- cache cleaning\n\n### Tags:\n- #DuckduckgoAIChat\n- #OpenAICompatibleAPI\n- #gpt4oMini\n- #claude3Haiku\n- #llama31\n- #Docker\n- #RenderDeployment\n- #DenoDeploy\n- #Deno\n- #EnvironmentVariables\n- #RateLimiting\n- #CacheManagement"},"finish_reason":"stop"}],"usage":{"prompt_tokens":554,"completion_tokens":145,"total_tokens":699},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Alice Cooper
  name: author
- content: {"id":"0193e85da607c2cd798c9abe047a7d5c","object":"chat.completion","created":1734770271,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Duckduckgo AI Chat\n- OpenAI-compatible API\n- gpt-4o-mini\n- claude-3-haiku\n- llama3.1\n- Docker\n- Render\n- Deno Deploy\n- Deno\n- environment variables\n- request rate limiting\n- cache cleaning\n\n### Tags:\n- #DuckduckgoAIChat\n- #OpenAICompatibleAPI\n- #gpt4oMini\n- #claude3Haiku\n- #llama31\n- #Docker\n- #RenderDeployment\n- #DenoDeploy\n- #Deno\n- #EnvironmentVariables\n- #RateLimiting\n- #CacheManagement"},"finish_reason":"stop"}],"usage":{"prompt_tokens":554,"completion_tokens":145,"total_tokens":699},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e85da607c2cd798c9abe047a7d5c","object":"chat.completion","created":1734770271,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Duckduckgo AI Chat\n- OpenAI-compatible API\n- gpt-4o-mini\n- claude-3-haiku\n- llama3.1\n- Docker\n- Render\n- Deno Deploy\n- Deno\n- environment variables\n- request rate limiting\n- cache cleaning\n\n### Tags:\n- #DuckduckgoAIChat\n- #OpenAICompatibleAPI\n- #gpt4oMini\n- #claude3Haiku\n- #llama31\n- #Docker\n- #RenderDeployment\n- #DenoDeploy\n- #Deno\n- #EnvironmentVariables\n- #RateLimiting\n- #CacheManagement"},"finish_reason":"stop"}],"usage":{"prompt_tokens":554,"completion_tokens":145,"total_tokens":699},"system_fingerprint":""}
theme: light
title: duckduckgo-ai-chat-service
---

# duckduckgo-ai-chat-service

## Repository URL: 
[https://github.com/wanghaisheng/duckduckgo-ai-chat-service](https://github.com/wanghaisheng/duckduckgo-ai-chat-service)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Use Duckduckgo AI Chat to provide an OpenAI-compatible API that can be used for free with gpt-4o-mini.

## README Content: 
# Duckduckgo AI Chat Service

![Docker Pulls](https://img.shields.io/docker/pulls/mumulhl/duckduckgo-ai-chat-service)
![GitHub Tag](https://img.shields.io/github/v/tag/mumu-lhl/duckduckgo-ai-chat-service)

English | [中文](./README_CN.md)

Provide an OpenAI-compatible API for [Duckduckgo AI Chat](https://duckduckgo.com/aichat) that can be used for free with gpt-4o-mini, claude-3-haiku, llama3.1...

## Deploy

### Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/mumu-lhl/duckduckgo-ai-chat-service)

### Docker

```sh
docker run -d mumulhl/duckduckgo-ai-chat-service
```

### Deno Deploy

#### Web

Fork this project, then visit <https://dash.deno.com> and create new project after loging in.

#### Command line

```sh
git clone https://github.com/mumu-lhl/duckduckgo-ai-chat-service --depth 1
deno install -A jsr:@deno/deployctl
deployctl deploy
```

### Deno

```sh
# Run directly
deno run --allow-env --allow-net --unstable-cron https://raw.githubusercontent.com/mumu-lhl/duckduckgo-ai-chat-service/main/main.ts

# Run after installation
deno install -g --allow-env --allow-net --unstable-cron -n duckduckgo-ai-chat-service https://raw.githubusercontent.com/mumu-lhl/duckduckgo-ai-chat-service/main/main.ts
duckduckgo-ai-chat-service
```

## Configuration

Configuration using environment variables:

* TOKEN - Limit the tokens that can access the API, if you don't fill in, any token can access the API.
* LIMIT - limit the request rate per second, default is 2
* CLEAN_CACHE_CRON - how many hours to clean up the cache, default is 1

## Usage

Just change the base url of the place where you need to use the OpenAI API to the one you deployed.

