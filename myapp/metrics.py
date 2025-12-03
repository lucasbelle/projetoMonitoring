from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "app_request_count_total",
    "Total de requisições",
    ["endpoint"]
)

REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Latência das requisições",
    ["endpoint"]
)

ERROR_4XX_COUNT = Counter(
    "app_request_client_errors_total",
    "Total de erros 4xx",
    ["endpoint", "status_code"]
)

ERROR_5XX_COUNT = Counter(
    "app_request_server_errors_total",
    "Total de erros 5xx",
    ["endpoint", "status_code"]
)

PURCHASE_COUNT = Counter(
    "app_checkout_finished_total",
    "Contagem total de finalizações de compra bem-sucedidas",
    ["endpoint"]
)
