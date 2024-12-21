---
author: John Doe
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Generate custom placeholder images, powered by Cloudflare Workers in 200+ edge locations'
featured: true
keywords: {"id":"0193e8662792afee4bf09d089eb08f24","object":"chat.completion","created":1734770829,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags:\n1. placeholder images\n2. Cloudflare Workers\n3. custom placeholder images\n4. edge locations\n5. Cloudflare PoPs\n6. image generation\n7. HTMLRewriter\n8. API options\n9. image caching\n10. deployment to Cloudflare Workers\n11. npm run commands\n12. wrangler CLI tool\n13. workers.dev\n14. placeholders.dev\n15. image customization\n16. responsive images\n17. transparency in images\n18. font styling in images"},"finish_reason":"stop"}],"usage":{"prompt_tokens":901,"completion_tokens":117,"total_tokens":1018},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: {"id":"0193e8662792afee4bf09d089eb08f24","object":"chat.completion","created":1734770829,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags:\n1. placeholder images\n2. Cloudflare Workers\n3. custom placeholder images\n4. edge locations\n5. Cloudflare PoPs\n6. image generation\n7. HTMLRewriter\n8. API options\n9. image caching\n10. deployment to Cloudflare Workers\n11. npm run commands\n12. wrangler CLI tool\n13. workers.dev\n14. placeholders.dev\n15. image customization\n16. responsive images\n17. transparency in images\n18. font styling in images"},"finish_reason":"stop"}],"usage":{"prompt_tokens":901,"completion_tokens":117,"total_tokens":1018},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e8662792afee4bf09d089eb08f24","object":"chat.completion","created":1734770829,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags:\n1. placeholder images\n2. Cloudflare Workers\n3. custom placeholder images\n4. edge locations\n5. Cloudflare PoPs\n6. image generation\n7. HTMLRewriter\n8. API options\n9. image caching\n10. deployment to Cloudflare Workers\n11. npm run commands\n12. wrangler CLI tool\n13. workers.dev\n14. placeholders.dev\n15. image customization\n16. responsive images\n17. transparency in images\n18. font styling in images"},"finish_reason":"stop"}],"usage":{"prompt_tokens":901,"completion_tokens":117,"total_tokens":1018},"system_fingerprint":""}
theme: light
title: placeholders-image-astro
---

# placeholders-image-astro

## Repository URL: 
[https://github.com/wanghaisheng/placeholders-image-astro](https://github.com/wanghaisheng/placeholders-image-astro)

## Stars: 
**1**

## Forks: 
**0**

## Description: 
Generate custom placeholder images, powered by Cloudflare Workers in 200+ edge locations

## README Content: 
# [placeholders.dev](https://placeholders.dev)
Generate super-fast placeholder images in 330+ edge locations, powered by Cloudflare Workers
![350x150 placeholder image](https://images.placeholders.dev/?width=350&amp;height=100)![200x100 placeholder image](https://images.placeholders.dev/?width=200&amp;height=100&amp;bgColor=%23000&amp;textColor=rgba(255,255,255,0.5))![140x100 placeholder image](https://images.placeholders.dev/?width=140&amp;height=100&amp;bgColor=%23313131&amp;textColor=%23dfdfde)
![1055x100 placeholder image](https://images.placeholders.dev/?width=1055&amp;height=100&amp;text=Hello%20World&amp;bgColor=%23434343&amp;textColor=%23dfdfde)

[![Deploy to Cloudflare Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/Cherry/placeholders.dev)

## Info

placeholders.dev generates custom placeholder images on the fly, such as the examples above. All of these images are generated on Cloudflare's Edge, at 330+ locations, ensuring the best possible performance for all of your users. All images are cached for lengthy periods of time.

## Technology

This project makes use of Cloudflare Workers, and Cloudflare Workers Sites via Workers KV. It also implements a HTMLRewriter to update the total Cloudflare PoPs in multiple locations.

### Available API Options

- `width`
	- Width of generated image. Defaults to `300`.
- `height`
	- Height of generated image. Defaults to 150.
- `text`
	- Text to display on generated image. Defaults to the image dimensions.
- `fontFamily`
	- Font to use for the text. Defaults to `sans-serif`.
- `fontWeight`
	- Font weight to use for the text. Defaults to `bold`.
- `fontSize`
	- Font size to use for the text. Defaults to 20% of the shortest image dimension, rounded down.
- `dy`
	- Adjustment applied to the dy attribute of the text element to appear vertically centered. Defaults to 35% of the font size.
- `bgColor`
	- Background color of the image. Defaults to `#ddd`
- `textColor`
	- Color of the text. For transparency, use an rgba or hsla value. Defaults to `rgba(0,0,0,0.5)`
- `textWrap`
	- Wrap text to fit within the image (to best ability). Will not alter font size, so especially long strings may still appear outside of the image. Defaults to `false`.

Example URL: `https://placeholders.shopconna.com/?width=1055&height=100&text=Made%20with%20placeholders.dev&bgColor=%23f7f6f6&textColor=%236d6e71`
## Dev

### Prerequisites

#### Wrangler
`wrangler` is a CLI tool from Cloudflare, designed to push projects to Cloudflare Workers. See [Cloudflare's documentation](https://developers.cloudflare.com/workers/wrangler/install-and-update/) for more information.

### Run

- `npm run start:dev` (this will use `wrangler dev` to locally start the Cloudflare Worker for testing)

or

- `npm run publish` (push to `placeholders-dev` workers.dev)

or

- `npm run publish:staging` (push to `placeholders-staging` workers.dev)

## Production

- `npm run publish:prod` (publishes to placeholders.dev via Workers)

