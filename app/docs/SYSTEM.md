```md
# 시스템 설명 문서

## 1. 오픈소스 구성
- 수집: Python(FastAPI) exporter, Prometheus
- 저장: Prometheus TSDB
- 시각화: Grafana

## 2. 수집 지표
- demo_cpu_usage_percent: CPU 사용률(%)
- demo_memory_usage_percent: 메모리 사용률(%)
- demo_system_abnormal: 시스템 상태 (0=정상, 1=비정상)

## 시스템 구조

```mermaid
graph LR
    A[수집 대상<br/>Server / API] --> B[Exporter<br/>metrics 노출]
    B --> C[Prometheus<br/>주기적 수집]
    C --> D[TSDB 저장]
    C --> E[Grafana<br/>대시보드 조회]
    E --> F[사용자 모니터링]