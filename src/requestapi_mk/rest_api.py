from aiohttp import web

async def health(request):
    return web.StreamResponse(status=204)

async def forward_request(request):
    #something
    return web.StreamResponse(status=201)

async def init():
    app = web.Application()
    app.router.add_get("/health", health)
    app.router.add_post("/v1/forward", forward_request)
    return app

if __name__ == "__main__":
    application = init()
    web.run_app(application, port=5000)
