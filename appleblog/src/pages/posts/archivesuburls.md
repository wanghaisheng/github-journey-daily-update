---
author: John Doe
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Simple tool to extract target subdomains + URLs from Wayback Machine'
featured: true
keywords: {"id":"0193e85a2ddfae54324548a470673f6b","object":"chat.completion","created":1734770044,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- archivesuburls\n- Wayback Machine\n- subdomains\n- URLs\n- bash tool\n- installation\n- Linux\n- git clone\n- script execution\n- cURL\n- max-time\n- time limit\n- file output\n\n### Tags\n- #tool\n- #security\n- #web-scraping\n- #github\n- #linux-command-line\n- #archive-analysis\n- #url-extraction\n- #subdomain-discovery\n- #cURL-option\n- #time-limit-script"},"finish_reason":"stop"}],"usage":{"prompt_tokens":312,"completion_tokens":111,"total_tokens":423},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: {"id":"0193e85a2ddfae54324548a470673f6b","object":"chat.completion","created":1734770044,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- archivesuburls\n- Wayback Machine\n- subdomains\n- URLs\n- bash tool\n- installation\n- Linux\n- git clone\n- script execution\n- cURL\n- max-time\n- time limit\n- file output\n\n### Tags\n- #tool\n- #security\n- #web-scraping\n- #github\n- #linux-command-line\n- #archive-analysis\n- #url-extraction\n- #subdomain-discovery\n- #cURL-option\n- #time-limit-script"},"finish_reason":"stop"}],"usage":{"prompt_tokens":312,"completion_tokens":111,"total_tokens":423},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e85a2ddfae54324548a470673f6b","object":"chat.completion","created":1734770044,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- archivesuburls\n- Wayback Machine\n- subdomains\n- URLs\n- bash tool\n- installation\n- Linux\n- git clone\n- script execution\n- cURL\n- max-time\n- time limit\n- file output\n\n### Tags\n- #tool\n- #security\n- #web-scraping\n- #github\n- #linux-command-line\n- #archive-analysis\n- #url-extraction\n- #subdomain-discovery\n- #cURL-option\n- #time-limit-script"},"finish_reason":"stop"}],"usage":{"prompt_tokens":312,"completion_tokens":111,"total_tokens":423},"system_fingerprint":""}
theme: light
title: archivesuburls
---

# archivesuburls

## Repository URL: 
[https://github.com/wanghaisheng/archivesuburls](https://github.com/wanghaisheng/archivesuburls)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Simple tool to extract target subdomains + URLs from Wayback Machine

## README Content: 
# archivesuburls
Simple bash tool to extract target subdomains + URLs from Wayback Machine. 



## Install - Linux enviroment

git clone https://github.com/osamahamad/archivesuburls

cd archivesuburls

chmod +x archivesuburls.sh


     


## Usage


```
./archivesuburls.sh target.com 
```

Result > target.com folder created > 2 files inside the folder, one for urls --> wayback-urls.out , other for sub/domains --> wayback-subdomains.out
  

```
./archivesuburls.sh target.com time 600
```



Sometimes when providing huge companies domains, the way back machine will have a long time searching and i don't know really know but i think the search will take a very long time. cURL have beautiful option called --max-time which allow you to set how much time do you want to wait to stop extracting urls in this script.

So you can provide ```time``` as second argument and hit ENTER, set your time in seconds i.e: 600 so the script will execute only for 10 minutes and end the process by giving you 2 files for urls and subdomains extracted from these urls in these 10 minutes.




