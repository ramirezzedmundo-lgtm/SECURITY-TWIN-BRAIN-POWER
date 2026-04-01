# 🛡️ Sistema de Seguridad + Pentesting Ético

Este repositorio integra **IA siamesa, PostgreSQL, Kubernetes, Redis y Python** para crear un protocolo de seguridad en 3 fases con pentesting ético y diagnóstico al usuario.

---

## Protocolo de 3 fases
1. **Defensa preventiva**: IA gestiona red, puertos y periféricos. Kubernetes reemplaza instancias comprometidas.  
2. **Respuesta activa**: despliegue de honeypots, rotación de tokens cada 10s, CAPTCHA Rust/C++ y Redis para desvío de tráfico.  
3. **Recuperación y aprendizaje**: reporte detallado del ataque, recuento de daños, información del atacante y ajuste del protocolo.  

---

## Pentesting Ético
- Escaneo con Nmap, Masscan, ZAP, Burp Suite.  
- Simulación de fuerza bruta con Hydra.  
- Reportes claros al usuario vía dashboard web.  

---

## Flujo completo del sistema

```mermaid
flowchart LR
    U[Usuario] --> F[Frontend Dashboard]
    F --> B[Backend FastAPI]
    B --> P[Pentesting Engine]
    P -->|Nmap / Hydra / ZAP| R[Resultados JSON]
    R --> F
    F --> U

---
## 🔐 Explicación del flujo
- **Usuario (U):** accede al dashboard web.  
- **Frontend (F):** hace la petición al backend.  
- **Backend (B):** expone endpoints REST con FastAPI.  
- **Pentesting Engine (P):** ejecuta pruebas (Nmap, Hydra, ZAP).  
- **Resultados (R):** se devuelven en formato JSON.  
- **Frontend (F):** muestra el diagnóstico claro al usuario.  

---

