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

# Variables
En JS, se pueden declarar variables con var, let y const.

## var
- Alcance de función: Las variables declaradas con var tienen alcance de función, lo que significa que su ámbito está limitado al bloque de función más cercano.
- Hoisting: Las declaraciones de variables con var se elevan (hoisting) al comienzo del ámbito en el que se declaran. Esto significa que se pueden acceder a las variables antes de que se declaren en el código, aunque su valor será undefined.
- Reasignación y redeclaración: Las variables declaradas con var pueden ser reasignadas y redeclaradas en el mismo ámbito sin generar errores

## let
- Alcance de bloque: Las variables declaradas con let tienen alcance de bloque, lo que significa que su ámbito está limitado al bloque más cercano, ya sea un bloque de función, un bloque if, un bucle for, entre otros.
- No hoisting: A diferencia de var, las declaraciones de variables con let no se elevan (hoisting), por lo que no se pueden acceder a ellas antes de su declaración.
- Reasignación: Las variables declaradas con let pueden ser reasignadas dentro del mismo ámbito, lo que significa que se les puede asignar un nuevo valor.
- No redeclaración: No se puede redeclarar una variable con let en el mismo ámbito. Si se intenta declarar una variable con el mismo nombre en el mismo ámbito, se producirá un error.

## const
- Alcance de bloque: Las variables declaradas con const tienen alcance de bloque, lo que significa que su ámbito está limitado al bloque más cercano, ya sea un bloque de función, un bloque if, un bucle for, entre otros.
- Asignación constante: Las variables declaradas con const deben recibir un valor en el momento de su declaración y no pueden ser reasignadas posteriormente. El valor asignado a una variable const es constante y no puede ser modificado.
- No redeclaración: No se puede redeclarar una variable con const en el mismo ámbito. Si se intenta declarar una variable con el mismo nombre en el mismo ámbito, se producirá un error.

**En general, se recomienda utilizar let en lugar de var en nuevos proyectos, ya que let ofrece un alcance más preciso y evita problemas relacionados con el hoisting. Por otro lado, const se utiliza para declarar variables cuyos valores no deben cambiar a lo largo del programa.**
s
