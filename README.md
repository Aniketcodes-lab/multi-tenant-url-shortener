# Multi-Tenant URL Shortener (Django)

## Overview
This project is a Django-based multi-tenant, white-label URL shortener system where
a single backend serves multiple branded frontends based on domain.

## Features
- Multi-tenant architecture (domain based)
- White-label branding (logo, name, theme color)
- URL shortening
- Redirect with click tracking
- Per-tenant data isolation
- Django admin based tenant management

## Tech Stack
- Python
- Django
- Django Rest Framework
- SQLite

## How It Works
- Tenant is resolved using request host
- Each domain maps to one tenant
- All URLs are scoped to tenant

## How to Run
1. Create virtualenv
2. Install requirements
3. Run migrations
4. Create superuser
5. Run server
6. Add domains in hosts file
7. Create tenants in admin

## Setup Local Domains (Important for Testing Multi-Tenant)

### On Windows
Edit this file as Administrator:

C:\Windows\System32\drivers\etc\hosts

Add:

127.0.0.1 branda.localhost
127.0.0.1 brandb.localhost

### On Mac / Linux

sudo nano /etc/hosts

Add:

127.0.0.1 branda.localhost
127.0.0.1 brandb.localhost

## Create Tenants (Brands)

Open:

http://127.0.0.1:8000/admin

Create tenants:

### Example Tenant 1
- Name: Brand A
- Domain: branda.localhost
- App Name: Brand A Shortener
- Primary Color: #ff0000

### Example Tenant 2
- Name: Brand B
- Domain: brandb.localhost
- App Name: Brand B Links
- Primary Color: #0066ff

## Access the App

Open in browser:

http://branda.localhost:8000
http://brandb.localhost:8000

## Example

### Shorten URL

POST /api/shorten/

{
  "url": "https://google.com"
}

### Redirect

GET /<short_code>/

Redirects to original URL.
