import requests
import os
import datetime
import yaml
import random
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load config file for default author and folder
CONFIG_FILE = "config.yaml"
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return yaml.safe_load(file)
    return {}

config = load_config()
DEFAULT_AUTHOR_LIST = config.get("author_list", ["unknown"])
OUTPUT_FOLDER = config.get("output_folder", "markdown_files")

# Ensure the output folder exists
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# GitHub API Token
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "your_github_access_token_here")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# OpenAI API Token
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_access_token_here")

# Fetch all repositories of a user
def get_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    repos = []
    params = {"per_page": 100, "page": 1}

    while True:
        response = requests.get(url, headers=HEADERS, params=params)
        if response.status_code != 200:
            print(f"Failed to fetch repos: {response.json().get('message', 'Unknown error')}")
            break

        data = response.json()
        if not data:
            break

        repos.extend(data)
        params["page"] += 1

    return repos

# Fetch README content
def get_readme_content(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        readme_data = response.json()
        readme_content = requests.get(readme_data["download_url"]).text
        return readme_content
    return None

# Generate a unique cover URL
def generate_cover():
    return "https://via.placeholder.com/600x400.png?text=Cover+Image"

# Extract keywords and tags using OpenAI API
def extract_keywords_and_tags(text):
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "text-davinci-003",
        "prompt": f"Extract keywords and tags from the following text:\n{text}\n", 
        "max_tokens": 100
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()["choices"][0]["text"].strip()
        keywords, tags = result.split("\n") if "\n" in result else (result, result)
        return keywords.split(", "), tags.split(", ")
    return ["default_keyword"], ["default_tag"]

# Select a random author from the list
def select_author():
    return random.choice(DEFAULT_AUTHOR_LIST)

# Create Markdown file for each repository
def create_markdown_files(repos, username):
    date_today = datetime.date.today().strftime("%Y-%m-%d")

    for repo in repos:
        repo_name = repo["name"]
        repo_url = repo["html_url"]
        stars_count = repo["stargazers_count"]
        forks_count = repo["forks_count"]
        description = repo["description"] or "No description provided."
        is_forked = repo["fork"]

        # Fetch README content or fallback to description
        readme_content = get_readme_content(username, repo_name) or description

        # Generate cover URL
        cover_url = generate_cover()

        # Extract keywords and tags
        keywords, tags = extract_keywords_and_tags(f"{repo_name} {description} {readme_content}")

        # Select author
        author = select_author()

        # Construct Markdown content
        md_content = f"""---
author: {author}
cover:
  alt: cover
  square: {cover_url}
  url: {cover_url}
description: '{description}'
featured: true
keywords: {', '.join(keywords)}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: {author}
  name: author
- content: {', '.join(keywords)}
  name: keywords
pubDate: '{date_today} 15:27:08'
tags:
- {', '.join(tags)}
theme: light
title: {repo_name}
---

# {repo_name}

## Repository URL: 
[{repo_url}]({repo_url})

## Stars: 
**{stars_count}**

## Forks: 
**{forks_count}**

## Description: 
{description}

## README Content: 
{readme_content}
"""

        # Save to .md file in the output folder
        filename = os.path.join(OUTPUT_FOLDER, f"{repo_name}.md")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(md_content)
        print(f"Markdown file created: {filename}")

# Main execution
def main():
    username = config.username
    repos = get_repositories(username)
    if not repos:
        print("No repositories found or failed to fetch repositories.")
        return

    create_markdown_files(repos, username)
    print("All markdown files have been created.")

if __name__ == "__main__":
    main()
