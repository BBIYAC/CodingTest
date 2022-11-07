function appendChildren(decorateDiv) {
//   var allDivs = [...document.getElementsByTagName("div")]; // getElementsByTagName는 요소 반환
  var allDivs = document.querySelectorAll("div"); // querySelectorAll은 배열 반환

  for (var i = 0; i < allDivs.length; i++) {
    var newDiv = document.createElement("div");
    decorateDiv(newDiv);
    allDivs[i].appendChild(newDiv);
  }
//   가독성을 위해서는 이렇게 사용함
//   allDivs.forEach((div) => {
//     const newDiv = document.createElement("div");
//     decorateDiv(newDiv);
//     div.appendChild(newDiv);
//   })
}

// Example case. 
document.body.innerHTML = `
  <div id="a">
    <div id="b">
    </div>
  </div>`;

appendChildren(function(div) {});
console.log(document.body.innerHTML);