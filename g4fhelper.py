from datetime import datetime
from typing import Dict, Optional, List
import g4f
from g4f.client import Client
from g4f.Provider import BaseProvider
import time
import subprocess
import re
from collections import defaultdict

class EnhancedBlogGenerator:
    def __init__(self, current_date: str, username: str,
                 provider_name: str = "g4f.Provider.Bing",
                 model_name: str = "gpt-4",
                 temperature: float = 0.7):
        self.current_date = current_date
        self.username = username
        self.provider_name = provider_name
        self.model_name = model_name
        self.temperature = temperature
        self.client = self._setup_client()

    def _setup_client(self) -> Client:
        provider_class = self._get_provider_class(self.provider_name)
        return Client(provider=provider_class)

    def _get_provider_class(self, provider_name: str) -> Optional[BaseProvider]:
        if provider_name == 'auto':
            return None
        try:
            provider_class = getattr(g4f.Provider, provider_name.split('.')[-1])
            if not issubclass(provider_class, BaseProvider):
                raise ValueError(f"Invalid provider: {provider_name}")
            return provider_class
        except AttributeError:
            raise ValueError(f"Provider not found: {provider_name}")

    def get_commit_history(self, repo_path: str) -> List[Dict]:
        """Get repository commit history."""
        try:
            # Get git log with format: hash|author|date|message
            cmd = ['git', '-C', repo_path, 'log', 
                  '--pretty=format:%H|%an|%ai|%s']
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            commits = []
            for line in result.stdout.split('\n'):
                if line:
                    hash_, author, date, message = line.split('|')
                    commits.append({
                        'hash': hash_,
                        'author': author,
                        'date': datetime.strptime(date, '%Y-%m-%d %H:%M:%S %z'),
                        'message': message
                    })
            return commits
        except Exception as e:
            print(f"Error getting commit history: {e}")
            return []

    def generate_timeline_chart(self, commits: List[Dict]) -> str:
        """Generate ASCII/Markdown timeline from commits."""
        if not commits:
            return "No commit history available"

        # Group commits by month
        monthly_commits = defaultdict(list)
        for commit in commits:
            month_key = commit['date'].strftime('%Y-%m')
            monthly_commits[month_key].append(commit)

        # Generate timeline
        timeline = "## Development Timeline\n\n"
        timeline += "```mermaid\ngantt\n"
        timeline += "dateFormat  YYYY-MM-DD\n"
        timeline += "title Project Development Timeline\n\n"

        # Add sections for each month
        for month, month_commits in sorted(monthly_commits.items()):
            timeline += f"section {month}\n"
            for commit in month_commits:
                # Clean commit message for Mermaid compatibility
                message = re.sub(r'[^\w\s-]', '', commit['message'])
                timeline += (f"{message} :"
                           f"{commit['date'].strftime('%Y-%m-%d')}, 1d\n")

        timeline += "```\n"
        return timeline

    def analyze_readme(self, readme_content: str) -> Dict[str, str]:
        """Extract key information from README content."""
        sections = {
            'technologies': [],
            'features': [],
            'setup': [],
            'dependencies': []
        }

        # Extract technologies (looking for common tech keywords)
        tech_pattern = r'\b(python|javascript|react|node|docker|kubernetes|aws|css|html|sql|api)\b'
        sections['technologies'] = list(set(re.findall(tech_pattern, 
                                                     readme_content.lower())))

        # Extract features (looking for bullet points)
        feature_lines = re.findall(r'[-*]\s+([^\n]+)', readme_content)
        sections['features'] = [line.strip() for line in feature_lines]

        # Extract setup instructions
        setup_pattern = r'(?i)(?:installation|setup|getting started).*?\n((?:.*?\n)+?)(?:\n|$)'
        setup_match = re.search(setup_pattern, readme_content)
        if setup_match:
            sections['setup'] = setup_match.group(1).strip()

        return sections

    def generate_section_content(self, section_name: str, prompt: str, 
                               readme_analysis: Dict = None,
                               max_retries: int = 3) -> str:
        """Generate content for a specific section using g4f."""
        retry_count = 0
        while retry_count < max_retries:
            try:
                # Include README analysis in prompt if available
                if readme_analysis:
                    prompt += f"\n\nREADME Analysis:\n"
                    for key, value in readme_analysis.items():
                        prompt += f"\n{key.title()}: {value}"

                messages = [
                    {
                        'role': 'system',
                        'content': f'You are a technical writer creating content for the "{section_name}" section of a developer blog post.'
                    },
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ]
                
                chat_completion = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=messages,
                    temperature=self.temperature,
                    max_tokens=2048
                )
                
                content = chat_completion.choices[0].message.content.strip()
                if content:
                    return content
                    
            except Exception as e:
                print(f"Error generating content (attempt {retry_count + 1}): {str(e)}")
                retry_count += 1
                time.sleep(2)
                
        return f"[Failed to generate content for {section_name} after {max_retries} attempts]"

    def generate_blog_post(self, repo_name: str, repo_description: str, 
                          readme_content: str, repo_path: str) -> str:
        """Generate complete blog post with timeline and README analysis."""
        
        # Analyze README content
        readme_analysis = self.analyze_readme(readme_content)
        
        # Get commit history and generate timeline
        commits = self.get_commit_history(repo_path)
        timeline_chart = self.generate_timeline_chart(commits)

        sections = {
            'introduction': {
                'title': '## Introduction',
                'prompt': f"""
Write an introduction for a project named "{repo_name}" with description:
"{repo_description}"

Include:
1. Project overview
2. Motivation
3. Key objectives

Use the following README analysis for context:
{readme_analysis}
"""
            },
            'research': {
                'title': '## Research and Planning',
                'prompt': f"""
Based on the repository analysis and README content, discuss:
1. Problem space analysis
2. Market research
3. Technical feasibility study
4. Design decisions

README Content:
{readme_content[:500]}...
"""
            },
            'implementation': {
                'title': '## Technical Implementation',
                'prompt': f"""
Describe the technical implementation based on:
1. Technologies used: {', '.join(readme_analysis['technologies'])}
2. Key features: {', '.join(readme_analysis['features'][:5])}
3. Architecture decisions
4. Development approach
"""
            },
            'development_journey': {
                'title': '## Development Journey',
                'prompt': f"""
Create a narrative about the development process, including:
1. Key milestones from the commit history
2. Major challenges and solutions
3. Learning outcomes

Commit History Summary:
{', '.join(c['message'] for c in commits[:5])}
"""
            }
        }

        # Generate blog header
        blog_content = f"""# Building {repo_name}: A Developer's Journey

*Posted on {self.current_date} by {self.username}*

"""

        # Generate each section
        for section_name, section_data in sections.items():
            print(f"Generating {section_name} section...")
            blog_content += f"{section_data['title']}\n\n"
            content = self.generate_section_content(
                section_name, 
                section_data['prompt'],
                readme_analysis
            )
            blog_content += f"{content}\n\n"

        # Add timeline
        blog_content += timeline_chart + "\n\n"

        # Add technical details section
        blog_content += "## Technical Details\n\n"
        blog_content += "### Technologies Used\n"
        for tech in readme_analysis['technologies']:
            blog_content += f"- {tech.title()}\n"
        
        blog_content += "\n### Key Features\n"
        for feature in readme_analysis['features'][:10]:
            blog_content += f"- {feature}\n"

        # Generate conclusion
        conclusion_prompt = f"""
Write a conclusion for {repo_name} that summarizes:
1. Project achievements
2. Lessons learned
3. Future directions

Based on:
- Features: {', '.join(readme_analysis['features'][:3])}
- Timeline: {len(commits)} commits over {len(monthly_commits)} months
- Current status: {commits[0]['message'] if commits else 'Active development'}
"""
        conclusion = self.generate_section_content('conclusion', conclusion_prompt)
        blog_content += f"\n## Conclusion\n\n{conclusion}\n"

        return blog_content

def main():
    # Example usage
    current_date = "2024-12-21 12:35:08"
    username = "wanghaisheng"
    repo_path = "/path/to/your/repo"
    
    # Read README content
    with open(f"{repo_path}/README.md", 'r', encoding='utf-8') as f:
        readme_content = f.read()

    generator = EnhancedBlogGenerator(
        current_date=current_date,
        username=username
    )

    blog_post = generator.generate_blog_post(
        repo_name="github-journey-daily-update",
        repo_description="Track and analyze GitHub activity",
        readme_content=readme_content,
        repo_path=repo_path
    )

    # Save output
    output_filename = f"blog_post_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(blog_post)
    
    print(f"Enhanced blog post generated and saved to: {output_filename}")

if __name__ == "__main__":
    main()

                              
