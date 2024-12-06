Para ejecutar el proyecto:
```bash
python -m venv .venv
source .venv/Scripts/activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt 
scrapy startproject bookscrape
```
Fase de desarrollo-instalaciones:
Dentro de bookscrape se ejecutó los siguientes comandos:
```bash
cd bookscrape/bookscrape/spiders/ ejecutar -> scrapy genspider bookspyder quotes.toscrape.com
dentro de spider -> pip install ipython
```

**Preparación para el examen final:**
Diseñar un spider en Scrapy para el sitio https://quotes.toscrape.com. El objetivo es: 

Extraer las citas que tengan el tag "inspirational" , con sus respectivos autores. 
Guardar los datos en un archivo JSON llamado citas.json.
Subir el proyecto correspondiente empaquetado (zip, rar)