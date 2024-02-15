# Sistemas de eventos discretos

## 1. n servidores en paralelo

Los clientes llegan a un sistema que tiene n servidores, con tiempo entre los arribos que distribuye M. Cuando un cliente llega, se une a la cola si ambos servidores están ocupados. Si el servidor 1 está libre, el cliente entra en servicio con el servidor 1. Si el servidor 1 está ocupado pero el servidor 2 está libre, el cliente entra en servicio con el servidor 2.

Cuando un cliente completa el servicio con un servidor (no importa cuál), ese cliente luego abandona el sistema. El cliente que ha estado en la cola durante más tiempo (si hay clientes en la cola) entra en servicio.

La distribución de servicio en el servidor i es Gi.

## 2. n servidores en serie

Los clientes llegan a un sistema que tiene n servidores, y las llegadas distribuye M. Cada cliente que llega debe ser atendido primero por el servidor 1 y, al completar el servicio en el servidor 1, el cliente pasa al servidor 2.

Cuando un cliente llega, entra en servicio con el servidor 1 si ese servidor está libre, o se une a la cola del servidor 1 en caso contrario. De manera similar, cuando el cliente completa el servicio en el servidor 1, entra en servicio con el servidor 2 si ese servidor está libre, o se une a su cola y asi sucesivamente. Después de ser atendido en el servidor n, el cliente abandona el sistema.

Los tiempos de servicio en el servidor i tienen la distribución Gi

## 3. inventario

Para satisfacer las demandas, el tendero debe mantener una cantidad del producto a mano, y siempre que el inventario a mano se vuelve bajo, se ordenan unidades adicionales al distribuidor. El tendero utiliza una política de pedido llamada (s, S); es decir, siempre que el inventario a mano es menor que s y no hay un pedido pendiente, entonces se ordena una cantidad para llevarlo hasta S, donde $s<S$. Es decir, si el nivel de inventario actual es x y no hay un pedido pendiente, entonces si $x<s$ se ordena la cantidad S−x.
El costo de pedir y unidades del producto es una función especificada c(y), y toma L unidades de tiempo hasta que se entrega el pedido, con el pago realizado a la entrega. Además, la tienda paga un costo de mantenimiento de inventario de h por unidad de artículo por unidad de tiempo.
Supongamos además que siempre que un cliente demanda más del producto de lo que está disponible actualmente, entonces se vende la cantidad a mano y el resto del pedido se pierde para la tienda.

## 4. Seguros

En este modelo, los diferentes asegurados de una compañía de seguros generan reclamaciones de acuerdo con con una distribución común M, y cada monto de reclamación tiene una distribución F.
Además, se supone que los nuevos clientes se registran de acuerdo con una distribución ν, y que cada asegurado existente permanece con la compañía durante un tiempo distribuido μ.
Finalmente, se supone que cada asegurado paga a la compañía de seguros a una tasa fija c por unidad de tiempo.
Comenzando con n0​ clientes y un capital inicial a0​≥0

## 5. n servidores con retroceso

Igual a 2 pero en servidor i con una probabilidad p pude se salta a la cola del servidor j.

## 6. Reparaciones

En este modelo, un sistema necesita n máquinas funcionando para estar operativo. Para protegerse contra las averías de las máquinas, se mantienen máquinas adicionales disponibles como repuestos. Cuando una máquina se avería, es inmediatamente reemplazada por un repuesto y se envía a la instalación de reparación, que consta de un único reparador que repara las máquinas averiadas una a la vez. Una vez que una máquina averiada ha sido reparada, se vuelve a disponer como repuesto para ser utilizada cuando sea necesario.
Todos los tiempos de reparación son variables aleatorias independientes que tienen la función de distribución común G. Cada vez que una máquina se pone en uso, la cantidad de tiempo que funciona antes de averiarse es una variable aleatoria, independiente del pasado, que tiene la función de distribución F.
Se dice que el sistema falla cuando una máquina falla y no hay repuestos disponibles. Asumiendo que inicialmente hay n+s máquinas funcionales de las cuales n se ponen en uso y s se mantienen como repuestos, estamos interesados en simular este sistema para aproximar E[T], donde T es el tiempo en el que el sistema se estrella.
