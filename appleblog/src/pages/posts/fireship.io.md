---
author: Jane Smith
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734780679218_vmzcj
  url: https://fluxapi.borninsea.com/image/image_1734780679218_vmzcj
description: 'Build and ship your app faster  https://fireship.io'
featured: true
keywords: fireship,pro,course,svelte,tailwind,hugo,firebase,flamethrower,contribute,markdown,Hugo Extended,web component,svelte,options,tag,greeting,encapsulated,Tailwind,command,npm
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: fireship,pro,course,svelte,tailwind,hugo,firebase,flamethrower,contribute,markdown,Hugo Extended,web component,svelte,options,tag,greeting,encapsulated,Tailwind,command,npm
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- fireship,app-building,svelte,tailwind,hugo,firebase,component-development,github-integration,static-site-generation
theme: light
title: fireship.io
---

# fireship.io

## Repository URL: 
[https://github.com/wanghaisheng/fireship.io](https://github.com/wanghaisheng/fireship.io)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Build and ship your app faster  https://fireship.io

## README Content: 
2024-1220

## Fireship course


The [Fireship PRO](https://fireship.io) course platform frontend built with Svelte, Tailwind, Hugo, Firebase, & Flamethrower. 

## Contributing

All static content is managed with Hugo in the `content` dir. You can easily fix typos by modifying the markdown directly in GitHub. 

### How to Run it

First, install [Hugo Extended](https://gohugo.io/getting-started/installing/) ver `0.101.0` or greater. 

```
git clone <this-repo>
npm install
npm start
```

Check it on on `http://localhost:6969/`.


## Developing Components 

Create a Svelte file in the `app/components` directory. It must have a custom element tag. 

```svelte
<svelte:options tag="hi-mom" />

<script>
    export let greeting: string;
</script>

<h1>Hi Mom! {greeting}</h1> 
```

Export the component from `app/main.ts`:

```ts
export * from './components/hi-mom.svelte';
```

Now use it in anywhere in your HTML or Markdown. 

```html
<hi-mom greeting="i made a web component"></hi-mom>
```

**Note:** A weird caveat with Svelte web components is that all styles must be encapsulated. You can use Tailwind, BUT only with `@apply` in the component. Global styles will not work.

## Commands

- `npm start`: Main dev server. Runs everything you need. 
- `npm run dev`: Runs components in isolation. Serves `app/index.html` as a playground for components. 
- `npm run hugo`: Only runs static site. 
- `npm run build`: Build for production

