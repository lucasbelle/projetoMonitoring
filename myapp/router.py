import time
import math
import random
import os
from fastapi import APIRouter, HTTPException
from starlette.responses import HTMLResponse
from .metrics import PURCHASE_COUNT
from .html_buy_page import BUY_PAGE_HTML
from .html_checkout_page import CHECKOUT_SUCCESS_HTML

router = APIRouter()

@router.get("/")
def health():
    return {"status": "ok"}


@router.get("/error")
def forced_error():
    raise HTTPException(500, "Erro proposital.")


@router.get("/slow")
def slow(delay: float = 10.0):
    time.sleep(delay)
    return {"status": "ok", "delay_seconds": delay}

@router.get("/random-error")
def random_error():
    r = random.random()
    if r < 0.4:
        raise HTTPException(400, "Erro 400 aleatório.")
    elif r < 0.6:
        raise HTTPException(500, "Erro 500 aleatório.")
    else:
        return {"status": "ok"}


@router.get("/memory")
def memory(size_mb: int = 150):
    block = "x" * (size_mb * 1024 * 1024)
    time.sleep(1)
    return {"allocated_mb": size_mb}


@router.get("/cpu")
def cpu(iterations: int = 1_000_000):
    result = 0
    for i in range(iterations):
        result += math.sqrt(i + 1)
    return {"status": "ok", "iterations": iterations}


@router.get("/disk")
def disk_io(size_mb: int = 50):
    filename = "/tmp/disk_test.bin"
    block = os.urandom(1024 * 1024)

    with open(filename, "wb") as f:
        for _ in range(size_mb):
            f.write(block)
            f.flush()
            os.fsync(f.fileno())

    os.remove(filename)
    return {"written_mb": size_mb}

@router.get("/checkout")
def checkout():
 
    PURCHASE_COUNT.labels(endpoint="/checkout").inc()
    
    return HTMLResponse(content=CHECKOUT_SUCCESS_HTML)

@router.get("/buy", response_class=HTMLResponse)
def buy_page():
    return HTMLResponse(content=BUY_PAGE_HTML)
 




