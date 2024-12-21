---
author: Jane Smith
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734782293893_n9c7bs
  url: https://fluxapi.borninsea.com/image/image_1734782293893_n9c7bs
description: '能够解出来的“羊了个羊”小游戏demo（react实现，支持自定义主题）'
featured: true
keywords: solvable-sheep-game,羊了个羊,小游戏,react实现,自定义主题,版本号,开源许可,星星数,分支数,问题数,关闭问题数,提交活动,最后提交,生产状态,预览状态,弹出,撤销,洗牌,关卡,内置主题,自定义主题,排行榜,交流,禁止商用,AI整活,深度强化学习,Vite,React,贡献,性能优化,BGM/音效,二次开发,后台存储,Bmob,GNU通用公共许可证,赞助
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: solvable-sheep-game,羊了个羊,小游戏,react实现,自定义主题,版本号,开源许可,星星数,分支数,问题数,关闭问题数,提交活动,最后提交,生产状态,预览状态,弹出,撤销,洗牌,关卡,内置主题,自定义主题,排行榜,交流,禁止商用,AI整活,深度强化学习,Vite,React,贡献,性能优化,BGM/音效,二次开发,后台存储,Bmob,GNU通用公共许可证,赞助
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- solvable-sheep-game,react,demo,自定义主题,小游戏,开源项目,github,版本控制,许可证,星星, forks,issues,提交活动,最后提交,部署状态,金轮主题,骚猪主题,iKUN主题,排行榜,贡献,技术支持,相关仓库,待办事项,二次开发,许可证,资助
theme: light
title: solvable-sheep-game
---

# solvable-sheep-game

## Repository URL: 
[https://github.com/wanghaisheng/solvable-sheep-game](https://github.com/wanghaisheng/solvable-sheep-game)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
能够解出来的“羊了个羊”小游戏demo（react实现，支持自定义主题）

## README Content: 
2024-11-22

# 能够解出来的 "羊了个羊" 小游戏 Demo

<p>
    <img src="https://img.shields.io/github/package-json/v/StreakingMan/solvable-sheep-game" alt="version"/>
    <img src="https://img.shields.io/github/license/StreakingMan/solvable-sheep-game" alt="license" />
    <img src="https://img.shields.io/github/stars/StreakingMan/solvable-sheep-game?style=social" alt="stars" />
    <img src="https://img.shields.io/github/forks/StreakingMan/solvable-sheep-game?style=social" alt="forks" />
    <img src="https://img.shields.io/github/issues-raw/StreaKingman/solvable-sheep-game" alt="issues" />
    <img src="https://img.shields.io/github/issues-closed-raw/StreaKingman/solvable-sheep-game" alt="issues" />
    <img src="https://img.shields.io/github/commit-activity/m/StreakingMan/solvable-sheep-game" alt="commit-activity" />
    <img src="https://img.shields.io/github/last-commit/StreakingMan/solvable-sheep-game" alt="last-commit" />
    <img src="https://img.shields.io/github/deployments/StreakingMan/solvable-sheep-game/Production?label=proccution%20state" alt="production-state" />
    <img src="https://img.shields.io/github/deployments/StreakingMan/solvable-sheep-game/Preview?label=preview%20state" alt="preview-state" />
</p>

坑爹的小游戏（本来玩法挺有意思的，非得恶心人），根本无解（99.99%无解），气的我自己写了个 demo，
扫二维码或<a href="https://solvable-sheep-game.streakingman.com/" target="_blank">pc 浏览器体验</a>

**声明：本项目仅供交流，禁止商用！否则后果自负。基于此项目的二创都是欢迎的，但非二创请不要删除原仓库地址
（啥都不改唯独删除来源我真的会谢 🙄️，请尊重他人劳动成果）**

<img src="qrcode.png" style="width: 250px;" alt="体验地址二维码">

## Feature

-   弹出：弹出队列左侧第一个，无限次数
-   撤销：撤销上一次操作，无限次数
-   洗牌：哗啦哗啦，无限次数
-   关卡：20 关玩到爽，可直接跳
-   内置主题：金轮<img style="width:36px" src="src/themes/jinlun/images/肌肉金轮1.png" />、
    骚猪<img style="width:36px" src="src/themes/pdd/images/1.png" />、
    ikun<img style="width:36px" src="src/themes/ikun/images/kun.png" />（露出黑脚）等
-   自定义主题：自定义图片和音效，快速整活
-   排行榜：皇城 pk

开心就好 😄

![previews.png](previews.png)

## Contribution

vite+react 实现，欢迎 star、issue、pr、fork（尽量标注原仓库地址）

## Related Repo

<a href="https://github.com/opendilab" target="_blank">opendilab</a> 的 AI 整活！移步
<a href="https://github.com/opendilab/DI-sheep" target="_blank">DI-sheep：深度强化学习 + 羊了个羊</a>

<img style="width:250px" src="https://github.com/opendilab/DI-sheep/raw/master/ui/public/demo.gif" alt="" />

## Todo List

-   [x] 基础操作
-   [x] 关卡生成
-   [x] UI/UX 优化
-   [x] 多主题
-   [x] 计时、得分、保存进度机制
-   [x] 排行榜
-   [ ] 性能优化
-   [x] BGM/音效
-   [ ] ~~点击时的缓冲队列，优化交互动画效果~~
-   [x] 该游戏似乎涉嫌抄袭，考证后补充来源说明
-   [ ] ~~桌面应用~~
-   [x] 路径区分主题
-   [x] 主题自定义
-   [x] 本地图片、音频配置

## 二次开发

项目的自定义主题功能涉及到后台存储（Bmob 懒人数据库），如果您只是简单的整活，可能并不需要相关的逻辑。
详细的二次开发说明请移步这里[DIY 指南](/diy/README.md)

## License

[GNU GENERAL PUBLIC LICENSE Version 3](LICENSE.md)

## 资助

~~由于各种白嫖的静态资源托管、后台服务的免费额度都已用完，目前自费升级了相关套餐。~~
如果您喜欢这个项目，觉得本项目对你有帮助的话，可以扫描下方付款码请我喝杯咖啡 ☕️/~~分摊后台服务费用~~～ 😘

2023.5.5 更新：Bmob 服务到期，后台服务已下线，相关功能暂时无法使用，如有需要请自行搭建后台服务

![wxQrCodes.png](wxQrCodes.png)

