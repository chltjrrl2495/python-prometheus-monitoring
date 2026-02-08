# 오픈소스 기반 데이터 수집·모니터링 시스템 구현

## 1. 프로젝트 개요
본 문서는 Python 기반 exporter와 Prometheus, Grafana를 활용하여
서버 리소스(CPU/Memory)를 수집·저장·시각화하는
로컬 모니터링 환경을 구성하고,
상태 인지 가능 여부를 확인한 구현 결과를 정리한 문서이다.


## 2. 시스템 구성
- 수집: Python(FastAPI) exporter, Prometheus
- 저장: Prometheus TSDB
- 시각화: Grafana
- 실행 환경: Windows + Docker Desktop(WSL2)


## 3. 실행 방법

### 3.1 실행 환경
- Docker Desktop 설치 필요 (WSL2 기반)

### 3.2 실행
```bash
cd app
docker compose up -d --build
```
### 3.3 접속 정보
- Python exporter: http://localhost:8000/metrics

- Prometheus: http://localhost:9090

- Grafana: http://localhost:3000
 - (기본 계정: admin / admin)


## 4. 수집 정상 동작 확인

### 4.1 Exporter 메트릭 확인
Python exporter는 /metrics 엔드포인트를 통해
Prometheus 포맷의 메트릭을 노출한다.

접속: http://localhost:8000/metrics

주요 확인 항목:

- demo_cpu_usage_percent: CPU 사용률(%)

- demo_memory_usage_percent: 메모리 사용률(%)

- demo_system_abnormal: 시스템 상태 (0=정상, 1=비정상)

### 4.2 Prometheus 수집 상태 확인
Prometheus에서 exporter 수집 상태를 확인한다.
- 접속: http://localhost:9090/targets
- python_exporter 항목이 UP 상태인지 확인

본 구성에서는 Python Exporter가 서버 리소스를 수집하고,
Prometheus가 해당 Exporter를 주기적으로 scrape하여
메트릭을 TSDB에 저장한 후, Grafana가 이를 조회하여 시각화한다.


## 5. 모니터링 대시보드 구성
Grafana를 통해 다음 항목을 대시보드로 구성하였다.
- CPU Usage (%)
- Memory Usage (%)
- System Status (NORMAL / ABNORMAL)
CPU 및 Memory 사용률은 그래프로 표현하였으며,
System Status는 Python exporter에서 판단한 상태 값을 기반으로
정상/비정상 여부를 직관적으로 확인할 수 있도록 구성하였다.


## 6. 이상 상황 재현 방법
상태 변화가 정상적으로 반영되는지 확인하기 위해
CPU 부하를 인위적으로 발생시켜 테스트를 수행하였다.

### 6.1 CPU 부하 발생
```bash
docker exec -it exporter bash
python -c "while True: pass"
```
### 6.2 확인 내용
- CPU 사용률이 설정된 임계치를 초과
- demo_system_abnormal 메트릭 값이 1로 변경
- Grafana 대시보드의 System Status 패널이 ABNORMAL(빨강) 상태로 표시됨