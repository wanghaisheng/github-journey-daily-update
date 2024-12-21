---
author: John Doe
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Realtime VRM Humanoid Avatar Animation using Human Library and ThreeJS'
featured: true
keywords: {"id":"0193e86123f4008d47787c5d0636c153","object":"chat.completion","created":1734770500,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Human VRM\n- Realtime VRM Animation\n- Humanoid Avatar\n- Human Library\n- ThreeJS\n- TypeScript\n- VRM Model\n- Face Tracking\n- Body Tracking\n- Hand Tracking\n- GLTF VRM\n- WebRTC\n- Internal HTTP Server\n- HTTPS\n- Development Environment\n- Project Logs\n\n### Tags:\n- VRM Technology\n- Realtime Animation\n- 3D Human Avatars\n- Human Tracking\n- Web Development\n- TypeScript Projects\n- GLTF Models\n- CORS\n- Web Server\n- Development Tools\n- Project Logs"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1066,"completion_tokens":126,"total_tokens":1192},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: {"id":"0193e86123f4008d47787c5d0636c153","object":"chat.completion","created":1734770500,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Human VRM\n- Realtime VRM Animation\n- Humanoid Avatar\n- Human Library\n- ThreeJS\n- TypeScript\n- VRM Model\n- Face Tracking\n- Body Tracking\n- Hand Tracking\n- GLTF VRM\n- WebRTC\n- Internal HTTP Server\n- HTTPS\n- Development Environment\n- Project Logs\n\n### Tags:\n- VRM Technology\n- Realtime Animation\n- 3D Human Avatars\n- Human Tracking\n- Web Development\n- TypeScript Projects\n- GLTF Models\n- CORS\n- Web Server\n- Development Tools\n- Project Logs"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1066,"completion_tokens":126,"total_tokens":1192},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86123f4008d47787c5d0636c153","object":"chat.completion","created":1734770500,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Human VRM\n- Realtime VRM Animation\n- Humanoid Avatar\n- Human Library\n- ThreeJS\n- TypeScript\n- VRM Model\n- Face Tracking\n- Body Tracking\n- Hand Tracking\n- GLTF VRM\n- WebRTC\n- Internal HTTP Server\n- HTTPS\n- Development Environment\n- Project Logs\n\n### Tags:\n- VRM Technology\n- Realtime Animation\n- 3D Human Avatars\n- Human Tracking\n- Web Development\n- TypeScript Projects\n- GLTF Models\n- CORS\n- Web Server\n- Development Tools\n- Project Logs"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1066,"completion_tokens":126,"total_tokens":1192},"system_fingerprint":""}
theme: light
title: human-vrm
---

# human-vrm

## Repository URL: 
[https://github.com/wanghaisheng/human-vrm](https://github.com/wanghaisheng/human-vrm)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Realtime VRM Humanoid Avatar Animation using Human Library and ThreeJS

## README Content: 
![Git Version](https://img.shields.io/github/package-json/v/vladmandic/human-three-vrm?style=flat-square&svg=true&label=git)
![Last Commit](https://img.shields.io/github/last-commit/vladmandic/human-three-vrm?style=flat-square&svg=true)
![License](https://img.shields.io/github/license/vladmandic/human-three-vrm?style=flat-square&svg=true)
![GitHub Status Checks](https://img.shields.io/github/checks-status/vladmandic/human-three-vrm/main?style=flat-square&svg=true)

# VR Humanoid Avatar using Human library

## Head, face, eye, body and hand tracking

Implementation in [TypeScript](https://www.typescriptlang.org/) using [`Human`](https://github.com/vladmandic/human) library for human analysis, [`three`](https://github.com/mrdoob/three.js) for 3D display and scene management and [`@pixiv/three-vrm`](https://github.com/pixiv/three-vrm) for VR model mapping

<br>

## Notes

### VR Model

- Supports any GLTF VRM model
- Examples: <https://hub.vroid.com/en>

### Face

- Implemented: 3D head angle, eye blinks, eye gaze direction, simple emotions, mouth opens

### Body

- Implemented: shoulder lean, positions for elbow, wrist, hip, knee
- Missing: front/back detection, detailed leg and arm positions, input validation to avoid unnatural movement

### Hands

- Based on calculating finger curl instead of updating positions
- Implemented: hand rotation, finger curls
- Missing: finger positions

<br>

## Installation

> Install using `npm install`  
> Run using `npm run dev` to build a JS bundle and start an internal http/https dev server

```js
2021-09-16 09:50:30 INFO:  human-vrm version 0.2.1
2021-09-16 09:50:30 INFO:  User: vlado Platform: linux Arch: x64 Node: v16.8.0
2021-09-16 09:50:30 INFO:  Application: { name: 'human-vrm', version: '0.2.1' }
2021-09-16 09:50:30 INFO:  Environment: { profile: 'development', config: 'build.json', tsconfig: true, eslintrc: true, git: true }
2021-09-16 09:50:30 INFO:  Toolchain: { build: '0.4.1', esbuild: '0.12.28', typescript: '4.4.3', typedoc: '0.21.9', eslint: '7.32.0' }
2021-09-16 09:50:30 INFO:  Build: { profile: 'development', steps: [ 'serve', 'watch', 'compile' ] }
2021-09-16 09:50:30 STATE: WebServer: { ssl: false, port: 8000, root: '.' }
2021-09-16 09:50:30 STATE: WebServer: { ssl: true, port: 8001, root: '.', sslKey: 'node_modules/@vladmandic/build/cert/https.key', sslCrt: 'node_modules/@vladmandic/build/cert/https.crt' }
2021-09-16 09:50:30 STATE: Watch: { locations: [ 'src/**', 'src/**' ] }
2021-09-16 09:50:31 STATE: Compile: { name: 'human-vrm', format: 'esm', platform: 'browser', input: 'src/human-vrm.ts', output: 'dist/human-vrm.esm.js', files: 2, inputBytes: 17217, outputBytes: 3780124 }
2021-09-16 09:50:31 INFO:  Listening...
```

> Navigate to `https://localhost:10031`


![Screenshot](assets/human-vrm-screenshot.jpg)

<br>

> ...Or use sources in your build environment and deploy on your web server

