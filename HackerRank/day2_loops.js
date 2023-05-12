function vowelsAndConsonants(s) {
  const vowels = [];
  const consonants = [];
  
  s.split('').forEach((char) => {
      if ('aeiou'.includes(char)) vowels.push(char);
      else consonants.push(char);
  })
  
  vowels.forEach(char => console.log(char));
  consonants.forEach(char => console.log(char));
}