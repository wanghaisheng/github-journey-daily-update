---
author: Alice Cooper
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'No description provided.'
featured: true
keywords: {"id":"0193e86249c10ed30ab5ff9f04d8a3a7","object":"chat.completion","created":1734770575,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- landingpage-animation\n- Theatre.js\n- Next.js\n- ContentLayer\n- development\n- deployment\n-_MUX_TOKEN_ID_\n- _MUX_TOKEN_SECRET_\n- mux\n- Git LFS\n- `\u003cMuxVideoWithFallback\u003e`\n- video hosting\n- workflow\n- `\u003cMuxVideoWithFallback\u003e`\n\n### Tags:\n- #Theatre.js\n- #Next.js\n- #ContentLayer\n- #middleware\n- #video-hosting\n- #deployment\n- #environment-variables\n- #git-ignored\n- #video-management\n- #open-source\n- #website-documentation"},"finish_reason":"stop"}],"usage":{"prompt_tokens":392,"completion_tokens":129,"total_tokens":521},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Alice Cooper
  name: author
- content: {"id":"0193e86249c10ed30ab5ff9f04d8a3a7","object":"chat.completion","created":1734770575,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- landingpage-animation\n- Theatre.js\n- Next.js\n- ContentLayer\n- development\n- deployment\n-_MUX_TOKEN_ID_\n- _MUX_TOKEN_SECRET_\n- mux\n- Git LFS\n- `\u003cMuxVideoWithFallback\u003e`\n- video hosting\n- workflow\n- `\u003cMuxVideoWithFallback\u003e`\n\n### Tags:\n- #Theatre.js\n- #Next.js\n- #ContentLayer\n- #middleware\n- #video-hosting\n- #deployment\n- #environment-variables\n- #git-ignored\n- #video-management\n- #open-source\n- #website-documentation"},"finish_reason":"stop"}],"usage":{"prompt_tokens":392,"completion_tokens":129,"total_tokens":521},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86249c10ed30ab5ff9f04d8a3a7","object":"chat.completion","created":1734770575,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- landingpage-animation\n- Theatre.js\n- Next.js\n- ContentLayer\n- development\n- deployment\n-_MUX_TOKEN_ID_\n- _MUX_TOKEN_SECRET_\n- mux\n- Git LFS\n- `\u003cMuxVideoWithFallback\u003e`\n- video hosting\n- workflow\n- `\u003cMuxVideoWithFallback\u003e`\n\n### Tags:\n- #Theatre.js\n- #Next.js\n- #ContentLayer\n- #middleware\n- #video-hosting\n- #deployment\n- #environment-variables\n- #git-ignored\n- #video-management\n- #open-source\n- #website-documentation"},"finish_reason":"stop"}],"usage":{"prompt_tokens":392,"completion_tokens":129,"total_tokens":521},"system_fingerprint":""}
theme: light
title: landingpage-animation
---

# landingpage-animation

## Repository URL: 
[https://github.com/wanghaisheng/landingpage-animation](https://github.com/wanghaisheng/landingpage-animation)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
No description provided.

## README Content: 
# Theatre.js website

The website/documentation for [Theatre.js](https://www.theatrejs.com).

Uses [Next.js](https://nextjs.org/docs) and [ContentLayer](https://www.contentlayer.dev/docs).

## Development

Run `$ npm run dev` to start next.

## Deployment

Pushing to the `production` branch will trigger a deploy.

## Hosting videos

We use [mux](https://mux.com) to host our videos. Here is the workflow for adding videos to the website:

Initially just add the file to the `./public` folder and use `<MuxVideoWithFallback>` to play it. During development, the video will be served from the `./public` folder. When deployed, the video will be served from Mux.

To _actually_ upload the video to Mux, run `$ yarn sync-with-mux`. This will upload all videos in the `./public` folder to Mux (unless they're alraedy there) and update the `./src/mux-db.json` file. `<MuxVideoWithFallback>` will then use the Mux URL instead of the local URL.

Note that you'll need to have the `MUX_TOKEN_ID` and `MUX_TOKEN_SECRET` environment variables set for this to work. Ask teammates to get yours. Don't commit these to the repo. Put them in `.env.production.local` so they'll be gitignored.

_TODO: Use Git LFS to store the videos instead of regular git._

## Credits

Credit goes to [@schickling](https://twitter.com/schickling) of [Contentlayer](https://www.contentlayer.dev) for open-sourcing their website 💚

