---
author: Alice Cooper
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Automatically submits URLs to participating search engines through the IndexNow protocol.'
featured: true
keywords: {"id":"0193e86178545f92a7da61a21d454da8","object":"chat.completion","created":1734770522,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Based on the provided text, here are the extracted keywords and tags:\n\n### Keywords\n- IndexNow\n- GitHub Action\n- URL Submission\n- Search Engines\n- Sitemap\n- Sitemap Index\n- RSS\n- Atom\n- Deployment\n- Security\n- Node.js\n- GitHub Secrets\n- Fetch API\n- XML Parsing\n- Date Calculations\n- Versioning\n\n### Tags\n- IndexNow Protocol\n- GitHub Actions\n- URL Indexing\n- Sitemap Submission\n- Search Engine Optimization (SEO)\n- Dynamic Key Generation\n- API Integration\n- Node.js\n- Security Best Practices\n- Deployment Strategy\n- Open Source\n- GitHub Pages\n- XML and RSS Feeds\n- Date Handling\n- Version Management\n- Polyfills\n- Frameworks and Libraries\n\nThese keywords and tags capture the main points and functionalities described in the text, focusing on the core concepts and technologies involved in the IndexNow Action."},"finish_reason":"stop"}],"usage":{"prompt_tokens":1680,"completion_tokens":192,"total_tokens":1872},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Alice Cooper
  name: author
- content: {"id":"0193e86178545f92a7da61a21d454da8","object":"chat.completion","created":1734770522,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Based on the provided text, here are the extracted keywords and tags:\n\n### Keywords\n- IndexNow\n- GitHub Action\n- URL Submission\n- Search Engines\n- Sitemap\n- Sitemap Index\n- RSS\n- Atom\n- Deployment\n- Security\n- Node.js\n- GitHub Secrets\n- Fetch API\n- XML Parsing\n- Date Calculations\n- Versioning\n\n### Tags\n- IndexNow Protocol\n- GitHub Actions\n- URL Indexing\n- Sitemap Submission\n- Search Engine Optimization (SEO)\n- Dynamic Key Generation\n- API Integration\n- Node.js\n- Security Best Practices\n- Deployment Strategy\n- Open Source\n- GitHub Pages\n- XML and RSS Feeds\n- Date Handling\n- Version Management\n- Polyfills\n- Frameworks and Libraries\n\nThese keywords and tags capture the main points and functionalities described in the text, focusing on the core concepts and technologies involved in the IndexNow Action."},"finish_reason":"stop"}],"usage":{"prompt_tokens":1680,"completion_tokens":192,"total_tokens":1872},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86178545f92a7da61a21d454da8","object":"chat.completion","created":1734770522,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Based on the provided text, here are the extracted keywords and tags:\n\n### Keywords\n- IndexNow\n- GitHub Action\n- URL Submission\n- Search Engines\n- Sitemap\n- Sitemap Index\n- RSS\n- Atom\n- Deployment\n- Security\n- Node.js\n- GitHub Secrets\n- Fetch API\n- XML Parsing\n- Date Calculations\n- Versioning\n\n### Tags\n- IndexNow Protocol\n- GitHub Actions\n- URL Indexing\n- Sitemap Submission\n- Search Engine Optimization (SEO)\n- Dynamic Key Generation\n- API Integration\n- Node.js\n- Security Best Practices\n- Deployment Strategy\n- Open Source\n- GitHub Pages\n- XML and RSS Feeds\n- Date Handling\n- Version Management\n- Polyfills\n- Frameworks and Libraries\n\nThese keywords and tags capture the main points and functionalities described in the text, focusing on the core concepts and technologies involved in the IndexNow Action."},"finish_reason":"stop"}],"usage":{"prompt_tokens":1680,"completion_tokens":192,"total_tokens":1872},"system_fingerprint":""}
theme: light
title: indexnow-action
---

# indexnow-action

## Repository URL: 
[https://github.com/wanghaisheng/indexnow-action](https://github.com/wanghaisheng/indexnow-action)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Automatically submits URLs to participating search engines through the IndexNow protocol.

## README Content: 
<h1 align="center">IndexNow Action</h1>
<p align="center">
<a href="https://github.com/bojieyang/indexnow-action/actions/workflows/basic-validation.yml">
  <img alt="Basic validation" src="https://github.com/bojieyang/indexnow-action/actions/workflows/basic-validation.yml/badge.svg">
</a>
<img alt="GitHub Workflow Status (with branch)" src="https://img.shields.io/github/actions/workflow/status/bojieyang/indexnow-action/test.yml?branch=main">
  <img alt="GitHub release (latest SemVer)" src="https://img.shields.io/github/v/release/bojieyang/indexnow-action">
<img alt="GitHub" src="https://img.shields.io/github/license/bojieyang/indexnow-action">
</p>
<p align="center">
A GitHub Action that automatically submits URLs to participating search engines through the IndexNow protocol.
</p>

<p align="center">
  <a href="README.zh.md">中文版本</a>
</p>

## Usage

### **Prerequisites**

The key file has been obtained from IndexNow and added to your website.

If you don't know how to get the key file, see [IndexNow Document](https://www.indexnow.org/documentation).

> [!TIP]
> If your website is stored in a public repository (such as GitHub Pages), saving the Key file directly in the repository will reveal the content and location of this file, which may be a potential security risk. If you want to avoid this, use a solution that dynamically generates key files at deployment time. Please refer to [Generate IndexNow Key file during deployment](#generate-indexnow-key-file-during-deployment) section.

### **Basic**

```yaml
steps:
  - uses: bojieyang/indexnow-action@v2 # v2 is the latest major version following the action-versioning.
    with:
    # The location of your sitemap must start with http(s). 
    # Currently, XML Sitemap, Sitemap index, RSS and Atom formats are supported.
      sitemap-location: 'https://example.com/sitemap.xml' 
      key: ${{ secrets.INDEXNOW_KEY }} # The key you get from IndexNow.
```

### **Examples**

A complete example used in my blog shows below:

```yaml
name: 'IndexNow'
on:
  schedule:
    # Set the schedule time
    - cron: '0 2 * * *'

jobs:
  check-and-submit:
    runs-on: ubuntu-latest
    steps:
      - name: indexnow-action
        uses: bojieyang/indexnow-action@v2
        with:
          sitemap-location: 'https://bojieyang.github.io/sitemap.xml'
          key: ${{ secrets.INDEXNOW_KEY }}
```

View code from [here](https://github.com/bojieyang/bojieyang.github.io/blob/master/.github/workflows/IndexNow.yml).

### **Inputs**

- sitemap-location
  `required`.
  The location of sitemap file in your website. Must start with https or http(e.g., https://example.com/sitemap.xml).

- key
  `required`.
  The IndexNow key that you get from search engines.

  > **Note** DO NOT stored as plaintext in the workflow file. Use GitHub Secrets instead.
  > More about GitHub Secrets, see [Encrypted Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets).

- key-location
  `optional`.
  Location of the IndexNow key file that you customed.
  If not set, it will assume that there is a file named `{your-indexnow-key}.txt` in the root directory of the website(e.g., https://example.com/{your-indexnow-key}.txt).

  > **Note** DO NOT stored as plaintext in the workflow file. Use GitHub Secrets instead.
  > More about GitHub Secrets, see [Encrypted Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets).

- since
  `optional`.
  URLs with `lastmod` fields in sitemap files within the last {since} {since-unit} will be submitted. The default value is 1.

- since-unit
  `optional`.
  The unit of since. Available units are `minute`, `hour`, `day`, `week`, `month` and `year`. The default value is `day`.

- endpoint
  `optional`.
  The endpoint of a special search engine. Available values are `api.indexnow.org`, `www.bing.com`, `search.seznam.cz` and `yandex.com`. For more details, see: [IndexNow FAQ](https://www.indexnow.org/faq). The default value is `www.bing.com`.

- limit
  `optional`.
  The upper limit for submitting URLs. The default value is 100.

- timeout
  `optional`.
  The timeout both fetch sitemap and submit to the search engine in milliseconds. The default value is 10000 (10 seconds).

- failure-strategy
  `optional`.
  Define the strategy when submit failed. Available strategies are `ignore` and `error`.
  For `ignore`, will outputting an notice only.
  For `error`, outputting an error message also sets the status of action to fail. The default value is `ignore`.


## Supported sitemap formats
- [x] XML Sitemap
- [x] Sitemap Index
- [x] RSS 2.0
- [x] Atom 1.0

## Generate IndexNow Key file during deployment

Dynamically generating the key file during deployment can avoid the problem of leakage caused by storing the key file in a public repository. Different platforms have their own solutions for dynamically generating files during the deployment process. Here we take GitHub Pages as an example to introduce the corresponding solution.

The specific steps of deploying the plan are as follows:
1. Store the contents of IndexNow’s key through GitHub Secrets.
2. Deploy the website through GitHub Action.
3. Add the following content to the deployment configuration corresponding to Action:

```yaml
 jobs:
   build:
     steps: 
      ### ... omit other steps
      - name: Setup IndexNow 
      # Generate files dynamically to prevent them from being leaked in public repositories.
      # This example will put the file in the root directory of the site.You may change the location by yourself.
        run: echo ${{ secrets.INDEXNOW_KEY }} > ${{ secrets.INDEXNOW_KEY }}.txt
      ### ... omit other steps
```
For complete deployment files, see [here](https://github.com/bojieyang/bojieyang.github.io/blob/master/.github/workflows/jekyll.yml)。

## About Versions

The v2 is the current maintenance version and is based on Node.js v20. It is recommended to use the V2 version whenever possible.

The v1 version is a legacy version and is based on Node.js v16. This version can be used when the Node.js v20 version is not available.

## Maintainers

[@bojieyang](https://github.com/bojieyang)

## Acknowledgements

Use [lquixada/cross-fetch](https://github.com/lquixada/cross-fetch) to polyfill the WHATWG Fetch API.

Use [@NaturalIntelligence/fast-xml-parser](https://github.com/NaturalIntelligence/fast-xml-parser) to parse XML.

Use [@iamkun/dayjs](https://github.com/iamkun/dayjs) to simplify date-related calculations.

## Contributing

Contributions are welcome! Please create an issue and if applicable, a design before proceeding with code.

## License

The scripts and documentation in this project are released under the [MIT License](LICENSE)

