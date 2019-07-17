# -*- coding: utf-8 -*-

from aiohttp.web import Application, HTTPSeeOther, Response

# ---------------------------------------------------------

headers = {
    'Cache-Control': 'private, no-cache, no-store, must-revalidate',
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'X-XSS-Protection': '1; mode=block',
}

repository_url = 'https://github.com/emoji-gen/web-monitor'

async def health(request):
    return Response(
        body='OK',
        headers=headers,
        content_type='text/plain',
        charset='utf-8')

async def redirect(request):
    return HTTPSeeOther(repository_url, headers=headers)

# ---------------------------------------------------------

async def app_factory():
    app = Application()
    app.router.add_get('/', redirect)
    app.router.add_get('/health', health)
    return app

