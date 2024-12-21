---
author: John Doe
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734781015387_1r0rob
  url: https://fluxapi.borninsea.com/image/image_1734781015387_1r0rob
description: 'Realtime VRM Humanoid Avatar Animation using Human Library and ThreeJS'
featured: true
keywords: human,vrm,avatar,animation,realtime,threejs,humanlibrary,VRL,MotionTracking,typescript,ThreeJS,@pixiv/three-vrm,humananalysis,Gltf,Vroid,face,body,hand,git,license,github,installation,npm,development,linux,x64,Node
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: human,vrm,avatar,animation,realtime,threejs,humanlibrary,VRL,MotionTracking,typescript,ThreeJS,@pixiv/three-vrm,humananalysis,Gltf,Vroid,face,body,hand,git,license,github,installation,npm,development,linux,x64,Node
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- human-vrm,vrm,humanoid/avatar-animation,realtime,threejs,vr,human tracking,face tracking,body tracking,hand tracking,gltf,typescript,git version,last commit,license,github checks,installation,npm,development server,esbuild,typescript,eslint,certificates,screenshot
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

