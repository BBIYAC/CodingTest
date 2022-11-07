function showCustomers(customers, targetList) {
  customers.forEach((item) => {
    const li = document.createElement("li");
    const name = document.createElement("p");
    name.textContent = item.name;
    name.addEventListener("click", (e) => {
      const parent = e.target.parentElement;
      if (parent.children.length == 1) {
        const email = document.createElement("p");
        email.textContent = item.email;
        parent.appendChild(email);
      } else {
        parent.lastChild.remove();
      }
    });
    li.appendChild(name);
    targetList.appendChild(li);
  });
}

document.body.innerHTML = `
  <div>
  <ul id="customers">
  </ul>
  </div>
  `;
let customers = [{name: "John", email: "john@example.com"},
                {name: "Mary", email: "mary@example.com"}];
showCustomers(customers, document.getElementById("customers"));

let customerParagraph = document.querySelectorAll("li > p")[0];
if(customerParagraph) {
  customerParagraph.click();
}
console.log(document.body.innerHTML);