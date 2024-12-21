---
author: Bob Johnson
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734782264552_5pn1j
  url: https://fluxapi.borninsea.com/image/image_1734782264552_5pn1j
description: 'Clone Snake.io is a fun online multiplayer game to battle worms as you slither for survival. Learn to play this new free competitive snake battle royale with ...'
featured: true
keywords: snakeio-remake,Clone,Snake.io,battle,worms,slither,生存,React,TypeScript,Vite,ESLint,Fast Refresh,SWC,tsconfig	node.json,tsconfig.app.json,eslint-plugin-react
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Bob Johnson
  name: author
- content: snakeio-remake,Clone,Snake.io,battle,worms,slither,生存,React,TypeScript,Vite,ESLint,Fast Refresh,SWC,tsconfig	node.json,tsconfig.app.json,eslint-plugin-react
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- snake.io,online multiplayer game,worms,battle royale,React,TypeScript,Vite,SWC,Babel,eslint-plugin-react
theme: light
title: snakeio-remake
---

# snakeio-remake

## Repository URL: 
[https://github.com/wanghaisheng/snakeio-remake](https://github.com/wanghaisheng/snakeio-remake)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Clone Snake.io is a fun online multiplayer game to battle worms as you slither for survival. Learn to play this new free competitive snake battle royale with ...

## README Content: 
2024-11-15

# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type aware lint rules:

- Configure the top-level `parserOptions` property like this:

```js
export default tseslint.config({
  languageOptions: {
    // other options...
    parserOptions: {
      project: ['./tsconfig.node.json', './tsconfig.app.json'],
      tsconfigRootDir: import.meta.dirname,
    },
  },
})
```

- Replace `tseslint.configs.recommended` to `tseslint.configs.recommendedTypeChecked` or `tseslint.configs.strictTypeChecked`
- Optionally add `...tseslint.configs.stylisticTypeChecked`
- Install [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react) and update the config:

```js
// eslint.config.js
import react from 'eslint-plugin-react'

export default tseslint.config({
  // Set the react version
  settings: { react: { version: '18.3' } },
  plugins: {
    // Add the react plugin
    react,
  },
  rules: {
    // other rules...
    // Enable its recommended rules
    ...react.configs.recommended.rules,
    ...react.configs['jsx-runtime'].rules,
  },
})
```

