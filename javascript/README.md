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

# Funciones
## Funciones declarativas
```javascript
function saludar(nombre) {
  return `Hola ${nombre}`;
}

saludar('Juan'); // 'Hola Juan'
```

## Funciones de expresión o anonimas
```javascript
const saludar = function(nombre) {
  return `Hola ${nombre}`;
}

saludar('Juan'); // 'Hola Juan'
```

# Operadores
## Operadores aritméticos
```javascript
// Suma
2 + 3 // 5
// Resta
5 - 3 // 2
// Multiplicación
4 * 2 // 8
// División
6 / 2 // 3
//Residuo
21 % 5 // 1
```

## Operadores de asignación
```javascript
// Asignación
let a = 1;
// Asignación de adición
a += 2; // a = a + 2
// Asignación de sustracción
a -= 2; // a = a - 2
// Asignación de multiplicación
a *= 2; // a = a * 2
// Asignación de división
a /= 2; // a = a / 2
// Asignación de residuo
a %= 2; // a = a % 2
```

## Operadores de comparación
```javascript
//Igualdad
""3"" == 3 // true
3 == 3 // true
// Igualdad estricta
""3"" === 3 // false
3 === 3 // true
// Desigualdad
2 != 2 // false
// Estrictamente desigual
2 !== 2 // false
// Mayor que    
2 > 2 // false
// Mayor o igual que
2 >= 2 // true
// Menor que
2 < 2 // false
// Menor o igual que
2 <= 2 // true
```

## Operadores lógicos
```javascript
// AND
true && true // true
true && false // false
false && true // false
false && false // false
// OR
true || true // true
true || false // true
false || true // true
false || false // false
// NOT
!true // false
!false // true
```

## Concatenacion
```javascript
"Hola " + "mundo" // "Hola mundo"
"Hola " + 3 // "Hola 3"
```

# Condicionales
## if, else, else if
```javascript
if (edad >= 18){
    console.log("Puedes conducir")
}
```

```javascript
if (edad >= 18){
    console.log("Puedes conducir")
} else {
    console.log("No puedes conducir")
}
```

```javascript
if (edad >= 18){
    console.log("Puedes conducir")
} else if (edad < 16) {
    console.log("No puedes conducir")
} else {
    console.log("Puedes sacar tu permiso")
}
```

```javascript
function calcularDescuento(articulos, precio) {
  var precioFinal

  if (articulos <= 5) {
    //Hasta 5 artículos
    precioFinal = precio * (1 - 0.1)
  } else if (articulos > 5 && articulos <= 10) {
    //De 6 a 10 artículos
    precioFinal = precio * (1 - 0.15)
  } else {
    //De 10 artículos en adelante
    precioFinal = precio * (1 - 0.2)
  }

  return precioFinal
}

calcularDescuento(4, 10) // 9
calcularDescuento(8, 20) // 17
calcularDescuento(15, 50) // 40
```

## Operador ternario
```javascript
var edad = 18
var mensaje = edad >= 18 ? "Eres mayor de edad" : "Eres menor de edad"
console.log(mensaje) // "Eres mayor de edad"
```

## Switch
```javascript
function semaforo(color) {
  switch (color) {
    case "verde": {
      console.log("¡Sigue!")
      break
    }
    case "amarillo": {
      console.log("¡Detente!")
      break
    }
    case "rojo": {
      console.log("¡No puedes avanzar!")
      break
    }
    default: {
      console.log("¡No reconozco ese color! :(")
    }
  }
}

semaforo("verde") //'¡Sigue!'
semaforo("amarillo") //'¡Detente!'
semaforo("rojo") //'¡No puedes avanzar!'
semaforo("morado") //'¡No reconozco ese color! :('
```

# Ciclos
## for
```javascript
for (var i = 0; i < 10; i++) {
  console.log(i)
}
```

## while
```javascript
var i = 0
while (i < 10) {
  console.log(i)
  i++
}
```

## do while
```javascript
var i = 0
do {
  console.log(i)
  i++
} while (i < 10)
```

## break
```javascript
for (var i = 0; i < 10; i++) {
  if (i === 5) {
    break
  }
  console.log(i)
}
```

## continue
```javascript
for (var i = 0; i < 10; i++) {
  if (i === 5) {
    continue
  }
  console.log(i)
}
```

# Arrays
## Creación de arrays
```javascript
var numeros = [1, 2, 3, 4, 5]
var nombres = ["Juan", "Pedro", "María", "Diana"]
var mixto = [1, "Pedro", true, null, undefined]
```

## Acceso a elementos
```javascript
var numeros = [1, 2, 3, 4, 5]
console.log(numeros[0]) // 1
console.log(numeros[1]) // 2
console.log(numeros[2]) // 3
```

## Modificación de elementos
```javascript
var numeros = [1, 2, 3, 4, 5]
numeros[0] = 10
console.log(numeros) // [10, 2, 3, 4, 5]
```

## Métodos
```javascript
var numeros = [1, 2, 3, 4, 5]
numeros.push(6)
console.log(numeros) // [1, 2, 3, 4, 5, 6]
numeros.pop()
console.log(numeros) // [1, 2, 3, 4, 5]
numeros.unshift(0)
console.log(numeros) // [0, 1, 2, 3, 4, 5]
numeros.shift()
console.log(numeros) // [1, 2, 3, 4, 5]
```

## Recorrrer Arrays con Metodos
```javascript
var articulos = [
  { nombre: "Bici", costo: 3000 },
  { nombre: "TV", costo: 2500 },
  { nombre: "Libro", costo: 320 },
  { nombre: "Celular", costo: 10000 },
  { nombre: "Laptop", costo: 20000 },
  { nombre: "Teclado", costo: 500 },
  { nombre: "Audifonos", costo: 1700 },
];

var articulosFiltrados = articulos.filter(function (articulo) {
  return articulo.costo <= 500;
});

var nombreArticulos = articulos.map(function (articulo) {
  return articulo.nombre;
});

var encuentraArticulo = articulos.find(function (articulo) {
  return articulo.nombre === "Laptop";
});

articulos.forEach(function (articulo) {
  console.log(articulo.nombre);
});

articulos.some(function (articulo) {
  return articulo.costo <= 700;
});
```




# Objetos en JavaScript
## Creación de objetos
```javascript
var persona = {
  nombre: "Juan",
  edad: 18,
  soltero: true,
  hobbies: ["Fútbol", "Videojuegos", "Leer"],
  direccion: {
    calle: "Av. Siempre viva",
    numero: 123,
    colonia: "Centro",
    ciudad: "Springfield",
    estado: "Springfield",
    pais: "EUA",
  },
}
```

## Acceso a propiedades
```javascript
console.log(persona.nombre) // "Juan"
console.log(persona.edad) // 18
```

## Modificación de propiedades
```javascript
persona.nombre = "Pedro"
console.log(persona.nombre) // "Pedro"
```

## Métodos
```javascript
var persona = {
  nombre: "Juan",
  edad: 18,
  soltero: true,
  hobbies: ["Fútbol", "Videojuegos", "Leer"],
  direccion: {
    calle: "Av. Siempre viva",
    numero: 123,
    colonia: "Centro",
    ciudad: "Springfield",
    estado: "Springfield",
    pais: "EUA",
  },
  saludar: function () {
    console.log("Hola, mi nombre es " + this.nombre)
  },
}

persona.saludar() // "Hola, mi nombre es Juan"
```

## Constructor
```javascript
function Persona(nombre, edad, soltero, hobbies, direccion) {
  this.nombre = nombre
  this.edad = edad
  this.soltero = soltero
  this.hobbies = hobbies
  this.direccion = direccion
  this.saludar = function () {
    console.log("Hola, mi nombre es " + this.nombre)
  }
}

var persona1 = new Persona(
  "Juan",
  18,
  true,
  ["Fútbol", "Videojuegos", "Leer"],
  {
    calle: "Av. Siempre viva",
    numero: 123,
    colonia: "Centro",
    ciudad: "Springfield",
    estado: "Springfield",
    pais: "EUA",
  }
)

var persona2 = new Persona(
  "Pedro",
  20,
  false,
  ["Fútbol", "Videojuegos", "Leer"],
  {
    calle: "Av. Siempre viva",
    numero: 123,
    colonia: "Centro",
    ciudad: "Springfield",
    estado: "Springfield",
    pais: "EUA",
  }
)

persona1.saludar() // "Hola, mi nombre es Juan"
persona2.saludar() // "Hola, mi nombre es Pedro"
```
















