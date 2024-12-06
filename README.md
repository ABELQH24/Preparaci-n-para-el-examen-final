Para ejecutar el proyecto:
```bash
python -m venv .venv
source .venv/Scripts/activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt 

```
Fase de desarrollo-instalaciones:
Dentro de bookscrape se ejecutó los siguientes comandos:
```bash
scrapy startproject bookscrape
cd bookscrape/bookscrape/spiders/ ejecutar -> scrapy genspider bookspyder quotes.toscrape.com
dentro de spider -> pip install ipython
```

Sobrescribir el archivo:
```bash
scrapy crawl bookspyder -O data_citas.csv
scrapy crawl bookspyder -O data_citas.json
```

**Preparación para el examen final:**
Diseñar un spider en Scrapy para el sitio https://quotes.toscrape.com. El objetivo es: 

Extraer las citas que tengan el tag "inspirational" , con sus respectivos autores. 
Guardar los datos en un archivo JSON llamado citas.json.
Subir el proyecto correspondiente empaquetado (zip, rar)