/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
  try {
      const reverseResult = s.split('').reverse().join('');
      console.log(reverseResult);
  } catch(e) {
      console.log(e.message);
      console.log(s);
  }
}