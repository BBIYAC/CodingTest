/*
 * Complete the Rectangle function
 */
function Rectangle(a, b) {
  return {
      length: a,
      width: b,
      perimeter: 2 * (a + b),
      area: a * b
  }
}

function main() {
  const a = +(readLine());
  const b = +(readLine());
  
  const rec = new Rectangle(a, b);
  
  console.log(rec.length);
  console.log(rec.width);
  console.log(rec.perimeter);
  console.log(rec.area);
}