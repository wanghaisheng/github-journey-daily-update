---
author: Jane Smith
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734782396067_i0mnsi
  url: https://fluxapi.borninsea.com/image/image_1734782396067_i0mnsi
description: 'Syrius AI - A clean code and architecture project designed to host knowledge sources in PDF format on AWS S3, leveraging RAG (Retrieval-Augmented Generation) for efficient source searching.'
featured: true
keywords:  syrius_ai, clean code, architecture, knowledge sources, PDF format, AWS S3, RAG, Retrieval-Augmented Generation, API, project-logo, MIT License, last-commit, repository-top-language, repository-language-count, JavaScript, Prettier, Jest, Axios, ESLint, Lodash, TypeScript, tsnode, Nx, JSON
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content:  syrius_ai, clean code, architecture, knowledge sources, PDF format, AWS S3, RAG, Retrieval-Augmented Generation, API, project-logo, MIT License, last-commit, repository-top-language, repository-language-count, JavaScript, Prettier, Jest, Axios, ESLint, Lodash, TypeScript, tsnode, Nx, JSON
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- clean code,architecture,AWS S3,RAG,retrieval-augmented generation,MIT License,last commit,repository top language,repository language count,JavaScript,Prettier,Jest,Axios,ESLint,Lodash,TypeScript,tsnode,Nx,JSON,overview,features,repository structure,getting started,installation,usage,tests,contributing,license
theme: light
title: syrius_ai
---

# syrius_ai

## Repository URL: 
[https://github.com/wanghaisheng/syrius_ai](https://github.com/wanghaisheng/syrius_ai)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Syrius AI - A clean code and architecture project designed to host knowledge sources in PDF format on AWS S3, leveraging RAG (Retrieval-Augmented Generation) for efficient source searching.

## README Content: 
<div align="center" style="width: 100%;">
  <img
    src="apps/api/src/assets/Syrius AI.png"
    alt="project-logo"
    style="max-width: 100%; height: auto;"
  />
</div>
<h1 align="center">SYRIUS_AI</h1>
<p align="center">
  <em>Enhancing AI Interactions with Seamless File Processing and Intelligent Retrieval.</em>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-0184a4?style=plastic&logo=opensourceinitiative&logoColor=white" alt="MIT License">
  <img src="https://img.shields.io/github/last-commit/Romain-Portanguen/syrius_ai?style=plastic&logo=git&logoColor=white&color=0184a4" alt="last-commit">
  <img src="https://img.shields.io/github/languages/top/Romain-Portanguen/syrius_ai?style=plastic&color=0184a4" alt="repo-top-language">
  <img src="https://img.shields.io/github/languages/count/Romain-Portanguen/syrius_ai?style=plastic&color=0184a4" alt="repo-language-count">
</p>
<p align="center">
  <em>Developed with the software and tools below.</em>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=plastic&logo=JavaScript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Prettier-F7B93E.svg?style=plastic&logo=Prettier&logoColor=black" alt="Prettier">
  <img src="https://img.shields.io/badge/Jest-C21325.svg?style=plastic&logo=Jest&logoColor=white" alt="Jest">
  <img src="https://img.shields.io/badge/Axios-5A29E4.svg?style=plastic&logo=Axios&logoColor=white" alt="Axios">
  <img src="https://img.shields.io/badge/ESLint-4B32C3.svg?style=plastic&logo=ESLint&logoColor=white" alt="ESLint">
  <br>
  <img src="https://img.shields.io/badge/Lodash-3492FF.svg?style=plastic&logo=Lodash&logoColor=white" alt="Lodash">
  <img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=plastic&logo=TypeScript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/tsnode-3178C6.svg?style=plastic&logo=ts-node&logoColor=white" alt="tsnode">
  <img src="https://img.shields.io/badge/Nx-143055.svg?style=plastic&logo=Nx&logoColor=white" alt="Nx">
  <img src="https://img.shields.io/badge/JSON-000000.svg?style=plastic&logo=JSON&logoColor=white" alt="JSON">
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [📍 Overview](#-overview)
- [🧩 Features](#-features)
- [🗂️ Repository Structure](#️-repository-structure)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Installation](#️-installation)
  - [🤖 Usage](#-usage)
  - [🧪 Tests](#-tests)
- [🤝 Contributing](#-contributing)
- [🎗 License](#-license)

</details>
<hr>

## 📍 Overview

The syrius_ai project is designed to enable files to be uploaded and to perform RAG (Retrieval-Augmented Generation) on these files in response to a question posed by the user. By integrating advanced AI models such as OpenAI, Anthropic and Mistral, the platform guarantees relevant and transparent contextual interactions. It supports file processing, text integration and vector storage, drawing on robust solutions such as AWS and Pinecone. Thanks to its modular architecture, syrius_ai offers reliable and scalable functionality for document processing, prompt generation and interaction with third-party services, while ensuring secure and efficient integration.

---

## 🧩 Features

|     | Feature          | Description                                                                                                                               |
|-----|------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| ⚙️  | **Architecture** | The project uses a modular architecture with Nx for managing build, serve, and test configurations, enhancing efficiency and scalability. |
| 🔩  | **Code Quality** | The codebase adheres to modern JavaScript standards with TypeScript, using Prettier and ESLint for consistent style and quality.          |
| 🔌  | **Integrations** | Integrates with NestJS, Langchain, and AWS SDK, among others, to provide a robust backend and AI capabilities.                            |
| 🧩  | **Modularity**   | Highly modular, leveraging Nx to manage multiple packages and configurations, facilitating reusability and maintainability.               |
| 🧪  | **Testing**      | Utilizes Jest with Nx Jest preset for testing, ensuring efficient and consistent testing practices across the project.                    |
| ⚡️  | **Performance**  | Performance is optimized through efficient use of TypeScript and modular architecture, though specific benchmarks are not detailed.       |
| 🛡️ | **Security**     | Uses NestJS which provides built-in security features like guards and interceptors.                                                       |
| 📦  | **Dependencies** | Key dependencies include NestJS, Langchain, AWS SDK, and various Nx plugins, supporting a wide range of functionalities.                  |
| 🚀  | **Scalability**  | Designed for scalability with Nx and NestJS, allowing for efficient handling of increased load and traffic.                               |

---

## 🗂️ Repository Structure

```sh
└── syrius_ai/
    ├── README.md
    ├── apps
    │   └── api
    ├── eslint.config.js
    ├── jest.config.ts
    ├── jest.preset.js
    ├── nx.json
    ├── package-lock.json
    ├── package.json
    └── tsconfig.base.json
```

---

## 🚀 Getting Started

**System Requirements:**

- **TypeScript**: `version ~5.5.2`

### ⚙️ Installation

<h4>From <code>source</code></h4>

> 1. Clone the syrius_ai repository:
>
> ```console
> git clone https://github.com/Romain-Portanguen/syrius_ai
> ```
>
> 2. Change to the project directory:
>
> ```console
> cd syrius_ai
> ```
>
> 3. Install the dependencies:
>
> ```console
> npm install
> ```

### 🤖 Usage

<h4>From <code>source</code></h4>

> Run syrius_ai using the command below:
>
> ```console
> nx serve api
> ```

### 🧪 Tests

> Run the test suite using the command below:
>
> ```console
> nx test api
> ```

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/Romain-Portanguen/syrius_ai/issues)**: Submit bugs found or log feature requests for the `syrius_ai` project.
- **[Submit Pull Requests](https://github.com/Romain-Portanguen/syrius_ai/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Romain-Portanguen/syrius_ai/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.

   ```sh
   git clone https://github.com/Romain-Portanguen/syrius_ai
   ```

3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.

   ```sh
   git checkout -b new-feature-x
   ```

4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.

   ```sh
   git commit -m 'Implemented new feature x.'
   ```

6. **Push to github**: Push the changes to your forked repository.

   ```sh
   git push origin new-feature-x
   ```

7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!

</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/Romain-Portanguen/syrius_ai/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Romain-Portanguen/syrius_ai">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [MIT](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

