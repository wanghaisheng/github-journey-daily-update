---
author: Bob Johnson
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: '2D to 3D CAD Conversion Using GPT-4o'
featured: true
keywords: {"id":"0193e85b9f7a832b3f75a4dedd449bc4","object":"chat.completion","created":1734770139,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Sure, here are the keywords and tags extracted from the provided text:\n\n### Keywords:\n- cad3dify\n- GPT-4o\n- CAD Conversion\n- 2D to 3D\n- STEP file\n- OpenAI API\n- Poetry installation\n- CLI script\n- Streamlit app\n- Claude 3.5 sonnet\n- Gemini 2.0 flash\n- Llama 3.2 on Vertex AI\n- Sample file\n- Input image\n- 3D CAD model\n\n### Tags:\n- CAD Conversion\n- Computer-Aided Design (CAD)\n- 2D to 3D\n- GPT-4o\n- Machine Learning\n- AI-Assisted Design\n- Open Source\n- Installation Guide\n- CLI Interface\n- Streamlit Application\n- Model Types (Claude, Gemini, Llama)\n- STEP File Generation\n- API Key\n- Poetic Installation\n- Sample Data"},"finish_reason":"stop"}],"usage":{"prompt_tokens":338,"completion_tokens":195,"total_tokens":533},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Bob Johnson
  name: author
- content: {"id":"0193e85b9f7a832b3f75a4dedd449bc4","object":"chat.completion","created":1734770139,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Sure, here are the keywords and tags extracted from the provided text:\n\n### Keywords:\n- cad3dify\n- GPT-4o\n- CAD Conversion\n- 2D to 3D\n- STEP file\n- OpenAI API\n- Poetry installation\n- CLI script\n- Streamlit app\n- Claude 3.5 sonnet\n- Gemini 2.0 flash\n- Llama 3.2 on Vertex AI\n- Sample file\n- Input image\n- 3D CAD model\n\n### Tags:\n- CAD Conversion\n- Computer-Aided Design (CAD)\n- 2D to 3D\n- GPT-4o\n- Machine Learning\n- AI-Assisted Design\n- Open Source\n- Installation Guide\n- CLI Interface\n- Streamlit Application\n- Model Types (Claude, Gemini, Llama)\n- STEP File Generation\n- API Key\n- Poetic Installation\n- Sample Data"},"finish_reason":"stop"}],"usage":{"prompt_tokens":338,"completion_tokens":195,"total_tokens":533},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e85b9f7a832b3f75a4dedd449bc4","object":"chat.completion","created":1734770139,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Sure, here are the keywords and tags extracted from the provided text:\n\n### Keywords:\n- cad3dify\n- GPT-4o\n- CAD Conversion\n- 2D to 3D\n- STEP file\n- OpenAI API\n- Poetry installation\n- CLI script\n- Streamlit app\n- Claude 3.5 sonnet\n- Gemini 2.0 flash\n- Llama 3.2 on Vertex AI\n- Sample file\n- Input image\n- 3D CAD model\n\n### Tags:\n- CAD Conversion\n- Computer-Aided Design (CAD)\n- 2D to 3D\n- GPT-4o\n- Machine Learning\n- AI-Assisted Design\n- Open Source\n- Installation Guide\n- CLI Interface\n- Streamlit Application\n- Model Types (Claude, Gemini, Llama)\n- STEP File Generation\n- API Key\n- Poetic Installation\n- Sample Data"},"finish_reason":"stop"}],"usage":{"prompt_tokens":338,"completion_tokens":195,"total_tokens":533},"system_fingerprint":""}
theme: light
title: cad3dify
---

# cad3dify

## Repository URL: 
[https://github.com/wanghaisheng/cad3dify](https://github.com/wanghaisheng/cad3dify)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
2D to 3D CAD Conversion Using GPT-4o

## README Content: 
# cad3dify

Using GPT-4o (or Claude 3.5 sonnet, Gemini 2.0 flash, Llama 3.2 on Vertex AI), generate a 3D CAD model (STEP file) from a 2D CAD image.

## Getting started

Installation.

```bash
git clone git@github.com:neka-nat/cad3dify.git
cd cad3dify
poetry install
```

Run script.
A STEP`file ("output.step") will be generated.

```bash
cd scripts
export OPENAI_API_KEY=<YOUR API KEY>
python cli.py <2D CAD Image File>
```

Or run streamlit spp

```bash
streamlit run scripts/app.py
streamlit run scripts/app.py -- --model_type claude  # Use Claude 3.5 sonnet
streamlit run scripts/app.py -- --model_type gemini  # Use Gemini 2.0 flash
streamlit run scripts/app.py -- --model_type llama  # Use Llama 3.2 on Vertex AI
```

## Demo

We will use the sample file [here](http://cad.wp.xdomain.jp/).

### Input image

![input](sample_data/g1-3.jpg)

### Generated 3D CAD model

![output](sample_data/gen_result1.png)

