const SecurityContext = React.createContext({ username: "", permissions: [] });

const ControlsComponent = (props) => {
  return (
    <SecurityContext.Provider value={{ username: props.username }}>
      <LogoutWrapper></LogoutWrapper>
    </SecurityContext.Provider>
  );
};

const LogoutWrapper = (props) => {
  var context = React.useContext(SecurityContext);
  
  return (
    <div>
      <p>{context.username}</p>
      <button>Click here to logout</button>
    </div>
  );
};

/*
context.username in the LogoutWrapper will have "James" as its value.
The value of context.username will be "" when LogoutWrapper is not a descendant of SecurityContext.Provider.
ControlsComponent can declare multiple instances of SecurityContext.Provider.
*/