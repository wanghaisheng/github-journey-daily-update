---
author: Bob Johnson
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'YouTube AutoComplete Scraper - An Apify actor that scrapes YouTube's search suggestions with intelligent deduplication using pglite and trigram similarity matching. Perfect for content research, SEO, and trend analysis.'
featured: true
keywords: {"id":"0193e86d452539fbdf30df7267b4ed59","object":"chat.completion","created":1734771295,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- YouTube autocomplete scraper\n- Apify actor\n- Intelligent deduplication\n- pglite\n- Trigram similarity matching\n- Content research\n- SEO\n- Trend analysis\n- TypeScript library\n- Similarity threshold\n- Deployment\n- Local development\n- Apify platform\n- API querying\n- Deduplication\n- Result processing\n- Input schema\n- Output\n\n### Tags\n- #YouTube\n- #SEO\n- #Scraping\n- #ContentResearch\n- #TrendAnalysis\n- #Apify\n- #TypeScript\n- #Deduplication\n- #WebScraping"},"finish_reason":"stop"}],"usage":{"prompt_tokens":695,"completion_tokens":133,"total_tokens":828},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Bob Johnson
  name: author
- content: {"id":"0193e86d452539fbdf30df7267b4ed59","object":"chat.completion","created":1734771295,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- YouTube autocomplete scraper\n- Apify actor\n- Intelligent deduplication\n- pglite\n- Trigram similarity matching\n- Content research\n- SEO\n- Trend analysis\n- TypeScript library\n- Similarity threshold\n- Deployment\n- Local development\n- Apify platform\n- API querying\n- Deduplication\n- Result processing\n- Input schema\n- Output\n\n### Tags\n- #YouTube\n- #SEO\n- #Scraping\n- #ContentResearch\n- #TrendAnalysis\n- #Apify\n- #TypeScript\n- #Deduplication\n- #WebScraping"},"finish_reason":"stop"}],"usage":{"prompt_tokens":695,"completion_tokens":133,"total_tokens":828},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86d452539fbdf30df7267b4ed59","object":"chat.completion","created":1734771295,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords\n- YouTube autocomplete scraper\n- Apify actor\n- Intelligent deduplication\n- pglite\n- Trigram similarity matching\n- Content research\n- SEO\n- Trend analysis\n- TypeScript library\n- Similarity threshold\n- Deployment\n- Local development\n- Apify platform\n- API querying\n- Deduplication\n- Result processing\n- Input schema\n- Output\n\n### Tags\n- #YouTube\n- #SEO\n- #Scraping\n- #ContentResearch\n- #TrendAnalysis\n- #Apify\n- #TypeScript\n- #Deduplication\n- #WebScraping"},"finish_reason":"stop"}],"usage":{"prompt_tokens":695,"completion_tokens":133,"total_tokens":828},"system_fingerprint":""}
theme: light
title: youtube-autocomplete-scraper
---

# youtube-autocomplete-scraper

## Repository URL: 
[https://github.com/wanghaisheng/youtube-autocomplete-scraper](https://github.com/wanghaisheng/youtube-autocomplete-scraper)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
YouTube AutoComplete Scraper - An Apify actor that scrapes YouTube's search suggestions with intelligent deduplication using pglite and trigram similarity matching. Perfect for content research, SEO, and trend analysis.

## README Content: 
# Youtube AutoComplete Scraper

A TypeScript library for scraping YouTube's autocomplete suggestions with intelligent deduplication.

## Features

- Scrapes YouTube's autocomplete API to get search suggestions
- Uses pglite for efficient similarity filtering
- Removes near-duplicate suggestions using trigram similarity
- Configurable similarity threshold
- TypeScript support
- Ready to deploy on Apify platform

## Installation

```bash
git clone https://github.com/yourusername/youtube-autocomplete-scraper.git
cd youtube-autocomplete-scraper
pnpm install
```

## Usage

There are two ways to use this scraper:

### 1. Local Development

Run the scraper locally by setting the required environment variables and using `pnpm start`:

```bash
# Set your input
export INPUT='{"query": "how to make"}'

# Run the scraper
pnpm start
```

The scraper will output results to the console and save them in the `apify_storage` directory.

### 2. Deploy to Apify

This scraper is designed to run on the Apify platform. To deploy:

1. Push this code to your Apify actor
2. Set the input JSON in Apify console:

```json
{
  "query": "how to make",
  "similarityThreshold": 0.7,
  "maxResults": 100,
  "language": "en",
  "region": "US"
}
```

## How it Works

Under the hood, this scraper does a few key things:

1. **API Querying**: Makes requests to YouTube's internal autocomplete API endpoint to get raw suggestions

2. **Deduplication**: Uses pglite (a lightweight Postgres implementation) to filter out near-duplicate results:

   - Converts suggestions to trigrams (3-letter sequences)
   - Calculates similarity scores between suggestions using trigram matching
   - Filters out suggestions that are too similar based on a configurable threshold
   - For example, "how to cook pasta" and "how to cook noodles" might be considered unique, while "how to make pancake" and "how to make pancakes" would be filtered as duplicates

3. **Result Processing**: Cleans and normalizes the suggestions before returning them

## Input Schema

The scraper accepts the following input parameters:

```typescript
interface Input {
  query: string // The search query to get suggestions for
  similarityThreshold?: number // How similar suggestions need to be to be considered duplicates (0-1)
  maxResults?: number // Maximum number of suggestions to return
  language?: string // Language code for suggestions
  region?: string // Region code for suggestions
}
```

## Output

The scraper outputs an array of unique autocomplete suggestions. Results are saved to the default dataset in Apify storage and can be accessed via the Apify API or console.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT

