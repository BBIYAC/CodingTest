// React is loaded and is available as React and ReactDOM
// imports should NOT be used
const Product = props => {
  const plus = (idx) => {
    props.onVote("+", idx);
};
  const minus = (idx) => {
    props.onVote("-", idx);
};
  return (
    <li>
    <span>{props.product.name}</span> - <span>votes: {props.product.votes}</span>
    <button onClick={() => plus(props.index)}>+</button>{" "}
    <button onClick={() => minus(props.index)}>-</button>
    </li>
  );
};

const GroceryApp = (props) => {
  let [products, setProducts] = React.useState(props.products);
  const onVote = (dir, index) => {
    const Products = [...products];
    
    if (dir === "+") {
    Products[index].votes = Products[index].votes + 1;
    setProducts(Products);
    } else {
    Products[index].votes = Products[index].votes - 1;
    setProducts(Products);
    }
  };

  return (
    <ul>
      {products.map((product, index) => (
        <Product key={index} onVote={onVote} index={index} product={product} />
      ))}
    </ul>
  );
}

document.body.innerHTML = "<div id='root'></div>";

ReactDOM.render(<GroceryApp
  products={[
    { name: "Oranges", votes: 0 },
    { name: "Bananas", votes: 0 }
  ]}
  />, document.getElementById('root'));

  let plusButton = document.querySelector("ul > li > button");
  if(plusButton) {
    plusButton.click();
  }
console.log(document.getElementById('root').outerHTML)