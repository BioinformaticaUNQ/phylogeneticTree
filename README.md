# Generar arbol filogenetico

## Requerimientos

* Se necesita tener docker instalado.

## Como se usa

* Poner archivo Fasta (alineado o no) en la carpeta data
* Ejecutar `./phylogeneticTree.sh --name {nombreDelArchivoFasta} --bootstrap {numero}`
* Al terminar dentro de la carpeta data se encontrara una carpeta `output` con el `.treefile` y el log de iqtree.
* Ir a la pagina https://hurrell-y-mottesi.github.io/phylogenetic-map
* cargar el archivo `.treefile` y un archivo de locación con el siguiente formato:

```json
[
    {
        "seq": "header de la sequencia del archivo fasta",
        "name": "el nombre de la ciudad, EJ: Buenos Aires, Argentina"
    },
    ...
]
```
