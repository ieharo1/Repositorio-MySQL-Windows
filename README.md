# ☸️ Cluster de Analisis de Ventas con Spark + MySQL

Sistema completo para generar datos de ventas, almacenarlos en MySQL y analizarlos con Apache Spark en Kubernetes.

---

## ✅ Descripcion

Pipeline de Big Data que simula ventas, guarda registros en MySQL y ejecuta jobs Spark para obtener metricas agregadas.

### ¿Que hace este proyecto?

- **Generador de datos**: Simula ventas y las inserta en MySQL
- **MySQL**: Almacena los registros de ventas
- **Spark Jobs**: Procesa datos a gran escala
- **Resultados**: Ventas totales, top productos, ventas por region, promedio por cliente

---

## ✨ Caracteristicas Principales

| Caracteristica | Descripcion |
|----------------|-------------|
| **ETL** | Generacion, carga y procesamiento de datos |
| **Procesamiento distribuido** | Spark en modo cluster |
| **Analitica** | Metricas agregadas por producto, region y cliente |
| **Docker Compose** | Pruebas locales |
| **Kubernetes** | Manifests listos para cluster |

---

## 🛠️ Stack Tecnologico

- **Python**: Generador y Spark Jobs
- **Apache Spark**: Analisis distribuido
- **MySQL**: Persistencia de datos
- **Docker / Kubernetes**: Orquestacion

---

## 📦 Instalacion y Uso

### Requisitos

- Docker Desktop
- `kubectl`

### Probar con Docker Compose

```bash
docker compose up --build
```

### Probar con Kubernetes

1) Construir imagenes:

```bash
docker build -t sales-generator:latest -f docker/generator.Dockerfile .
docker build -t spark-sales-job:latest -f docker/spark.Dockerfile .
```

2) Aplicar manifests:

```bash
kubectl apply -f k8s/mysql.yaml
kubectl apply -f k8s/spark-master.yaml
kubectl apply -f k8s/spark-worker.yaml
kubectl apply -f k8s/generator-job.yaml
kubectl apply -f k8s/spark-job.yaml
```

---

## 🗂️ Estructura del Proyecto

```
spark-mysql-analytics-cluster
├── generator
├── spark-jobs
├── mysql
├── k8s
├── docker
├── docker-compose.yml
└── README.md
```

---

## 👤 Desarrollado por Isaac Esteban Haro Torres

**Ingeniero en Sistemas · Full Stack · Automatizacion · Data**

- Email: zackharo1@gmail.com
- WhatsApp: 098805517
- GitHub: https://github.com/ieharo1
- Portafolio: https://ieharo1.github.io/portafolio-isaac.haro/

---

© 2026 Isaac Esteban Haro Torres - Todos los derechos reservados.

