function setup() {
  const elements = document.getElementsByClassName("remove");
    for (let i = 0; i < elements.length; i++) {
        elements[i].addEventListener('click', (e) => {
            e.preventDefault();
            e.target.closest('div.image').remove();
        });
    }
}
  
// Example case. 
document.body.innerHTML = `
<div class="image">
  <img src="https://bit.ly/3lmYVna" alt="First">
  <button class="remove">X</button>
</div>
<div class="image">
  <img src="https://bit.ly/3flyaMj" alt="Second">
  <button class="remove">X</button>
</div>`;

setup();

document.getElementsByClassName("remove")[0].click();
console.log(document.body.innerHTML);