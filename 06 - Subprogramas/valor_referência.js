function porValor(x) {
    x += 10;
    console.log("Dentro da função (x):", x);
}

function porReferencia(arr) {
    arr.push(99);
    console.log("Dentro da função (arr):", arr);
}

let a = 5;
console.log("Antes da função (a):", a);
porValor(a);
console.log("Depois da função (a):", a);

let b = [1, 2, 3];
console.log("Antes da função (b):", b);
porReferencia(b);
console.log("Depois da função (b):", b);
