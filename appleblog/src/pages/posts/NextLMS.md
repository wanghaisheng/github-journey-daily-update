---
author: John Doe
cover:
  alt: cover
  square: https://fluxapi.borninsea.com/image/image_1734781586569_p937q
  url: https://fluxapi.borninsea.com/image/image_1734781586569_p937q
description: 'Code With Antonio - Build an LMS Platform: Next.js 13, React, Stripe, Mux, Prisma, Tailwind, MySQL |  https://youtu.be/Big_aFLmekI?si=vv-QnJ3A36wfhZva'
featured: true
keywords: NextLMS,Next.js,React,Stripe,Mux,Prisma,Tailwind,MySQL,Clerk,UploadThing,HLS,rich text editor,authentication,ORM,database,search function,Dashboards,drag and drop,Video processing,user interface,contributions,project integration,deployment,Vercel,MongoDB Atlas,server-less hosting,Courser Development
layout: ../../layouts/MarkdownPost.astro
meta:
- content: John Doe
  name: author
- content: NextLMS,Next.js,React,Stripe,Mux,Prisma,Tailwind,MySQL,Clerk,UploadThing,HLS,rich text editor,authentication,ORM,database,search function,Dashboards,drag and drop,Video processing,user interface,contributions,project integration,deployment,Vercel,MongoDB Atlas,server-less hosting,Courser Development
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- Next.js,React,Stripe,Mux,Prisma,Tailwind,MySQL,Clerk,NextLMS,open-source,LMS platform,deployment,Vercel,MongoDB Atlas,benefitsImageSharp,video-processing,HLS,drag-and-drop,rich-text-editor,authentication,ORM,user-interface,search-function,teacher-mode,course-management,black-screen,enhancements,planned-enhancements,Curse-of-Windows-FFMPEG,Quizmify
theme: light
title: NextLMS
---

# NextLMS

## Repository URL: 
[https://github.com/wanghaisheng/NextLMS](https://github.com/wanghaisheng/NextLMS)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Code With Antonio - Build an LMS Platform: Next.js 13, React, Stripe, Mux, Prisma, Tailwind, MySQL |  https://youtu.be/Big_aFLmekI?si=vv-QnJ3A36wfhZva

## README Content: 
2024-12-06

## LMS Platform

# LMS Platform

This repository contains a faithful copy and enhancement of the LMS platform created by CodeWithAntonio in the tutorial [Learn Next & React and get Hired!](https://www.youtube.com/watch?v=Big_aFLmekI).

## Live Demo

A working version of this app is available at [https://lms.kendevco.co](https://lms.kendevco.co).

## Development Status

- Versions and dependencies have been updated.
- Comments have been added and code has been tidied up.
- Occasional reports of black screen or other issues at runtime have been received, possibly related to Clerk integration.

## Call for Collaboration

If you're a budding developer looking for an exciting project:

- Consider contributing to [Payload Nuke](https://github.com/payloadnuke)
- Help shape its future by contributing to the [draft constitution](https://docs.google.com/document/d/1TaYHs0CSk76xBFu5ps-2BpyWsZkS2getV41_8Q0tO34/edit?usp=sharing)

**Key Features:**

* Browse and filter courses
* Purchase courses using Stripe
* Mark chapters as completed or uncompleted
* Progress calculation of each course
* Student dashboard
* Teacher mode
* Create new courses
* Create new chapters
* Easily reorder chapter position with drag and drop
* Upload thumbnails, attachments, and videos using UploadThing
* Video processing using Mux
* HLS Video player using Mux
* Rich text editor for chapter description
* Authentication using Clerk
* ORM using Prisma
* MySQL database using Planetscale

**Enhancements:**

* Added a search function to the courses page
* Improved the user interface of the student and teacher dashboards

**Planned Enhancement:**
Integrate Elliot Chong's Quizmify into this.

**Usage:**

To use this repository, you will need to have Node.js and NPM installed on your machine. Once you have installed the necessary dependencies, you can clone the repository and run the following commands:

**Deployment:**

To deploy the application to production, you will need to sign up for accounts on the following services:

Vercel https://vercel.com - for server-less hosting.

Mux https://mux.com - for Videos storage. 

Clerk https://clerk.com This is covered in the first hour or so of the video. It's the easiest 
authentication available and just works. It is so simple and easy to integrate into your app at least for 
me it is awesome. I've integrated it into my own Portfolio app https://github.com/kendevco/Portfolio https://folio.kendec.co. 

MongoDB Atlas https://mongodb.com This project has deviated from Antonio's by using MongoDb.com. I've 
found it to be much more flexible for budding NextJS developers. I've created 7 free databases there
so far and it is perfect for my needs. I had no problems modifying the schema for use with MongoDB and 
if you are looking for a project already adapted for Mongo - honestly the only changes were in the 
Schema! And Copilot did all the heavy lifting.  

UploadThing https://uploadthing.com/ for serverless upload storage.

Stripe Payments: https://stripe.com

If you need further instruction on configuring these services, they are all covered in the course
video https://www.youtube.com/watch?v=Big_aFLmekI. 

To reset the database, run 

    npx prisma migrate reset
    npx prisma db push

Note that when I ran npx prisma migrate reset against mongodb.com I ran
into errors in the terminal stating I lacked permission. However, after
running the command I did reinitialize the database. 

Note also if reinitializing the datbase you also need to run:
node scripts/seed.ts

See https://youtu.be/Big_aFLmekI?t=30748 for step-by-step

