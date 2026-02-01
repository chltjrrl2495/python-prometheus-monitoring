import os
import time
import psutil
from fastapi import FastAPI, Response
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI()

cpu_usage = Gauge("demo_cpu_usage_percent", "CPU usage percent")
mem_usage = Gauge("demo_memory_usage_percent", "Memory usage percent")
system_abnormal = Gauge("demo_system_abnormal", "0=normal, 1=abnormal")

CPU_WARN = float(os.getenv("CPU_WARN", "80"))
MEM_WARN = float(os.getenv("MEM_WARN", "80"))

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    cpu = psutil.cpu_percent(interval=0.2)
    mem = psutil.virtual_memory().percent

    cpu_usage.set(cpu)
    mem_usage.set(mem)

    abnormal = 1 if (cpu >= CPU_WARN or mem >= MEM_WARN) else 0
    system_abnormal.set(abnormal)

    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
