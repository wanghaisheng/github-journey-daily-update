---
author: John Doe
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Some data storage costing nothing'
featured: true
keywords: {"id":"0193e85f0fde25d66f8b7643d84028a3","object":"chat.completion","created":1734770364,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- free databases\n- serverless databases\n- data storage\n- testing\n- providers\n- todo-list implementation\n- open-source\n- MIT license\n- cookies as a data store\n- dead providers\n- broken demos\n- local setup\n- unit tests\n- cypress tests\n- thanks to providers\n- known issues\n- todos\n\n### Tags\n- #FreeDatabases\n- #ServerlessDatabases\n- #DataStorage\n- #Testing\n- #Providers\n- #TodoListImplementation\n- #OpenSource\n- #MITLicense\n- #CookiesDataStore\n- #DeadProviders\n- #BrokenDemos\n- #LocalSetup\n- #UnitTests\n- #CypressTests\n- #ThanksToProviders\n- #KnownIssues\n- #Todos"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1061,"completion_tokens":167,"total_tokens":1228},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: {"id":"0193e85f0fde25d66f8b7643d84028a3","object":"chat.completion","created":1734770364,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- free databases\n- serverless databases\n- data storage\n- testing\n- providers\n- todo-list implementation\n- open-source\n- MIT license\n- cookies as a data store\n- dead providers\n- broken demos\n- local setup\n- unit tests\n- cypress tests\n- thanks to providers\n- known issues\n- todos\n\n### Tags\n- #FreeDatabases\n- #ServerlessDatabases\n- #DataStorage\n- #Testing\n- #Providers\n- #TodoListImplementation\n- #OpenSource\n- #MITLicense\n- #CookiesDataStore\n- #DeadProviders\n- #BrokenDemos\n- #LocalSetup\n- #UnitTests\n- #CypressTests\n- #ThanksToProviders\n- #KnownIssues\n- #Todos"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1061,"completion_tokens":167,"total_tokens":1228},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e85f0fde25d66f8b7643d84028a3","object":"chat.completion","created":1734770364,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- free databases\n- serverless databases\n- data storage\n- testing\n- providers\n- todo-list implementation\n- open-source\n- MIT license\n- cookies as a data store\n- dead providers\n- broken demos\n- local setup\n- unit tests\n- cypress tests\n- thanks to providers\n- known issues\n- todos\n\n### Tags\n- #FreeDatabases\n- #ServerlessDatabases\n- #DataStorage\n- #Testing\n- #Providers\n- #TodoListImplementation\n- #OpenSource\n- #MITLicense\n- #CookiesDataStore\n- #DeadProviders\n- #BrokenDemos\n- #LocalSetup\n- #UnitTests\n- #CypressTests\n- #ThanksToProviders\n- #KnownIssues\n- #Todos"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1061,"completion_tokens":167,"total_tokens":1228},"system_fingerprint":""}
theme: light
title: free-databases
---

# free-databases

## Repository URL: 
[https://github.com/wanghaisheng/free-databases](https://github.com/wanghaisheng/free-databases)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Some data storage costing nothing

## README Content: 
# Free Serverless Databases 🙌

Testing different free serverless database providers with a small todo-list implementation: [free-databases.vercel.app](https://free-databases.vercel.app/)

[![issues welcome](https://badgers.space/badge/issues/welcome/green?corner_radius=s)](#)
[![PRs welcome](https://badgers.space/badge/PRs/welcome/green?corner_radius=s)](#)
[![MIT](https://badgers.space/badge/license/MIT/blue?corner_radius=s)](#)


## Featured providers
- [Aiven](https://aiven.io/)
- ~~[Bit.io](https://bit.io/)~~
- [CockroachDB](https://www.cockroachlabs.com/)
- [Convex](https://www.convex.dev/)
- _[CosmosDB](https://learn.microsoft.com/en-us/azure/cosmos-db/)_
- [Deta](https://deta.space/)
- _[ElephantSQL](https://www.elephantsql.com/)_
- [FaunaDB](https://fauna.com/)
- [Firebase](https://firebase.google.com/)
- [Fly.io](https://fly.io/)
- [Koyeb](https://www.koyeb.com/)
- [MongoDB Atlas](https://www.mongodb.com/atlas/database)
- [Neon](https://neon.tech/)
- ~~[PlanetScale](https://planetscale.com/)~~
- [PocketHost](https://pockethost.io/)
- ~~[Railway](https://railway.app/)~~
- [Supabase](https://supabase.com/)
- [Tembo](https://tembo.io/)
- [TiDB Cloud](https://tidbcloud.com/)
- [Turso](https://turso.tech/)
- [Upstash](https://upstash.com/)
- [Vercel Postgres](https://vercel.com/docs/storage/vercel-postgres)
- [Xata](https://xata.io/)
- [Yugabyte](https://www.yugabyte.com/)
- Cookies as a data store (no third party)
- Please open a PR or an issue to suggest more!

### Dead providers or broken demos

* Bit.io is discontinued
* CosmosDB stopped working after 2 weeks
* ElephantSQL will be discontinued in 2025
* Railway required an update from me (which I might do later)

## Getting started locally

Run `yarn install`, then `yarn dev`.

To make the different databases work locally, you will need to create accounts
with the third parties and add your credentials in your `.env`.

You will also need to create the todos table:

```sql
-- PostgreSQL table for most providers
CREATE TABLE IF NOT EXISTS "todos" (
	"id" text PRIMARY KEY NOT NULL,
	"created_at" timestamp DEFAULT now() NOT NULL,
	"updated_at" timestamp DEFAULT now() NOT NULL,
	"name" text NOT NULL,
	"done" boolean NOT NULL
);

-- MySQL table for PlanetScale
CREATE TABLE `Todo` (
	`id` varchar(191) NOT NULL,
	`createdAt` datetime(3) NOT NULL DEFAULT current_timestamp(3),
	`updatedAt` datetime(3) NOT NULL,
	`name` text NOT NULL,
	`done` tinyint(1) NOT NULL,
	PRIMARY KEY (`id`),
	UNIQUE KEY `Todo_id_key` (`id`)
) ENGINE InnoDB,
  CHARSET utf8mb4,
  COLLATE utf8mb4_unicode_ci;
```

## Test

* Unit tests: `yarn test`
* Cypress tests: `yarn e2e`

## Thanks

* All the providers for providing free tiers
* Vercel too, also for the generous free tier

## Known issues / be aware / miscellaneous

* Took a shortcut and set `NODE_TLS_REJECT_UNAUTHORIZED=0`, which is probably not something that you should do in
  production.
* ~~For Fly.io, I am allocating to database to an IPv4 address, which costs $2/month. I could not find a way to use the
  free IPv6 address with NextJS+Vercel.~~ Fly.io never charged me, so I guess it's free.
* Using Next.js app directory, I couldn't find a way to nicely define special `export const dynamic = '...'`
  or `export const fetchCache = '...'`. It forced me to copy some folders (`convex`, `cookie`, `deta`), it would be nice
  if this could be avoided.
* Databases descriptions are taken from any place I could find them or AI-generated, they might not be very accurate. 

## Todos

- [ ] Add this into [🕶️ Awesome](https://github.com/sindresorhus/awesome) or somewhere

