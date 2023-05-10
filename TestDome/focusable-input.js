// React is loaded and is available as React and ReactDOM
// imports should NOT be used
const FocusableInput = (props) => {
  // DOM에서 특정 값 참조하는 Hook
  const inputRef = React.useRef();

  React.useEffect(() => {
    if (props.shouldFocus) inputRef.current.focus();
  }, []);
  return <input ref={inputRef}/>;
};

document.body.innerHTML = "<div id='root' />";
ReactDOM.render(<FocusableInput shouldFocus={true} />, document.getElementById("root"));
setTimeout(() => console.log(document.getElementById("root").innerHTML));