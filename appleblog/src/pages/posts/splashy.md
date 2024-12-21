---
author: Bob Johnson
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Given any image (GIF, PNG, WebP, AVIF, etc) extract predominant & palette colors.'
featured: true
keywords: {"id":"0193e869d755314a1f0fa4080be4ecf2","object":"chat.completion","created":1734771070,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags Extraction\n\nFrom the provided text, the key points that can be extracted as keywords and tags focus on the functionality and usage of the `splashy` package. Here are the relevant keywords and tags:\n\n**Keywords:**\n1. splashy\n2. image analysis\n3. color extraction\n4. predominant colors\n5. palette colors\n6. image formats\n7. URL\n8. buffer\n9. npm package\n10. npm\n\n**Tags:**\n1. `#image-analysis`\n2. `#color-extraction`\n3. `#npm`\n4. `#javascript`\n5. `#nodejs`\n6. `#streaming`\n7. `#image-processing`\n8. `#palette`\n9. `#predominant-colors`\n\nThese tags and keywords capture the essence of the `splashy` package and its functionalities, as well as its integration with JavaScript and Node.js environments."},"finish_reason":"stop"}],"usage":{"prompt_tokens":833,"completion_tokens":194,"total_tokens":1027},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Bob Johnson
  name: author
- content: {"id":"0193e869d755314a1f0fa4080be4ecf2","object":"chat.completion","created":1734771070,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags Extraction\n\nFrom the provided text, the key points that can be extracted as keywords and tags focus on the functionality and usage of the `splashy` package. Here are the relevant keywords and tags:\n\n**Keywords:**\n1. splashy\n2. image analysis\n3. color extraction\n4. predominant colors\n5. palette colors\n6. image formats\n7. URL\n8. buffer\n9. npm package\n10. npm\n\n**Tags:**\n1. `#image-analysis`\n2. `#color-extraction`\n3. `#npm`\n4. `#javascript`\n5. `#nodejs`\n6. `#streaming`\n7. `#image-processing`\n8. `#palette`\n9. `#predominant-colors`\n\nThese tags and keywords capture the essence of the `splashy` package and its functionalities, as well as its integration with JavaScript and Node.js environments."},"finish_reason":"stop"}],"usage":{"prompt_tokens":833,"completion_tokens":194,"total_tokens":1027},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e869d755314a1f0fa4080be4ecf2","object":"chat.completion","created":1734771070,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags Extraction\n\nFrom the provided text, the key points that can be extracted as keywords and tags focus on the functionality and usage of the `splashy` package. Here are the relevant keywords and tags:\n\n**Keywords:**\n1. splashy\n2. image analysis\n3. color extraction\n4. predominant colors\n5. palette colors\n6. image formats\n7. URL\n8. buffer\n9. npm package\n10. npm\n\n**Tags:**\n1. `#image-analysis`\n2. `#color-extraction`\n3. `#npm`\n4. `#javascript`\n5. `#nodejs`\n6. `#streaming`\n7. `#image-processing`\n8. `#palette`\n9. `#predominant-colors`\n\nThese tags and keywords capture the essence of the `splashy` package and its functionalities, as well as its integration with JavaScript and Node.js environments."},"finish_reason":"stop"}],"usage":{"prompt_tokens":833,"completion_tokens":194,"total_tokens":1027},"system_fingerprint":""}
theme: light
title: splashy
---

# splashy

## Repository URL: 
[https://github.com/wanghaisheng/splashy](https://github.com/wanghaisheng/splashy)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Given any image (GIF, PNG, WebP, AVIF, etc) extract predominant & palette colors.

## README Content: 
<div align="center">
  <img src="https://github.com/microlinkhq/cdn/raw/master/dist/logo/banner.png#gh-light-mode-only" alt="microlink logo">
  <img src="https://github.com/microlinkhq/cdn/raw/master/dist/logo/banner-dark.png#gh-dark-mode-only" alt="microlink logo">
  <br>
  <br>
</div>

![Last version](https://img.shields.io/github/tag/microlinkhq/splashy.svg?style=flat-square)
[![Coverage Status](https://img.shields.io/coveralls/microlinkhq/splashy.svg?style=flat-square)](https://coveralls.io/github/microlinkhq/splashy)
[![NPM Status](https://img.shields.io/npm/dm/splashy.svg?style=flat-square)](https://www.npmjs.org/package/splashy)

> Given an image, extract predominant & palette colors. [20+ image formats well tested](https://github.com/microlinkhq/splashy/tree/master/test/fixtures).

## Install

```bash
$ npm install splashy --save
```

## Usage

### From URL

```js
(async () => {
  const splashy = require('splashy')
  const got = require('got')

  const url = 'https://kikobeats.com/images/avatar.jpg'
  const { body } = await got(url, { responseType: 'buffer' })
  const palette = await splashy(body)

  console.log(palette)
  // => [ '#941c1c', '#841c16', '#aa695e', '#ca866c', '#6c5444', '#cca4a4' ]
})()
```

### From Buffer

```js
(async () => {
  const splashy = require('splashy')
  const path = require('path')
  const fs = require('fs')

  const filepath = path.resolve(__dirname, 'avatar.jpg')
  const buffer = await fs.readFile(filepath)
  const palette = await splashy(buffer)

  console.log(palette)
  // => [ '#941c1c', '#841c16', '#aa695e', '#ca866c', '#6c5444', '#cca4a4' ]
})()
```

## API

### splashy(input)

#### input

*Required*<br>
Type: [ImageSource](https://github.com/akfish/node-vibrant#imagesource)

The raw content for detecting the color information.

## Related

- [color-microservice](https://github.com/Kikobeats/color-microservice) – Get color information from any URL image microservice.
- [colorable-dominant](https://github.com/Kikobeats/colorable-dominant) – Create ARIA-compliant color themes based on a predominant color palette.

## License

**microlink-function** © [Microlink](https://microlink.io), released under the [MIT](https://github.com/microlink/microlink-function/blob/master/LICENSE.md) License.<br>
Authored and maintained by [Kiko Beats](https://kikobeats.com) with help from [contributors](https://github.com/microlink/microlink-function/contributors).

> [microlink.io](https://microlink.io) · GitHub [microlinkhq](https://github.com/microlinkhq) · X [@microlinkhq](https://x.com/microlinkhq)


