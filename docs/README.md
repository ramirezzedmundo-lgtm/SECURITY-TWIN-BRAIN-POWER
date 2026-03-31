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

## 📊 Diagrama de arquitectura

```mermaid
flowchart TD
    A[Usuario] -->|Acceso Gmail/Outlook/Drive| B[IA Siamesa]
    B -->|Aprende patrones| C[PostgreSQL]
    B -->|Gestión de puertos y periféricos| D[Kubernetes]
    D -->|Reemplazo automático| B
    B -->|Detección de ataque| E[Honeypots + Redis]
    E -->|Rotación de tokens| F[Seguridad Activa]
    F -->|Reporte de Pentesting| G[Dashboard Web]
    G -->|Diagnóstico claro| A
