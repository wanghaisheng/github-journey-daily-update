---
author: Jane Smith
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Redirect domains using Cloudflare Workers and KV'
featured: true
keywords: {"id":"0193e8676ccccc30c6d38ec457030917","object":"chat.completion","created":1734770912,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags\n\n- Cloudflare Workers\n- KV (Key-Value Storage)\n- Domain Redirection\n- Wrangler CLI\n- GitHub Repository\n- Deployment\n- Cloudflare Account\n- TypeScript\n- MIT License\n- Project Structure\n- Contributing\n- Documentation\n\n### Tags\n\n- #Cloudflare\n- #WebDevelopment\n- #DomainManagement\n- #WorkersKV\n- #JavaScript\n- #TypeScript\n- #Redirection\n- #APIs\n- #DeploymentTools\n- #OpenSource"},"finish_reason":"stop"}],"usage":{"prompt_tokens":558,"completion_tokens":109,"total_tokens":667},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: {"id":"0193e8676ccccc30c6d38ec457030917","object":"chat.completion","created":1734770912,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags\n\n- Cloudflare Workers\n- KV (Key-Value Storage)\n- Domain Redirection\n- Wrangler CLI\n- GitHub Repository\n- Deployment\n- Cloudflare Account\n- TypeScript\n- MIT License\n- Project Structure\n- Contributing\n- Documentation\n\n### Tags\n\n- #Cloudflare\n- #WebDevelopment\n- #DomainManagement\n- #WorkersKV\n- #JavaScript\n- #TypeScript\n- #Redirection\n- #APIs\n- #DeploymentTools\n- #OpenSource"},"finish_reason":"stop"}],"usage":{"prompt_tokens":558,"completion_tokens":109,"total_tokens":667},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e8676ccccc30c6d38ec457030917","object":"chat.completion","created":1734770912,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags\n\n- Cloudflare Workers\n- KV (Key-Value Storage)\n- Domain Redirection\n- Wrangler CLI\n- GitHub Repository\n- Deployment\n- Cloudflare Account\n- TypeScript\n- MIT License\n- Project Structure\n- Contributing\n- Documentation\n\n### Tags\n\n- #Cloudflare\n- #WebDevelopment\n- #DomainManagement\n- #WorkersKV\n- #JavaScript\n- #TypeScript\n- #Redirection\n- #APIs\n- #DeploymentTools\n- #OpenSource"},"finish_reason":"stop"}],"usage":{"prompt_tokens":558,"completion_tokens":109,"total_tokens":667},"system_fingerprint":""}
theme: light
title: redirector
---

# redirector

## Repository URL: 
[https://github.com/wanghaisheng/redirector](https://github.com/wanghaisheng/redirector)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Redirect domains using Cloudflare Workers and KV

## README Content: 
2024-12-07

# Redirector

Redirector is a Cloudflare Workers script that uses Workers KV to manage and perform domain redirections.

## Features

- Redirect any domain pointed to the worker to a desired target URL.
- One place (Workers KV) to manage all your redirect rules.
- Easy to deploy and manage using Cloudflare's Wrangler.

## Requirements

- [Cloudflare Account](https://dash.cloudflare.com/)
- [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/)

## Installation

1. **Clone this repository:**

    ```sh
    git clone https://github.com/CasualCodersProjects/redirector.git
    cd redirector
    ```

2. **Install the dependencies:**

    ```sh
    npm install
    ```

3. **Update `wrangler.toml`:**

   Ensure the details like `name`, `kv_namespaces`, and `compatibility_date` are accurate.

4. **Set up Workers KV namespace:**

   Create a KV namespace named `RULES` from the Cloudflare dashboard, replace the `id` field in `wrangler.toml` with the actual ID from Cloudflare dashboard.

## Usage

### 1. Adding Redirect Rules

1. **Go to the Cloudflare dashboard.**
2. **Navigate to Workers KV** and find your `RULES` namespace.
3. **Add Key-Value Pairs** where keys are the domains you want to redirect and values are the target URLs.

### 2. Deploying the Worker

**Deploy the worker to Cloudflare:**

```sh
npm run deploy
```
OR
```sh
wrangler deploy
```

## Project Structure

- **`src/index.ts`**: Main worker code. It fetches the rules from KV and performs redirects.
- **Configuration files**: `.editorconfig`, `.prettierrc` for coding standards; `tsconfig.json` for TypeScript settings.
- **Deployment files**: `wrangler.toml`, `package.json` for project dependencies and scripts.

## Contributing

Feel free to fork this repository, make changes, and open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

Happy Redirecting!

For more details on Cloudflare Workers and Workers KV, refer to the [Cloudflare Documentation](https://developers.cloudflare.com/workers/).

