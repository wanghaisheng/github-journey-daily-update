---
author: John Doe
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734780010692_5nzug
  url: https://fluxapi.borninsea.com/image/image_1734780010692_5nzug
description: 'Crawler for Google, Apple Stores and App Ads.txt'
featured: true
keywords: app-ads-sdk-crawler,Google_Play_Shop,iOS_App_Store,app_ads.txt,crawler,scrapers,AppGoblin,advertising_tools,SQL,DDL,Interactive_Advertising_Bureau,Tech_Lab,ads.txt,csv,store_ids,developer_URL,port_forwarding,PostgreSQL,app_discovery,app_details,SSH,tunnel,update_app_details,app_ads_txt_scrape,limit_processes
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: app-ads-sdk-crawler,Google_Play_Shop,iOS_App_Store,app_ads.txt,crawler,scrapers,AppGoblin,advertising_tools,SQL,DDL,Interactive_Advertising_Bureau,Tech_Lab,ads.txt,csv,store_ids,developer_URL,port_forwarding,PostgreSQL,app_discovery,app_details,SSH,tunnel,update_app_details,app_ads_txt_scrape,limit_processes
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- app-ads-sdk-crawler,appgoblin,web-crawler,google-play-store,crawler,apple-app-store,app-adst-txt,crawling,ads-txt,sqlite,python,setup,installation,scraper,decompilation,api-scraping,sql,postgresql,advertising-tools,iabtechlab,crawling-apps,id-discovery,ssh-port-forwarding,remote-database
theme: light
title: app-ads-sdk-crawler
---

# app-ads-sdk-crawler

## Repository URL: 
[https://github.com/wanghaisheng/app-ads-sdk-crawler](https://github.com/wanghaisheng/app-ads-sdk-crawler)

## Stars: 
**1**

## Forks: 
**0**

## Description: 
Crawler for Google, Apple Stores and App Ads.txt

## README Content: 
# Crawl App-Adst.txt and App Store Apps

Various tools used for [AppGoblin](https://appgoblin.info). Mostly scripts for crawling the Google Play and Apple App Stores for as many apps as it can and also checks for their app-ads.txt files. 

Scrapers:
 - pull apps from app store and google play store top lists
 - pull apps from some 3rd party stores
 - unzip/decompile Android APKs and iOS IPAs to look for 3rd party tracking/advertising tools
 - Various SQL ddl for https://github.com/ddxv/app-store-dash

App-ads.txt files are crawled based on the Interactive Advertising Bureau's Tech Lab specs. https://iabtechlab.com/ads-txt/



To get app-ads.txt files, there are several additional steps that need to be taken when compared to regular ads.txt files.
 - Get store ids
 - Get store ids' developer URL
 - Crawl developer URL

These steps make it a bit more challenging to collect app-ads.txt, as the first step is to have your list of store_ids to check. Thus this project comes bunded with two crawlers for both Apple iTunes and Google Play stores to discover new ids. If you do not need to discover new ids, then these steps are not needed and you can directly inject your store_ids into the database's store_apps table.

# Setup and Installation
 - Python environment: Python 3.11/3.12
 - Requires: NodeJS
 - PostgreSQL: 15
 - Init db using pg-ddl/db.sql
 - Setup python environment `python3.12 -m venv .virtualenv` & `source .virtualenv/bin/activate`
 - `pip install -r requirements.txt`
 - `npm install --save google-play-scraper`


# Prep before running (optional)
 - App discovery is quite slow, to speed things up you can inject store_ids to postgresql public.store_apps by finding a pre-existing list of store_ids.

# Run
 - From your environment run `python main.py` to check setup. This will also help verify the database connection is working.

## Run Options
 - `-t --use-ssh-tunnel` Use to toggle SSH port forwarding for connecting to a remote PostgreSQL database
 - `-n --new-apps-check` Crawl stores to discover new app store ids. This is limited and not fast. By default it will check top apps for each category and collection.
 - `-u --update-app-details` Update app store details. Requires that you have some app store ids already in store_apps. Will keep ids up to date within a few days for big apps and a week for smaller apps.
 - `-a --app-ads-txt-scrape` Requires that store_ids and their details (which include the developer URLs) have been scraped. Will crawl the developer's URL for an app-ads.txt file. Results are stored in app_ads_entrys for each URL.
 - `-l --limit-processes` Run only 1 instance of adscrawler. Will check to see if /adscrawler/main.py is already in process. If it already exists the program will not run. 

