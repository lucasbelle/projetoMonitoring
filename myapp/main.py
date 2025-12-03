import time
from fastapi import FastAPI
from prometheus_client import generate_latest
from starlette.responses import Response
from .router import router
from .metrics import REQUEST_COUNT, REQUEST_LATENCY, ERROR_4XX_COUNT, ERROR_5XX_COUNT

app = FastAPI()

# MIDDLEWARE (Métricas de Latência e Erro)
@app.middleware("http")
async def metrics_middleware(request, call_next):
    endpoint = request.url.path
    REQUEST_COUNT.labels(endpoint=endpoint).inc()

    start = time.time()

    try:
        response = await call_next(request)
        status = response.status_code

        if 400 <= status < 500:
            ERROR_4XX_COUNT.labels(endpoint=endpoint, status_code=status).inc()

        elif status >= 500:
            ERROR_5XX_COUNT.labels(endpoint=endpoint, status_code=status).inc()

    except Exception:
        ERROR_5XX_COUNT.labels(endpoint=endpoint, status_code=500).inc()
        raise

    elapsed = time.time() - start
    REQUEST_LATENCY.labels(endpoint=endpoint).observe(elapsed)

    return response

# ROTAS E PROMETHEUS
app.include_router(router)

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
