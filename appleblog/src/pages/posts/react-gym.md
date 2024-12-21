---
author: Alice Cooper
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'A complete Project  that use TypeScript, React, Tailwind CSS and Cloudflare Pages for deploying.'
featured: true
keywords: {"id":"0193e8671df2a9000a60a5c196174c8b","object":"chat.completion","created":1734770892,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- React\n- TypeScript\n- Vite\n- Tailwind CSS\n- Framer Motion\n- React Hook Form\n- React Icons\n- Cloudflare Pages\n- Smooth Scroll\n- Dynamic Forms\n- Interactive Icons\n- Smooth Animations\n- Responsive Design\n- ESLint\n- Prettier\n- Smooth Navigation\n- Development Scripts\n\n### Tags\n- #GymProject\n- #TypeScript\n- #ReactFramework\n- #ViteJS\n- #TailwindCSS\n- #FramerMotion\n- #ReactHookForm\n- #InteractiveIcons\n- #SmoothAnimations\n- #ResponsiveDesign\n- #ESLint\n- #Prettier\n- #DevelopmentTools\n- #WebDevelopment\n- #CloudflarePages"},"finish_reason":"stop"}],"usage":{"prompt_tokens":965,"completion_tokens":159,"total_tokens":1124},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Alice Cooper
  name: author
- content: {"id":"0193e8671df2a9000a60a5c196174c8b","object":"chat.completion","created":1734770892,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- React\n- TypeScript\n- Vite\n- Tailwind CSS\n- Framer Motion\n- React Hook Form\n- React Icons\n- Cloudflare Pages\n- Smooth Scroll\n- Dynamic Forms\n- Interactive Icons\n- Smooth Animations\n- Responsive Design\n- ESLint\n- Prettier\n- Smooth Navigation\n- Development Scripts\n\n### Tags\n- #GymProject\n- #TypeScript\n- #ReactFramework\n- #ViteJS\n- #TailwindCSS\n- #FramerMotion\n- #ReactHookForm\n- #InteractiveIcons\n- #SmoothAnimations\n- #ResponsiveDesign\n- #ESLint\n- #Prettier\n- #DevelopmentTools\n- #WebDevelopment\n- #CloudflarePages"},"finish_reason":"stop"}],"usage":{"prompt_tokens":965,"completion_tokens":159,"total_tokens":1124},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e8671df2a9000a60a5c196174c8b","object":"chat.completion","created":1734770892,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- React\n- TypeScript\n- Vite\n- Tailwind CSS\n- Framer Motion\n- React Hook Form\n- React Icons\n- Cloudflare Pages\n- Smooth Scroll\n- Dynamic Forms\n- Interactive Icons\n- Smooth Animations\n- Responsive Design\n- ESLint\n- Prettier\n- Smooth Navigation\n- Development Scripts\n\n### Tags\n- #GymProject\n- #TypeScript\n- #ReactFramework\n- #ViteJS\n- #TailwindCSS\n- #FramerMotion\n- #ReactHookForm\n- #InteractiveIcons\n- #SmoothAnimations\n- #ResponsiveDesign\n- #ESLint\n- #Prettier\n- #DevelopmentTools\n- #WebDevelopment\n- #CloudflarePages"},"finish_reason":"stop"}],"usage":{"prompt_tokens":965,"completion_tokens":159,"total_tokens":1124},"system_fingerprint":""}
theme: light
title: react-gym
---

# react-gym

## Repository URL: 
[https://github.com/wanghaisheng/react-gym](https://github.com/wanghaisheng/react-gym)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
A complete Project  that use TypeScript, React, Tailwind CSS and Cloudflare Pages for deploying.

## README Content: 
# Gym Typescript Project

Este é um projeto de uma página web de academia desenvolvida com **React** e **TypeScript**, utilizando as melhores práticas de desenvolvimento moderno. O projeto utiliza **Vite** como bundler e **Tailwind CSS** para o estilo da interface.

Acesse o site: [Gym Typescript Live](https://86676157.react-gym-f52.pages.dev/)

## Funcionalidades Principais

- **Páginas de navegação suave** com o uso da biblioteca `react-anchor-link-smooth-scroll`.
- **Formulários dinâmicos** e validados utilizando `react-hook-form`.
- **Ícones interativos** com o uso de `react-icons`.
- **Animações** suaves para uma melhor experiência do usuário com `framer-motion`.
- Estilização responsiva e moderna com **Tailwind CSS**.

## Scripts Disponíveis

- **Iniciar o servidor de desenvolvimento:**
  ```bash
  npm run dev
  ```
  Isso irá iniciar o servidor local de desenvolvimento. O projeto será servido em [http://localhost:3000](http://localhost:3000).

- **Build para produção:**
  ```bash
  npm run build
  ```
  Esse comando irá criar uma versão otimizada para produção na pasta `dist`.

- **Visualizar o build:**
  ```bash
  npm run preview
  ```
  Isso permitirá visualizar o build de produção localmente.

- **Gerar o CSS com Tailwind:**
  ```bash
  npm run build:css
  ```
  Esse comando compila o arquivo `src/index.css` com Tailwind e o coloca na pasta `dist`.

- **Linting:**
  ```bash
  npm run lint
  ```
  Esse comando verifica o código com as regras configuradas no ESLint.

## Estrutura do Projeto

A estrutura do projeto foi organizada da seguinte forma:

- **src/assets**: Armazena os ativos, como imagens e logotipos.
- **src/hooks**: Contém hooks personalizados, como o `useMediaQuery`.
- **src/scenes**: Dividido em subpastas que correspondem às páginas da aplicação, como `benefits`, `home`, `contactUs`, `navbar`, etc.
- **src/shared**: Componentes e funções reutilizáveis que podem ser compartilhados entre várias partes do projeto, como botões, tipos e estilizações.

### Dependências

O projeto utiliza as seguintes bibliotecas e ferramentas:

- **React**: ^18.3.1
- **TypeScript**: ^5.2.2
- **Vite**: ^5.3.4
- **Tailwind CSS**: ^3.4.8
- **Framer Motion**: ^11.3.23
- **React Hook Form**: ^7.53.0
- **React Icons**: ^5.3.0

### Desenvolvimento e Boas Práticas

- **ESLint**: Utilizado para garantir a qualidade do código, com regras específicas para TypeScript e React.
- **Prettier**: Configurado com `prettier-plugin-tailwindcss` para manter a formatação consistente, especialmente para classes CSS.
- **Tailwind CSS**: Integração com PostCSS e autoprefixer para otimização do CSS.

## Como Contribuir

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-repositorio.git
   ```
2. Instale as dependências:
   ```bash
   npm install
   ```
3. Crie uma nova branch para suas modificações:
   ```bash
   git checkout -b minha-nova-feature
   ```
4. Faça suas alterações e realize o commit:
   ```bash
   git commit -m "Adiciona nova feature"
   ```
5. Envie suas mudanças:
   ```bash
   git push origin minha-nova-feature
   ```

6. Abra um **Pull Request** para revisão.

