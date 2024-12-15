import requests
import json
import os
import datetime
import random
import yaml
from dotenv import load_dotenv
import openai
import asyncio

# Load environment variables from .env file
load_dotenv()

# Load config file for default author, folder, and OpenAI model
CONFIG_FILE = "config.yaml"
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return yaml.safe_load(file)
    return {}

config = load_config()
DEFAULT_AUTHOR_LIST = config.get("author_list", ["unknown"])
OUTPUT_FOLDER = config.get("output_folder", "markdown_files")
IMAGE_FOLDER = config.get("image_folder", "generated_images")  # Image folder to save images
BASE_URL = config.get("base_url", "http://localhost:3000/")  # Base URL for generated images

# Ensure the output folder exists
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

# GitHub API Token
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "your_github_access_token_here")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# OpenAI API Token
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_access_token_here")

# Image generation API URL and Token
IMAGE_API_URL = "https://your-worker-url.workers.dev/api/image"
IMAGE_API_KEY = os.getenv("IMAGE_API_KEY", "your_image_api_key_here")

# OpenAI chat initialization function
class Chat:
    def __init__(self):
        self.model = None

    async def init_chat(self, model_name):
        self.model = model_name
        openai.api_key = OPENAI_API_KEY
        print(f"Chat model initialized: {self.model}")

    async def fetch_response(self, prompt):
        if not self.model:
            raise Exception("Chat model is not initialized.")
        
        response = openai.Completion.create(
            model=self.model,
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()

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

# Extract keywords and tags using OpenAI API
async def extract_keywords_and_tags(chat, text):
    prompt = f"Extract keywords and tags from the following text:\n{text}\n"
    keywords_response = await chat.fetch_response(prompt)
    keywords, tags = keywords_response.split("\n") if "\n" in keywords_response else (keywords_response, keywords_response)
    return keywords.split(", "), tags.split(", ")

# Select a random author from the list
def select_author():
    return random.choice(DEFAULT_AUTHOR_LIST)

# Check if the repository was recently updated
def is_recently_updated(repo, days_threshold=30):
    last_updated = datetime.datetime.strptime(repo["pushed_at"], "%Y-%m-%dT%H:%M:%SZ")
    today = datetime.datetime.utcnow()
    delta = today - last_updated
    return delta.days <= days_threshold

# Save the generated image locally
def save_image_locally(image_data, image_name):
    image_path = os.path.join(IMAGE_FOLDER, image_name)
    with open(image_path, 'wb') as image_file:
        image_file.write(image_data)
    return image_path

# Generate a cover image based on the prompt
def generate_cover_image(prompt):
    headers = {
        "Authorization": f"Bearer {IMAGE_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "DS-8-CF"
    }
    response = requests.post(IMAGE_API_URL, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        result = response.json()
        print(f"原始提示词: {result['prompt']}")
        print(f"翻译后的提示词: {result['translatedPrompt']}")
        image_data = result.get('image', '')
        if image_data:
            # Save the image locally
            image_name = f"{prompt[:10]}.png"  # Save with a short name based on prompt
            image_path = save_image_locally(image_data.encode(), image_name)
            image_url = BASE_URL + IMAGE_FOLDER + "/" + image_name  # URL to access the image
            return image_url
        else:
            print("No image data received.")
    else:
        print(f"Failed to generate cover image: {response.status_code}")
    return None

# Create Markdown file for each repository
def create_markdown_files(repos, username, chat, days_threshold=30):
    date_today = datetime.date.today().strftime("%Y-%m-%d")

    for repo in repos:
        # Skip repositories that haven't been updated recently
        if not is_recently_updated(repo, days_threshold):
            print(f"Skipping {repo['name']} (not updated recently).")
            continue
        
        repo_name = repo["name"]
        repo_url = repo["html_url"]
        stars_count = repo["stargazers_count"]
        forks_count = repo["forks_count"]
        description = repo["description"] or "No description provided."
        is_forked = repo["fork"]

        # Fetch README content or fallback to description
        readme_content = get_readme_content(username, repo_name) or description

        # Generate cover image based on the description or repository name
        cover_image_url = generate_cover_image(f"A creative image representing the repository: {repo_name}")

        # Extract keywords and tags using OpenAI API
        keywords, tags = asyncio.run(extract_keywords_and_tags(chat, f"{repo_name} {description} {readme_content}"))

        # Select author
        author = select_author()

        # Construct Markdown content
        md_content = f"""---
author: {author}
cover:
  alt: cover
  square: {cover_image_url}
  url: {cover_image_url}
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
async def main():
    # Initialize the chat with the model from config
    chat = Chat()
    await chat.init_chat(config.get("openai", {}).get("model", "gpt-4o-mini"))

    # Get the username from config
    username = config.get("username", "default_username")
    repos = get_repositories(username)
    if not repos:
        print("No repositories found or failed to fetch repositories.")
        return

    create_markdown_files(repos, username, chat)
    print("All markdown files have been created.")

if __name__ == "__main__":
    asyncio.run(main())
