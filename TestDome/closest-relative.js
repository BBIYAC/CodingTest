/**
 * @param {HTMLElement} parent The HTML element of the parent
 * @param {string} relativeName The name of relative to be searched
 * @return {HTMLElement} The HTML element of the closest relative
 */
function closestRelative(parent, relativeName) {
  const queue = [...parent.children];
  const tagName = relativeName.toUpperCase();
  let element;

  while (queue.length) {
    element = queue.shift();
    if (element.tagName === tagName) return element;
    if (!element.hasChildNodes()) { continue; }

    for (const childElement of element.children) {
    queue.push(childElement);
    }
  }
  return null;
}

// Example case
document.body.innerHTML = 
  '<James>' +
  '<Dave></Dave>' +
  '<Mike></Mike>' +
  '<Sarah></Sarah>' +
  '</James>';

const parent = document.getElementsByTagName('James')[0];
const relative = closestRelative(parent, 'Mike');
console.log(relative && relative.tagName); // prints MIKE