---
author: John Doe
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'No description provided.'
featured: true
keywords: {"id":"0193e86c4ddb532bb8f7424633da9b14","object":"chat.completion","created":1734771232,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Wa-AutoAI\n- koyeb\n- Node Express\n- serverless platform\n- deployment\n- infrastructure management\n- developer-friendly\n- application\n- expressjs\n- tutorials\n- documentation\n- deployment guide\n- serverless\n- global deployment\n\n### Tags:\n- #Wa-AutoAI\n- #koyeb\n- #NodeExpress\n- #ServerlessPlatform\n- #Deployment\n- #InfrastructureManagement\n- #DeveloperFriendly\n- #Application\n- #ExpressJS\n- #Tutorials\n- #Documentation\n- #DeploymentGuide\n- #ServerlessDeployment\n- #GlobalDeployment"},"finish_reason":"stop"}],"usage":{"prompt_tokens":948,"completion_tokens":133,"total_tokens":1081},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: {"id":"0193e86c4ddb532bb8f7424633da9b14","object":"chat.completion","created":1734771232,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Wa-AutoAI\n- koyeb\n- Node Express\n- serverless platform\n- deployment\n- infrastructure management\n- developer-friendly\n- application\n- expressjs\n- tutorials\n- documentation\n- deployment guide\n- serverless\n- global deployment\n\n### Tags:\n- #Wa-AutoAI\n- #koyeb\n- #NodeExpress\n- #ServerlessPlatform\n- #Deployment\n- #InfrastructureManagement\n- #DeveloperFriendly\n- #Application\n- #ExpressJS\n- #Tutorials\n- #Documentation\n- #DeploymentGuide\n- #ServerlessDeployment\n- #GlobalDeployment"},"finish_reason":"stop"}],"usage":{"prompt_tokens":948,"completion_tokens":133,"total_tokens":1081},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86c4ddb532bb8f7424633da9b14","object":"chat.completion","created":1734771232,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Wa-AutoAI\n- koyeb\n- Node Express\n- serverless platform\n- deployment\n- infrastructure management\n- developer-friendly\n- application\n- expressjs\n- tutorials\n- documentation\n- deployment guide\n- serverless\n- global deployment\n\n### Tags:\n- #Wa-AutoAI\n- #koyeb\n- #NodeExpress\n- #ServerlessPlatform\n- #Deployment\n- #InfrastructureManagement\n- #DeveloperFriendly\n- #Application\n- #ExpressJS\n- #Tutorials\n- #Documentation\n- #DeploymentGuide\n- #ServerlessDeployment\n- #GlobalDeployment"},"finish_reason":"stop"}],"usage":{"prompt_tokens":948,"completion_tokens":133,"total_tokens":1081},"system_fingerprint":""}
theme: light
title: Wa-AutoAI--koyeb-
---

# Wa-AutoAI--koyeb-

## Repository URL: 
[https://github.com/wanghaisheng/Wa-AutoAI--koyeb-](https://github.com/wanghaisheng/Wa-AutoAI--koyeb-)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
No description provided.

## README Content: 
[![example-expressjs](https://github.com/koyeb/example-expressjs/actions/workflows/deploy.yaml/badge.svg)](https://github.com/koyeb/example-expressjs/actions)

<div align="center">
  <a href="https://koyeb.com">
    <img src="https://www.koyeb.com/static/images/icons/koyeb.svg" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">Koyeb Serverless Platform</h3>
  <p align="center">
    Deploy a Node Express application on Koyeb
    <br />
    <a href="https://koyeb.com">Learn more about Koyeb</a>
    ·
    <a href="https://koyeb.com/docs">Explore the documentation</a>
    ·
    <a href="https://koyeb.com/tutorials">Discover our tutorials</a>
  </p>
</div>


## About Koyeb and the Node Express example application

Koyeb is a developer-friendly serverless platform to deploy apps globally. No-ops, servers, or infrastructure management.  This repository contains a Node Express application you can deploy on the Koyeb serverless platform for testing.

This example application is designed to show how a Node Express application can be deployed on Koyeb.  You can follow the associated [deploy guide](https://www.koyeb.com/docs/deploy/express) to learn more about the application and how to extend it.

## Getting Started

Follow the steps below to deploy and run the Node Express application on your Koyeb account.

### Requirements

You need a Koyeb account to successfully deploy and run this application. If you don't already have an account, you can sign-up for free [here](https://app.koyeb.com/auth/signup).

### Deploy using the Koyeb button

The fastest way to deploy the Node Express application is to click the **Deploy to Koyeb** button below.

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/koyeb/example-expressjs&branch=main&name=express-on-koyeb)

Clicking on this button brings you to the Koyeb App creation page with everything pre-set to launch this application.

_To modify this application example, you will need to fork this repository. Checkout the [fork and deploy](#fork-and-deploy-to-koyeb) instructions._

### Fork and deploy to Koyeb

If you want to customize and enhance this application, you need to fork this repository.

If you used the **Deploy to Koyeb** button, you can simply link your service to your forked repository to be able to push changes.  Alternatively, you can manually create the application as described below.

On the [Koyeb Control Panel](https://app.koyeb.com/), on the **Overview** tab, click the **Create Web Service** button to begin.

1. Select **GitHub** as the deployment method.
2. In the repositories list, select the repository you just forked.
3. In the **Builder** section, choose the builder you wish to use.  This repository can be built using buildpacks or a Dockerfile.
4. Choose a name for your App and Service.  For example, `express-on-koyeb`.
5. Click **Deploy**.

You will be taken to the deployment page where you can follow the build of your Express application. Once the build is completed, your application will be deployed and you will be able to access it via `<YOUR_APP_NAME>-<YOUR_ORG_NAME>.koyeb.app`.

## Contributing

If you have any questions, ideas or suggestions regarding this application sample, feel free to open an [issue](//github.com/koyeb/example-expressjs/issues) or fork this repository and open a [pull request](//github.com/koyeb/example-expressjs/pulls).

## Contact

[Koyeb](https://www.koyeb.com) - [@gokoyeb](https://twitter.com/gokoyeb) - [Slack](http://slack.koyeb.com/)

