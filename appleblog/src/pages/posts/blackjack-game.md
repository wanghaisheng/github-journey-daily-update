---
author: John Doe
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Claude 3.5 Sonnet Chat + Cursor + open source images. I created this game to develop a workflow between chat and Cursor'
featured: true
keywords: {"id":"0193e85b4b08ec9a4879d79bdb3d3ead","object":"chat.completion","created":1734770117,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Blackjack Game\n- Claude 3.5 Sonnet Chat\n- Cursor\n- Open source images\n- Web-based implementation\n- Classic casino game\n- Responsive Design\n- Realistic Gameplay\n- Betting System\n- Multiple Hands\n- Animations\n- Sound Effects\n- Statistics Tracking\n- Customizable\n- Game Parameters\n- HTML5\n- CSS3\n- JavaScript (ES6+)\n- GSAP (GreenSock Animation Platform)\n- MIT License\n\n### Tags:\n#BlackjackGame\n#WebGame\n#CasinoGame\n#OpenSource\n#GameDevelopment\n#ResponsiveDesign\n#RealisticGameplay\n#BettingSystem\n#MultipleHands\n#Animations\n#SoundEffects\n#Statistics\n#CustomizableGame\n#HTML5\n#CSS3\n#JavaScript\n#GreenSock\n#OpenSourceProject\n#MITLicense"},"finish_reason":"stop"}],"usage":{"prompt_tokens":627,"completion_tokens":182,"total_tokens":809},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: {"id":"0193e85b4b08ec9a4879d79bdb3d3ead","object":"chat.completion","created":1734770117,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Blackjack Game\n- Claude 3.5 Sonnet Chat\n- Cursor\n- Open source images\n- Web-based implementation\n- Classic casino game\n- Responsive Design\n- Realistic Gameplay\n- Betting System\n- Multiple Hands\n- Animations\n- Sound Effects\n- Statistics Tracking\n- Customizable\n- Game Parameters\n- HTML5\n- CSS3\n- JavaScript (ES6+)\n- GSAP (GreenSock Animation Platform)\n- MIT License\n\n### Tags:\n#BlackjackGame\n#WebGame\n#CasinoGame\n#OpenSource\n#GameDevelopment\n#ResponsiveDesign\n#RealisticGameplay\n#BettingSystem\n#MultipleHands\n#Animations\n#SoundEffects\n#Statistics\n#CustomizableGame\n#HTML5\n#CSS3\n#JavaScript\n#GreenSock\n#OpenSourceProject\n#MITLicense"},"finish_reason":"stop"}],"usage":{"prompt_tokens":627,"completion_tokens":182,"total_tokens":809},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e85b4b08ec9a4879d79bdb3d3ead","object":"chat.completion","created":1734770117,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- Blackjack Game\n- Claude 3.5 Sonnet Chat\n- Cursor\n- Open source images\n- Web-based implementation\n- Classic casino game\n- Responsive Design\n- Realistic Gameplay\n- Betting System\n- Multiple Hands\n- Animations\n- Sound Effects\n- Statistics Tracking\n- Customizable\n- Game Parameters\n- HTML5\n- CSS3\n- JavaScript (ES6+)\n- GSAP (GreenSock Animation Platform)\n- MIT License\n\n### Tags:\n#BlackjackGame\n#WebGame\n#CasinoGame\n#OpenSource\n#GameDevelopment\n#ResponsiveDesign\n#RealisticGameplay\n#BettingSystem\n#MultipleHands\n#Animations\n#SoundEffects\n#Statistics\n#CustomizableGame\n#HTML5\n#CSS3\n#JavaScript\n#GreenSock\n#OpenSourceProject\n#MITLicense"},"finish_reason":"stop"}],"usage":{"prompt_tokens":627,"completion_tokens":182,"total_tokens":809},"system_fingerprint":""}
theme: light
title: blackjack-game
---

# blackjack-game

## Repository URL: 
[https://github.com/wanghaisheng/blackjack-game](https://github.com/wanghaisheng/blackjack-game)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Claude 3.5 Sonnet Chat + Cursor + open source images. I created this game to develop a workflow between chat and Cursor

## README Content: 
2024-12-14

I used Claude 3.5 Sonnet Chat + Cursor + open source images. I created this game to develop a workflow between chat and Cursor

# Blackjack Game

This project is a feature-rich, web-based implementation of the classic casino game Blackjack. It offers an immersive gaming experience with smooth animations, sound effects, and realistic gameplay.

## Features

- **Responsive Design**: Adapts to different screen sizes for optimal play on both desktop and mobile devices.
- **Realistic Gameplay**: Follows standard Blackjack rules including hit, stand, double down, and split.
- **Betting System**: Players can place bets using chips of different denominations.
- **Multiple Hands**: Support for playing and splitting multiple hands.
- **Animations**: Smooth card dealing and chip animations for an engaging experience.
- **Sound Effects**: Audio feedback for actions like dealing cards and placing bets.
- **Statistics Tracking**: Keeps track of games played, won, and win percentage.
- **Customizable**: Easy to adjust game parameters like minimum deck size and dealer stand value.

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/entrepeneur4lyf/blackjack.git
   ```

2. Navigate to the project directory:
   ```
   cd blackjack
   ```

3. Open `index.html` in a modern web browser.

## Project Structure

- `index.html`: Main HTML file that structures the game interface.
- `styles.css`: Contains all the styling for the game.
- `main.js`: Entry point of the application.
- `blackjack.js`: Core game logic and state management.
- `blackjackui.js`: Handles UI updates and user interactions.
- `blackjackaudio.js`: Manages sound effects.
- `card.js`: Defines the Card class.
- `deck.js`: Implements the Deck class for card management.
- `gsap.min.js` & `TweenMax.min.js`: Animation libraries for smooth transitions.

## Technologies Used

- HTML5
- CSS3
- JavaScript (ES6+)
- GSAP (GreenSock Animation Platform)

## Customization

You can easily customize various game parameters by modifying the `Blackjack` class in `blackjack.js`:

- `dealerMustStand`: The value at which the dealer must stand (default: 17)
- `minDeckSize`: Minimum number of cards before reshuffling (default: 20)
- `maxBet`: Maximum allowed bet (default: 500)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

