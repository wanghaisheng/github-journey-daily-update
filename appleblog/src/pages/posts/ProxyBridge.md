---
author: Bob Johnson
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: '这是借用 actions workflow 产生网络环境并使用 sing-box + cloudflare tunnel (临时 argo) + vmess 共享网络环境并通过 cloudflared tunnel 加速网络数据从而让我访问国际互联网的临时应急方案。'
featured: true
keywords: {"id":"0193e866c1c44d5ec5be6ca77df88a24","object":"chat.completion","created":1734770868,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### 关键词\n- ProxyBridge\n- workflow\n- sing-box\n- cloudflare tunnel\n- vmess\n- cloudflared tunnel\n- 国际互联网\n- 临时应急方案\n- GITHUB_TOKEN\n- environment variables\n- email smtp\n- secret\n-_actions\n- 二维码\n- .git large files\n\n### 标签\n- 技术方案\n- 互联网访问\n- GitHub Actions\n- 代理工具\n- 网络加速\n- 开源项目\n- 邮件通知\n- 系统配置\n- 安全措施"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1843,"completion_tokens":127,"total_tokens":1970},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Bob Johnson
  name: author
- content: {"id":"0193e866c1c44d5ec5be6ca77df88a24","object":"chat.completion","created":1734770868,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### 关键词\n- ProxyBridge\n- workflow\n- sing-box\n- cloudflare tunnel\n- vmess\n- cloudflared tunnel\n- 国际互联网\n- 临时应急方案\n- GITHUB_TOKEN\n- environment variables\n- email smtp\n- secret\n-_actions\n- 二维码\n- .git large files\n\n### 标签\n- 技术方案\n- 互联网访问\n- GitHub Actions\n- 代理工具\n- 网络加速\n- 开源项目\n- 邮件通知\n- 系统配置\n- 安全措施"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1843,"completion_tokens":127,"total_tokens":1970},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e866c1c44d5ec5be6ca77df88a24","object":"chat.completion","created":1734770868,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### 关键词\n- ProxyBridge\n- workflow\n- sing-box\n- cloudflare tunnel\n- vmess\n- cloudflared tunnel\n- 国际互联网\n- 临时应急方案\n- GITHUB_TOKEN\n- environment variables\n- email smtp\n- secret\n-_actions\n- 二维码\n- .git large files\n\n### 标签\n- 技术方案\n- 互联网访问\n- GitHub Actions\n- 代理工具\n- 网络加速\n- 开源项目\n- 邮件通知\n- 系统配置\n- 安全措施"},"finish_reason":"stop"}],"usage":{"prompt_tokens":1843,"completion_tokens":127,"total_tokens":1970},"system_fingerprint":""}
theme: light
title: ProxyBridge
---

# ProxyBridge

## Repository URL: 
[https://github.com/wanghaisheng/ProxyBridge](https://github.com/wanghaisheng/ProxyBridge)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
这是借用 actions workflow 产生网络环境并使用 sing-box + cloudflare tunnel (临时 argo) + vmess 共享网络环境并通过 cloudflared tunnel 加速网络数据从而让我访问国际互联网的临时应急方案。

## README Content: 
# ProxyBridge
这是借用 actions workflow 产生网络环境并使用 sing-box + cloudflare tunnel (临时 argo) + vmess 共享网络环境并通过 cloudflared tunnel 加速网络数据从而让我访问国际互联网的临时应急方案。

[![GitHub Workflow Status](https://github.com/20241204/ProxyBridge/actions/workflows/actions.yml/badge.svg)](https://github.com/20241204/ProxyBridge/actions/workflows/actions.yml)![Watchers](https://img.shields.io/github/watchers/20241204/ProxyBridge) ![Stars](https://img.shields.io/github/stars/20241204/ProxyBridge) ![Forks](https://img.shields.io/github/forks/20241204/ProxyBridge) ![Vistors](https://visitor-badge.laobi.icu/badge?page_id=20241204.ProxyBridge) ![LICENSE](https://img.shields.io/badge/license-CC%20BY--SA%204.0-green.svg)
<a href="https://star-history.com/#20241204/ProxyBridge&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=20241204/ProxyBridge&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=20241204/ProxyBridge&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=20241204/ProxyBridge&type=Date" />
  </picture>
</a>

## 描述
1. 这个项目主要是为了临时能够正常看 youtube 和 google。  
2. 为了实现 actions workflow 自动化运行，需要添加 `GITHUB_TOKEN` 环境变量，这个是访问 GitHub API 的令牌，可以在 GitHub 主页，点击个人头像，Settings -> Developer settings -> Personal access tokens -> Tokens (classic) -> Generate new token -> Generate new token (classic) ，设置名字为 GITHUB_TOKEN 接着要配置 环境变量有效时间，勾选环境变量作用域 repo write:packages workflow 和 admin:repo_hook 即可，最后点击Generate token，如图所示
![image](assets/00.jpeg)
![image](assets/01.jpeg)
![image](assets/02.jpeg)
![image](assets/03.jpeg)

3. 赋予 actions[bot] 读/写仓库权限，在仓库中点击 Settings -> Actions -> General -> Workflow Permissions -> Read and write permissions -> save，如图所示
![image](assets/04.jpeg) 

4. 添加 email smtp 服务器域名 `MAILADDR` 在 GitHub 仓库页 -> Settings -> Secrets -> actions -> New repository secret    
5. 添加 email smtp 服务器端口 `MAILPORT` 在 GitHub 仓库页 -> Settings -> Secrets -> actions -> New repository secret    
6. 添加 email smtp 服务器登录账号 `MAILUSERNAME` 在 GitHub 仓库页 -> Settings -> Secrets -> actions -> New repository secret  
7. 添加 email smtp 服务器第三方登陆授权码 `MAILPASSWORD` 在 GitHub 仓库页 -> Settings -> Secrets -> actions -> New repository secret  
8. 添加  email smtp 服务器应该发送邮件位置 `MAILSENDTO` 在 GitHub 仓库页 -> Settings -> Secrets -> actions -> New repository secret
9. 以上 4~9 步流程类似如图所示
![image](assets/05.jpeg)
![image](assets/06.jpeg)

10. 转到 Actions

        -> ProxyBridge 启动 workflow，实现自动化启动桥接代理，连接方式会发送到邮件  
        -> Remove Old Workflow Runs 启动 workflow，实现移除老旧的 workflow  
        -> Clean Git Large Files 启动 workflow，实现清理 .git 大文件  

12. 新目录结构  

        .
        ├── .github                                     # github actions workflow 配置目录  
        │   └── workflows                               # github actions workflow 配置文件目录  
        │       ├── actions.yml                         # github actions workflow 执行配置
        │       ├── clean-git-large-files.yml           # github actions workflow 清理 .git 大文件
        │       └── remove-old-workflow.yml             # github actions workflow 移除老旧的 workflow
        ├── assets                                      # 描述文件图片资源
        ├── set-sing-box.sh                             # 搭建配置 sing-box 脚本  
        └── README.md                                   # 这个是说明文件   

14. 脚本会生成4个文件发送到邮箱，如下图  

        1. result.txt
            a. 包含 vmess 端口转发信息以及共享支持 nekobox 导入链接
        2. VMESS.png
            a. vmess 支持 nekobox 二维码扫描导入
        3. client-nekobox-config.yaml
            a. nekobox 配置文件支持 nekobox 导入
        4. client-sing-box-config.json
            a. sing-box 配置文件支持 sing-box 导入

![image](assets/07.jpeg)

# 更新
    1. 出于安全考虑还是使用邮箱把发送内容发给自己的邮箱，生成的文件支持 sing-box nekobx 客户端  
    2. 维持的时间还是不稳定，最长维持 44min42s  
    3. 修改发件内容为文本附近形式  
    4. 修改了描述文件，提供详细的描述，方便他人
    5. 添加注释，方便以后的人改写脚本代码
    6. 更新添加优选IP
    7. 生成 vmess 二维码图片和链接方便 nekobox 客户端导入
    8. 生成 yaml 配置文件方便 nekobox 客户端导入

# 缺陷
    1. 经历了许多次无奈，反复折磨，tcp和udp互转，我终于认清了现实，
       在github的actions流环境下，cloudflare 不支持 sing-box 的 udp 数据转发
       我尝试了很多，udp转tcp，tcp转udp，端口监听，我真的尽力了，现在我一点办法也没有，
       唉，我只能用vmess，也许你会问我为什么不买云服务器，我只是想说，太贵了，
       唉，我不想花钱，忍着吧

# 声明
本项目仅作学习交流使用，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。  

# 注意
多人 fork 本项目且一起运行 actions 时，可能会导致本人项目被ban掉，所以，你可以创建新项目，把文件复制过去，自己享用

# 感谢&参考  
sing-box: https://sing-box.sagernet.org/   
cloudflared: https://github.com/cloudflare/cloudflared  
CloudflareSpeedTest: https://github.com/XIU2/CloudflareSpeedTest  
使用 email smtp 发送邮件: https://blog.csdn.net/liuyuinsdu/article/details/113878840  
youtube 绵阿羊 在sing-box上安装reality和hysteria2: https://www.youtube.com/watch?v=hbrOxWrGmTc  
文档 绵阿羊 在sing-box上安装reality和hysteria2: https://blog.mareep.net/posts/15209  
github vveg26/sing-box-reality-hysteria2: https://github.com/vveg26/sing-box-reality-hysteria2  
github teddysun/across: https://github.com/teddysun/across  
github 233boy: https://github.com/233boy/sing-box

