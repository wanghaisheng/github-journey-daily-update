---
author: Bob Johnson
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Automation software to provision Google accounts (GMail) using GHOSTPVA privacy strategy'
featured: true
keywords: {"id":"0193e860729900e3bb33191625c7c5bc","object":"chat.completion","created":1734770455,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- Google Account Automation\n- GHOSTPVA Privacy Strategy\n- Puppeteer Stealth Addons\n- Basic Google Account Management\n- Vaultwarden Instance\n- Bitwarden CLI Module\n- Textverified.com API Key\n- Google Account Provisioning\n- 2FA (Two-Factor Authentication)\n- App Password\n- Forward Email\n- Two-Factor Confirmation Code\n- Android Support\n- Termux\n\n### Tags\n- #google-account\n- #automation\n- #privacy\n- #gapi-auth\n- #puppeteer\n- #vaultwarden\n- #bitwarden\n- #textverified\n- #2fa\n- #app-password\n- #forward-email\n- #2fa-confirmation-code\n- #android-support\n- #termux"},"finish_reason":"stop"}],"usage":{"prompt_tokens":637,"completion_tokens":166,"total_tokens":803},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Bob Johnson
  name: author
- content: {"id":"0193e860729900e3bb33191625c7c5bc","object":"chat.completion","created":1734770455,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- Google Account Automation\n- GHOSTPVA Privacy Strategy\n- Puppeteer Stealth Addons\n- Basic Google Account Management\n- Vaultwarden Instance\n- Bitwarden CLI Module\n- Textverified.com API Key\n- Google Account Provisioning\n- 2FA (Two-Factor Authentication)\n- App Password\n- Forward Email\n- Two-Factor Confirmation Code\n- Android Support\n- Termux\n\n### Tags\n- #google-account\n- #automation\n- #privacy\n- #gapi-auth\n- #puppeteer\n- #vaultwarden\n- #bitwarden\n- #textverified\n- #2fa\n- #app-password\n- #forward-email\n- #2fa-confirmation-code\n- #android-support\n- #termux"},"finish_reason":"stop"}],"usage":{"prompt_tokens":637,"completion_tokens":166,"total_tokens":803},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e860729900e3bb33191625c7c5bc","object":"chat.completion","created":1734770455,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- Google Account Automation\n- GHOSTPVA Privacy Strategy\n- Puppeteer Stealth Addons\n- Basic Google Account Management\n- Vaultwarden Instance\n- Bitwarden CLI Module\n- Textverified.com API Key\n- Google Account Provisioning\n- 2FA (Two-Factor Authentication)\n- App Password\n- Forward Email\n- Two-Factor Confirmation Code\n- Android Support\n- Termux\n\n### Tags\n- #google-account\n- #automation\n- #privacy\n- #gapi-auth\n- #puppeteer\n- #vaultwarden\n- #bitwarden\n- #textverified\n- #2fa\n- #app-password\n- #forward-email\n- #2fa-confirmation-code\n- #android-support\n- #termux"},"finish_reason":"stop"}],"usage":{"prompt_tokens":637,"completion_tokens":166,"total_tokens":803},"system_fingerprint":""}
theme: light
title: google-account
---

# google-account

## Repository URL: 
[https://github.com/wanghaisheng/google-account](https://github.com/wanghaisheng/google-account)

## Stars: 
**1**

## Forks: 
**0**

## Description: 
Automation software to provision Google accounts (GMail) using GHOSTPVA privacy strategy

## README Content: 
# google-account

Implementation of GHOSTPVA with bulletproof privacy and automation, using puppeteer stealth addons.

Includes toolset for basic Google account management.

## Setup

Install this project as well as the @bitwarden/cli module, globally, with yarn.

Target your vaultwarden instance and login with

```sh
bw config server https://<vaultwarden server>
bw login
# enter credentials into inquirer
```

bw will output the `export` line to add to ~/.bashrc

Fund a [textverified.com](https://textverified.com) API key with cryptocurrency and export a `TEXTVERIFIED_TOKEN` variable in ~/.bashrc with the simple access token.

## Usage

First, name a session so that it can be resumed for additional commands. The logged in session will be persisted to ~/.google-account/<session name>.json

```sh
google-account init some-name
```

To use the create-account full featureset (Google account, 2FA enabled, app password, save to Bitwarden), use a command similar to the one below:

```sh
google-account create-account --username ghostinthemsoftly9000 --password 'gh0st10109471@@' --name 'Ghost Rider' --enable-2fa --app-password --save
```

Alternatively, log in to an existing Google account to use additional commands in the software

```sh
google-account init somegmail
google-account login --email somegmail@gmail.com --password somepassword11 --totp-secret 1fj4abc3dcb3bdnfdn4nd
```

Or for accounts that use a recovery E-mail for untrusted logins

```sh
google-account init somegmail
google-account login --email somegmail@gmail.com --password somepassword11 --recovery-email somegmail12@outllok.com
```

Some example commands for a logged in session below:

```sh
google-account to-muttrc
google-account forward-email --to someothergmail12@gmail.com
google-account enter-forwarding-confirmation-code --code 481585812
google-account enable2fa
google-account enable-app-password
google-account dump-gvoice
google-account save-to-bitwarden
```


## Android Support

Yes, it works.

Install Termux from F-Droid and acquire a proot Ubuntu shell as follows

```sh
pkg update
pkg install proot proot-distro
proot-distro install ubuntu
proot-distro login ubuntu
```

Once you have a shell, you will have to get a working Chromium binary on the system for puppeteer to work, since there is no Chrome release that will work. The easiest way is to use:

```sh



