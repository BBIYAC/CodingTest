function ensure(value) {
  if (value === undefined) {
    throw new Error('value is undefined');
  }

  return value;
}

try {
  console.log(ensure());
} catch(err) {
  console.log(err);
}