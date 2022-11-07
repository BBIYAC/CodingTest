function ensure(value) {
  if (value) return value;
  else throw Error;
}

try {
  console.log(ensure());
} catch(err) {
  console.log(err);
}