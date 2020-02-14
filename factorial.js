function factorial(n) {
  if (n == 1) return 1;
  return n * factorial(n - 1);
}

const n = 1000;

const inicio = new Date().getTime();
result = factorial(n);
const final = new Date().getTime();
console.log(
  `Js caculo el facotorial de ${n} en: ${final - inicio} milisegundos`
);
