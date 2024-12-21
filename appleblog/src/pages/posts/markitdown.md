---
author: John Doe
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Python tool for converting files and office documents to Markdown.'
featured: true
keywords: {"id":"0193e86361194036196fc9e1649ea8d9","object":"chat.completion","created":1734770647,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Based on the provided text, the following keywords and tags can be extracted:\n\n**Keywords:**\n- markitdown\n- markdown conversion\n- library\n- office documents\n- third-party client\n- AI\n- Large Language Models\n- PDF\n- PowerPoint\n- Word\n- Excel\n- images\n- audio\n- HTML\n- text-based formats\n- installation\n- usage\n- CLA\n- Microsoft Open Source Code of Conduct\n- tests\n- pre-commit checks\n- trademarks\n\n**Tags:**\n- markdown\n- document conversion\n- Python\n- utility tool\n- AI integration\n- file formats\n- open source\n- API\n- contributions\n- testing\n- office files\n- images and audio\n- text and data formats\n- open source contributors\n- code of conduct"},"finish_reason":"stop"}],"usage":{"prompt_tokens":715,"completion_tokens":166,"total_tokens":881},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: {"id":"0193e86361194036196fc9e1649ea8d9","object":"chat.completion","created":1734770647,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Based on the provided text, the following keywords and tags can be extracted:\n\n**Keywords:**\n- markitdown\n- markdown conversion\n- library\n- office documents\n- third-party client\n- AI\n- Large Language Models\n- PDF\n- PowerPoint\n- Word\n- Excel\n- images\n- audio\n- HTML\n- text-based formats\n- installation\n- usage\n- CLA\n- Microsoft Open Source Code of Conduct\n- tests\n- pre-commit checks\n- trademarks\n\n**Tags:**\n- markdown\n- document conversion\n- Python\n- utility tool\n- AI integration\n- file formats\n- open source\n- API\n- contributions\n- testing\n- office files\n- images and audio\n- text and data formats\n- open source contributors\n- code of conduct"},"finish_reason":"stop"}],"usage":{"prompt_tokens":715,"completion_tokens":166,"total_tokens":881},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86361194036196fc9e1649ea8d9","object":"chat.completion","created":1734770647,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Based on the provided text, the following keywords and tags can be extracted:\n\n**Keywords:**\n- markitdown\n- markdown conversion\n- library\n- office documents\n- third-party client\n- AI\n- Large Language Models\n- PDF\n- PowerPoint\n- Word\n- Excel\n- images\n- audio\n- HTML\n- text-based formats\n- installation\n- usage\n- CLA\n- Microsoft Open Source Code of Conduct\n- tests\n- pre-commit checks\n- trademarks\n\n**Tags:**\n- markdown\n- document conversion\n- Python\n- utility tool\n- AI integration\n- file formats\n- open source\n- API\n- contributions\n- testing\n- office files\n- images and audio\n- text and data formats\n- open source contributors\n- code of conduct"},"finish_reason":"stop"}],"usage":{"prompt_tokens":715,"completion_tokens":166,"total_tokens":881},"system_fingerprint":""}
theme: light
title: markitdown
---

# markitdown

## Repository URL: 
[https://github.com/wanghaisheng/markitdown](https://github.com/wanghaisheng/markitdown)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Python tool for converting files and office documents to Markdown.

## README Content: 
1. add thirdparty client
2. organize md use ai
3. 
https://github.com/igorbenav/clientai


# MarkItDown

The MarkItDown library is a utility tool for converting various files to Markdown (e.g., for indexing, text analysis, etc.)

It presently supports:

- PDF (.pdf)
- PowerPoint (.pptx)
- Word (.docx)
- Excel (.xlsx)
- Images (EXIF metadata, and OCR)
- Audio (EXIF metadata, and speech transcription)
- HTML (special handling of Wikipedia, etc.)
- Various other text-based formats (csv, json, xml, etc.)

# Installation

You can install `markitdown` using pip:

```python
pip install markitdown
```

or from the source

```sh
pip install -e .
```


# Usage
The API is simple:

```python
from markitdown import MarkItDown

markitdown = MarkItDown()
result = markitdown.convert("test.xlsx")
print(result.text_content)
```

You can also configure markitdown to use Large Language Models to describe images. To do so you must provide mlm_client and mlm_model parameters to MarkItDown object, according to your specific client.

```python
from markitdown import MarkItDown
from openai import OpenAI

client = OpenAI()
md = MarkItDown(mlm_client=client, mlm_model="gpt-4o")
result = md.convert("example.jpg")
print(result.text_content)
```

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

### Running Tests

To run the tests for this project, use the following command:

```sh
hatch shell
hatch test
```

### Running Pre-commit Checks

```sh
pre-commit run --all-files
```

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

