---
author: John Doe
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734782501103_dshmr
  url: https://fluxapi.borninsea.com/image/image_1734782501103_dshmr
description: 'This project will Transcribe text/subtitles from a video using whisper.wasm web assembly, also this is in the development phase.'
featured: true
keywords: transcribe, text, subtitles, video, whisper.wasm, WebAssembly, whisper.cpp, inference, OpenAI, audio data, local processing, modern CPU, performance, real-time, models
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: transcribe, text, subtitles, video, whisper.wasm, WebAssembly, whisper.cpp, inference, OpenAI, audio data, local processing, modern CPU, performance, real-time, models
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- transcribe-text-from-video,whisper.wasm,webassembly,whisper.cpp,ASR,inference,browser,local-processing,tiny-models,base-models,performance-real-time
theme: light
title: Transcribe-Text-from-Video
---

# Transcribe-Text-from-Video

## Repository URL: 
[https://github.com/wanghaisheng/Transcribe-Text-from-Video](https://github.com/wanghaisheng/Transcribe-Text-from-Video)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
This project will Transcribe text/subtitles from a video using whisper.wasm web assembly, also this is in the development phase.

## README Content: 
video to text


*This is still in development phase, not yet completed./*


Inference of OpenAI's Whisper ASR model inside the browser

This example uses a WebAssembly (WASM) port of the whisper.cpp implementation of the transformer to run the inference inside a web page. The audio data does not leave your computer - it is processed locally on your machine. The performance is not great but you should be able to achieve x2 or x3 real-time for the tiny and base models on a modern CPU and browser (i.e. transcribe a 60 seconds audio in about ~20-30 seconds).

