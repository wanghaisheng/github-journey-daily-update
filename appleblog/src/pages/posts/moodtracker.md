---
author: Bob Johnson
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'A serverless and offline-first PWA that lets you track your mood'
featured: true
keywords: {"id":"0193e86454accc394e44f6a7284361b3","object":"chat.completion","created":1734770709,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- moodtracker\n- serverless\n- offline-first\n- PWA\n- mood tracking\n- emotional landscape\n- open source\n- web app\n- UI\n- component library\n- Eri\n- Node.js\n- Python\n- Poetry\n- CORS\n- Firebase\n- AWS CloudFormation\n- Troposphere\n- Netlify\n- development dependencies\n- testing\n- deployment\n\n### Tags:\n#MoodTracker\n#Serverless\n#OfflineFirst\n#PWALibrary\n#OpenSourceWebApp\n#EmotionalLandscapeTracking\n#DevelopmentDependencies\n#Testing\n#Deployment\n#CloudFormation\n#TroposphereAWS\n#NetlifyDeployment\n#IconsGeneration\n#ComponentLibraryEri"},"finish_reason":"stop"}],"usage":{"prompt_tokens":621,"completion_tokens":154,"total_tokens":775},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Bob Johnson
  name: author
- content: {"id":"0193e86454accc394e44f6a7284361b3","object":"chat.completion","created":1734770709,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- moodtracker\n- serverless\n- offline-first\n- PWA\n- mood tracking\n- emotional landscape\n- open source\n- web app\n- UI\n- component library\n- Eri\n- Node.js\n- Python\n- Poetry\n- CORS\n- Firebase\n- AWS CloudFormation\n- Troposphere\n- Netlify\n- development dependencies\n- testing\n- deployment\n\n### Tags:\n#MoodTracker\n#Serverless\n#OfflineFirst\n#PWALibrary\n#OpenSourceWebApp\n#EmotionalLandscapeTracking\n#DevelopmentDependencies\n#Testing\n#Deployment\n#CloudFormation\n#TroposphereAWS\n#NetlifyDeployment\n#IconsGeneration\n#ComponentLibraryEri"},"finish_reason":"stop"}],"usage":{"prompt_tokens":621,"completion_tokens":154,"total_tokens":775},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86454accc394e44f6a7284361b3","object":"chat.completion","created":1734770709,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- moodtracker\n- serverless\n- offline-first\n- PWA\n- mood tracking\n- emotional landscape\n- open source\n- web app\n- UI\n- component library\n- Eri\n- Node.js\n- Python\n- Poetry\n- CORS\n- Firebase\n- AWS CloudFormation\n- Troposphere\n- Netlify\n- development dependencies\n- testing\n- deployment\n\n### Tags:\n#MoodTracker\n#Serverless\n#OfflineFirst\n#PWALibrary\n#OpenSourceWebApp\n#EmotionalLandscapeTracking\n#DevelopmentDependencies\n#Testing\n#Deployment\n#CloudFormation\n#TroposphereAWS\n#NetlifyDeployment\n#IconsGeneration\n#ComponentLibraryEri"},"finish_reason":"stop"}],"usage":{"prompt_tokens":621,"completion_tokens":154,"total_tokens":775},"system_fingerprint":""}
theme: light
title: moodtracker
---

# moodtracker

## Repository URL: 
[https://github.com/wanghaisheng/moodtracker](https://github.com/wanghaisheng/moodtracker)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
A serverless and offline-first PWA that lets you track your mood

## README Content: 
# MoodTracker

[![CI](https://github.com/benji6/moodtracker/actions/workflows/main.yml/badge.svg)](https://github.com/benji6/moodtracker/actions/workflows/main.yml)
[![Netlify Status](https://api.netlify.com/api/v1/badges/0d744c93-11e8-4072-85e2-4a168c1ae8ae/deploy-status)](https://app.netlify.com/sites/benji6-moodtracker/deploys)

## About

MoodTracker is a free and open source web app that aims to help you understand yourself better. Track your emotional landscape, keep a mood journal, time your meditations, keep a meditation log and gain new insights into yourself. It's simple to use, works offline and because it runs in your browser you can use it across all your devices!

[Check it out here](https://moodtracker.link)

The MoodTracker UI was built using a component library I made called [Eri](https://github.com/benji6/eri).

## Getting started

### Dependencies required on host machine

- [Node.js](https://nodejs.org) (version specified in [.nvmrc](/client/.nvmrc))
- [Python](https://www.python.org) (latest version 3.x)
- [Poetry](https://python-poetry.org/docs/) (latest version 1.x)

### Install project dependencies

```sh
make init
```

### Run frontend locally

```sh
make start
```

### Test application locally

You will need to be running the client locally on the default port for the end-to-end tests to pass and you will need credentials for a registered user on the platform that you can use to set the `CYPRESS_MOODTRACKER_TEST_USER_EMAIL` and `CYPRESS_MOODTRACKER_TEST_USER_PASSWORD` environment variables.

```sh
make test
```

### Deploy

#### Backend and infrastructure

Majority of the infrastructure is managed with AWS CloudFormation (via [Troposphere](https://troposphere.readthedocs.io)). Firebase, secrets and a few AWS things that aren't well supported have been done manually.

```sh
make deploy
```

**N.B. making changes to the API doesn't trigger a new deployment, but you can trigger a manual deployment by copying the value of the `ApiGatewayDeployCommand` output and running that.**

#### UI

Continuously deployed with [Netlify](http://netlify.com).

**N.B. Icons are stored in version control and are generated by running `npm run icons` in the `/client` dir.**

