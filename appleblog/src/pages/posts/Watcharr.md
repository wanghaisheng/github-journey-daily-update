---
author: Alice Cooper
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Open source, self-hostable watched list for all your content (movies, tv series, anime, games) with user authentication, modern and clean UI and a very simple setup.'
featured: true
keywords: {"id":"0193e86c92b5089b3d14fb3588224c35","object":"chat.completion","created":1734771249,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Watcharr\n- Open source\n- self-hostable\n- watched list\n- user authentication\n- modern UI\n- clean UI\n- simple setup\n- content management\n- movies\n- TV series\n- anime\n- video games\n- Go\n- Svelte(Kit)\n- self-hosted\n- demo\n- documentation\n- configuration\n- Docker\n- community tools\n- support\n\n### Tags:\n- Open Source\n- Self-Hostable\n- Watched List\n- User Authentication\n- Modern UI\n- Clean Design\n- Simple Setup\n- Content Management\n- Movies\n- TV Shows\n- Anime\n- Video Games\n- Go Programming Language\n- Svelte(Kit)\n- Docker Support\n- Demo Instance\n- Documentation\n- Community Contributions\n- Support Channels"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1141,"completion_tokens":168,"total_tokens":1309},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Alice Cooper
  name: author
- content: {"id":"0193e86c92b5089b3d14fb3588224c35","object":"chat.completion","created":1734771249,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Watcharr\n- Open source\n- self-hostable\n- watched list\n- user authentication\n- modern UI\n- clean UI\n- simple setup\n- content management\n- movies\n- TV series\n- anime\n- video games\n- Go\n- Svelte(Kit)\n- self-hosted\n- demo\n- documentation\n- configuration\n- Docker\n- community tools\n- support\n\n### Tags:\n- Open Source\n- Self-Hostable\n- Watched List\n- User Authentication\n- Modern UI\n- Clean Design\n- Simple Setup\n- Content Management\n- Movies\n- TV Shows\n- Anime\n- Video Games\n- Go Programming Language\n- Svelte(Kit)\n- Docker Support\n- Demo Instance\n- Documentation\n- Community Contributions\n- Support Channels"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1141,"completion_tokens":168,"total_tokens":1309},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86c92b5089b3d14fb3588224c35","object":"chat.completion","created":1734771249,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Watcharr\n- Open source\n- self-hostable\n- watched list\n- user authentication\n- modern UI\n- clean UI\n- simple setup\n- content management\n- movies\n- TV series\n- anime\n- video games\n- Go\n- Svelte(Kit)\n- self-hosted\n- demo\n- documentation\n- configuration\n- Docker\n- community tools\n- support\n\n### Tags:\n- Open Source\n- Self-Hostable\n- Watched List\n- User Authentication\n- Modern UI\n- Clean Design\n- Simple Setup\n- Content Management\n- Movies\n- TV Shows\n- Anime\n- Video Games\n- Go Programming Language\n- Svelte(Kit)\n- Docker Support\n- Demo Instance\n- Documentation\n- Community Contributions\n- Support Channels"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1141,"completion_tokens":168,"total_tokens":1309},"system_fingerprint":""}
theme: light
title: Watcharr
---

# Watcharr

## Repository URL: 
[https://github.com/wanghaisheng/Watcharr](https://github.com/wanghaisheng/Watcharr)

## Stars: 
**1**

## Forks: 
**0**

## Description: 
Open source, self-hostable watched list for all your content (movies, tv series, anime, games) with user authentication, modern and clean UI and a very simple setup.

## README Content: 
<h1 align="center">Watcharr</h1>
<p align="center"><img src="./static/logo-col.png" alt="logo" width="250" /></p>

<p align="center">
  <a href="https://github.com/sbondCo/Watcharr/pkgs/container/watcharr"><img src="https://img.shields.io/github/v/release/sbondCo/Watcharr?label=version&style=for-the-badge" /></a>
  <a href="https://beta.watcharr.app"><img src="https://img.shields.io/website?label=DEMO&style=for-the-badge&url=https%3A%2F%2Fbeta.watcharr.app" /></a>
  <a href="https://watcharr.app"><img src="https://img.shields.io/website?label=DOCS&style=for-the-badge&url=https%3A%2F%2Fwatcharr.app" /></a>
  <a href="https://github.com/sbondCo/Watcharr/issues"><img src="https://img.shields.io/github/issues-raw/sbondCo/Watcharr?label=ISSUES&style=for-the-badge" /></a>
  <a href="/LICENSE"><img src="https://img.shields.io/github/license/sbondCo/Watcharr?style=for-the-badge" /></a>
  <a href="https://matrix.to/#/#watcharr:matrix.org"><img src="https://img.shields.io/matrix/watcharr%3Amatrix.org?style=for-the-badge&logo=matrix" /></a>
</p>

I'm your new easily self-hosted content watched list. The place you store your watched (or watching, planned, etc) **movies** and **tv shows** (and **anime**), rate them and track their status.

With [some extra configuration](https://watcharr.app/docs/server_config/game-support-igdb) I can also track your **video games**.

I am built with Go and Svelte(Kit).

Feel free to abuse this demo instance (nicely), which runs on the latest `dev` build (there may be bugs, as new features are tested on here too): [https://beta.watcharr.app/](https://beta.watcharr.app/)

[Track Progress Until Next Version](https://github.com/orgs/sbondCo/projects/9/views/3)

### Contents

- [Screenshots](#screenshots)
- [Setup](#set-up)
- [Contributing](CONTRIBUTING.md)
- [Community Made Tools](#community-made-tools)
- [Getting Help](#getting-help)

# Screenshots

<p align="center">

| Homepage                                                   | Watched Show Hover                                                      |
| ---------------------------------------------------------- | ----------------------------------------------------------------------- |
| <img src="./screenshot/homepage.png" alt="Watched List" /> | <img src="./screenshot/homepage-poster-hover.png" alt="Watched List" /> |

| Watched Show Status Change                                                              | Movie Details                                                                  |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| <img src="./screenshot/homepage-poster-change-status.png" alt="Changing Show Status" /> | <img src="./screenshot/content-details-page.png" alt="Content Details Page" /> |

| User Profile                                                        | Discover                                                         |
| ------------------------------------------------------------------- | ---------------------------------------------------------------- |
| <img src="./screenshot/user-profile.png" alt="User Profile Page" /> | <img src="./screenshot/discover-page.png" alt="Discover Page" /> |

| Dark Homepage                                                          | Dark Content Details                                                                   |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| <img src="./screenshot/homepage-dark.png" alt="Dark Theme Homepage" /> | <img src="./screenshot/content-details-page-dark.png" alt="Dark Theme Content Page" /> |

</p>

# Set Up

[Checkout our documentation](https://watcharr.app/docs/category/installation) for an up to date guide on setup! If you hate manuals, but love docker, this [docker-compose.yml](./docker-compose.yml) file is your friend.

# Community Made Tools

Third-party tools made by the community for enhancing your Watcharr experience!

- [Kodi Plugin](https://github.com/airdogvan/watcharr_kodi) by [airdogvan](https://github.com/airdogvan) for automatically tracking your watched shows/movies.

Thanks to anyone that has made a script or tool for Watcharr. Feel free to add your own to the list if you have one!

**Note:** I cannot provide any assurances for these tools or stay on top of them (code review, etc), if you have any problems please open an issue in the project for the tool so that they can stay organized.

# Getting Help

If something isn't working for you or you are stuck, [creating an issue](https://github.com/sbondCo/Watcharr/issues/new) is the best way to get help! Every type of issue is accepted, so don't be afraid to ask anything!

You can also [join our space on Matrix](https://matrix.to/#/#watcharr:matrix.org) for support.

