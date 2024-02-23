# Simulación de Eventos Discretos

## Sistema a simular: n servidores en paralelo

Los clientes llegan a un sistema que tiene n servidores, con tiempo entre los arribos que distribuye M. Cuando un cliente llega, se une a la cola si ambos servidores están ocupados. Si el servidor 1 está libre, el cliente entra en servicio con el servidor 1. Si el servidor 1 está ocupado pero el servidor 2 está libre, el cliente entra en servicio con el servidor 2.

Cuando un cliente completa el servicio con un servidor (no importa cuál), ese cliente luego abandona el sistema. El cliente que ha estado en la cola durante más tiempo (si hay clientes en la cola) entra en servicio.

La distribución de servicio en el servidor i es Gi.

## Estructura del repositorio:

* La implementación del sistema se encuentra en la carpeta src.
* La orientación del proyecto y el informe en LaTeX se encuentran en la carpeta report.
