---
author: John Doe
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Interface to generate Github Issue Forms'
featured: true
keywords: {"id":"0193e861a77088d13bf75aa60ffa04c4","object":"chat.completion","created":1734770534,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Certainly! Here are the extracted keywords and tags from the given text:\n\n### Keywords:\n- Issue Forms\n- Github\n- Issue Forms Creator\n- YAML\n- Forms generator\n- Live preview\n- Drag and drop\n- Repositories\n- Labels\n- Contributors\n- Validations\n- Bug/Feature request\n- UI Component Library\n- Storybook\n- Open source\n\n### Tags:\n- #GitHub\n- #DeveloperTools\n- #FormsGenerator\n- #YAML\n- #IssueForms\n- #LivePreview\n- #DragDrop\n- #Repositories\n- #Labels\n- #Contributors\n- #Validations\n- #BugFix\n- #FeatureRequest\n- #UIComponentLibrary\n- #Storybook\n- #OpenSource"},"finish_reason":"stop"}],"usage":{"prompt_tokens":445,"completion_tokens":160,"total_tokens":605},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: {"id":"0193e861a77088d13bf75aa60ffa04c4","object":"chat.completion","created":1734770534,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Certainly! Here are the extracted keywords and tags from the given text:\n\n### Keywords:\n- Issue Forms\n- Github\n- Issue Forms Creator\n- YAML\n- Forms generator\n- Live preview\n- Drag and drop\n- Repositories\n- Labels\n- Contributors\n- Validations\n- Bug/Feature request\n- UI Component Library\n- Storybook\n- Open source\n\n### Tags:\n- #GitHub\n- #DeveloperTools\n- #FormsGenerator\n- #YAML\n- #IssueForms\n- #LivePreview\n- #DragDrop\n- #Repositories\n- #Labels\n- #Contributors\n- #Validations\n- #BugFix\n- #FeatureRequest\n- #UIComponentLibrary\n- #Storybook\n- #OpenSource"},"finish_reason":"stop"}],"usage":{"prompt_tokens":445,"completion_tokens":160,"total_tokens":605},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e861a77088d13bf75aa60ffa04c4","object":"chat.completion","created":1734770534,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Certainly! Here are the extracted keywords and tags from the given text:\n\n### Keywords:\n- Issue Forms\n- Github\n- Issue Forms Creator\n- YAML\n- Forms generator\n- Live preview\n- Drag and drop\n- Repositories\n- Labels\n- Contributors\n- Validations\n- Bug/Feature request\n- UI Component Library\n- Storybook\n- Open source\n\n### Tags:\n- #GitHub\n- #DeveloperTools\n- #FormsGenerator\n- #YAML\n- #IssueForms\n- #LivePreview\n- #DragDrop\n- #Repositories\n- #Labels\n- #Contributors\n- #Validations\n- #BugFix\n- #FeatureRequest\n- #UIComponentLibrary\n- #Storybook\n- #OpenSource"},"finish_reason":"stop"}],"usage":{"prompt_tokens":445,"completion_tokens":160,"total_tokens":605},"system_fingerprint":""}
theme: light
title: issue-forms-creator
---

# issue-forms-creator

## Repository URL: 
[https://github.com/wanghaisheng/issue-forms-creator](https://github.com/wanghaisheng/issue-forms-creator)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Interface to generate Github Issue Forms

## README Content: 
<p align="center">
 <img width="20%" height="20%" src="./src/assets/svg/logo.svg" alt="project logo">
</p>

<br />

> build Issue Forms with forms with ease

Issue Forms Creator is a generator for the [Github Issue Forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository#creating-issue-forms) feature.
Rather than typing your own yaml file, fill a form and copy the yaml version.

Benefits :
* ✅ less prone errors
* ✅ expose the all available options
* ✅ live preview
* ✅ drag and drop support to sort your content
* ✅ bug/feature request starters
* ✅ yaml import support
* ✅ use most of the [validations](https://gh-community.github.io/issue-template-feedback/structured/#common-validation-errors) made by Github
* ✅ load an existing repo to retrieve labels and contributors

## Usage

* (optional) load your repository to retrieve labels and contributors
* add and fill fields
* copy the yaml file
* create a `.yml` file into the `.github/ISSUE_TEMPLATE` folder
* paste the copied content into this new file
* commit the changes

## Developer

You will find guidelines to run the project [here](https://github.com/geromegrignon/issue-forms-creator/blob/main/docs/DEVELOPER.md)

## Contributing

Read through our [contributing guidelines](https://github.com/geromegrignon/issue-forms-creator/blob/main/CONTRIBUTING.md) to learn about our submission process, coding rules and more.

## Ui Component Library

The UI Component Library is built with Storybook and deployed [here](https://issue-forms-creator-storybook.netlify.app/).

