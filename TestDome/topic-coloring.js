function newMessage(topicName) {
    const elements = document.querySelectorAll(`[data-topic-name=${topicName}]`);
    elements.forEach((element) => {
        element.style.background = "red";
    })
  }
  
  // Example case
  document.body.innerHTML = `<div>
    <p data-topic-name="discussion">General discussion</p>
    <p data-topic-name="bugs">Bugs</p>
    <p data-topic-name="animals">Animals</p>
  </div>`;
  newMessage("discussion");
  console.log(document.body.innerHTML);