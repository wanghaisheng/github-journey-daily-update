---
author: Jane Smith
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'url to get html content, convert it to markdown,convert to json,etc'
featured: true
keywords: {"id":"0193e86753a1748a7f8ea8230f67d773","object":"chat.completion","created":1734770906,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags\n\n1. **markitdown**\n2. **MarkItDown**\n3. **Markdown Conversion**\n4. **File Formats**\n5. **PDF Conversion**\n6. **PowerPoint Conversion**\n7. **Word Document Conversion**\n8. **Excel Spreadsheet Conversion**\n9. **Image Conversion**\n10. **Audio Conversion**\n11. **HTML Conversion**\n12. **PDF (.pdf)**\n13. **PowerPoint (.pptx)**\n14. **Word (.docx)**\n15. **Excel (.xlsx)**\n16. **Images (EXIF metadata, and OCR)**\n17. **Audio (EXIF metadata, and speech transcription)**\n18. **HTML (special handling of Wikipedia)**\n19. **Text-based Formats (csv, json, xml)**\n20. **Installation (pip)**\n21. **Usage API**\n22. **Large Language Models (LLMs)**\n23. **Contributing**\n24. **Contributor License Agreement (CLA)**\n25. **Code of Conduct**\n26. **Tests (hatch command)**\n27. **Pre-commit Checks**\n28. **Trademarks**\n29. **Microsoft Trademarks**\n30. **Third-party Trademarks**\n\nThese tags and keywords capture the main components, functionalities, and aspects of the `markitdown` library as described in the provided text."},"finish_reason":"stop"}],"usage":{"prompt_tokens":692,"completion_tokens":299,"total_tokens":991},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: {"id":"0193e86753a1748a7f8ea8230f67d773","object":"chat.completion","created":1734770906,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags\n\n1. **markitdown**\n2. **MarkItDown**\n3. **Markdown Conversion**\n4. **File Formats**\n5. **PDF Conversion**\n6. **PowerPoint Conversion**\n7. **Word Document Conversion**\n8. **Excel Spreadsheet Conversion**\n9. **Image Conversion**\n10. **Audio Conversion**\n11. **HTML Conversion**\n12. **PDF (.pdf)**\n13. **PowerPoint (.pptx)**\n14. **Word (.docx)**\n15. **Excel (.xlsx)**\n16. **Images (EXIF metadata, and OCR)**\n17. **Audio (EXIF metadata, and speech transcription)**\n18. **HTML (special handling of Wikipedia)**\n19. **Text-based Formats (csv, json, xml)**\n20. **Installation (pip)**\n21. **Usage API**\n22. **Large Language Models (LLMs)**\n23. **Contributing**\n24. **Contributor License Agreement (CLA)**\n25. **Code of Conduct**\n26. **Tests (hatch command)**\n27. **Pre-commit Checks**\n28. **Trademarks**\n29. **Microsoft Trademarks**\n30. **Third-party Trademarks**\n\nThese tags and keywords capture the main components, functionalities, and aspects of the `markitdown` library as described in the provided text."},"finish_reason":"stop"}],"usage":{"prompt_tokens":692,"completion_tokens":299,"total_tokens":991},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86753a1748a7f8ea8230f67d773","object":"chat.completion","created":1734770906,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords and Tags\n\n1. **markitdown**\n2. **MarkItDown**\n3. **Markdown Conversion**\n4. **File Formats**\n5. **PDF Conversion**\n6. **PowerPoint Conversion**\n7. **Word Document Conversion**\n8. **Excel Spreadsheet Conversion**\n9. **Image Conversion**\n10. **Audio Conversion**\n11. **HTML Conversion**\n12. **PDF (.pdf)**\n13. **PowerPoint (.pptx)**\n14. **Word (.docx)**\n15. **Excel (.xlsx)**\n16. **Images (EXIF metadata, and OCR)**\n17. **Audio (EXIF metadata, and speech transcription)**\n18. **HTML (special handling of Wikipedia)**\n19. **Text-based Formats (csv, json, xml)**\n20. **Installation (pip)**\n21. **Usage API**\n22. **Large Language Models (LLMs)**\n23. **Contributing**\n24. **Contributor License Agreement (CLA)**\n25. **Code of Conduct**\n26. **Tests (hatch command)**\n27. **Pre-commit Checks**\n28. **Trademarks**\n29. **Microsoft Trademarks**\n30. **Third-party Trademarks**\n\nThese tags and keywords capture the main components, functionalities, and aspects of the `markitdown` library as described in the provided text."},"finish_reason":"stop"}],"usage":{"prompt_tokens":692,"completion_tokens":299,"total_tokens":991},"system_fingerprint":""}
theme: light
title: reddit-comment-collect
---

# reddit-comment-collect

## Repository URL: 
[https://github.com/wanghaisheng/reddit-comment-collect](https://github.com/wanghaisheng/reddit-comment-collect)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
url to get html content, convert it to markdown,convert to json,etc

## README Content: 
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

