function endangeredSpecies(continent, species) {
  const dataContinent = document.querySelector(`div [data-continent="${continent}"]`);
  const dataSpecies = dataContinent.querySelector(`[data-species="${species}"]`);
  return dataSpecies.innerHTML;
}

// Example case
document.body.innerHTML =
  `<div>
    <ul data-continent="North America">
      <li data-species="California condor">Critically Endangered</li>
      <li data-species="American bison">Near Threatened</li>
    </ul>
    <ul data-continent="Europe">
      <li data-species="Cave bear">Extinct</li>
    </ul>
  </div>`;

console.log(endangeredSpecies('North America', 'American bison')); // should print 'Near Threatened'