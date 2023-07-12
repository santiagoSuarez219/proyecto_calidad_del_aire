function factorial(numero) {
    if (numero === 0 || numero === 1) {
      return 1;
    } else {
      return numero * factorial(numero - 1);
    }
  }
  
  let numero = 5;
  let resultado = factorial(numero);
  console.log("El factorial de " + numero + " es: " + resultado);
  