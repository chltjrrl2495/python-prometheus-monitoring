# 시스템 설명 문서

## 1. 오픈소스 구성
- 수집: Python(FastAPI) exporter, Prometheus
- 저장: Prometheus TSDB
- 시각화: Grafana

## 2. 수집 흐름
Python exporter가 서버 리소스를 수집하고,
Prometheus가 이를 주기적으로 scrape하여
TSDB에 저장한 후 Grafana가 조회한다.

## 3. 수집 지표
- demo_cpu_usage_percent: CPU 사용률(%)
- demo_memory_usage_percent: 메모리 사용률(%)
- demo_system_abnormal: 시스템 상태 (0=정상, 1=비정상)

## 4. 이상 상황 재현
CPU 부하를 발생시켜 상태 메트릭 변경 및
대시보드 반영 여부를 확인하였다.
