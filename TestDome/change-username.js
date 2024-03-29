// React is loaded and is available as React and ReactDOM
// imports should NOT be used
class Username extends React.Component {
    state = { value: "" };
  
    changeValue(value) {
      this.setState({ value });
    }
  
    render() {
      const { value } = this.state;
      return <h1>{value}</h1>;
    }
  }
  
  function App() {
    const userNameRef = React.useRef();
    function clickHandler() {
      document.querySelector("h1").innerHTML = userNameRef.current.value;
    }
  
    return (
      <div>
        <button onClick={clickHandler}>Change Username</button>
        <input ref={userNameRef} type="text" />
        <Username />
      </div>
    );
  }
  
  document.body.innerHTML = "<div id='root'></div>";
  const rootElement = document.getElementById("root");
  ReactDOM.render(<App />, rootElement);
  
  document.querySelector("input").value = "John Doe";
  document.querySelector("button").click();
  setTimeout(() => console.log(document.getElementById("root").innerHTML));