---
author: Jane Smith
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734782313939_wwqusi
  url: https://fluxapi.borninsea.com/image/image_1734782313939_wwqusi
description: 'Given any image (GIF, PNG, WebP, AVIF, etc) extract predominant & palette colors.'
featured: true
keywords: 图像处理,颜色提取,WebP,AVIF,GIF,PNG,Logo,Banner,GitHub,Node.js,NPM,颜色调色板,色彩分析,微服务,ARIA,MIT许可,contributor列表
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: 图像处理,颜色提取,WebP,AVIF,GIF,PNG,Logo,Banner,GitHub,Node.js,NPM,颜色调色板,色彩分析,微服务,ARIA,MIT许可,contributor列表
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- gif,png,webp,avif,color_extraction,predominant_colors,palette_colors,image_processing,js_module,npm_package,microservice,aria_compliance
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


