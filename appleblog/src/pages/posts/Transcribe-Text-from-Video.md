---
author: Jane Smith
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'This project will Transcribe text/subtitles from a video using whisper.wasm web assembly, also this is in the development phase.'
featured: true
keywords: {"id":"0193e86bab4f9f3130dc33d4caaa737b","object":"chat.completion","created":1734771190,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Sure, here are the extracted keywords and tags from the provided text:\n\n### Keywords:\n- Transcribe\n- Text/Subtitles\n- Video\n- Whisper.wasm\n- WebAssembly (WASM)\n- inference\n- OpenAI's Whisper ASR model\n- transformer\n- audio data\n- local processing\n- Web page\n- real-time\n- performance\n\n### Tags:\n- Development\n- WebAssembly\n- Transcription\n- Video Processing\n- OpenAI\n- Real-Time\n- Performance\n- Locally Processed\n- Whisper Model"},"finish_reason":"stop"}],"usage":{"prompt_tokens":201,"completion_tokens":113,"total_tokens":314},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: {"id":"0193e86bab4f9f3130dc33d4caaa737b","object":"chat.completion","created":1734771190,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Sure, here are the extracted keywords and tags from the provided text:\n\n### Keywords:\n- Transcribe\n- Text/Subtitles\n- Video\n- Whisper.wasm\n- WebAssembly (WASM)\n- inference\n- OpenAI's Whisper ASR model\n- transformer\n- audio data\n- local processing\n- Web page\n- real-time\n- performance\n\n### Tags:\n- Development\n- WebAssembly\n- Transcription\n- Video Processing\n- OpenAI\n- Real-Time\n- Performance\n- Locally Processed\n- Whisper Model"},"finish_reason":"stop"}],"usage":{"prompt_tokens":201,"completion_tokens":113,"total_tokens":314},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86bab4f9f3130dc33d4caaa737b","object":"chat.completion","created":1734771190,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Sure, here are the extracted keywords and tags from the provided text:\n\n### Keywords:\n- Transcribe\n- Text/Subtitles\n- Video\n- Whisper.wasm\n- WebAssembly (WASM)\n- inference\n- OpenAI's Whisper ASR model\n- transformer\n- audio data\n- local processing\n- Web page\n- real-time\n- performance\n\n### Tags:\n- Development\n- WebAssembly\n- Transcription\n- Video Processing\n- OpenAI\n- Real-Time\n- Performance\n- Locally Processed\n- Whisper Model"},"finish_reason":"stop"}],"usage":{"prompt_tokens":201,"completion_tokens":113,"total_tokens":314},"system_fingerprint":""}
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

