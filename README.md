# mypython-backyard
Repositorio de varias cosas que trato de replicar usando Python. Hay un poco de todo...

Para correr lo que hay aqui, es necesario tener instalado Python 3 y los siguientes paquetes:

``` 
pip install numpy sympy matplotlib openpyxl
```
Para los archivos de la carpeta nidaqmx-python, es necesario tener el siguiente paquete instalado:

``` 
pip install nidaqmx
```
Para el correcto funcionamiento de los archivos de esta carpeta, es necesario tener instalado el **driver oficial de NI DAQmx**. Estos archivos pueden funcionar con Hardware real o con Hardware simulado creado en NI MAX (Measurement and Automation Explorer)

Para mayor información, pueden consultar los siguientes enlaces:

[Crear equipo NI DAQ Simulado](https://knowledge.ni.com/KnowledgeArticleDetails?id=kA03q000000x0PxCAI&l=es-MX "Create Simulated NI-DAQmx Devices in NI MAX")

[Descargar los drivers de NI](https://www.ni.com/es-mx/support/downloads/drivers/download.ni-daqmx.html#460239 "NI DAQmx Driver Download")

[Paquete NI DAQmx para Python](https://nidaqmx-python.readthedocs.io/en/latest/index.html# "NI-DAQmx Python Documentation")

Hay algunos ejemplos que corren en **Jupyter Lab**, para que los puedan ver de manera correcta, hay que instalar el siguiente paquete:
``` 
pip install jupyterlab
```