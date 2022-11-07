function setup() {
  let btnList = document.querySelectorAll('button')

  for (const button of btnList) {
    button.addEventListener('click', handleClick)
  }
}

function handleClick(e) {
  const parent = e.target.parentElement;
  const isUp = e.target.textContent === 'Up!';
  const isDown = e.target.textContent === 'Down!';
  const isFirst = !parent.previousElementSibling;
  const isLast = !parent.nextElementSibling;

  if (isUp && !isFirst) {
    parent.parentNode.insertBefore(parent, parent.previousElementSibling);
  }
    
  if (isDown && !isLast) {
    parent.parentNode.insertBefore(parent.nextElementSibling, parent);
  }
}

// Example case
document.body.innerHTML = `<ol>
<li><button>Up!</button>Taco<button>Down!</button></li>
<li><button>Up!</button>Pizza<button>Down!</button></li>
<li><button>Up!</button>Eggs<button>Down!</button></li>
</ol>`;

setup();
document.getElementsByTagName('button')[2].click();

console.log(document.body.innerHTML);