function pipeline(...funcs) {
    return (arg) => {
      funcs.forEach(func => arg = func(arg));
      return arg;
    }
  }
  
  let fun = pipeline(x => x * 3, x => x + 1, x => x / 2);
  console.log(fun(3)); // Should print 5