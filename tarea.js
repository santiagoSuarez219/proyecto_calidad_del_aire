function obtenerMaximo(num1, num2, num3) {
  var maximo = num1;
  
  if (num2 > maximo) {
    maximo = num2;
  }
  
  if (num3 > maximo) {
    maximo = num3;
  }
  
  return maximo;
}
