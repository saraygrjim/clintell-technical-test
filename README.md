# clintell-technical-test

Este proyecto tiene su origen en una prueba técnica solicitada por la empresa Clintell. La prueba consiste en implementar en Python una economía que comercializa con tarjetas gráficas, donde intervienen agentes de varios tipos que operan con ciertas reglas.

## Tabla de Contenidos

- [clintell-technical-test](#clintell-technical-test)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Características](#características)
  - [Requisitos](#requisitos)
  - [Instalación](#instalación)

## Características

- Mercado
  - Stock de **tarjetas** limitado a **100.000 unidades**
  - 100 **agentes** que compran y venden en el mercado
  - Cada vez que un agente compra, el precio de las tarjetas gráficas **sube un 0.5%**
  - Cada vez que un agente vende, el precio de las tarjetas gráfica **baja un 0.5%**
  - **1000 días** de ventas simulados
    - Cada día los agentes se ordenan de forma aleatoria en una cola y uno a uno elige 3 posibles acciones: **comprar, vender o no hacer nada**.
  - El precio inicial de las tarjetas es de 200$
  
- Agentes
  - Los agentes se distribuyen en diferentes grupos organizados por tipo:
    - **RANDOM**: En cada iteración tienen 1/3 de probabilidades de comprar, 1/3 de probabilidades de vender y 1/3 de probabilidades de no hacer nada. En total hay *53 agentes* de este tipo.
    - **TRENDING**: En cada iteración tienen un 75% de probabilidades de comprar y un 25% de probabilidades de no hacer nada si el precio ha subido un 1% (o más) con respecto al final de la iteración. En total hay *24 agentes* de este tipo.
    - **NON-TRENDING**: En cada iteración tienen un 75% de probabilidades de comprar y un 25% de probabilidades de no hacer nada si el precio ha bajado un 1% (o más) con respecto al final de la iteración anterior. En caso contrario tienen un 20% de probabilidades de vender y un 80% de probabilidades de no hacer nada. En total hay *24 agentes* de este tipo.
    - **CUSTOM**: lógica definida por ti con el objetivo de maximizar su balance económico al final de la simulación. El agente debe terminar la última iteración con cero tarjetas gráficas en su poder. En total hay *1 agente* de este tipo.
  - Cada agente cuenta con un balance inicial de 1.000$

- Asunciones
  - Aunque un agente tenga la capacidad de comprar por su tipo asociado, si no tiene dinero suficiente para ello no se le habilita esa capacidad.
  - Aunque un agente tenga la capacidad de vender por su tipo asociado, si no tiene tarjetas en su poder no se le habilita esa capacidad.
  - El mercado no tiene una cartera por lo que puede comprar tarjetas sin comprobaciones.
  - El mercado debe comprobar previamente hay stock de tarjetas antes de realizar una venta.

## Requisitos

- Python 3.9
- Dependencias: consultar el fichero de [requisitos](requirements.tzt)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone git@github.com:saraygrjim/clintell-technical-test.git
   cd clintell-technical-test
    ```
2. Instala las dependencias necesarias para el proyecto
   ```bash 
   make install
   ```
3. Ejecución del proyecto
   ```bash 
   make run
   ```

