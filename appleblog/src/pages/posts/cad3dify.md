---
author: Jane Smith
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734780281232_k6m48l
  url: https://fluxapi.borninsea.com/image/image_1734780281232_k6m48l
description: '2D to 3D CAD Conversion Using GPT-4o'
featured: true
keywords: cad3dify,3D CAD Conversion,GPT-4o,STEP file,installation,POETRY INSTALL,OPENAI_API_KEY,2D CAD Image File,Streamlit,claude 3.5 sonnet,gemini 2.0 flash, llama 3.2 on vertex ai,Demo,Sample File,Input Image,Generated 3D CAD Model
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: cad3dify,3D CAD Conversion,GPT-4o,STEP file,installation,POETRY INSTALL,OPENAI_API_KEY,2D CAD Image File,Streamlit,claude 3.5 sonnet,gemini 2.0 flash, llama 3.2 on vertex ai,Demo,Sample File,Input Image,Generated 3D CAD Model
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- cad3dify,GPT-4o,CAD Conversion,3D CAD Model,STEP file,2D CAD Image,installation,script,Claude 3.5 sonnet,Gemini 2.0 flash,Llama 3.2,OpenAI API,Streamlit
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

