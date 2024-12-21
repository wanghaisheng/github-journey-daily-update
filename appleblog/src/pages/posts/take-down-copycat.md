---
author: Jane Smith
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Open-source tool to (legally) take down scam domains'
featured: true
keywords: {"id":"0193e86aba7dccf269943956e5d09618","object":"chat.completion","created":1734771128,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- take-down-copycat\n- open-source tool\n- legally take down scam domains\n- abuse report process\n- GNU GPLv3\n- WHOIS lookup\n- Groq's llama3-70b-8192 model\n- Mailgun\n- self-hosting\n- investment scams\n- crypto pump and dump\n- phishing pages\n- animal abuse\n- domain registrars\n- hosting providers\n- TLDs\n- abuse report\n- self-hosting instructions\n- proxy services\n\n### Tags:\n- TakeDown\n- ScamDomains\n- OpenSource\n- LegalActions\n- Automation\n- WHOIS\n- AIReporting\n- MailgunIntegration\n- SelfHosting\n- Proxies\n- SecurityTools\n- PhishingProtection"},"finish_reason":"stop"}],"usage":{"prompt_tokens":498,"completion_tokens":160,"total_tokens":658},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: {"id":"0193e86aba7dccf269943956e5d09618","object":"chat.completion","created":1734771128,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- take-down-copycat\n- open-source tool\n- legally take down scam domains\n- abuse report process\n- GNU GPLv3\n- WHOIS lookup\n- Groq's llama3-70b-8192 model\n- Mailgun\n- self-hosting\n- investment scams\n- crypto pump and dump\n- phishing pages\n- animal abuse\n- domain registrars\n- hosting providers\n- TLDs\n- abuse report\n- self-hosting instructions\n- proxy services\n\n### Tags:\n- TakeDown\n- ScamDomains\n- OpenSource\n- LegalActions\n- Automation\n- WHOIS\n- AIReporting\n- MailgunIntegration\n- SelfHosting\n- Proxies\n- SecurityTools\n- PhishingProtection"},"finish_reason":"stop"}],"usage":{"prompt_tokens":498,"completion_tokens":160,"total_tokens":658},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86aba7dccf269943956e5d09618","object":"chat.completion","created":1734771128,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- take-down-copycat\n- open-source tool\n- legally take down scam domains\n- abuse report process\n- GNU GPLv3\n- WHOIS lookup\n- Groq's llama3-70b-8192 model\n- Mailgun\n- self-hosting\n- investment scams\n- crypto pump and dump\n- phishing pages\n- animal abuse\n- domain registrars\n- hosting providers\n- TLDs\n- abuse report\n- self-hosting instructions\n- proxy services\n\n### Tags:\n- TakeDown\n- ScamDomains\n- OpenSource\n- LegalActions\n- Automation\n- WHOIS\n- AIReporting\n- MailgunIntegration\n- SelfHosting\n- Proxies\n- SecurityTools\n- PhishingProtection"},"finish_reason":"stop"}],"usage":{"prompt_tokens":498,"completion_tokens":160,"total_tokens":658},"system_fingerprint":""}
theme: light
title: take-down-copycat
---

# take-down-copycat

## Repository URL: 
[https://github.com/wanghaisheng/take-down-copycat](https://github.com/wanghaisheng/take-down-copycat)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Open-source tool to (legally) take down scam domains

## README Content: 
2024-12-02

This is an opensource tool to (legally) take down scam domains. It automates the boring abuse report process. Licensed under GNU GPLv3.

Created by 
[@richardvanorton](https://www.github.com/richardvanorton) and
[@oliviavanorton](https://www.github.com/oliviavanorton)

![image](https://github.com/user-attachments/assets/679ef9bc-0f36-4ab5-b941-fd8050bef6ed)
Website: https://scammerlocker.vercel.app/

<b>Here's how it works:-</b> <br>
The tool does a WHOIS lookup to get the domain registrar's abuse contact email. Then it uses Groq's llama3-70b-8192 model to use the context and target URL provided by the user to generate an abuse report email with a matching subject. Using Mailgun, it emails the domain provider at their designated abuse contact.

The tool works for any illegal websites, including but not limited to investment scams, crypto pump, and dump, phishing pages, animal abuse, etc. All domain registrars, hosting providers, and TLDs are legally required to take action when they receive an abuse report. Typically, it takes several days to a few weeks to take the website down.

## Self-hosting Instructions

1. Run the following
```bash
npm i
npm run dev
```

2. Add the following to your .env
```bash
GROQ_API_KEY=''
MAILGUN_API_KEY=''
FULL_NAME=''
HCAPTCHA_SECRET=''
FROM_SENDER=''
FROM_DOMAIN=''
PROXY_PASS=''
```
[step 3 no longer required] <br>
3. Remember to set the proxy port, username and host IP in app/actions.ts
```bash
Proxy services:
IProyal
Oxylabs
Webshare
Free proxy services from Google
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

