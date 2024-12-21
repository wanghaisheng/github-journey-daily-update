---
author: Bob Johnson
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'No description provided.'
featured: true
keywords: {"id":"0193e85d4158b37ebb34b89ef0e194a0","object":"chat.completion","created":1734770245,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n1. Domain Deployment\n2. Cloudflare Domains\n3. Offer Submission System\n4. Node.js\n5. Wrangler CLI\n6. Prerequisites\n7. Setup Instructions\n8. Domain Creation Script\n9. Turnstile Protection\n10. Cloudflare Workers\n11. KV Storage\n12. DNS Propagation\n13. Admin Dashboard\n14. Offer Management\n15. Domain Management\n16. Batch Setup\n\n### Tags:\n1. #DomainManagement\n2. #Cloudflare\n3. #Node.js\n4. #WebDevelopment\n5. #DomainOffer\n6. #DeploymentScript\n7. #Security\n8. #FormSubmission\n9. #KVStorage\n10. #AdminDashboard\n11. #Turnstile\n12. #Workers\n13. #DNS\n14. #Setup\n15. #BatchDeployment\n16. #OffersManagement"},"finish_reason":"stop"}],"usage":{"prompt_tokens":545,"completion_tokens":199,"total_tokens":744},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Bob Johnson
  name: author
- content: {"id":"0193e85d4158b37ebb34b89ef0e194a0","object":"chat.completion","created":1734770245,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n1. Domain Deployment\n2. Cloudflare Domains\n3. Offer Submission System\n4. Node.js\n5. Wrangler CLI\n6. Prerequisites\n7. Setup Instructions\n8. Domain Creation Script\n9. Turnstile Protection\n10. Cloudflare Workers\n11. KV Storage\n12. DNS Propagation\n13. Admin Dashboard\n14. Offer Management\n15. Domain Management\n16. Batch Setup\n\n### Tags:\n1. #DomainManagement\n2. #Cloudflare\n3. #Node.js\n4. #WebDevelopment\n5. #DomainOffer\n6. #DeploymentScript\n7. #Security\n8. #FormSubmission\n9. #KVStorage\n10. #AdminDashboard\n11. #Turnstile\n12. #Workers\n13. #DNS\n14. #Setup\n15. #BatchDeployment\n16. #OffersManagement"},"finish_reason":"stop"}],"usage":{"prompt_tokens":545,"completion_tokens":199,"total_tokens":744},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e85d4158b37ebb34b89ef0e194a0","object":"chat.completion","created":1734770245,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n1. Domain Deployment\n2. Cloudflare Domains\n3. Offer Submission System\n4. Node.js\n5. Wrangler CLI\n6. Prerequisites\n7. Setup Instructions\n8. Domain Creation Script\n9. Turnstile Protection\n10. Cloudflare Workers\n11. KV Storage\n12. DNS Propagation\n13. Admin Dashboard\n14. Offer Management\n15. Domain Management\n16. Batch Setup\n\n### Tags:\n1. #DomainManagement\n2. #Cloudflare\n3. #Node.js\n4. #WebDevelopment\n5. #DomainOffer\n6. #DeploymentScript\n7. #Security\n8. #FormSubmission\n9. #KVStorage\n10. #AdminDashboard\n11. #Turnstile\n12. #Workers\n13. #DNS\n14. #Setup\n15. #BatchDeployment\n16. #OffersManagement"},"finish_reason":"stop"}],"usage":{"prompt_tokens":545,"completion_tokens":199,"total_tokens":744},"system_fingerprint":""}
theme: light
title: domain-dash
---

# domain-dash

## Repository URL: 
[https://github.com/wanghaisheng/domain-dash](https://github.com/wanghaisheng/domain-dash)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
No description provided.

## README Content: 
# Domain Offer Page Deployer

Deploy "Domain For Sale" pages to your unused Cloudflare domains with a built-in offer submission system.

## Prerequisites

- Node.js installed
- A Cloudflare account
- One or more domains on Cloudflare
- [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/install-and-update/) installed

## Setup

1. Clone this repository

```bash
git clone [repository-url]
cd [repository-name]
```

2. Install dependencies

```bash
npm install
```

3. Login to Wrangler

```bash
npx wrangler login
```

4. Set up Turnstile
   - Visit [Cloudflare Dashboard](https://dash.cloudflare.com/?to=/:account/turnstile)
   - Click "Add Site" to create a new widget
   - Note down both the Site Key and Secret Key

## Deploying to Your Domains

Run the domain creation script:

```bash
npm run create-domain
```

The script will guide you through:

1. Setting up an admin password (for accessing the admin dashboard)
2. Creating or using an existing KV namespace
3. Configuring your domain
4. Setting up Turnstile protection
5. Deploying to Cloudflare Workers

### Optional: Batch Setup

You can speed up deployment for multiple domains by providing the KV namespace ID and admin password as arguments:

```bash
npm run create-domain --kv-id your-kv-id --admin-password your-password
```

## Post-Deployment

After deployment:

- Your domain will show a "For Sale" page
- Potential buyers can submit offers through the protected form
- Access the admin dashboard at `https://your-domain.com/admin`
- Review and manage offers through the admin dashboard

## Managing Multiple Domains

- All domains can share the same KV namespace and admin password
- Each domain gets its own configuration in the `domains/` directory
- Offers for each domain are stored separately in KV storage

## Updating Admin Password

To change the admin password for a specific domain:

```bash
npx wrangler secret put ADMIN_PASSWORD -c domains/your-domain/wrangler.toml
```

## Notes

- DNS propagation may take up to 48 hours
- Turnstile protection helps prevent spam submissions
- All offers are stored in Cloudflare KV storage
- The admin dashboard is protected by the password you set during setup

