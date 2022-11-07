function createCheckDigit(membershipId) {
  let ids = Array.from(membershipId).map(Number);
  let sum;

  while (1) {
    sum = ids.reduce((accumulator, current) => accumulator + current);
    if (String(sum).length === 1) break;
    ids = Array.from(String(sum)).map(Number);
  }

  return sum;
}

console.log(createCheckDigit("55555"));