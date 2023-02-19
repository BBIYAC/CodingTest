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

// other solution
function createCheckDigit(membershipId) {
  // Write the code that goes here.
  let str = membershipId;
  while ( str.length !== 1 ){
    str = str
      .split('')
      .reduce((accumulator, current)=>accumulator + parseInt(current), 0)
      .toString()
  }
  return str
}

console.log(createCheckDigit("55555"));