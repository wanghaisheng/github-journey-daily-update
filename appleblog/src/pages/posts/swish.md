---
author: John Doe
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734782390440_a69uis
  url: https://fluxapi.borninsea.com/image/image_1734782390440_a69uis
description: 'Swish, more like a song wish service built on top of Cloudflare Workers, Cloudflare Pages, PostgreSQL, Lavalink using Pants, TypeScript, Go and Astro for GKŠM'
featured: true
keywords: Swish,Song_Wish,Cloudflare_Workers,Cloudflare_Pages,PostgreSQL,Lavalink,Pants,TypeScript,Go,Astro,GKŠM,pants,node.js,pnpm,golang,web_application,queue,workers,web_application_framework,database,application,cross-platform
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: Swish,Song_Wish,Cloudflare_Workers,Cloudflare_Pages,PostgreSQL,Lavalink,Pants,TypeScript,Go,Astro,GKŠM,pants,node.js,pnpm,golang,web_application,queue,workers,web_application_framework,database,application,cross-platform
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- swish,song wish,cloudflare workers,cloudflare pages,postgresql,lavalink,pants,typescript,go,astro
theme: light
title: swish
---

# swish

## Repository URL: 
[https://github.com/wanghaisheng/swish](https://github.com/wanghaisheng/swish)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Swish, more like a song wish service built on top of Cloudflare Workers, Cloudflare Pages, PostgreSQL, Lavalink using Pants, TypeScript, Go and Astro for GKŠM

## README Content: 
update

**Swish** stands for **Song Wish**, it's a web application that allows users to search for songs and submit them to a queue. The queue is handled by an app that runs on a computer.

Built on top of [Cloudflare Workers](https://workers.cloudflare.com/), [Cloudflare Pages](https://pages.cloudflare.com/), [PostgreSQL](https://www.postgresql.org/), [Lavalink](https://lavalink.dev/) using [Pants](https://www.pantsbuild.org/), [TypeScript](https://www.typescriptlang.org/), [Go](https://golang.org/) and [Astro](https://astro.build/) for GKŠM.

## Requirements

- [pants](https://www.pantsbuild.org/)
- [node.js](https://nodejs.org/)
- [pnpm](https://pnpm.js.org/)
- [golang](https://golang.org/)

## Structure

- `page/` contains the web application, written in Astro.
- `api/` contains the worker that handles requests from the web application and adds them to the queue, written in TypeScript.
- `app/` contains the app that handles the queue, written in Go.
- `scripts/` contains scripts to build, deploy and run easily.

