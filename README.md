::: {align="center"}
# 🚀 Self-Healing Kubernetes Platform

### CI/CD • Kubernetes • Prometheus • Grafana

**Proyek Portofolio DevOps \| DevOps Portfolio Project**

Membangun dan memantau aplikasi berbasis container dengan automated
testing, Kubernetes self-healing, serta observability menggunakan
Prometheus dan Grafana.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?logo=kubernetes&logoColor=white)
![GitHub
Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?logo=githubactions&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C?logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-Dashboard-F46800?logo=grafana&logoColor=white)

[Repository](https://github.com/defrisdoloksaribu/devops-deployment-pipeline)
·
[Issues](https://github.com/defrisdoloksaribu/devops-deployment-pipeline/issues)
:::

------------------------------------------------------------------------

## 📌 Tentang Proyek \| About

Proyek ini merupakan latihan praktis DevOps yang menunjukkan alur
pengujian aplikasi, pembuatan Docker image, deployment ke Kubernetes,
pemulihan pod, dan monitoring metrik aplikasi.

This project demonstrates a containerized FastAPI application with CI/CD
checks, Kubernetes self-healing behavior, and application monitoring in
a local development environment.

### 🎯 Tujuan \| Goals

-   Mengotomatisasi pengujian dan proses build menggunakan GitHub
    Actions.
-   Menjalankan aplikasi dengan tiga replika Kubernetes.
-   Menguji penggantian pod setelah pod dihapus.
-   Mengumpulkan metrik aplikasi melalui Prometheus.
-   Menampilkan metrik melalui dashboard Grafana.

## ✨ Fitur Utama \| Key Features

  -----------------------------------------------------------------------
  Fitur                               Deskripsi
  ----------------------------------- -----------------------------------
  ⚙️ **CI/CD**                        GitHub Actions menjalankan
                                      automated tests dan Docker image
                                      build.

  🐳 **Containerization**             Aplikasi FastAPI dikemas ke dalam
                                      Docker image.

  ☸️ **Kubernetes Deployment**        Deployment dikonfigurasi dengan
                                      tiga replika.

  🔄 **Self-Healing**                 Kubernetes membuat pod pengganti
                                      ketika sebuah pod dihapus.

  ❤️ **Health Probes**                Readiness dan liveness probes
                                      menggunakan endpoint `/health`.

  📊 **Metrics**                      Metrik aplikasi tersedia di
                                      endpoint `/metrics` untuk
                                      Prometheus.

  📈 **Monitoring**                   Grafana menampilkan empat panel
                                      pemantauan aplikasi.

  ✅ **Manifest Validation**          Kubernetes manifests diperiksa
                                      dengan kubeconform melalui GitHub
                                      Actions.
  -----------------------------------------------------------------------

## 🏗️ Arsitektur \| Architecture

``` text
Developer
   |
   v
GitHub Repository
   |
   v
GitHub Actions
   +--> Automated Tests
   +--> Docker Image Build
   +--> Kubernetes Manifest Validation
   |
   v
Kubernetes Cluster
   +--> FastAPI Application (3 replicas)
   +--> Health Probes (/health)
   +--> Application Metrics (/metrics)
   +--> Pod Self-Healing
              |
              v
          Prometheus
              |
              v
        Grafana Dashboard
```

> **Catatan:** Diagram ini menunjukkan komponen utama proyek. Tahapan
> CI/CD dan deployment ke lingkungan remote bergantung pada konfigurasi
> workflow masing-masing; tidak semua komponen berarti berjalan sebagai
> satu deployment otomatis.

## 🧰 Teknologi \| Tech Stack

  -----------------------------------------------------------------------
  Teknologi                           Penggunaan
  ----------------------------------- -----------------------------------
  Python + FastAPI                    Aplikasi API

  pytest                              Automated testing

  Docker                              Container image

  Kubernetes + kubectl                Deployment, replicas, services, dan
                                      health probes

  GitHub Actions                      CI/CD workflow

  kubeconform                         Validasi manifest Kubernetes

  Prometheus                          Pengumpulan dan query metrik

  Grafana                             Dashboard monitoring
  -----------------------------------------------------------------------

## 📁 Struktur Proyek \| Project Structure

``` text
devops-deployment-pipeline/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── kubernetes-validation.yml
├── app/
│   ├── main.py
│   └── requirements.txt
├── k8s/
│   ├── deployment.yaml
│   └── monitoring/
│       └── monitoring.yaml
├── tests/
│   └── test_main.py
├── Dockerfile
├── requirements-dev.txt
├── requirements.txt
└── README.md
```

## 🚀 Menjalankan Proyek \| Getting Started

### Prasyarat \| Prerequisites

-   Git dan Python tersedia di komputer.
-   Docker berjalan.
-   Kubernetes cluster aktif dan dapat diakses oleh `kubectl`.
-   Untuk lingkungan lokal Windows, Docker Desktop dengan Kubernetes
    atau cluster lokal lain yang sesuai.

### 1. Clone repository

``` bash
git clone https://github.com/defrisdoloksaribu/devops-deployment-pipeline.git
cd devops-deployment-pipeline
```

### 2. Install dependencies dan jalankan tests

Di Windows, gunakan Python launcher `py`:

``` cmd
py -m pip install -r requirements-dev.txt
py -m pytest -v
```

### 3. Build Docker image

``` cmd
docker build -t devops-deployment-pipeline:monitoring .
```

Pastikan image dapat diakses oleh Kubernetes cluster yang digunakan.
Pada cluster lokal, image perlu dibangun atau dimuat ke lingkungan
container yang digunakan oleh cluster tersebut.

### 4. Deploy aplikasi

``` cmd
kubectl apply -f k8s/deployment.yaml
kubectl rollout status deployment/devops-app
kubectl get pods
kubectl get services
```

### 5. Deploy Prometheus dan Grafana

``` cmd
kubectl apply -f k8s/monitoring/monitoring.yaml
kubectl rollout status deployment/prometheus -n monitoring
kubectl rollout status deployment/grafana -n monitoring
kubectl get pods -n monitoring
```

### 6. Akses aplikasi \| Access the application

Jalankan perintah berikut di terminal terpisah:

``` cmd
kubectl port-forward service/devops-app 8000:8000
```

  -----------------------------------------------------------------------
  Endpoint                            Fungsi
  ----------------------------------- -----------------------------------
  <http://localhost:8000/>            Halaman utama API

  <http://localhost:8000/health>      Status kesehatan aplikasi

  <http://localhost:8000/metrics>     Metrik aplikasi untuk Prometheus
  -----------------------------------------------------------------------

### 7. Akses Prometheus

``` cmd
kubectl port-forward -n monitoring service/prometheus 9090:9090
```

Buka <http://localhost:9090>. Contoh query PromQL:

``` promql
sum(http_requests_total)
```

### 8. Akses Grafana

``` cmd
kubectl port-forward -n monitoring service/grafana 3000:3000
```

Buka <http://localhost:3000>. Atur Prometheus sebagai data source dengan
URL internal berikut:

``` text
http://prometheus.monitoring.svc.cluster.local:9090
```

Jalankan port-forward Prometheus dan Grafana di terminal yang berbeda
jika keduanya ingin dibuka bersamaan.

## 📊 Monitoring Dashboard

Dashboard Grafana berisi empat panel:

1.  **Total HTTP Requests** --- jumlah request HTTP yang tercatat.
2.  **HTTP Requests per Second** --- laju request berdasarkan interval
    waktu.
3.  **Average Response Time** --- rata-rata durasi request berdasarkan
    metrik instrumentasi.
4.  **Requests by Endpoint** --- jumlah request yang dikelompokkan
    berdasarkan endpoint.

Contoh query PromQL yang digunakan:

**Total requests**

``` promql
sum(http_requests_total)
```

**Request rate**

``` promql
sum(rate(http_requests_total[5m]))
```

**Average response time**

``` promql
sum(rate(http_request_duration_seconds_sum[5m]))
/
sum(rate(http_request_duration_seconds_count[5m]))
```

**Requests per endpoint**

``` promql
sum by (handler) (http_requests_total)
```

## 🔄 Pengujian Self-Healing \| Self-Healing Test

Pengujian ini memverifikasi bahwa Kubernetes berusaha mempertahankan
jumlah replika yang dikonfigurasi.

1.  Periksa pod:

    ``` cmd
    kubectl get pods
    ```

2.  Hapus satu pod aplikasi. Ganti `<pod-name>` dengan nama pod yang
    benar:

    ``` cmd
    kubectl delete pod <pod-name>
    ```

3.  Pantau pod dan penggantinya:

    ``` cmd
    kubectl get pods -w
    ```

4.  Periksa Deployment:

    ``` cmd
    kubectl get deployment devops-app
    ```

**Hasil yang diharapkan:** Kubernetes membuat pod pengganti agar jumlah
replika kembali ke jumlah yang diinginkan. Perilaku ini membuktikan
pemulihan pod yang dikelola oleh Deployment.

## ✅ Validasi \| Validation

Pemeriksaan yang telah dilakukan selama pengembangan:

-   [x] Dua application tests lulus di lingkungan lokal.
-   [x] Docker image berhasil dibangun.
-   [x] Deployment aplikasi berjalan dengan tiga replika.
-   [x] Pod pengganti dibuat setelah satu pod dihapus.
-   [x] Monitoring manifest lolos client-side dry-run validation.
-   [x] Prometheus berhasil mengambil metrik aplikasi.
-   [x] Grafana berhasil terhubung ke Prometheus dan menampilkan empat
    panel.
-   [x] Pemeriksaan GitHub Actions untuk CI dan validasi manifest
    berhasil pada pull request monitoring.

## 📸 Screenshot \| Bukti Implementasi

Tambahkan screenshot asli dari hasil pengujian ke folder `screenshots/`,
lalu aktifkan gambar di bawah dengan nama file yang sesuai.

  Bukti                Nama file
  -------------------- -----------------------------------------
  GitHub Actions       `screenshots/01-github-actions.png`
  Kubernetes pods      `screenshots/02-kubernetes-pods.png`
  Self-healing test    `screenshots/03-self-healing.png`
  Prometheus targets   `screenshots/04-prometheus-targets.png`
  Grafana dashboard    `screenshots/05-grafana-dashboard.png`

Contoh cara menampilkan dashboard setelah file screenshot ditambahkan:

``` markdown
![Grafana Monitoring Dashboard](screenshots/05-grafana-dashboard.png)
```

## 🎓 Hal yang Dipelajari \| Learning Outcomes

Melalui proyek ini, saya mempraktikkan:

-   Penyusunan CI/CD checks dan automated testing.
-   Containerization menggunakan Docker.
-   Kubernetes Deployment, Services, replicas, dan health probes.
-   Konsep self-healing dan desired replica count.
-   Pengumpulan serta query metrik menggunakan Prometheus.
-   Pembuatan dashboard monitoring dengan Grafana.
-   Validasi konfigurasi Kubernetes.
-   Pengelolaan perubahan melalui Git dan GitHub Pull Requests.

## 🔮 Pengembangan Selanjutnya \| Future Improvements

-   Menambahkan alerting rules dan notifikasi.
-   Menyiapkan persistent storage untuk Prometheus dan Grafana.
-   Menambahkan monitoring penggunaan CPU dan memory.
-   Mengelola deployment menggunakan Helm.
-   Memperluas automated deployment ke Kubernetes.
-   Menambahkan pengujian availability dan recovery.

## 👨‍💻 Author

**Defris Doloksaribu**

-   GitHub: [@defrisdoloksaribu](https://github.com/defrisdoloksaribu)
-   Repository:
    [devops-deployment-pipeline](https://github.com/defrisdoloksaribu/devops-deployment-pipeline)

------------------------------------------------------------------------

*Built as a hands-on portfolio project to develop practical DevOps,
Kubernetes, CI/CD, and monitoring skills.*
