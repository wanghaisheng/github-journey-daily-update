---
author: John Doe
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Auto deploy vaultwarden on fly.io with auto backups and cloudflare tunnel'
featured: true
keywords: {"id":"0193e86bf8a7e10394a9d592594d7f3d","object":"chat.completion","created":1734771210,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Vaultwarden\n- Auto deploy\n- Fly.io\n- Automated deployment\n- Cloudflare Tunnel\n- Automatic backups\n- Dependency management\n- Dockerfile\n- GitHub Actions\n- Supercronic\n- Overmind\n- Caddy\n- Caddy Reverse Proxy\n- Cloudflared\n\n### Tags:\n- #Vaultwarden\n- #AutoDeploy\n- #Flyio\n- #CloudflareTunnel\n- #AutomatedBackups\n- #DependencyManagement\n- #Docker\n- #GitHubActions\n- #Supercronic\n- #Overmind\n- #Caddy\n- #ReverseProxy\n- #SelfHosting\n- #PasswordManager"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1076,"completion_tokens":143,"total_tokens":1219},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: {"id":"0193e86bf8a7e10394a9d592594d7f3d","object":"chat.completion","created":1734771210,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Vaultwarden\n- Auto deploy\n- Fly.io\n- Automated deployment\n- Cloudflare Tunnel\n- Automatic backups\n- Dependency management\n- Dockerfile\n- GitHub Actions\n- Supercronic\n- Overmind\n- Caddy\n- Caddy Reverse Proxy\n- Cloudflared\n\n### Tags:\n- #Vaultwarden\n- #AutoDeploy\n- #Flyio\n- #CloudflareTunnel\n- #AutomatedBackups\n- #DependencyManagement\n- #Docker\n- #GitHubActions\n- #Supercronic\n- #Overmind\n- #Caddy\n- #ReverseProxy\n- #SelfHosting\n- #PasswordManager"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1076,"completion_tokens":143,"total_tokens":1219},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86bf8a7e10394a9d592594d7f3d","object":"chat.completion","created":1734771210,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Vaultwarden\n- Auto deploy\n- Fly.io\n- Automated deployment\n- Cloudflare Tunnel\n- Automatic backups\n- Dependency management\n- Dockerfile\n- GitHub Actions\n- Supercronic\n- Overmind\n- Caddy\n- Caddy Reverse Proxy\n- Cloudflared\n\n### Tags:\n- #Vaultwarden\n- #AutoDeploy\n- #Flyio\n- #CloudflareTunnel\n- #AutomatedBackups\n- #DependencyManagement\n- #Docker\n- #GitHubActions\n- #Supercronic\n- #Overmind\n- #Caddy\n- #ReverseProxy\n- #SelfHosting\n- #PasswordManager"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1076,"completion_tokens":143,"total_tokens":1219},"system_fingerprint":""}
theme: light
title: vaultwarden-password-cf-worker
---

# vaultwarden-password-cf-worker

## Repository URL: 
[https://github.com/wanghaisheng/vaultwarden-password-cf-worker](https://github.com/wanghaisheng/vaultwarden-password-cf-worker)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Auto deploy vaultwarden on fly.io with auto backups and cloudflare tunnel

## README Content: 
# Vaultwarden Auto-Deploy on Fly.io

This project automates the deployment and maintenance of Vaultwarden (formerly Bitwarden_RS) on Fly.io, featuring automatic backups, secure access via Cloudflare Tunnel, and streamlined dependency management.

## Features

* **Automated Deployment:** Effortlessly deploy Vaultwarden to Fly.io for self-hosting your password manager.
* **Automatic Backups:** Secure daily backups to GitHub Releases, Backblaze B2, and Cloudflare R2.
* **Automated Backup Pruning:** GitHub Actions automatically deletes old release files.
* **Cloudflare Tunnel:** Secure and encrypted access to your Vaultwarden instance.
* **Automatic Dependency Updates:**  Downloads the latest versions of:
    * Vaultwarden
    * Vaultwarden Web Vault
    * Overmind
    * Supercronic
    * Caddy
    * Cloudflared
* **Caddy Reverse Proxy:**  Handles HTTPS and other web server tasks for improved security and efficiency.

## Dependencies

* [Fly.io](https://fly.io/)
* [Vaultwarden](https://github.com/dani-garcia/vaultwarden)
* [GitHub](https://github.com/)
* [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps)
* [Supercronic](https://github.com/aptible/supercronic)
* [Overmind](https://github.com/DarthSim/overmind)
* [Caddy](https://caddyserver.com/)


## Getting Started

1. **Fork this Repository:**  Click the "Fork" button.
2. **Fly.io Account:** Sign up for a [Fly.io](https://fly.io/) account if you don't have one.
3. **Configure Settings:** Adjust Fly.io and GitHub settings to match your needs.
4. **Environment Variables:** Update the `Dockerfile` with necessary environment variables (see below).
5. **GitHub Secrets:** Add the following secrets to your GitHub repository:
    * `ADMIN_TOKEN`
    * `DATABASE` (Database URL)
    * `FLY_API_TOKEN`
    * `FLY_APP` (Fly.io app name)
    * `USERNAME` (GitHub username for backups)
    * `PASS` (Passphrase to encrypt/decrypt backups)
    * `PUSH_INSTALLATION_ID` (Refer to Vaultwarden documentation)
    * `PUSH_INSTALLATION_KEY`
    * `B2_APPLICATION_KEY_ID`
    * `B2_APPLICATION_KEY`
    * `B2_BUCKET`
    * `SMTP_HOST` (e.g., `smtp.gmail.com`)
    * `SMTP_PORT` (e.g., `465` or `587`)
    * `SMTP_SECURITY` (e.g., `force_tls`)
    * `SMTP_USERNAME`
    * `SMTP_PASSWORD`
    * `CF_ACCESS_KEY` (Cloudflare R2 Access Key ID)
    * `CF_ACCESS_KEY_SECRET` (Cloudflare R2 Access Key Secret)
    * `CF_R2_ENDPOINT` (Cloudflare R2 Endpoint)
    * `DOMAIN` (Your domain, e.g., `vault.my.com`)
    * `TOKEN` (GitHub token for uploading backups)
    *  `CF_TOKEN` (Cloudflare Tunnel token -- see `start_cloudflared.sh`)

6. **Backup Scripts:** Update `scripts/restore-data-github.sh` and `scripts/backup-data-github.sh` with your GitHub repository information (username, repo name).
7. **Deploy:** Use `flyctl deploy` to deploy to Fly.io (refer to `deploy-fly.yml` for example usage).

## Backing Up and Restoring

* **Manual Backup:** SSH into your Fly.io instance and execute the relevant backup script in the `scripts` directory.
* **Restore from GitHub:**  Use `./restore-data-github.sh <backup_filename>` (e.g., `./restore-data-github.sh backup-10-22-22.tar.gz.gpg`) within your Fly.io instance.
* **Release Pruning:**  Adjust the retention period in `.github/workflows/clear-old-releases.yml` if needed.


## Configuration

Refer to the respective files (e.g., `Dockerfile`, `fly.toml`, `Caddyfile`, scripts in the `scripts` directory) for configuration options.


## Acknowledgements

* [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps)
* [Supercronic](https://github.com/aptible/supercronic)
* [Overmind](https://github.com/DarthSim/overmind)
* [Caddy](https://caddyserver.com/)
* [Vaultwarden](https://github.com/dani-garcia/vaultwarden)

## License

[MIT License](LICENSE)


## Author

[MartinatorTime](https://github.com/MartinatorTime)

