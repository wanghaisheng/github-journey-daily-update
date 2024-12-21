---
author: Alice Cooper
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'DRG Completionist is a free, open-source online progress tracker for Deep Rock Galactic. It's designed to help keep track of all the different overclocks and cosmetics available for hard-working employees like yourselves, as well as to serve as an handy reference for overclock data.'
featured: true
keywords: {"id":"0193e85d84f079f28ed66b00b1d4bc14","object":"chat.completion","created":1734770263,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- DRG Completionist\n- Deep Rock Galactic\n- Progress tracker\n- Overclocks\n- Cosmetics\n- Open-source\n- Free\n- Progressive Web App (PWA)\n- Save file parsing\n- WebAssembly (WASM)\n- Umami\n- Privacy\n- Serverless\n- Custom snazzy tools\n\n### Tags:\n- DRG Completionist\n- DRG\n- Online Progress Tracker\n- Deep Rock Galactic\n- Overclocks\n- Cosmetics\n- Open Source\n- Free Software\n- PWA\n- Save File Parsing\n- WebAssembly\n- Privacy-Focused\n- Analytics\n- GitHub\n- Rust\n- Umami Analytics"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1058,"completion_tokens":143,"total_tokens":1201},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Alice Cooper
  name: author
- content: {"id":"0193e85d84f079f28ed66b00b1d4bc14","object":"chat.completion","created":1734770263,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- DRG Completionist\n- Deep Rock Galactic\n- Progress tracker\n- Overclocks\n- Cosmetics\n- Open-source\n- Free\n- Progressive Web App (PWA)\n- Save file parsing\n- WebAssembly (WASM)\n- Umami\n- Privacy\n- Serverless\n- Custom snazzy tools\n\n### Tags:\n- DRG Completionist\n- DRG\n- Online Progress Tracker\n- Deep Rock Galactic\n- Overclocks\n- Cosmetics\n- Open Source\n- Free Software\n- PWA\n- Save File Parsing\n- WebAssembly\n- Privacy-Focused\n- Analytics\n- GitHub\n- Rust\n- Umami Analytics"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1058,"completion_tokens":143,"total_tokens":1201},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e85d84f079f28ed66b00b1d4bc14","object":"chat.completion","created":1734770263,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- DRG Completionist\n- Deep Rock Galactic\n- Progress tracker\n- Overclocks\n- Cosmetics\n- Open-source\n- Free\n- Progressive Web App (PWA)\n- Save file parsing\n- WebAssembly (WASM)\n- Umami\n- Privacy\n- Serverless\n- Custom snazzy tools\n\n### Tags:\n- DRG Completionist\n- DRG\n- Online Progress Tracker\n- Deep Rock Galactic\n- Overclocks\n- Cosmetics\n- Open Source\n- Free Software\n- PWA\n- Save File Parsing\n- WebAssembly\n- Privacy-Focused\n- Analytics\n- GitHub\n- Rust\n- Umami Analytics"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1058,"completion_tokens":143,"total_tokens":1201},"system_fingerprint":""}
theme: light
title: drg-completionist
---

# drg-completionist

## Repository URL: 
[https://github.com/wanghaisheng/drg-completionist](https://github.com/wanghaisheng/drg-completionist)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
DRG Completionist is a free, open-source online progress tracker for Deep Rock Galactic. It's designed to help keep track of all the different overclocks and cosmetics available for hard-working employees like yourselves, as well as to serve as an handy reference for overclock data.

## README Content: 
# DRG Completionist

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/spicyboys/drg-completionist?color=darkgreen)](https://github.com/spicyboys/drg-completionist/releases)
[![GitHub stars](https://img.shields.io/github/stars/spicyboys/drg-completionist)](https://github.com/spicyboys/drg-completionist/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/spicyboys/drg-completionist)](https://github.com/spicyboys/drg-completionist/issues)
[![GitHub license](https://img.shields.io/github/license/spicyboys/drg-completionist?color=darkred)](https://github.com/spicyboys/drg-completionist/blob/main/LICENSE)

_[DRG Completionist](https://drg-completionist.com/)_ is a free, open-source online progress tracker for [Deep Rock Galactic](https://www.deeprockgalactic.com/). It's designed to help keep track of all the different overclocks and cosmetics available for hard-working employees like yourselves, as well as to serve as an handy reference for overclock data.

_DRG Completionist_ is a fully-fledged [Progressive Web App (PWA)](https://en.wikipedia.org/wiki/Progressive_web_application), which means it will automatically continue to function without an Internet connection and can be installed as a stand-alone app on supported browsers _(e.g., Google Chrome, Microsoft Edge, Safari on iOS)_. The app is also responsively designed for both desktop and mobile use, and it supports using both mouse and touchscreen on nearly any screen size. We recommend installing this app via your browser for the best experience.

While progress can be input by clicking and tapping the old-fashioned way, _DRG Completionist_ also utilizes a custom snazzy [WASM](https://en.wikipedia.org/wiki/WebAssembly)-based [save file parsing tool](https://github.com/rob0rt/drg-save-parser/) that locally analyzes your PC's Deep Rock Galactic save file. Simply upload your save file and the Save Parser will automatically input your current progress into each page so you don't have to!

_The Steam save file is located here by default on Windows, but may vary based on your install location:_

`C:\Program Files (x86)\Steam\steamapps\common\Deep Rock Galactic\FSD\Saved\SaveGames\{steam_ID}_Player.sav`

## Upcoming Features

- Re-introducing collectables that have not been migrated to DRG-Completionist v5

## Privacy

_DRG Completionist_ respects your privacy. The app is entirely serverless and uses the browser's local storage to keep track of your progress. No personally identifying information is ever collected or stored.

If you choose to upload your save file, neither the file nor its contents ever leaves your computer. The save file parser is compiled from [Rust](<https://en.wikipedia.org/wiki/Rust_(programming_language)>) into [WASM](https://en.wikipedia.org/wiki/WebAssembly) specifically so it can run completely within your browser. We encourage you to [inspect the source code](https://github.com/rob0rt/drg-save-parser) if you want to see what it's doing.

For site usage analytics, we utilize [Umami](https://umami.is/), an anonymoized, privacy-focused web analytics platform. If you use any of the privacy-oriented browser settings or extensions that are widely available today, or your browser sends the [Do Not Track](https://www.eff.org/issues/do-not-track) signal, these analytics will be blocked. You can inspect the integration with Umami in [gatsby-ssr.tsx](gatsby-ssr.tsx).

## Special Thanks

- The folks who maintain the [Deep Rock Galactic Wiki](https://deeprockgalactic.wiki.gg/wiki/Deep_Rock_Galactic_Wiki), which provided all the pictures and data that make this app run
- [@iAmAsval](https://github.com/iAmAsval) for their work on [FModel](https://github.com/iAmAsval/FModel) that let us move forward with identifying the cosmetic GUIDs in the save file
- The helpful folks on the _DRG Community Tools_ Discord server, who always helped us out with our questions

## Disclaimer

Neither this app nor its developers are associated with Deep Rock Galactic or Ghost Ship Games in any way. _(But we really admire what they do.)_

---

###### README Last Updated: July 27, 2023

