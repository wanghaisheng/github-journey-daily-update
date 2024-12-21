---
author: Jane Smith
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Fun with procedurally generated visionary art!'
featured: true
keywords: {"id":"0193e864973c2d872ce41f196b142335","object":"chat.completion","created":1734770726,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Procedural Art\n- Visionary Art\n- Procedurally Generated Art\n- Web Site\n- Experiment\n- NodeJS\n- TypeScript\n- Prettier\n- GitHub Pages\n- Firebase\n- Cloud Firestore\n- Code Integration\n- Editor Support\n- Online Viewing\n\n### Tags:\n- Procedural Art Project\n- Artistic Experimentation\n- Code and Art Collaboration\n- Web Development\n- Interactive Art\n- Type Checking\n- Editor Integration\n- Online Accessibility\n- Local Development\n- Code Style Management\n- Deployment Tools\n- Firebase Integration\n- Art and Technology"},"finish_reason":"stop"}],"usage":{"prompt_tokens":801,"completion_tokens":126,"total_tokens":927},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: {"id":"0193e864973c2d872ce41f196b142335","object":"chat.completion","created":1734770726,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Procedural Art\n- Visionary Art\n- Procedurally Generated Art\n- Web Site\n- Experiment\n- NodeJS\n- TypeScript\n- Prettier\n- GitHub Pages\n- Firebase\n- Cloud Firestore\n- Code Integration\n- Editor Support\n- Online Viewing\n\n### Tags:\n- Procedural Art Project\n- Artistic Experimentation\n- Code and Art Collaboration\n- Web Development\n- Interactive Art\n- Type Checking\n- Editor Integration\n- Online Accessibility\n- Local Development\n- Code Style Management\n- Deployment Tools\n- Firebase Integration\n- Art and Technology"},"finish_reason":"stop"}],"usage":{"prompt_tokens":801,"completion_tokens":126,"total_tokens":927},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e864973c2d872ce41f196b142335","object":"chat.completion","created":1734770726,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Procedural Art\n- Visionary Art\n- Procedurally Generated Art\n- Web Site\n- Experiment\n- NodeJS\n- TypeScript\n- Prettier\n- GitHub Pages\n- Firebase\n- Cloud Firestore\n- Code Integration\n- Editor Support\n- Online Viewing\n\n### Tags:\n- Procedural Art Project\n- Artistic Experimentation\n- Code and Art Collaboration\n- Web Development\n- Interactive Art\n- Type Checking\n- Editor Integration\n- Online Accessibility\n- Local Development\n- Code Style Management\n- Deployment Tools\n- Firebase Integration\n- Art and Technology"},"finish_reason":"stop"}],"usage":{"prompt_tokens":801,"completion_tokens":126,"total_tokens":927},"system_fingerprint":""}
theme: light
title: mysticsymbolic.github.io
---

# mysticsymbolic.github.io

## Repository URL: 
[https://github.com/wanghaisheng/mysticsymbolic.github.io](https://github.com/wanghaisheng/mysticsymbolic.github.io)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Fun with procedurally generated visionary art!

## README Content: 
This is an attempt by [Nina Paley][] (art) and [Atul Varma][] (code) to tinker
with procedural art.

Right now there is no particular goal other than to explore various ideas.
The project consists of a web site with multiple pages, each of which is
an experiment of some kind.

It can be [viewed online][] or iterated on locally using the instructions below.

## Quick start

This requires [NodeJS][].  It was started with
NodeJS 14.15.4, but hopefully it should work with
any recent version.

After cloning the repository and entering it, run:

```
npm run watch
```

then visit http://localhost:1234.

## Adding symbols

Documentation for adding and changing symbols can be found in [`assets/symbols/_instructions.md`](assets/symbols/_instructions.md).

## Running tests

To run tests interactively, run:

```
npm run test:watch
```

## Type checking

To make sure that everything type-checks okay, run:

```
npm run typecheck
```

Note that you may want to install a [TypeScript plugin for your favorite editor][ts-editor].  Aside from telling you what type errors you have in real-time, editor integration also provides code autocompletion and other affordances that can greatly improve your productivity. For more details, see Atul's [Fun with TypeScript][] series of videos.

[ts-editor]: https://github.com/Microsoft/TypeScript/wiki/TypeScript-Editor-Support
[Fun with TypeScript]: https://www.youtube.com/playlist?list=PL79r88piDzwZVwCI_26T3ZjC3xKvQLgjh

## Code style

All code styling is managed by [Prettier][].

To format the code automatically, run:

```
npm run prettier:fix
```

You can alternatively install a Prettier extension for your editor; see its website for more details.

[Prettier]: https://prettier.io/

## Deployment

To deploy the project to GitHub Pages, run:

```
npm run deploy
```

## Firebase support

The website features optional Firebase integration.

Currently, the details for the integration are hard-coded
into the application code; see `lib/firebase.tsx` for details.

Currently, the Firebase project that we integrate with needs
to have the following configured:

* Cloud Firestore should be enabled with a collection called
  `compositions` and the following rules:

  ```
  rules_version = '2';
  service cloud.firestore {
    match /databases/{database}/documents {
      match /{document=**} {
        // The gallery is globally readable.
        allow read: if true;

        allow write: if request.auth != null &&
          request.resource.data.keys().hasOnly(['kind', 'serializedValue', 'owner', 'ownerName', 'title', 'createdAt']) &&
          [request.resource.data.kind].hasAny(['creature', 'mandala']) &&
          request.resource.data.serializedValue is string &&
          request.resource.data.owner == request.auth.uid &&
          request.resource.data.ownerName is string &&
          request.resource.data.title is string &&
          request.resource.data.createdAt is timestamp;
      }
    }
  }
  ```

* The GitHub sign-in provider must be enabled.

[NodeJS]: https://nodejs.org/en/
[Nina Paley]: https://blog.ninapaley.com/
[Atul Varma]: https://portfolio.toolness.org/
[viewed online]: https://mysticsymbolic.art/

