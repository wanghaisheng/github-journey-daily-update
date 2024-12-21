---
author: Jane Smith
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734780082334_gs6n3h
  url: https://fluxapi.borninsea.com/image/image_1734780082334_gs6n3h
description: 'Simple tool to extract target subdomains + URLs from Wayback Machine'
featured: true
keywords: archivesuburls,Wayback_Machine,subdomains,URLs,Linux,bash,installation,git,script,usage,time_limit,cURL
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: archivesuburls,Wayback_Machine,subdomains,URLs,Linux,bash,installation,git,script,usage,time_limit,cURL
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- archivesuburls,bash,WaybackMachine[subdomain,URL extraction],git,CURL,max-time
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




