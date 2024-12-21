---
author: John Doe
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734782436263_xtnleo
  url: https://fluxapi.borninsea.com/image/image_1734782436263_xtnleo
description: 'Let your Claude able to think'
featured: true
keywords: Thinking,Protocol,Browser,Extension,Comprehensive,Thinking,Process,Collapsible,-sections,Clean,Modern,Design,Strike,Through-Thought-Process,Easy-To-Read,Automatically-Organized
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: Thinking,Protocol,Browser,Extension,Comprehensive,Thinking,Process,Collapsible,-sections,Clean,Modern,Design,Strike,Through-Thought-Process,Easy-To-Read,Automatically-Organized
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- thinking,claude,prompt,deep_thought,comprehensive_thinking,browser_extension,project_structure,github,chrome_extension,firefox_extension,intellectual_process,easy_to_read,automatic_organization,collapsible_sections,clean_design
theme: light
title: Thinking-Claude-prompt
---

# Thinking-Claude-prompt

## Repository URL: 
[https://github.com/wanghaisheng/Thinking-Claude-prompt](https://github.com/wanghaisheng/Thinking-Claude-prompt)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Let your Claude able to think

## README Content: 
# Thinking Claude

Let Claude think comprehensively before responding!

> **A super quick reminder:**
> Thinking claude **is not aimed for benchmarks or huge leaps in math or something**, since those are pre-determined by the base model (new Claude-3.5 Sonnet).
> I only want to explore how further we could reach with Claude's "deep mindset". That said, when using it in your daily tasks, you will find Claude's inner monolog (thinking process) very very fun and interesting.

## Demo

https://github.com/user-attachments/assets/88ff0c75-c51b-42b9-a042-00d47053795a

## Overview

This project consists of two main components:

1. **Thinking Protocol**: A comprehensive set of instructions that guides Claude to think deeply and systematically before responding
2. **Browser Extension**: A tool that makes Claude's thinking process more readable and manageable in the browser interface

## Project Structure

```bash
thinking-claude/
├── extensions/
│   ├── chrome/          # Current version of Chrome extension
│   ├── chrome_v0/       # Legacy Chrome extension (deprecated)
│   ├── firefox/         # Firefox extension (in development)
│   └── changelog.md
├── model_instructions/
│   ├── changelog.md
│   ├── v5.1-extensive-20241201.md
│   ├── v5.1-20241125.md
│   ├── v5-lite-20241124.md
│   ├── v4-20241118.md
│   ├── v4-lite-20241118.md
│   └── v3.5-20241113.md
├── .github/             # GitHub configurations and workflows
├── .husky/             # Git hooks for development
├── LICENSE
└── README.md
```

The project is organized into two main components:

- `extensions/`: Browser extension implementations

  - `chrome/`: Current version with modern architecture and features
  - `chrome_v0/`: Legacy version (deprecated)
  - `firefox/`: Firefox version (in development)

- `model_instructions/`: Thinking protocols for different versions
  - Contains versioned instruction sets
  - Each version brings improvements to Claude's thinking process

## Thinking Protocol

The thinking protocol instructs Claude to follow a natural, thorough thought process before providing responses.

## Browser Extension

The browser extension makes Claude's thinking process easier to read and use! It automatically organizes Claude's thoughts into neat, collapsible sections.

### Features

- 🎯 Makes Claude's thinking process easy to read
- 🔄 Fold and unfold different parts of Claude's thoughts
- 📋 Copy any part with just one click
- ⚡ Works automatically with new messages
- 🎨 Clean, modern design that's easy on the eyes

### 🚀 Quick Install Guide

1. **Chrome Users (Recommended)**

   - Install directly from the [Chrome Web Store](https://chromewebstore.google.com/detail/thinking-claude/ncjafpbbndpggfhfgjngkcimeaciahpo)

2. **Manual Installation**
   - Download the latest version from our [Releases Page](https://github.com/richards199999/Thinking-Claude/releases)
   - Unzip the file
   - Open Chrome and go to `chrome://extensions/`
   - Turn on "Developer mode" (top right corner)
   - Click "Load unpacked" and select the unzipped folder `dist`

👉 Want more details? Check out our [Extension Guide](extensions/chrome/README.md) for:

- Step-by-step installation instructions
- Development setup
- Advanced features and usage
- Troubleshooting tips

### 🎉 Getting Started

Once installed, just:

1. Visit [Claude.ai](https://claude.ai)
2. Click on the `Choose style` selector in the bottom of input box -> click on `Create & Edit Styles` -> click on `Create Custom Style` -> click on `Describe style manually` -> click on `Start from scratch` -> click on `Use custom instructions (advanced)` -> paste the content of the desired instruction set from `model_instructions/` folder
3. Start chatting with Claude
4. That's it! The extension will automatically make Claude's thinking process more readable

## Why Use Thinking Claude?

- **Better Reasoning**: Get more thorough and well-thought-out responses
- **Transparency**: See how Claude arrives at its conclusions
- **Improved Organization**: Manage long conversations more effectively
- **Quality Control**: Benefit from built-in verification steps

## Contributing

Contributions are welcome! Feel free to:

- Submit bug reports
- Propose new features
- Create pull requests

## License

MIT License - feel free to use and modify as needed.

## Acknowledgments

Special thanks to [@lumpinif](https://github.com/lumpinif) and Claude for the extension!

