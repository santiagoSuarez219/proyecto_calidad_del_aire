# Preparacion de entorno de trabajo

## Instalacion de NodeJS
[Instalacion](https://github.com/nvm-sh/nvm#installing-and-updating)

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
```

Es posible, que necesites cerrar la terminal y abrirla de nuevo para poder ejecutar el siguiente comando:

```bash
nvm install lts
```

## Extensiones de VSCode
- Bracket Pair Color DLW
- Code Runner
- Error Lens
- JavaScriot ES6
- Node Require

# Tipos de datos 
## Primitivos
- number: indica un valor numérico, ya sea entero o flotante (con decimales).
- string: indica una cadena de caracteres, el valor está envuelto en comillas dobles " o simples '.
- boolean indica un valor lógico binario, es decir, los valores true o false.
- null: indica un valor nulo.
- undefined: indica un valor no definido.

Tipos no primitivos o de objeto

- function: indica una representación de función.
- object: indica una representación de objetos.

### Palabra reservada typeof

```javascript
// Tipos de datos primitivos
typeof 5  // 'number'
typeof "hola" // 'string'
typeof true  // 'boolean'
typeof null  // 'object'
typeof undefined // 'undefined'

// Tipos de datos de objeto 
typeof console.log  // 'function'
typeof {tipo: "objeto"} // 'object'
typeof [1,2,3,4]  // 'object'
```



