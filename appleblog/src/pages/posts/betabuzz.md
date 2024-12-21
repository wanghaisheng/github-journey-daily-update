---
author: Alice Cooper
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734780213277_8yu56
  url: https://fluxapi.borninsea.com/image/image_1734780213277_8yu56
description: '朋友圈那么多卖课的 能不能搞个打分的🔥Creating a buzz around the latest beta products'
featured: true
keywords:  BetaBuzz, social platform, beta products, voting system, comments system, JWT Authentication, S3 storage, Stripe integration, recursive comments, markdown support, folder structure, installation guide, third party libraries, Next.js
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Alice Cooper
  name: author
- content:  BetaBuzz, social platform, beta products, voting system, comments system, JWT Authentication, S3 storage, Stripe integration, recursive comments, markdown support, folder structure, installation guide, third party libraries, Next.js
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- betabuzz,course_reviews,product_buzz,authentication,jwt,S3_storage,stripe_integration,recursive_comments,markdown_support,Voting_system,Hacker_News_replacement,GitHub_repo_info,API_structure,Web_app_development,Kentico_Kontent_alternative,CircleCI,vercel_nextjs
theme: light
title: betabuzz
---

# betabuzz

## Repository URL: 
[https://github.com/wanghaisheng/betabuzz](https://github.com/wanghaisheng/betabuzz)

## Stars: 
**1**

## Forks: 
**0**

## Description: 
朋友圈那么多卖课的 能不能搞个打分的🔥Creating a buzz around the latest beta products

## README Content: 
<p align="center">
  <a href="https://github.com/iamsahebgiri/betabuzz">
    <img alt="betabuzz" height="80" src="https://raw.githubusercontent.com/iamsahebgiri/betabuzz/main/app/public/favicon.png">
  </a>
</p>
<h1 align="center">BetaBuzz</h1>

<div align="center">
Creating a buzz around the latest beta products
</div>

<br />

<div align="center">
  <a href="https://standardjs.com">
    <img src="https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat-square"
      alt="Standard" />
  </a>
  
  <img src="https://img.shields.io/github/languages/code-size/iamsahebgiri/betabuzz?style=flat-square" alt="Code size" />

  <img src="https://img.shields.io/github/license/iamsahebgiri/betabuzz?style=flat-square" alt="License" />

  <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/iamsahebgiri/betabuzz?style=flat-square">

  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/iamsahebgiri/betabuzz?style=social">
</div>

## ⚡️ Introduction

BetaBuzz is website to share and discover new products. Users submit products, which are listed in a linear format. The site includes a comments system and a voting system similar to Hacker News or Reddit.

![Products](art/products.png)
![Community](art/community.png)
![Profile](art/profile.jpeg)
![Settings](art/settings.png)
![Product](art/product.png)
![Comments](art/comments.png)
![Grafana dashboard](art/monitoring.png)

## 🎯 Features

- JWT Based Authentication
- Storing user generated content in S3
- Stripe integration for subscription (Premium features such as markdown editor, blue tick, etc.)
- Recursive comments (like Reddit, HN) with markdown support

## 📁 Folder

Here's the folder structure of the api and app:

```sh
.
├── api
│   ├── src
│   │   ├── config
│   │   ├── controllers
│   │   ├── docs
│   │   ├── middlewares
│   │   ├── models
│   │   ├── routes
│   │   ├── services
│   │   ├── utils
│   │   └── validations
│   └── tests
│       ├── fixtures
│       ├── integration
│       ├── unit
│       └── utils
└── app
    ├── assets
    ├── components
    ├── config
    ├── hooks
    ├── layouts
    ├── lib
    ├── pages
    ├── public
    ├── services
    ├── styles
    └── types

```

## ⚙️ Installation

Make sure you have [Node.js](https://nodejs.org/en/download/) installed.
Run this followed commands:

To install the api

```bash
# Change directory to api
cd api

# Copy environment variables and Make sure to change them
cp .env.example .env

# Install dependencies (only the first time)
npm install

# Run the local server at localhost:8000
npm run dev
```

To run the web app

```sh
# Change directory to app
cd app
# Install dependencies (only the first time)
npm install

# Run the local server at localhost:3000
npm run dev

# Build for production in the dist/ directory
npm run build
```

## 🌱 Third Party Libraries

- [vercel/next.js](https://github.com/vercel/next.js)
- [expressjs/express](https://github.com/expressjs/express)
- [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)

## 📚️ Roadmap

- [ ] Login with Google and Github
- [ ] AI Integration for creating product description

## ❤️ Acknowledgements

- [plane](https://github.com/makeplane/plane)

## ‍💻 Author

- [@iamsahebgiri](https://github.com/iamsahebgiri)

## ⭐️ Contribute

If you want to say thank you and/or support the active development of betabuzz:

1. Add a GitHub Star to the project.
2. Tweet about the project on your Twitter.
3. Write a review or tutorial on Medium, Dev.to or personal blog.
4. Support the project by donating a cup of coffee.

## 🧾 License

MIT License Copyright (c) 2023 [Saheb Giri](https://github.com/iamsahebgiri).

