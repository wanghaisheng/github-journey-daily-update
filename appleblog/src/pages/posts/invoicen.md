---
author: Jane Smith
cover:
  alt: cover
  square: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
  url: {'error': 'exception', 'message': "Invalid URL 'image_api_url': No scheme supplied. Perhaps you meant https://image_api_url?"}
description: 'Invoicen is a simple invoice generator for freelancers and small businesses. It is a self hostable web application that can be used to generate invoices and download PDFs'
featured: true
keywords: {"id":"0193e86196e9de6a50eec83ccc199f1e","object":"chat.completion","created":1734770530,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- invoice generator\n- freelancers\n- small businesses\n- self hostable web application\n- PDF\n- Next.js\n- Tailwind CSS\n- Shadcn\n- PostgreSQL\n- guest user\n- registered user\n- create invoice\n- download PDF\n- local storage\n- database\n- payment details\n- company details\n- send email\n- time based invoice\n- product based invoice\n\n### Tags:\n- #InvoiceGenerator\n- #FreelanceTools\n- #WebApp\n- #SelfHosted\n- #PDF\n- #Next.js\n- #TailwindCSS\n- #Shadcn\n- #PostgreSQL\n- #UserTypes\n- #GuestUser\n- #RegisteredUser\n- #InvoiceCreation\n- #DownloadPDF\n- #LocalStorage\n- #DatabaseStorage\n- #PaymentDetails\n- #CompanyDetails\n- #EmailSent\n- #TimeBasedInvoice\n- #ProductBasedInvoice"},"finish_reason":"stop"}],"usage":{"prompt_tokens":750,"completion_tokens":199,"total_tokens":949},"system_fingerprint":""}
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Jane Smith
  name: author
- content: {"id":"0193e86196e9de6a50eec83ccc199f1e","object":"chat.completion","created":1734770530,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- invoice generator\n- freelancers\n- small businesses\n- self hostable web application\n- PDF\n- Next.js\n- Tailwind CSS\n- Shadcn\n- PostgreSQL\n- guest user\n- registered user\n- create invoice\n- download PDF\n- local storage\n- database\n- payment details\n- company details\n- send email\n- time based invoice\n- product based invoice\n\n### Tags:\n- #InvoiceGenerator\n- #FreelanceTools\n- #WebApp\n- #SelfHosted\n- #PDF\n- #Next.js\n- #TailwindCSS\n- #Shadcn\n- #PostgreSQL\n- #UserTypes\n- #GuestUser\n- #RegisteredUser\n- #InvoiceCreation\n- #DownloadPDF\n- #LocalStorage\n- #DatabaseStorage\n- #PaymentDetails\n- #CompanyDetails\n- #EmailSent\n- #TimeBasedInvoice\n- #ProductBasedInvoice"},"finish_reason":"stop"}],"usage":{"prompt_tokens":750,"completion_tokens":199,"total_tokens":949},"system_fingerprint":""}
  name: keywords
pubDate: '2024-12-21 15:27:08'
tags:
- {"id":"0193e86196e9de6a50eec83ccc199f1e","object":"chat.completion","created":1734770530,"model":"Qwen/Qwen2.5-7B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"### Keywords:\n- invoice generator\n- freelancers\n- small businesses\n- self hostable web application\n- PDF\n- Next.js\n- Tailwind CSS\n- Shadcn\n- PostgreSQL\n- guest user\n- registered user\n- create invoice\n- download PDF\n- local storage\n- database\n- payment details\n- company details\n- send email\n- time based invoice\n- product based invoice\n\n### Tags:\n- #InvoiceGenerator\n- #FreelanceTools\n- #WebApp\n- #SelfHosted\n- #PDF\n- #Next.js\n- #TailwindCSS\n- #Shadcn\n- #PostgreSQL\n- #UserTypes\n- #GuestUser\n- #RegisteredUser\n- #InvoiceCreation\n- #DownloadPDF\n- #LocalStorage\n- #DatabaseStorage\n- #PaymentDetails\n- #CompanyDetails\n- #EmailSent\n- #TimeBasedInvoice\n- #ProductBasedInvoice"},"finish_reason":"stop"}],"usage":{"prompt_tokens":750,"completion_tokens":199,"total_tokens":949},"system_fingerprint":""}
theme: light
title: invoicen
---

# invoicen

## Repository URL: 
[https://github.com/wanghaisheng/invoicen](https://github.com/wanghaisheng/invoicen)

## Stars: 
**0**

## Forks: 
**0**

## Description: 
Invoicen is a simple invoice generator for freelancers and small businesses. It is a self hostable web application that can be used to generate invoices and download PDFs

## README Content: 
# Invoicen

Invoicen is a simple invoice generator for freelancers and small businesses. It is a self hostable web application that can be used to generate invoices and download PDFs. It is built using [Next.js](https://nextjs.org/).

## Features

1. Create and manage invoice
1. Download invoice as PDF
1. Send invoice as email

## System overview

```mermaid
flowchart TD
  User[User] -->|Accesses as| GuestUser[Guest User]
  User -->|Accesses as| RegisteredUser[Registered User]

  subgraph GuestUser
    direction TB
    GU_CreateInvoice[Create Invoice] --> GU_DownloadPDF[Download Invoice as PDF]
    GU_DownloadPDF --> GU_StoreLocal[Store in Browser Local Storage]
  end

  subgraph RegisteredUser
    direction TB
    RU_CreateInvoice[Create Invoice] --> RU_SaveInvoice[Save Invoice]
    RU_SaveInvoice --> RU_DownloadPDF[Download Invoice as PDF]
    RU_SaveInvoice --> RU_StoreDatabase[Store in Database]
    RU_SaveInvoice --> RU_SendEmail[Send Invoice as Email]
    RU_SaveInvoice --> RU_ViewInvoices[View All Past Invoices]
    RU_SaveInvoice --> RU_SaveDetails[Save Payment & Company Details for Future Use]
  end
```

There will be 2 types of users:

1. As a guest user
1. As a registered user

### Guest User

1. Guest users can create invoices without signing up.
1. They can download the invoice as PDF.
1. The invoice will be stored in the browser's local storage.

### Registered User

1. Registered users can create invoices and save them.
1. They can download the invoice as PDF.
1. The invoice will be stored in the database.
1. They can save their payment details, company details, etc for future use.
1. They can also send the invoice as an email.
1. They can access all the invoices they have created in the past.
1. They can upload their logo which will be displayed in the invoice.

## Types of Invoices

Currently the application supports 2 types of invoices:

1. Time based invoice
1. Product based invoice

### Time based invoice

This type of invoice is used when the user wants to charge the client based on the time spent on the project. The user can add multiple time entries and the application will calculate the total amount based on the hourly rate.

### Product based invoice

This type of invoice is used when the user wants to charge the client based on the products/services provided. The user can add multiple products/services and the application will calculate the total amount based on the price of the product/service.

## Tech Stack

1. [Next.js](https://nextjs.org/)
1. [Tailwind CSS](https://tailwindcss.com/)
1. [Shadcn](https://shadcn.com/)
1. [PostgreSQL](https://www.postgresql.org/)

## Docs

For detailed documentation, please refer to the [wiki](https://github.com/keizerworks/invoicen/wiki).

## Contributing

Take a look at the [contributing guidelines](CONTRIBUTING.md) for this project.

