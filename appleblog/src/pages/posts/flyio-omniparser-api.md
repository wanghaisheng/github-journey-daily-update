---
author: Alice Cooper
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Self-hosted version of Microsoft's OmniParser Image-to-text model'
featured: true
keywords: {"id":"0193e85ede14946ed442d7dbadfd32fa","object":"chat.completion","created":1734770351,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- flyio-omniparser-api\n- Self-hosted\n- Microsoft\n- OmniParser\n- Image-to-text\n- UI screenshot\n- Structured format\n- LLM based UI agent\n- Interactable icon detection\n- Icon description dataset\n- Gradio\n- HuggingFace\n- FastAPI\n- Docker\n- GPU\n- RAM\n- fly.io\n- API documentation\n- bounding boxes\n- parsed elements\n- swift deployment\n- OneQuery\n- agent\n\n### Tags:\n- #OmniParser-API\n- #ImageToText\n- #UIParsing\n- #MachineLearning\n- #SelfHosted\n- #Docker\n- #FastAPI\n- #Gradio\n- #HuggingFace\n- #Web scrapping\n- #StructuredData\n- #UIAgent\n- #FlyIoDeployment\n- #Swag\n- #APIEndpoint"},"finish_reason":"stop"}],"usage":{"prompt_tokens":585,"completion_tokens":189,"total_tokens":774},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Alice Cooper
  name: author
- content: {"id":"0193e85ede14946ed442d7dbadfd32fa","object":"chat.completion","created":1734770351,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- flyio-omniparser-api\n- Self-hosted\n- Microsoft\n- OmniParser\n- Image-to-text\n- UI screenshot\n- Structured format\n- LLM based UI agent\n- Interactable icon detection\n- Icon description dataset\n- Gradio\n- HuggingFace\n- FastAPI\n- Docker\n- GPU\n- RAM\n- fly.io\n- API documentation\n- bounding boxes\n- parsed elements\n- swift deployment\n- OneQuery\n- agent\n\n### Tags:\n- #OmniParser-API\n- #ImageToText\n- #UIParsing\n- #MachineLearning\n- #SelfHosted\n- #Docker\n- #FastAPI\n- #Gradio\n- #HuggingFace\n- #Web scrapping\n- #StructuredData\n- #UIAgent\n- #FlyIoDeployment\n- #Swag\n- #APIEndpoint"},"finish_reason":"stop"}],"usage":{"prompt_tokens":585,"completion_tokens":189,"total_tokens":774},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e85ede14946ed442d7dbadfd32fa","object":"chat.completion","created":1734770351,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- flyio-omniparser-api\n- Self-hosted\n- Microsoft\n- OmniParser\n- Image-to-text\n- UI screenshot\n- Structured format\n- LLM based UI agent\n- Interactable icon detection\n- Icon description dataset\n- Gradio\n- HuggingFace\n- FastAPI\n- Docker\n- GPU\n- RAM\n- fly.io\n- API documentation\n- bounding boxes\n- parsed elements\n- swift deployment\n- OneQuery\n- agent\n\n### Tags:\n- #OmniParser-API\n- #ImageToText\n- #UIParsing\n- #MachineLearning\n- #SelfHosted\n- #Docker\n- #FastAPI\n- #Gradio\n- #HuggingFace\n- #Web scrapping\n- #StructuredData\n- #UIAgent\n- #FlyIoDeployment\n- #Swag\n- #APIEndpoint"},"finish_reason":"stop"}],"usage":{"prompt_tokens":585,"completion_tokens":189,"total_tokens":774},"system_fingerprint":""}
theme: light
title: flyio-omniparser-api
---

# flyio-omniparser-api

## Repository URL: 
[https://github.com/wanghaisheng/flyio-omniparser-api](https://github.com/wanghaisheng/flyio-omniparser-api)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Self-hosted version of Microsoft's OmniParser Image-to-text model

## README Content: 
# OmniParser API

Self-hosted version of Microsoft's [OmniParser](https://huggingface.co/microsoft/OmniParser) Image-to-text model.

> OmniParser is a general screen parsing tool, which interprets/converts UI screenshot to structured format, to improve existing LLM based UI agent. Training Datasets include: 1) an interactable icon detection dataset, which was curated from popular web pages and automatically annotated to highlight clickable and actionable regions, and 2) an icon description dataset, designed to associate each UI element with its corresponding function.

## Why?

There's already a great HuggingFace gradio [app](https://huggingface.co/spaces/microsoft/OmniParser) for this model. It even offers an API. But

- Gradio is much slower than serving the model directly (like we do here)
- HF is rate-limited

## How it works

If you look at the Dockerfile, we start off with the HF demo image to retrive all the weights and util functions. Then we add a simple FastAPI server (under main.py) to serve the model.

## Getting Started

### Requirements

- GPU
- 16 GB Ram (swap recommended)

### Locally

1. Clone the repository
2. Build the docker image: `docker build -t omni-parser-app .`
3. Run the docker container: `docker run -p 7860:7860 omni-parser-app`

### Self-hosted API

I suggest hosting on [fly.io](https://fly.io) because it's quick and simple to deploy with a CLI.

This repo is ready-made for deployment on fly.io (see fly.toml for configuration). Just run `fly launch` and follow the prompts.

## Docs

Visit `http://localhost:7860/docs` for the API documentation. There's only one route `/process_image` which returns

- The image with bounding boxes drawn on (in base64) format
- The parsed elements in a list with text descriptions
- The bounding box coordinates of the parsed elements

## Examples

| Before Image                       | After Image                   |
| ---------------------------------- | ----------------------------- |
| ![Before](examples/screenshot.png) | ![After](examples/after.webp) |

## Related Projects

Check out [OneQuery](https://query-rho.vercel.app), an agent that browses the web and returns structured responses for any query, simple or complex. OneQuery is built using OmniParser to enhance its capabilities.

