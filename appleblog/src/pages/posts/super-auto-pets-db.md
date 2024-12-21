---
author: Bob Johnson
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'This database website is an un-official guide and reference for the pets, food and stats from the game Super Auto Pets.'
featured: true
keywords: {"id":"0193e86a3870094a6768cc9094432a46","object":"chat.completion","created":1734771095,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- super-auto-pets-db\n- pets\n- food\n- stats\n- unofficial guide\n- database\n- game Super Auto Pets\n- node\n- npm\n- development server\n- documentation\n- pet database\n- food items\n- pets items\n- status effects\n- project structure\n- API\n- data schema\n- JSON\n- ability description\n- trigger entity\n- effect\n- addon/pack\n- code files\n- website hosting\n- GitHub Pages\n\n### Tags:\n- #UnofficialGuide\n- #SuperAutoPets\n- #Database\n- #PetDatabase\n- #Development\n- #WebDevelopment\n- #Node.js\n- #NPM\n- #API\n- #DataSchema\n- #PetInfo\n- #FoodItems\n- #StatusEffects\n- #GameGuide\n- #ProjectStructure\n- #Documentation"},"finish_reason":"stop"}],"usage":{"prompt_tokens":882,"completion_tokens":183,"total_tokens":1065},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Bob Johnson
  name: author
- content: {"id":"0193e86a3870094a6768cc9094432a46","object":"chat.completion","created":1734771095,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- super-auto-pets-db\n- pets\n- food\n- stats\n- unofficial guide\n- database\n- game Super Auto Pets\n- node\n- npm\n- development server\n- documentation\n- pet database\n- food items\n- pets items\n- status effects\n- project structure\n- API\n- data schema\n- JSON\n- ability description\n- trigger entity\n- effect\n- addon/pack\n- code files\n- website hosting\n- GitHub Pages\n\n### Tags:\n- #UnofficialGuide\n- #SuperAutoPets\n- #Database\n- #PetDatabase\n- #Development\n- #WebDevelopment\n- #Node.js\n- #NPM\n- #API\n- #DataSchema\n- #PetInfo\n- #FoodItems\n- #StatusEffects\n- #GameGuide\n- #ProjectStructure\n- #Documentation"},"finish_reason":"stop"}],"usage":{"prompt_tokens":882,"completion_tokens":183,"total_tokens":1065},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86a3870094a6768cc9094432a46","object":"chat.completion","created":1734771095,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- super-auto-pets-db\n- pets\n- food\n- stats\n- unofficial guide\n- database\n- game Super Auto Pets\n- node\n- npm\n- development server\n- documentation\n- pet database\n- food items\n- pets items\n- status effects\n- project structure\n- API\n- data schema\n- JSON\n- ability description\n- trigger entity\n- effect\n- addon/pack\n- code files\n- website hosting\n- GitHub Pages\n\n### Tags:\n- #UnofficialGuide\n- #SuperAutoPets\n- #Database\n- #PetDatabase\n- #Development\n- #WebDevelopment\n- #Node.js\n- #NPM\n- #API\n- #DataSchema\n- #PetInfo\n- #FoodItems\n- #StatusEffects\n- #GameGuide\n- #ProjectStructure\n- #Documentation"},"finish_reason":"stop"}],"usage":{"prompt_tokens":882,"completion_tokens":183,"total_tokens":1065},"system_fingerprint":""}
theme: light
title: super-auto-pets-db
---

# super-auto-pets-db

## Repository URL: 
[https://github.com/wanghaisheng/super-auto-pets-db](https://github.com/wanghaisheng/super-auto-pets-db)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
This database website is an un-official guide and reference for the pets, food and stats from the game Super Auto Pets.

## README Content: 
2024-12-13

# super-auto-pets-db

This database website is an un-official guide and reference for the pets, food and stats from the game Super Auto Pets.

## Usage

### Prerequisites

- Install node (I use `v14.16.0`, your mileage may vary on earlier versions).
- Run `npm install`.

### Building the project

You can use `npm run prod:build` or `npm run dev:build` to build the site. This will write the website to the `docs/` directory, for hosting through GitHub Pages.

You can use `npm run dev` to create a local development server.

### Navigating the project

- `docs/` - The output directory for the website files. Everything in this directory is generated from the `src/` files, you probably don't want to be changing these files directly.
- `src/` - Code files used in the project
  - `db/` - Files involved in building and populating the pets database.
    - `food/` - Files defining all the food items in the game.
    - `pets/` - Files defining all the pets items in the game.
    - `statusEffects/` - Files defining all the status effects items in the game.
  - `emoji/` - Git submodules for the emoji fonts that contain the animal icons.
  - `web/` - Files involved in building the website.
    - `assets/` - Static files and images
    - `components/` - React components.
    - `hooks/` - React hooks.
    - `live/` - Entry point for the run-time code.
    - `ssr/` - Entry point for static site rendering code.

## API

One goal of this project is to have all pets and food described as data so that they can be used and consumed by other applications.

For this reason we are also building an `api.json` file that other applications can use and consume.

The JSON follows the following schema:

```typescript
export type Pack = "StandardPack" | "ExpansionPack1";

export interface Pet {
  // The name of the pet.
  name: String;
  // The tier the pet appears in.
  tier: number;
  // The standard starting attack points for the pet.
  baseAttack: number;
  // The standard starting health points for the pet.
  baseHealth: number;
  // Which packs the pet appears in.
  packs?: Pack[];
  // The ability the pet has at level 1.
  level1Ability?: Ability;
  // The ability the pet has at level 2.
  level2Ability?: Ability;
  // The ability the pet has at level 3.
  level3Ability?: Ability;
}

export interface Ability {
  // The text description of the ability.
  description: string;
  // What behaviour (by the trigger entity) will initiate the ability.
  trigger: Trigger;
  // Which entity will trigger the effect.
  triggeredBy: Target;
  // What the effect does.
  effect: Effect;
}
```

The purpose of the extra information on the `Ability` type is so that in the future we could do things like:

- Generate more detailed/precise descriptions for what each ability does.
- Allow filtering on things like "pets that spawn other pets".

**This extra ability information is still subject to change as the data model becomes clearer.** Check out `src/database/index.ts` to get a better idea of how this information is structured.

## Useful Resources

- [Emojipedia, source of icons](https://emojipedia.org/)
- [Steam Guide, All Pets and Food](https://steamcommunity.com/sharedfiles/filedetails/?id=2628954046)
- [Background images](https://opengameart.org/content/backgrounds-3)

