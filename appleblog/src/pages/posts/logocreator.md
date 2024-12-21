---
author: Alice Cooper
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'A free + OSS logo generator powered by Flux on Together AI'
featured: true
keywords: {"id":"0193e862d91170fa44031d4c5f571b73","object":"chat.completion","created":1734770612,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- logocreator\n- free\n- OSS (Open Source Software)\n- logo generator\n- Flux Pro\n- Together AI\n- Next.js\n- TypeScript\n- Shadcn\n- Tailwind CSS\n- Upstash Redis\n- rate limiting\n- Clerk\n- authentication\n- Plausible\n- Helicone\n- analytics\n- observability\n- future tasks\n- dashboard\n- user's logo history\n- SVG exports\n- additional styles\n- image size\n- approximate price\n- Together AI API key\n- vision model\n- reference logo\n- redesign\n- popular brand’s logos\n\n### Tags:\n- AI\n- Logo Creation\n- Open Source\n- Web Development\n- Machine Learning\n- API Integration\n- User Interface\n- Rate Limiting\n- Authentication\n- Analytics\n- Future Enhancements"},"finish_reason":"stop"}],"usage":{"prompt_tokens":472,"completion_tokens":174,"total_tokens":646},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Alice Cooper
  name: author
- content: {"id":"0193e862d91170fa44031d4c5f571b73","object":"chat.completion","created":1734770612,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- logocreator\n- free\n- OSS (Open Source Software)\n- logo generator\n- Flux Pro\n- Together AI\n- Next.js\n- TypeScript\n- Shadcn\n- Tailwind CSS\n- Upstash Redis\n- rate limiting\n- Clerk\n- authentication\n- Plausible\n- Helicone\n- analytics\n- observability\n- future tasks\n- dashboard\n- user's logo history\n- SVG exports\n- additional styles\n- image size\n- approximate price\n- Together AI API key\n- vision model\n- reference logo\n- redesign\n- popular brand’s logos\n\n### Tags:\n- AI\n- Logo Creation\n- Open Source\n- Web Development\n- Machine Learning\n- API Integration\n- User Interface\n- Rate Limiting\n- Authentication\n- Analytics\n- Future Enhancements"},"finish_reason":"stop"}],"usage":{"prompt_tokens":472,"completion_tokens":174,"total_tokens":646},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e862d91170fa44031d4c5f571b73","object":"chat.completion","created":1734770612,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- logocreator\n- free\n- OSS (Open Source Software)\n- logo generator\n- Flux Pro\n- Together AI\n- Next.js\n- TypeScript\n- Shadcn\n- Tailwind CSS\n- Upstash Redis\n- rate limiting\n- Clerk\n- authentication\n- Plausible\n- Helicone\n- analytics\n- observability\n- future tasks\n- dashboard\n- user's logo history\n- SVG exports\n- additional styles\n- image size\n- approximate price\n- Together AI API key\n- vision model\n- reference logo\n- redesign\n- popular brand’s logos\n\n### Tags:\n- AI\n- Logo Creation\n- Open Source\n- Web Development\n- Machine Learning\n- API Integration\n- User Interface\n- Rate Limiting\n- Authentication\n- Analytics\n- Future Enhancements"},"finish_reason":"stop"}],"usage":{"prompt_tokens":472,"completion_tokens":174,"total_tokens":646},"system_fingerprint":""}
theme: light
title: logocreator
---

# logocreator

## Repository URL: 
[https://github.com/wanghaisheng/logocreator](https://github.com/wanghaisheng/logocreator)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
A free + OSS logo generator powered by Flux on Together AI

## README Content: 
<a href="https://www.logo-creator.io">
  <img alt="AI Logo Generator" src="./public/og-image.png">
  <h1 align="center">AI Logo Generator</h1>
</a>

<p align="center">
  An open source logo generator – create professional logos in seconds with customizable styles.
</p>

## Tech stack

- [Flux Pro 1.1](https://dub.sh/flux-playground) on [Together AI](https://dub.sh/together-ai) for logo generation
- [Next.js](https://nextjs.org/) with TypeScript for the app framework
- [Shadcn](https://ui.shadcn.com/) for UI components & [Tailwind](https://tailwindcss.com/) for styling
- [Upstash Redis](https://upstash.com/) for rate limiting
- [Clerk](https://clerk.com/) for authentication
- [Plausible](https://plausible.io/) & [Helicone](https://helicone.ai/) for analytics & observability

## Cloning & running

1. Clone the repo: `git clone https://github.com/Nutlope/logocreator`
2. Create a `.env` file and add your [Together AI API key](https://api.together.xyz/settings/api-keys): `TOGETHER_API_KEY=`
3. Run `npm install` and `npm run dev` to install dependencies and run locally.

## Future Tasks

- [ ] Create a dashboard with a user's logo history
- [ ] Support SVG exports instead of just PNG
- [ ] Add support for additional styles
- [ ] Add a dropdown for image size (can do up to 1440x1440)
- [ ] Show approximate price when using your own Together AI key
- [ ] Allow the ability to upload a reference logo (use vision model to read it)
- [ ] Redesign popular brand’s logos with my logo maker and have it in a showcase

