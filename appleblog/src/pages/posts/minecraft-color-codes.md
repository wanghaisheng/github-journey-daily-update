---
author: John Doe
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'a tool to help user generate text use minecraft color codes and available fonts'
featured: true
keywords: {"id":"0193e863ad951beda8b7618f632bf3f8","object":"chat.completion","created":1734770666,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- Minecraft color codes\n- Font Generator\n- Installation\n- Development server\n- Cloudflare Pages\n- Docker Image\n- Contributing\n- License\n\n### Tags\n- #FontGenerator\n- #MinecraftColorCodes\n- #Installation\n- #DevelopmentServer\n- #CloudflarePages\n- #DockerImage\n- #Contributing\n- #License"},"finish_reason":"stop"}],"usage":{"prompt_tokens":398,"completion_tokens":79,"total_tokens":477},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: {"id":"0193e863ad951beda8b7618f632bf3f8","object":"chat.completion","created":1734770666,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- Minecraft color codes\n- Font Generator\n- Installation\n- Development server\n- Cloudflare Pages\n- Docker Image\n- Contributing\n- License\n\n### Tags\n- #FontGenerator\n- #MinecraftColorCodes\n- #Installation\n- #DevelopmentServer\n- #CloudflarePages\n- #DockerImage\n- #Contributing\n- #License"},"finish_reason":"stop"}],"usage":{"prompt_tokens":398,"completion_tokens":79,"total_tokens":477},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e863ad951beda8b7618f632bf3f8","object":"chat.completion","created":1734770666,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- Minecraft color codes\n- Font Generator\n- Installation\n- Development server\n- Cloudflare Pages\n- Docker Image\n- Contributing\n- License\n\n### Tags\n- #FontGenerator\n- #MinecraftColorCodes\n- #Installation\n- #DevelopmentServer\n- #CloudflarePages\n- #DockerImage\n- #Contributing\n- #License"},"finish_reason":"stop"}],"usage":{"prompt_tokens":398,"completion_tokens":79,"total_tokens":477},"system_fingerprint":""}
theme: light
title: minecraft-color-codes
---

# minecraft-color-codes

## Repository URL: 
[https://github.com/wanghaisheng/minecraft-color-codes](https://github.com/wanghaisheng/minecraft-color-codes)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
a tool to help user generate text use minecraft color codes and available fonts

## README Content: 
# Font Generator

2024-10-17

 
## Installation

To set up the Font Generator project locally, follow these steps:

1. Clone the repository:

```sh
git clone https://github.com/seadfeng/font-generator.git
cd font-generator
```

2. Install dependencies:

```sh
npm install
# or
yarn install
# or
pnpm install
```

## Usage Guide

### Running the Development Server

To start the development server, run one of the following commands:

```sh
npm run dev
# or
# yarn dev
or
# pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser to see the result.

## Deploy to Cloudflare Pages

### Local Deploy

Simple Deployment

```sh
# install wrangler
npm install -g wrangler

# Cloudflare Login 
wrangler login

# Deploy to Cloudflare Pages
npm run deploy
```


## Docker Image

```sh
docker pull seadfeng/font-generator
docker run -p 3000:3000 seadfeng/font-generator
```

## Resource
 
`src/fonts.ts` Source of Unicode font:

- [unicode-formatter](https://github.com/DenverCoder1/unicode-formatter)
- [yaytext.com](https://yaytext.com/)

## Contributing

We welcome contributions to the Font Generator project. Please feel free to submit issues, feature requests, or pull requests.

## License

[MIT License](MIT-LICENSE)

