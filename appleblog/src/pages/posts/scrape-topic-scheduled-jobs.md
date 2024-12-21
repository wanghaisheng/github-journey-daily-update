---
author: Jane Smith
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Collection of jobs scheduled to scrape data. define a topic, config app store category url,reddit sub url'
featured: true
keywords: {"id":"0193e8681105808704fba0877c3b26e7","object":"chat.completion","created":1734770954,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Sure, here are the keywords and tags extracted from the given text:\n\n### Keywords:\n- Scrape\n- Jobs\n- Scheduled\n- Data\n- App Store\n- Finance\n- Mortgage Rates\n- Reddit\n- Subreddits\n- Top Headlines\n- Spotify\n- Podcast Charts\n- Kworb\n- Parcels\n- LDS Meetinghouses\n- Zillow\n- GoFundMe\n- S3\n- TSA\n- MTA\n- 311 Requests\n- NYC\n- NYRR\n- KSL\n- Travel Advisories\n- Hacker News\n\n### Tags:\n- Python\n- R\n- Daily\n- Every 4 Hours\n- Finance Apps\n- Mortgage Rates\n- Reddit Posts\n- Reddit Comments\n- News API\n- Spotify Playlist\n- Spotify Podcast\n- Kworb Data\n- Property Listings\n- Passenger Volume\n- Elevator Status\n- 311 Requests\n- Upcoming Races\n- Rental Listings\n- Travel Advisories\n- Hacker News\n\nThese tags and keywords should help in categorizing and searching for the relevant information about the scheduled jobs."},"finish_reason":"stop"}],"usage":{"prompt_tokens":1134,"completion_tokens":231,"total_tokens":1365},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: {"id":"0193e8681105808704fba0877c3b26e7","object":"chat.completion","created":1734770954,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Sure, here are the keywords and tags extracted from the given text:\n\n### Keywords:\n- Scrape\n- Jobs\n- Scheduled\n- Data\n- App Store\n- Finance\n- Mortgage Rates\n- Reddit\n- Subreddits\n- Top Headlines\n- Spotify\n- Podcast Charts\n- Kworb\n- Parcels\n- LDS Meetinghouses\n- Zillow\n- GoFundMe\n- S3\n- TSA\n- MTA\n- 311 Requests\n- NYC\n- NYRR\n- KSL\n- Travel Advisories\n- Hacker News\n\n### Tags:\n- Python\n- R\n- Daily\n- Every 4 Hours\n- Finance Apps\n- Mortgage Rates\n- Reddit Posts\n- Reddit Comments\n- News API\n- Spotify Playlist\n- Spotify Podcast\n- Kworb Data\n- Property Listings\n- Passenger Volume\n- Elevator Status\n- 311 Requests\n- Upcoming Races\n- Rental Listings\n- Travel Advisories\n- Hacker News\n\nThese tags and keywords should help in categorizing and searching for the relevant information about the scheduled jobs."},"finish_reason":"stop"}],"usage":{"prompt_tokens":1134,"completion_tokens":231,"total_tokens":1365},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e8681105808704fba0877c3b26e7","object":"chat.completion","created":1734770954,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Sure, here are the keywords and tags extracted from the given text:\n\n### Keywords:\n- Scrape\n- Jobs\n- Scheduled\n- Data\n- App Store\n- Finance\n- Mortgage Rates\n- Reddit\n- Subreddits\n- Top Headlines\n- Spotify\n- Podcast Charts\n- Kworb\n- Parcels\n- LDS Meetinghouses\n- Zillow\n- GoFundMe\n- S3\n- TSA\n- MTA\n- 311 Requests\n- NYC\n- NYRR\n- KSL\n- Travel Advisories\n- Hacker News\n\n### Tags:\n- Python\n- R\n- Daily\n- Every 4 Hours\n- Finance Apps\n- Mortgage Rates\n- Reddit Posts\n- Reddit Comments\n- News API\n- Spotify Playlist\n- Spotify Podcast\n- Kworb Data\n- Property Listings\n- Passenger Volume\n- Elevator Status\n- 311 Requests\n- Upcoming Races\n- Rental Listings\n- Travel Advisories\n- Hacker News\n\nThese tags and keywords should help in categorizing and searching for the relevant information about the scheduled jobs."},"finish_reason":"stop"}],"usage":{"prompt_tokens":1134,"completion_tokens":231,"total_tokens":1365},"system_fingerprint":""}
theme: light
title: scrape-topic-scheduled-jobs
---

# scrape-topic-scheduled-jobs

## Repository URL: 
[https://github.com/wanghaisheng/scrape-topic-scheduled-jobs](https://github.com/wanghaisheng/scrape-topic-scheduled-jobs)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Collection of jobs scheduled to scrape data. define a topic, config app store category url,reddit sub url

## README Content: 
# Scheduled Jobs

| Name  | Type | Frequency | Description | Job |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| `apple-app-store.py`  | Python  | Daily  | Scrapes top 100 free Finance apps from the [Apple App Store](https://apps.apple.com/us/charts/iphone/finance-apps/6015?chart=top-free), dumps to S3.  | Job 1 |
| `freddie-mac-rates.py`  | Python  | Daily  | Scrapes mortgage rates published on the home page of [Freddie Mac](https://www.freddiemac.com/), dumps to S3. | Job 1 |
| `mormon-reddit-submissions.py`  | Python  | Daily  | Grabs the latest 250 posts across the ["mormon"](https://www.reddit.com/r/mormon/) subreddits, dumps to S3.  | Job 1 |
| `mormon-reddit-comments.py`  | Python  | Every 4 Hours  | Grabs the latest 250 comments per ["mormon"](https://www.reddit.com/r/mormon/) subreddit, dumps to S3.  | Job 2 |
| `newsapi-top-headlines.py`  | Python  | Daily  | Collects the top headlines from the day from the [News API](https://newsapi.org/), dumps to S3.  | Job 1 |
| `spotify-playlist-history.py`  | Python  | Daily  | Scrapes track list for Spotify's [Rap Cavier](https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd?si=8f0f87a0d4e04e0f) playlist, dumps to S3. | Job 1 |
| `spotify-podcast-charts.py`  | Python  | Daily  | Collects the Spotify [podcast charts](https://podcastcharts.byspotify.com/), dumps to S3. | Job 1 |
| `kworb-scrape.py`  | Python  | Daily  | Grabs [kworb](https://kworb.net/) artist, listener, and chart objects, dumps to S3. | Job 1 |
| `gila-buttes-parcels.r`  | R  | Daily  | Scrapes details for ~280 parcels in the Gila Buttes subdivision in Casa Grande, Arizona, dumps to S3. | Job 3 |
| `lds-meetinghouses-v2.r`  | R  | Daily  | Scrapes [LDS meetinghouse](https://ldsmeetinghouses.com/) locations and unit assignments, dumps to S3. | Job 3 |
| `zillow-scrape.r`  | R  | Daily  | Scrapes [Zillow](https://www.zillow.com/research/data/)'s basic, zipcode-level ZHVF file, dumps to S3. | Job 3 |
| `go-fund-me.r`  | R  | Daily  | Scrapes [GoFundMe](https://www.gofundme.com/discover)'s trending fundraiser list, dumps to S3. | Job 3 |
| `s3-snapshots.py`  | Python  | Daily  | Saves snapshot of all files and directories within S3 bucket, dumps to S3.  | Job 1 |
| `tsa-passenger-volumes.r`  | R  | Daily  | Scrapes daily passenger volume counts reported by the TSA, dumps to S3.  | Job 3 |
| `mta-lift-status.r`  | R  | Daily  | Scrapes elevator and escalator status logs from NY's Metro North Railroad, dumps to S3.  | Job 3 |
| `nyc-311-requests.py`  | Python  | Daily  | Scrapes 10k of the latest NYC 311 requests, dumps to S3. | Job 1 |
| `nyrr-races.r`  | R  | Daily  | Scrapes a list of upcoming races hosted by NYRR, dumps to S3. | Job 3 |
| `ksl-rentals.r`  | R  | Daily  | Scrapes [KSL's](https://homes.ksl.com/rent/search) rental unit listings in Utah County, dumps to S3. | Job 3 |
| `travel-advisories.r`  | R  | Daily  | Scrapes the US State Department's [travel advisory](https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html/) list, dumps to S3. | Job 3 |
| `hacker-news.r`  | R  | Daily  | Scrapes the first ten pages of YC's [Hacker News](https://news.ycombinator.com/news?p=1), dumps to S3. | Job 3 |

