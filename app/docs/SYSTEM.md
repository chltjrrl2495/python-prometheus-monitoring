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

```md
### 데이터 흐름 설명
1. Exporter가 시스템 상태를 metrics 형태로 노출한다.
2. Prometheus가 일정 주기로 해당 metrics를 Pull 방식으로 수집한다.
3. 수집된 데이터는 Prometheus TSDB에 데이터로 저장된다.
4. Grafana는 Prometheus를 데이터소스로 사용하여 데이터를 조회한다.
5. 사용자는 대시보드를 통해 시스템 상태를 확인하고 이상 상황을 인지한다.