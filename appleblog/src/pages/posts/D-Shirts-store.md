---
author: Alice Cooper
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'D-shirts: A full-stack e-commerce platform showcasing tech-inspired T-shirt designs. Built with the VILT stack (Vue, Inertia, Laravel, Tailwind), featuring Stripe payments, Resend emails, and a dynamic admin dashboard. Open-source and perfect for learning or hosting your own version!'
featured: true
keywords: {"id":"0193e85cc5095e12c2bc253406b069de","object":"chat.completion","created":1734770214,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- e-commerce platform\n- tech-inspired T-shirt designs\n- full-stack\n- Vue\n- Inertia\n- Laravel\n- Tailwind CSS\n- Stripe payments\n- Resend emails\n- dynamic admin dashboard\n- open-source\n- developer portfolio project\n\n### Tags:\n- #D-Shirts\n- #E-commerce\n- #TechInspired\n- #VueJs\n- #InertiaJs\n- #Laravel\n- #TailwindCss\n- #Stripe\n- #Resend\n- #AdminDashboard\n- #OpenSource\n- #DeveloperPortfolio"},"finish_reason":"stop"}],"usage":{"prompt_tokens":676,"completion_tokens":122,"total_tokens":798},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Alice Cooper
  name: author
- content: {"id":"0193e85cc5095e12c2bc253406b069de","object":"chat.completion","created":1734770214,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- e-commerce platform\n- tech-inspired T-shirt designs\n- full-stack\n- Vue\n- Inertia\n- Laravel\n- Tailwind CSS\n- Stripe payments\n- Resend emails\n- dynamic admin dashboard\n- open-source\n- developer portfolio project\n\n### Tags:\n- #D-Shirts\n- #E-commerce\n- #TechInspired\n- #VueJs\n- #InertiaJs\n- #Laravel\n- #TailwindCss\n- #Stripe\n- #Resend\n- #AdminDashboard\n- #OpenSource\n- #DeveloperPortfolio"},"finish_reason":"stop"}],"usage":{"prompt_tokens":676,"completion_tokens":122,"total_tokens":798},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e85cc5095e12c2bc253406b069de","object":"chat.completion","created":1734770214,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- e-commerce platform\n- tech-inspired T-shirt designs\n- full-stack\n- Vue\n- Inertia\n- Laravel\n- Tailwind CSS\n- Stripe payments\n- Resend emails\n- dynamic admin dashboard\n- open-source\n- developer portfolio project\n\n### Tags:\n- #D-Shirts\n- #E-commerce\n- #TechInspired\n- #VueJs\n- #InertiaJs\n- #Laravel\n- #TailwindCss\n- #Stripe\n- #Resend\n- #AdminDashboard\n- #OpenSource\n- #DeveloperPortfolio"},"finish_reason":"stop"}],"usage":{"prompt_tokens":676,"completion_tokens":122,"total_tokens":798},"system_fingerprint":""}
theme: light
title: D-Shirts-store
---

# D-Shirts-store

## Repository URL: 
[https://github.com/wanghaisheng/D-Shirts-store](https://github.com/wanghaisheng/D-Shirts-store)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
D-shirts: A full-stack e-commerce platform showcasing tech-inspired T-shirt designs. Built with the VILT stack (Vue, Inertia, Laravel, Tailwind), featuring Stripe payments, Resend emails, and a dynamic admin dashboard. Open-source and perfect for learning or hosting your own version!

## README Content: 
2024-12-16

# Welcome to D-shirts 🌟

A full-stack e-commerce platform showcasing tech-inspired t-shirt designs, built as a developer portfolio project.

### 🌐 It's live at https://d-shirts.galdi.dev

## 🏠 Homepage:
![Home Video](Home.gif)

## 👨🏻‍💻 Admin Dashboard:
![Admin Dashboard](Admin.gif)

### 🔐 Admin login credentials:
- url: https://d-shirts.galdi.dev/secret-login-url
- email: guest-admin@guest-admin.com
- password: 00000000

## 💻 Tech Stack

- **Backend**: Laravel
- **Frontend**: Vue + Inertia
- **Styling**: Tailwind CSS
- **Components**: PrimeVue
- **Payments**: Stripe
- **Email**: Resend

## Developer’s Journey 🚀

**This project was a learning adventure where I:**

- Used Inertia.js for the first time to bridge Laravel and Vue.

- Mastered Stripe integration for secure payments.

- Delved into email services with Resend.

- Explored Laravel queue jobs for background task handling.

- Strengthened my grasp on Laravel authorization.

- Leveraged Laravel sessions to implement a user-friendly cart system, enabling seamless shopping experiences for customers without requiring account creation.

## Installation: Build Your Own Store 🛠️

**Prerequisites**

- PHP 8.1+
- Composer
- Node.js
- NPM
- MySQL

**Installation Steps**

```shell
# Clone Cosmic Repo
git clone https://github.com/Mohamed-Galdi/D-Shirts
cd d-shirts

# Dependencies Warp Speed
composer install && npm install

# Configuration Sequence
cp .env.example .env
php artisan key:generate
php artisan migrate:fresh --seed
php artisan storage:link

# Start Development Server
npm run dev
php artisan serve

# Open http://localhost:8000

# later you may need to run the queue worker
php artisan queue:work
```
### ⚙️ Environment Secrets:
```ini
# Stripe Coordinates
STRIPE_KEY=pk_test_your_magic_key
STRIPE_SECRET=sk_test_your_secret_passage

# Resend Communication Channel
RESEND_API_KEY=your_email_gateway_key
```
You can obtain these keys from your Stripe Dashboard and Resend account.
## Open Source License 📜

D-shirts is open-source under the MIT License. Contributions and forks are always welcome. Let’s build and innovate together!

## 📭 Contact

If you have any questions or suggestions, please feel free to reach out to me [contact.galdi@gmail.com](mailto:contact.galdi@gmail.com)

