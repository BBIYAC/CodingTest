// React is loaded and is available as React and ReactDOM
// imports should NOT be used
class ImageGallery extends React.Component {
  constructor(props) {
    super(props);
    this.state = { links: props.links };
  }

  remove = (link) => {
    this.setState((state) => ({
      links: state.links.filter((url) => url !== link)
    }));
  };

  render() {
    const links = this.state.links;
    
    return (
      <div>
        {links.map((link, index) => (
          <div key={index}>
            <div className="image">
              <img src={link} />
              <button className="remove" onClick={() => this.remove(link)}>
                X
              </button>
            </div>
          </div>
        ))}
      </div>
    );
  }
}

document.body.innerHTML = "<div id='root'> </div>";

const rootElement = document.getElementById("root");
const links = ["https://bit.ly/3lmYVna", "https://bit.ly/3flyaMj"];
ReactDOM.render(<ImageGallery links={ links } />,
                rootElement);
document.querySelectorAll('.remove')[0].click();
console.log(rootElement.innerHTML);