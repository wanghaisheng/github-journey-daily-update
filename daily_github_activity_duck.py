import traceback
import requests
import json
import os
import datetime
import random
import yaml
from dotenv import load_dotenv
import asyncio
from g4fhelper import EnhancedBlogGenerator
# Load environment variables from .env file
load_dotenv()
print('Script started')

# Load config file for default author, folder, and OpenAI model
CONFIG_FILE = "config.yml"
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return yaml.safe_load(file)
    return {}

config = load_config()
CHAT_URL=config.get('chat_url','https://heisenberg-duckduckgo-87.deno.dev/v1/chat/completions')
CHAT_URL = "https://duckduckgo.com/duckchat/v1/chat"
STATUS_URL = "https://duckduckgo.com/duckchat/v1/status"

DEFAULT_AUTHOR_LIST = config.get("author_list", ["unknown"])
OUTPUT_FOLDER = config.get("output_folder", "markdown_files")
IMAGE_FOLDER = config.get("image_folder", "generated_images")  # Image folder to save images
BASE_URL = config.get("base_url", "http://localhost:3000/")  # Base URL for generated images
IMAGE_API_URL = config.get("image_api_url", "image_api_url")

print('yml config',config)
# Ensure the output folder exists
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

# GitHub API Token
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "your_github_access_token_here")
SILICON_TOKEN = os.getenv("SILICON_TOKEN", "your_SILICON_TOKEN_access_token_here")

print('your token',GITHUB_TOKEN)
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# Image generation API URL and Token


IMAGE_API_KEY = os.getenv("IMAGE_API_KEY", "your_image_api_key_here")

print('your IMAGE_API_KEY',IMAGE_API_KEY)

# Chat class and method integration
class Chat:
    def __init__(self, vqd: str, model: str):
        self.old_vqd = vqd
        self.new_vqd = vqd
        self.model = model
        self.messages = []

    def fetch(self, content: str) -> requests.Response:
        """ Send a message to the chat API. """
        self.messages.append({"content": content, "role": "user"})
        payload = {
            "model": self.model,
            "messages": self.messages,
        }
        headers = {"x-vqd-4": self.new_vqd, "Content-Type": "application/json"}
        response = requests.post(CHAT_URL, headers=headers, json=payload)

        if not response.ok:
            raise Exception(f"{response.status_code}: Failed to send message. {response.text}")
        return response

    async def fetch_response(self, prompt: str) -> str:
        """ Fetch the response from the chat API and return the text. """
        response = self.fetch(prompt)
        text = ""
        for event in response.iter_lines():
            if event and event != b"[DONE]":
                message_data = json.loads(event.decode("utf-8"))
                message = message_data.get("message", "")
                if message:
                    text += message
        return text

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


def siliconflow(text,token,model='Qwen2.5'):
    url = "https://api.siliconflow.cn/v1/chat/completions"

    payload = {
     "model": "Qwen/Qwen2.5-7B-Instruct",

        "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": text
                }
            ]
        }
    ]
}
    headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)
    data= response.json()
    if data:
        try:
            result=data['choices'][0]['message']['content']
            return result
        except:
            return None 
    return None 
# Extract keywords and tags using Chat class
async def extract_keywords_and_tags(chat, text):
    text=text[:3000]
    prompt = f"Extract keywords  from the following text:\n{text}\n, return results as keywords:xx,xxx,xx"
    # keywords_response = await chat.fetch_response(prompt)
    keywords_response=siliconflow(text=prompt,token=SILICON_TOKEN)
    keywords = keywords_response.split(":")[1] if ":" in keywords_response else keywords_response
    prompt = f"Extract tags from the following text:\n{text}\n,return tags as tags:xx,xx,xx"
    tags_response=siliconflow(text=prompt,token=SILICON_TOKEN)


    
    tags = tags_response.split(":")[1] if ":" in tags_response else tags_response

    
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
    prompt=prompt[:1000]
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

def call_image_endpoint(api_url, api_key, prompt, size="1024x1024", n=1):
    """
    Calls the Cloudflare Worker image generation endpoint.
    
    Args:
        api_url (str): The endpoint URL of the Cloudflare Worker.
        api_key (str): The API key for authentication.
        prompt (str): The text prompt to generate the image.
        size (str, optional): The size of the generated image (e.g., "1024x1024"). Defaults to "1024x1024".
        n (int, optional): The number of images to generate. Defaults to 1.
    
    Returns:
        dict: The JSON response from the endpoint.
    """
    prompt=prompt[:1000]
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload={
  "messages": [
    {
      "role": "user",
      "content": prompt
    }
  ],
  "stream": False
}    

    
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        
        if response.status_code == 200:
            data=response.json()
            if data:
                try:
                    url=data['choices'][0]['message']['url']
                    print('create image',url)
                    return url
                except:
                    return None
            return None
        else:
            print("error:\n", response.status_code, "message:\n", response.text)
            return None # Error handling
    except Exception as e:
        return None 

def generateblog(repo_name,repo_description,readme_content,username=None,current_date=None):
    if current_date is None:
        current_date = datetime.datetime.now().strftime('%Y%m%d %H%M%S')
        
    if username is None:
       username="wanghaisheng" 
    generator = EnhancedBlogGenerator(
        current_date=current_date,
        username=username,
        provider_name="g4f.Provider.Bing",
        model_name="gpt-4",
        temperature=0.7
    )
    blog_post,title = generator.generate_blog_post(
        repo_name=repo_name,
        repo_description=repo_description,
        readme_content=readme_content,
        repo_path='.'
    )
    return blog_post,title
# Create Markdown file for each repository
def create_all_markdown_files(repos, username, chat, days_threshold=30):
    date_today = datetime.date.today().strftime("%Y-%m-%d")
    pubdate = datetime.datetime.now().strftime('%Y%m%d %H%M%S')

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
        readme_content = get_readme_content(username, repo_name)
        blogmd,title= generateblog(repo_name,repo_description=description,readme_content=readme_content,username=username,current_date=None)
            
        # Generate cover image based on the description or repository name
        cover_image_url = call_image_endpoint(
                    api_url=IMAGE_API_URL,
        api_key=IMAGE_API_KEY,
prompt=            f"A creative image representing the repository: {readme_content}")


            
        # Extract keywords and tags using Chat class
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
pubDate: '{pubdate}'
tags:
- {', '.join(tags)}
theme: light
title: {title}
---

{blogmd}


* Repository URL: 
[{repo_url}]({repo_url})

*  Stars: 
**{stars_count}**

* Forks: 
**{forks_count}**

"""

        # Save to .md file in the output folder
        filename = os.path.join(OUTPUT_FOLDER, f"{repo_name}.md")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(md_content)
        print(f"Markdown file created: {filename}")
async def create_new_markdown_files(repos, username, chat, days_threshold=30):
    date_today = datetime.date.today().strftime("%Y-%m-%d")
    pubdate = datetime.datetime.now().strftime('%Y%m%d %H%M%S')

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

        # Check if markdown file already exists for this repository
        md_filename = os.path.join(OUTPUT_FOLDER, f"{repo_name}.md")
        if os.path.exists(md_filename):
            print(f"Skipping {repo_name} (markdown file already exists).")
            continue

        # Fetch README content or fallback to description
        readme_content = get_readme_content(username, repo_name) or description
        blogmd,title= generateblog(repo_name,repo_description=description,readme_content=readme_content,username=username,current_date=None)

        # Generate cover image based on the description or repository name
        cover_image_url = call_image_endpoint(
                    api_url=IMAGE_API_URL,
        api_key=IMAGE_API_KEY,
prompt=            f"A creative image representing the repository: {readme_content}")
        # if cover_image_url is None:
            # cover_image_url = generate_cover_image(f"A creative image representing the repository: {readme_content}")

        # Extract keywords and tags using Chat class
        keywords=None
        tags=None
        keywords, tags = await extract_keywords_and_tags(chat, f"{repo_name} {description} {readme_content}")


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
pubDate: '{pubdate}'
tags:
- {', '.join(tags)}
theme: light
title: {title}
---

 {blogmd}

* Repository URL: 
[{repo_url}]({repo_url})

* Stars: 
**{stars_count}**

* Forks: 
**{forks_count}**


"""

        # Save to .md file in the output folder
        with open(md_filename, "w", encoding="utf-8") as file:
            file.write(md_content)
        print(f"Markdown file created: {md_filename}")

# Main execution
async def main():
    try:
        print('main function start')
    # Initialize the chat with the model from config
        chat = Chat(vqd="your_vqd_here", model="gpt-4o-mini")

    # Get the username from config
        username = config.get("username", "default_username")
        print('start to detect all repos')
        repos = get_repositories(username)[:10]
        if not repos:
            print("No repositories found or failed to fetch repositories.")
            return
        print('create md for repos')
        await create_new_markdown_files(repos, username, chat)
    except Exception as e:
        print(f"Exception in main: {e}")
        
        traceback.print_exc()

# Run the async main function
if __name__ == "__main__":
    print('we are coming')
    asyncio.run(main())
