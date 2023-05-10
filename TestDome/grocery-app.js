// React is loaded and is available as React and ReactDOM
// imports should NOT be used
const Product = props => {
  // plus 함수
  const plus = () => {
    props.onVote("+", props.index);
};
  // minus 함수
  const minus = () => {
    props.onVote("-", props.index);
};
  return (
    <li>
    <span>{props.name}</span> - <span>votes: {props.votes}</span>
    <button onClick={plus}>+</button>{" "}
    <button onClick={minus}>-</button>
    </li>
  );
};

const GroceryApp = (props) => {
  let [products, setProducts] = React.useState(props.products);
  const onVote = (dir, index) => {
    const Products = [...products];
    
    if (dir === "+") Products[index].votes += 1;
    else Products[index].votes -=  1;

    setProducts(Products);
  };

  return (
    <ul>
      {products.map((product, index) => (
        <Product key={index} onVote={onVote} index={index} name={product.name} votes={product.name} />
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