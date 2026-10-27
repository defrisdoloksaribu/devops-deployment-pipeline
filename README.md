# \# 🚀 Self-Healing Kubernetes Platform with CI/CD and Monitoring

#

# \*\*A DevOps Portfolio Project | Proyek Portofolio DevOps\*\*

#

# Membangun platform aplikasi berbasis container dengan automated CI/CD, Kubernetes self-healing, dan monitoring real-time menggunakan Prometheus dan Grafana.

#

# <p align="center">

# &#x20; <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python\&logoColor=white" alt="Python"/>

# &#x20; <img src="https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi\&logoColor=white" alt="FastAPI"/>

# &#x20; <img src="https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker\&logoColor=white" alt="Docker"/>

# &#x20; <img src="https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?logo=kubernetes\&logoColor=white" alt="Kubernetes"/>

# &#x20; <img src="https://img.shields.io/badge/GitHub\_Actions-CI%2FCD-2088FF?logo=githubactions\&logoColor=white" alt="GitHub Actions"/>

# &#x20; <img src="https://img.shields.io/badge/Prometheus-Monitoring-E6522C?logo=prometheus\&logoColor=white" alt="Prometheus"/>

# &#x20; <img src="https://img.shields.io/badge/Grafana-Dashboard-F46800?logo=grafana\&logoColor=white" alt="Grafana"/>

# </p>

#

# \## 📌 Tentang Proyek | About This Project

#

# Proyek ini merupakan implementasi praktik DevOps untuk menunjukkan bagaimana aplikasi dapat diuji, dikemas ke dalam Docker image, dijalankan di Kubernetes, dan dipantau melalui sistem monitoring.

#

# The platform demonstrates automated testing, containerization, Kubernetes orchestration, pod recovery, and application observability in a local development environment.

#

# \*\*Tujuan proyek:\*\*

# \- Menerapkan CI/CD menggunakan GitHub Actions.

# \- Menjalankan aplikasi dengan tiga replika Kubernetes.

# \- Menguji mekanisme self-healing ketika sebuah pod dihapus.

# \- Mengumpulkan metrik aplikasi menggunakan Prometheus.

# \- Memvisualisasikan performa aplikasi melalui dashboard Grafana.

#

# \## ✨ Key Features | Fitur Utama

#

# | Fitur | Penjelasan |

# |---|---|

# | ⚙️ CI/CD Automation | GitHub Actions menjalankan automated tests dan Docker image build. |

# | 🐳 Containerization | FastAPI dikemas dalam Docker image. |

# | ☸️ Kubernetes Deployment | Aplikasi dikonfigurasi menggunakan tiga replika. |

# | 🔄 Self-Healing | Kubernetes membuat pod pengganti ketika sebuah pod dihapus. |

# | ❤️ Health Probes | Readiness dan liveness probes menggunakan endpoint `/health`. |

# | 📊 Metrics Collection | Prometheus mengambil metrik dari endpoint `/metrics`. |

# | 📈 Monitoring Dashboard | Grafana menampilkan empat panel monitoring aplikasi. |

# | ✅ Manifest Validation | Kubernetes manifests divalidasi menggunakan kubeconform melalui GitHub Actions. |

#

# \## 🏗️ Architecture | Arsitektur Sistem

#

# ```text

# Developer

# &#x20;   |

# &#x20;   v

# GitHub Repository

# &#x20;   |

# &#x20;   v

# GitHub Actions

# &#x20;   |

# &#x20;   +---- Automated Tests

# &#x20;   |

# &#x20;   +---- Docker Image Build

# &#x20;   |

# &#x20;   +---- Kubernetes Manifest Validation

# &#x20;   |

# &#x20;   v

# Kubernetes Cluster

# &#x20;   |

# &#x20;   +---- FastAPI Application

# &#x20;   |       |

# &#x20;   |       +---- 3 Replicas

# &#x20;   |       +---- /health

# &#x20;   |       +---- /metrics

# &#x20;   |

# &#x20;   +---- Self-Healing

# &#x20;   |

# &#x20;   v

# Prometheus

# &#x20;   |

# &#x20;   v

# Grafana Dashboard

# ```

#

# \*Catatan: deployment otomatis ke lingkungan remote merupakan bagian terpisah dari workflow yang sudah ada. Diagram ini menggambarkan komponen utama proyek, bukan jaminan bahwa seluruh tahap berjalan dalam satu deployment otomatis.\*

#

# \## 🧰 Tech Stack | Teknologi

#

# | Teknologi | Kegunaan |

# |---|---|

# | Python \& FastAPI | Membangun aplikasi API. |

# | pytest | Menjalankan pengujian aplikasi. |

# | Docker | Mengemas aplikasi ke dalam container image. |

# | Kubernetes | Mengelola replika, health probes, dan pemulihan pod. |

# | GitHub Actions | Mengotomatisasi pengujian dan proses build. |

# | kubeconform | Memvalidasi konfigurasi Kubernetes. |

# | Prometheus | Mengumpulkan dan menyimpan metrik. |

# | Grafana | Membuat dashboard visualisasi metrik. |

#

# \## 📁 Project Structure | Struktur Folder

#

# ```text

# devops-deployment-pipeline/

# ├── .github/

# │   └── workflows/

# │       ├── ci.yml

# │       └── kubernetes-validation.yml

# ├── app/

# │   ├── main.py

# │   └── requirements.txt

# ├── k8s/

# │   ├── deployment.yaml

# │   └── monitoring/

# │       └── monitoring.yaml

# ├── tests/

# │   └── test\_main.py

# ├── Dockerfile

# ├── requirements-dev.txt

# ├── requirements.txt

# └── README.md

# ```

#

# \## 🚀 Getting Started | Cara Menjalankan

#

# \### 1. Clone Repository

#

# ```bash

# git clone https://github.com/defrisdoloksaribu/devops-deployment-pipeline.git

# cd devops-deployment-pipeline

# ```

#

# \### 2. Install Dependencies dan Jalankan Tests

#

# ```bash

# py -m pip install -r requirements-dev.txt

# py -m pytest -v

# ```

#

# Perintah di atas dapat digunakan di Windows apabila launcher `py` sudah tersedia.

#

# \### 3. Build Docker Image

#

# ```bash

# docker build -t devops-deployment-pipeline:monitoring .

# ```

#

# Pastikan image tersedia bagi Kubernetes cluster yang digunakan.

#

# \### 4. Deploy Aplikasi ke Kubernetes

#

# ```bash

# kubectl apply -f k8s/deployment.yaml

# kubectl rollout status deployment/devops-app

# kubectl get pods

# kubectl get services

# ```

#

# \### 5. Deploy Monitoring Stack

#

# ```bash

# kubectl apply -f k8s/monitoring/monitoring.yaml

# kubectl rollout status deployment/prometheus -n monitoring

# kubectl rollout status deployment/grafana -n monitoring

# kubectl get pods -n monitoring

# ```

#

# \### 6. Access Application | Akses Aplikasi

#

# Jalankan port forwarding:

#

# ```bash

# kubectl port-forward service/devops-app 8000:8000

# ```

#

# Buka endpoint berikut di browser:

#

# | Endpoint | Fungsi |

# |---|---|

# | \[localhost:8000](http://localhost:8000/) | Halaman utama API. |

# | \[localhost:8000/health](http://localhost:8000/health) | Memeriksa status kesehatan aplikasi. |

# | \[localhost:8000/metrics](http://localhost:8000/metrics) | Melihat metrik untuk Prometheus. |

#

# \### 7. Access Prometheus

#

# ```bash

# kubectl port-forward -n monitoring service/prometheus 9090:9090

# ```

#

# Buka \[Prometheus UI](http://localhost:9090).

#

# Contoh query untuk melihat jumlah HTTP request:

#

# ```promql

# sum(http\_requests\_total)

# ```

#

# \### 8. Access Grafana

#

# ```bash

# kubectl port-forward -n monitoring service/grafana 3000:3000

# ```

#

# Buka \[Grafana Dashboard](http://localhost:3000).

#

# Konfigurasikan data source Prometheus dengan URL berikut:

#

# ```text

# http://prometheus.monitoring.svc.cluster.local:9090

# ```

#

# Pastikan port forwarding untuk Prometheus dan Grafana dijalankan pada terminal terpisah apabila keduanya ingin diakses bersamaan.

#

# \## 📊 Monitoring Dashboard

#

# Dashboard Grafana mencakup empat visualisasi utama:

#

# 1\. \*\*Total HTTP Requests\*\* — jumlah permintaan HTTP yang tercatat.

# 2\. \*\*HTTP Requests per Second\*\* — laju permintaan dalam interval waktu.

# 3\. \*\*Average Response Time\*\* — estimasi rata-rata durasi penanganan permintaan.

# 4\. \*\*Requests by Endpoint\*\* — distribusi permintaan berdasarkan endpoint.

#

# Contoh PromQL yang digunakan:

#

# ```promql

# sum(http\_requests\_total)

# ```

#

# ```promql

# sum(rate(http\_requests\_total\[5m]))

# ```

#

# ```promql

# sum(rate(http\_request\_duration\_seconds\_sum\[5m]))

# /

# sum(rate(http\_request\_duration\_seconds\_count\[5m]))

# ```

#

# ```promql

# sum by (handler) (http\_requests\_total)

# ```

#

# \## 🔄 Self-Healing Test | Pengujian Pemulihan Pod

#

# Pengujian dilakukan untuk memverifikasi kemampuan Kubernetes mempertahankan jumlah replika yang diinginkan.

#

# \*\*Langkah pengujian:\*\*

#

# 1\. Periksa pod aplikasi:

#

# &#x20;  ```bash

# &#x20;  kubectl get pods

# &#x20;  ```

#

# 2\. Hapus satu pod aplikasi:

#

# &#x20;  ```bash

# &#x20;  kubectl delete pod <pod-name>

# &#x20;  ```

#

# &#x20;  Ganti `<pod-name>` dengan nama pod yang sebenarnya.

#

# 3\. Pantau proses pemulihan:

#

# &#x20;  ```bash

# &#x20;  kubectl get pods -w

# &#x20;  ```

#

# 4\. Periksa status Deployment:

#

# &#x20;  ```bash

# &#x20;  kubectl get deployment devops-app

# &#x20;  ```

#

# \*\*Expected result:\*\* Kubernetes membuat pod pengganti dan berusaha mengembalikan Deployment ke tiga replika yang diinginkan.

#

# \## ✅ Validation Results | Hasil Pengujian

#

# Pengujian berikut telah berhasil dilakukan selama pengembangan:

#

# \- \[x] Automated application tests passed.

# \- \[x] Docker image berhasil dibangun.

# \- \[x] Kubernetes Deployment mencapai kondisi running.

# \- \[x] Pod pengganti dibuat setelah sebuah pod dihapus.

# \- \[x] Monitoring manifests lolos client-side dry-run validation.

# \- \[x] Prometheus berhasil mengambil metrik aplikasi.

# \- \[x] Grafana berhasil terhubung ke Prometheus dan menampilkan empat panel.

# \- \[x] GitHub Actions CI dan Kubernetes manifest validation berhasil pada Pull Request monitoring.

#

# \## 📸 Screenshots | Bukti Implementasi

#

# Bukti visual akan ditambahkan setelah screenshot disimpan ke folder `screenshots/`.

#

# | Bukti | Nama File |

# |---|---|

# | GitHub Actions | `screenshots/01-github-actions.png` |

# | Kubernetes Pods | `screenshots/02-kubernetes-pods.png` |

# | Self-Healing Test | `screenshots/03-self-healing.png` |

# | Prometheus Targets | `screenshots/04-prometheus-targets.png` |

# | Grafana Dashboard | `screenshots/05-grafana-dashboard.png` |

#

# \## 🎯 Learning Outcomes | Hal yang Dipelajari

#

# Melalui proyek ini, saya mempraktikkan:

#

# \- Dasar implementasi CI/CD dan automated testing.

# \- Containerization menggunakan Docker.

# \- Kubernetes Deployment, Services, dan health probes.

# \- Konsep self-healing dan desired replica count.

# \- Pengumpulan metrik dengan Prometheus.

# \- Visualisasi monitoring menggunakan Grafana.

# \- Validasi konfigurasi Kubernetes.

# \- Pengelolaan perubahan kode menggunakan Git dan GitHub Pull Requests.

#

# \## 🔮 Future Improvements | Pengembangan Selanjutnya

#

# \- Implementasi alerting rules dan notifikasi.

# \- Persistent storage untuk Prometheus dan Grafana.

# \- Monitoring resource CPU dan memory.

# \- Pengelolaan deployment menggunakan Helm.

# \- Pengembangan automated deployment ke Kubernetes.

# \- Penambahan pengujian availability dan recovery.

#

# \## 👨‍💻 Author

#

# \*\*Defris Doloksaribu\*\*

#

# \- GitHub: \[@defrisdoloksaribu](https://github.com/defrisdoloksaribu)

# \- Repository: \[devops-deployment-pipeline](https://github.com/defrisdoloksaribu/devops-deployment-pipeline)

#

# \*Built as a hands-on learning project to develop practical DevOps, Kubernetes, CI/CD, and monitoring skills.\*
