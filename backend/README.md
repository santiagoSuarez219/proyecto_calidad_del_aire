# Creacion del proyecto

1. Crear carpeta del proyecto
2. Iniciar un proyecto de nodejs con el comando 
```bash
npm init
```
3. Iniciar el repositorio de git con el comando 
```bash
git init
```
4. Crear el archivo .gitignore y agregar los archivos que no se quieren subir al repositorio
5. Crear la carpeta src y dentro de ella el archivo index.js
6. Modificar el archivo package.json para agregar los script de start
```json
"scripts": {
    "dev": "nodemon src/index.js",
    "start": "node src/index.js",
  },
```
7. Instalar las dependencias necesarias para el proyecto
```bash
npm i nodemon express
```

8. Para correr el programa utilice
```bash
npm run dev
```

# Servidor HTTP con Express JS
1. Instalar Express
```bash
npm i express
```
2. En el archivo src/index.js implemente el siguiente codigo

```javascript
const express = require('express');
const app = express();
const port = 3000;

app.get('/',(req,res) =>{
  res.send('Hello World');
});

app.get('/otra-ruta',(req,res) =>{
  res.json({
    "sensor":"SCD40",
    "temperatura": 25.5
  });
});

app.get('/respuesta-html',(req,res) =>{
  res.send('<h1>Esta es una respuesta en HTML</h1>');
});

app.listen(port, () => {
  console.log('Mi port' + port);
});
```

NOTA: Para ver mejor los JSON en el navegador puede instalar la extension JSONViewer

# Metodo GET
## Parametros de ruta
```javascript
app.get('/products',(req,res) =>{
  res.json([
    {
      name: 'Producto 1',
      price: 1000
    },
    {
      name: 'Producto 2',
      price: 2000
    }
  ]);
});

app.get('/products/:id',(req,res) =>{
  const { id } = req.params;
  res.json({
    id,
    name: 'Producto 1',
    price: 1000
  });
});

app.get('/categories/:category_id/products/:product_id',(req,res) =>{
  const { category_id, product_id } = req.params;
  res.json({
    category_id,
    product_id
  });
})
```

## Parametros Query

![Parametros Query](https://github.com/santiagoSuarez219/backend_node_js_API_REST#get-par%C3%A1metros-query)

```javascript
app.get('/users',(req,res) =>{
  const { limit, offset } = req.query;
  if (limit && offset) {
    res.json({
      limit,
      offset
    });
  } else {
    res.send('No hay parametros');
  }
});
```

# Generar data fake
1. Instalar faker
```bash
npm i @faker-js/faker
```

2. Importar faker
```javascript
const { faker } = require('@faker-js/faker');
(...)
app.get('/products',(req,res) =>{
  const products = [];
  const {size} = req.query;
  const limit = size || 10;
  for (let i = 0; i < limit; i++) {
    products.push({
      name: faker.commerce.productName(),
      price: parseInt(faker.commerce.price(),10),
      image: faker.image.imageUrl()
    });
  }
  res.json(products);
});
```










