---
author: Jane Smith
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: '[QwikJS] A website and dashboard for selling courses in video format. Created withqwikjs (extended react framweork kindof), using stripe for the backend payments, tailwind for styling, authentication by auth js , and orm by drizzle orm'
featured: true
keywords: {"id":"0193e85ca495de1221c4183603bdb265","object":"chat.completion","created":1734770205,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags\n\n1. **Technology and Frameworks**\n   - QwikJS\n   - QwikCity\n   - React\n   - Vite\n   - TypeScript\n   - DRizzle ORM\n   - Auth.js\n   - Stripe\n   - Tailwind\n\n2. **Deployment and Integration**\n   - Vercel\n   - Cloudflare Pages\n   - Git Integration\n   - Edge Functions\n   - Static Site Generation (SSG)\n\n3. **Development Commands**\n   - `npm start`\n   - `npm build`\n   - `pnpm`\n   - `pnpm preview`\n   - `pnpm deploy`\n\n4. **Project Structure**\n   - `src/routes`\n   - `src/components`\n   - `public`\n\n5. **Additional Tools and Resources**\n   - Qwik Docs\n   - Discord\n   - Qwik GitHub\n   - QwikDev Twitter\n\nThis summary captures the main technologies, frameworks, and deployment methods used in the described project."},"finish_reason":"stop"}],"usage":{"prompt_tokens":1994,"completion_tokens":206,"total_tokens":2200},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: {"id":"0193e85ca495de1221c4183603bdb265","object":"chat.completion","created":1734770205,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags\n\n1. **Technology and Frameworks**\n   - QwikJS\n   - QwikCity\n   - React\n   - Vite\n   - TypeScript\n   - DRizzle ORM\n   - Auth.js\n   - Stripe\n   - Tailwind\n\n2. **Deployment and Integration**\n   - Vercel\n   - Cloudflare Pages\n   - Git Integration\n   - Edge Functions\n   - Static Site Generation (SSG)\n\n3. **Development Commands**\n   - `npm start`\n   - `npm build`\n   - `pnpm`\n   - `pnpm preview`\n   - `pnpm deploy`\n\n4. **Project Structure**\n   - `src/routes`\n   - `src/components`\n   - `public`\n\n5. **Additional Tools and Resources**\n   - Qwik Docs\n   - Discord\n   - Qwik GitHub\n   - QwikDev Twitter\n\nThis summary captures the main technologies, frameworks, and deployment methods used in the described project."},"finish_reason":"stop"}],"usage":{"prompt_tokens":1994,"completion_tokens":206,"total_tokens":2200},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e85ca495de1221c4183603bdb265","object":"chat.completion","created":1734770205,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags\n\n1. **Technology and Frameworks**\n   - QwikJS\n   - QwikCity\n   - React\n   - Vite\n   - TypeScript\n   - DRizzle ORM\n   - Auth.js\n   - Stripe\n   - Tailwind\n\n2. **Deployment and Integration**\n   - Vercel\n   - Cloudflare Pages\n   - Git Integration\n   - Edge Functions\n   - Static Site Generation (SSG)\n\n3. **Development Commands**\n   - `npm start`\n   - `npm build`\n   - `pnpm`\n   - `pnpm preview`\n   - `pnpm deploy`\n\n4. **Project Structure**\n   - `src/routes`\n   - `src/components`\n   - `public`\n\n5. **Additional Tools and Resources**\n   - Qwik Docs\n   - Discord\n   - Qwik GitHub\n   - QwikDev Twitter\n\nThis summary captures the main technologies, frameworks, and deployment methods used in the described project."},"finish_reason":"stop"}],"usage":{"prompt_tokens":1994,"completion_tokens":206,"total_tokens":2200},"system_fingerprint":""}
theme: light
title: coursegod.com
---

# coursegod.com

## Repository URL: 
[https://github.com/wanghaisheng/coursegod.com](https://github.com/wanghaisheng/coursegod.com)

## Stars: 
**1**

## Forks: 
**0**

## Description: 
[QwikJS] A website and dashboard for selling courses in video format. Created withqwikjs (extended react framweork kindof), using stripe for the backend payments, tailwind for styling, authentication by auth js , and orm by drizzle orm

## README Content: 
20241206


# Qwik City App ⚡️Refactored

- [Qwik Docs](https://qwik.builder.io/)
- [Discord](https://qwik.builder.io/chat)
- [Qwik GitHub](https://github.com/BuilderIO/qwik)
- [@QwikDev](https://twitter.com/QwikDev)
- [Vite](https://vitejs.dev/)

---

## Project Structure

This project is using Qwik with [QwikCity](https://qwik.builder.io/qwikcity/overview/). QwikCity is just an extra set of tools on top of Qwik to make it easier to build a full site, including directory-based routing, layouts, and more.

Inside your project, you'll see the following directory structure:

```
├── public/
│   └── ...
└── src/
    ├── components/
    │   └── ...
    └── routes/
        └── ...
```

- `src/routes`: Provides the directory-based routing, which can include a hierarchy of `layout.tsx` layout files, and an `index.tsx` file as the page. Additionally, `index.ts` files are endpoints. Please see the [routing docs](https://qwik.builder.io/qwikcity/routing/overview/) for more info.

- `src/components`: Recommended directory for components.

- `public`: Any static assets, like images, can be placed in the public directory. Please see the [Vite public directory](https://vitejs.dev/guide/assets.html#the-public-directory) for more info.

## Add Integrations and deployment

Use the `pnpm qwik add` command to add additional integrations. Some examples of integrations includes: Cloudflare, Netlify or Express Server, and the [Static Site Generator (SSG)](https://qwik.builder.io/qwikcity/guides/static-site-generation/).

```shell
pnpm qwik add # or `pnpm qwik add`
```

## Development

Development mode uses [Vite's development server](https://vitejs.dev/). The `dev` command will server-side render (SSR) the output during development.

```shell
npm start # or `pnpm start`
```

> Note: during dev mode, Vite may request a significant number of `.js` files. This does not represent a Qwik production build.

## Preview

The preview command will create a production build of the client modules, a production build of `src/entry.preview.tsx`, and run a local server. The preview server is only for convenience to preview a production build locally and should not be used as a production server.

```shell
pnpm preview # or `pnpm preview`
```

## Production

The production build will generate client and server modules by running both client and server build commands. The build command will use Typescript to run a type check on the source code.

```shell
pnpm build # or `pnpm build`
```

## Vercel Edge

This starter site is configured to deploy to [Vercel Edge Functions](https://vercel.com/docs/concepts/functions/edge-functions), which means it will be rendered at an edge location near to your users.

## Installation

The adaptor will add a new `vite.config.ts` within the `adapters/` directory, and a new entry file will be created, such as:

```
└── adapters/
    └── vercel-edge/
        └── vite.config.ts
└── src/
    └── entry.vercel-edge.tsx
```

Additionally, within the `package.json`, the `build.server` script will be updated with the Vercel Edge build.

## Production build

To build the application for production, use the `build` command, this command will automatically run `pnpm build.server` and `pnpm build.client`:

```shell
pnpm build
```

[Read the full guide here](https://github.com/BuilderIO/qwik/blob/main/starters/adapters/vercel-edge/README.md)

## Dev deploy

To deploy the application for development:

```shell
pnpm deploy
```

Notice that you might need a [Vercel account](https://docs.Vercel.com/get-started/) in order to complete this step!

## Production deploy

The project is ready to be deployed to Vercel. However, you will need to create a git repository and push the code to it.

You can [deploy your site to Vercel](https://vercel.com/docs/concepts/deployments/overview) either via a Git provider integration or through the Vercel CLI.

## Cloudflare Pages

Cloudflare's [wrangler](https://github.com/cloudflare/wrangler) CLI can be used to preview a production build locally. To start a local server, run:

```
pnpm serve
```

Then visit [http://localhost:8787/](http://localhost:8787/)

### Deployments

[Cloudflare Pages](https://pages.cloudflare.com/) are deployable through their [Git provider integrations](https://developers.cloudflare.com/pages/platform/git-integration/).

If you don't already have an account, then [create a Cloudflare account here](https://dash.cloudflare.com/sign-up/pages). Next go to your dashboard and follow the [Cloudflare Pages deployment guide](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/).

Within the projects "Settings" for "Build and deployments", the "Build command" should be `pnpm build`, and the "Build output directory" should be set to `dist`.

### Function Invocation Routes

Cloudflare Page's [function-invocation-routes config](https://developers.cloudflare.com/pages/platform/functions/routing/#functions-invocation-routes) can be used to include, or exclude, certain paths to be used by the worker functions. Having a `_routes.json` file gives developers more granular control over when your Function is invoked.
This is useful to determine if a page response should be Server-Side Rendered (SSR) or if the response should use a static-site generated (SSG) `index.html` file.

By default, the Cloudflare pages adaptor _does not_ include a `public/_routes.json` config, but rather it is auto-generated from the build by the Cloudflare adaptor. An example of an auto-generate `dist/_routes.json` would be:

```
{
  "include": [
    "/*"
  ],
  "exclude": [
    "/_headers",
    "/_redirects",
    "/build/*",
    "/favicon.ico",
    "/manifest.json",
    "/service-worker.js",
    "/about"
  ],
  "version": 1
}
```

In the above example, it's saying _all_ pages should be SSR'd. However, the root static files such as `/favicon.ico` and any static assets in `/build/*` should be excluded from the Functions, and instead treated as a static file.

In most cases the generated `dist/_routes.json` file is ideal. However, if you need more granular control over each path, you can instead provide you're own `public/_routes.json` file. When the project provides its own `public/_routes.json` file, then the Cloudflare adaptor will not auto-generate the routes config and instead use the committed one within the `public` directory.

## Vercel Edge

This starter site is configured to deploy to [Vercel Edge Functions](https://vercel.com/docs/concepts/functions/edge-functions), which means it will be rendered at an edge location near to your users.

## Installation

The adaptor will add a new `vite.config.ts` within the `adapters/` directory, and a new entry file will be created, such as:

```
└── adapters/
    └── vercel-edge/
        └── vite.config.ts
└── src/
    └── entry.vercel-edge.tsx
```

Additionally, within the `package.json`, the `build.server` script will be updated with the Vercel Edge build.

## Production build

To build the application for production, use the `build` command, this command will automatically run `pnpm build.server` and `pnpm build.client`:

```shell
pnpm build
```

[Read the full guide here](https://github.com/BuilderIO/qwik/blob/main/starters/adapters/vercel-edge/README.md)

## Dev deploy

To deploy the application for development:

```shell
pnpm deploy
```

Notice that you might need a [Vercel account](https://docs.Vercel.com/get-started/) in order to complete this step!

## Production deploy

The project is ready to be deployed to Vercel. However, you will need to create a git repository and push the code to it.

You can [deploy your site to Vercel](https://vercel.com/docs/concepts/deployments/overview) either via a Git provider integration or through the Vercel CLI.

