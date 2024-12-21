---
author: Jane Smith
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'No description provided.'
featured: true
keywords: {"id":"0193e869e942237a1cab8854d9ead30e","object":"chat.completion","created":1734771075,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- FaWeb\n- 游戏站代码模板\n- 在线一站式出海游戏网站\n- 快速上站\n- 多语言支持\n- 游戏iframe内嵌\n- 游戏下载链接配置\n- 游戏相关视频配置\n- 游戏评论配置\n- 游戏推荐配置\n- 游戏FAQ配置\n- 发布新模板版本\n- update.json配置\n- 更新记录\n- 修复游戏推荐卡片组件类型编译报错\n- 多语言游戏推荐\n- 子游戏页面模板\n- 游戏推荐位置\n- iframe加载问题\n- 路径正确性\n\n### Tags:\n- FaWeb\n- 代码模板\n- 游戏网站制作工具\n- 快速上线\n- 多语言支持\n- 游戏内嵌\n- 游戏下载\n- 游戏配置\n- 多功能配置\n- 更新记录\n- 调试修复"},"finish_reason":"stop"}],"usage":{"prompt_tokens":336,"completion_tokens":212,"total_tokens":548},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: {"id":"0193e869e942237a1cab8854d9ead30e","object":"chat.completion","created":1734771075,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- FaWeb\n- 游戏站代码模板\n- 在线一站式出海游戏网站\n- 快速上站\n- 多语言支持\n- 游戏iframe内嵌\n- 游戏下载链接配置\n- 游戏相关视频配置\n- 游戏评论配置\n- 游戏推荐配置\n- 游戏FAQ配置\n- 发布新模板版本\n- update.json配置\n- 更新记录\n- 修复游戏推荐卡片组件类型编译报错\n- 多语言游戏推荐\n- 子游戏页面模板\n- 游戏推荐位置\n- iframe加载问题\n- 路径正确性\n\n### Tags:\n- FaWeb\n- 代码模板\n- 游戏网站制作工具\n- 快速上线\n- 多语言支持\n- 游戏内嵌\n- 游戏下载\n- 游戏配置\n- 多功能配置\n- 更新记录\n- 调试修复"},"finish_reason":"stop"}],"usage":{"prompt_tokens":336,"completion_tokens":212,"total_tokens":548},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e869e942237a1cab8854d9ead30e","object":"chat.completion","created":1734771075,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- FaWeb\n- 游戏站代码模板\n- 在线一站式出海游戏网站\n- 快速上站\n- 多语言支持\n- 游戏iframe内嵌\n- 游戏下载链接配置\n- 游戏相关视频配置\n- 游戏评论配置\n- 游戏推荐配置\n- 游戏FAQ配置\n- 发布新模板版本\n- update.json配置\n- 更新记录\n- 修复游戏推荐卡片组件类型编译报错\n- 多语言游戏推荐\n- 子游戏页面模板\n- 游戏推荐位置\n- iframe加载问题\n- 路径正确性\n\n### Tags:\n- FaWeb\n- 代码模板\n- 游戏网站制作工具\n- 快速上线\n- 多语言支持\n- 游戏内嵌\n- 游戏下载\n- 游戏配置\n- 多功能配置\n- 更新记录\n- 调试修复"},"finish_reason":"stop"}],"usage":{"prompt_tokens":336,"completion_tokens":212,"total_tokens":548},"system_fingerprint":""}
theme: light
title: sprunkihub
---

# sprunkihub

## Repository URL: 
[https://github.com/wanghaisheng/sprunkihub](https://github.com/wanghaisheng/sprunkihub)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
No description provided.

## README Content: 
# FaWeb游戏站代码模板
当前项目用于 Faweb(https://fafafa.ai) 在线一站式出海游戏网站制作工具所使用的代码模板。

# FaWeb 特点
- 无需编写代码即可实现快速上站，不懂一行代码的人也能完成游戏上站
- 支持多语言，支持游戏iframe内嵌配置，支持游戏下载链接配置，配置游戏相关视频，游戏评论，游戏推荐，游戏FAQ等配置

# 演示站点
- [https://sprunkiretake.fun/](https://sprunkiretake.fun/) Iframe嵌入模式
- [https://devourer.fun/](https://devourer.fun/) 下载链接模式



 # update.json配置注意事项
 - 当需要发布新模板版本时，文件更新列里面不可以添加文件夹目录，只需要将需要更新的文件相对路径添加到更新列表中即可。

 # 版本更新记录
 - 2024-11-19 修复游戏推荐卡片组件类型编译报错，支持多语言游戏推荐、增加子游戏页面模板
  - 修复游戏推荐组件不显示的问题
  - 支持设置游戏推荐位置
  - 修复子游戏iframe无法加载正确地址的问题
  - 修复多语言下出现路径不正确导致google抓取404的问题
