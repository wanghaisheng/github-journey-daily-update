---
author: Alice Cooper
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'astro x turso db '
featured: true
keywords: {"id":"0193e85a6477de4333e63f03bc8618d6","object":"chat.completion","created":1734770058,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags\n\n- Astro\n- Starter Kit\n- Blog\n- npm\n- StackBlitz\n- CodeSandbox\n- GitHub Codespaces\n- Seasoned astronaut\n- Minimal styling\n- 100/100 Lighthouse performance\n- SEO-friendly\n- Canonical URLs\n- OpenGraph data\n- Sitemap support\n- RSS Feed support\n- Markdown\n- MDX\n- Project Structure\n- Components\n- Content Collections\n- Dev server\n- Production build\n- Astro CLI\n- Documentation\n- Discord server\n\n### Additional Tags\n\n- .astro files\n- .md files\n- Static assets\n- Public directory\n- Content collections\n- Frontmatter\n- Blog theme\n- Developer tools"},"finish_reason":"stop"}],"usage":{"prompt_tokens":793,"completion_tokens":152,"total_tokens":945},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Alice Cooper
  name: author
- content: {"id":"0193e85a6477de4333e63f03bc8618d6","object":"chat.completion","created":1734770058,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags\n\n- Astro\n- Starter Kit\n- Blog\n- npm\n- StackBlitz\n- CodeSandbox\n- GitHub Codespaces\n- Seasoned astronaut\n- Minimal styling\n- 100/100 Lighthouse performance\n- SEO-friendly\n- Canonical URLs\n- OpenGraph data\n- Sitemap support\n- RSS Feed support\n- Markdown\n- MDX\n- Project Structure\n- Components\n- Content Collections\n- Dev server\n- Production build\n- Astro CLI\n- Documentation\n- Discord server\n\n### Additional Tags\n\n- .astro files\n- .md files\n- Static assets\n- Public directory\n- Content collections\n- Frontmatter\n- Blog theme\n- Developer tools"},"finish_reason":"stop"}],"usage":{"prompt_tokens":793,"completion_tokens":152,"total_tokens":945},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e85a6477de4333e63f03bc8618d6","object":"chat.completion","created":1734770058,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags\n\n- Astro\n- Starter Kit\n- Blog\n- npm\n- StackBlitz\n- CodeSandbox\n- GitHub Codespaces\n- Seasoned astronaut\n- Minimal styling\n- 100/100 Lighthouse performance\n- SEO-friendly\n- Canonical URLs\n- OpenGraph data\n- Sitemap support\n- RSS Feed support\n- Markdown\n- MDX\n- Project Structure\n- Components\n- Content Collections\n- Dev server\n- Production build\n- Astro CLI\n- Documentation\n- Discord server\n\n### Additional Tags\n\n- .astro files\n- .md files\n- Static assets\n- Public directory\n- Content collections\n- Frontmatter\n- Blog theme\n- Developer tools"},"finish_reason":"stop"}],"usage":{"prompt_tokens":793,"completion_tokens":152,"total_tokens":945},"system_fingerprint":""}
theme: light
title: astro-http-turso-db
---

# astro-http-turso-db

## Repository URL: 
[https://github.com/wanghaisheng/astro-http-turso-db](https://github.com/wanghaisheng/astro-http-turso-db)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
astro x turso db 

## README Content: 
2024-1213

# Astro Starter Kit: Blog

```sh
npm create astro@latest -- --template blog
```

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/withastro/astro/tree/latest/examples/blog)
[![Open with CodeSandbox](https://assets.codesandbox.io/github/button-edit-lime.svg)](https://codesandbox.io/p/sandbox/github/withastro/astro/tree/latest/examples/blog)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/withastro/astro?devcontainer_path=.devcontainer/blog/devcontainer.json)

> 🧑‍🚀 **Seasoned astronaut?** Delete this file. Have fun!

![blog](https://github.com/withastro/astro/assets/2244813/ff10799f-a816-4703-b967-c78997e8323d)

Features:

- ✅ Minimal styling (make it your own!)
- ✅ 100/100 Lighthouse performance
- ✅ SEO-friendly with canonical URLs and OpenGraph data
- ✅ Sitemap support
- ✅ RSS Feed support
- ✅ Markdown & MDX support

## 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
├── public/
├── src/
│   ├── components/
│   ├── content/
│   ├── layouts/
│   └── pages/
├── astro.config.mjs
├── README.md
├── package.json
└── tsconfig.json
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

The `src/content/` directory contains "collections" of related Markdown and MDX documents. Use `getCollection()` to retrieve posts from `src/content/blog/`, and type-check your frontmatter using an optional schema. See [Astro's Content Collections docs](https://docs.astro.build/en/guides/content-collections/) to learn more.

Any static assets, like images, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## 👀 Want to learn more?

Check out [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).

## Credit

This theme is based off of the lovely [Bear Blog](https://github.com/HermanMartinus/bearblog/).

