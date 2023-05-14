// The days of the week are: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
function getDayName(dateString) {
  // Write your code here
  const dayName = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  const date = new Date(dateString);
  return dayName[date.getDay()];
}


function main() {
  const d = +(readLine());
  
  for (let i = 0; i < d; i++) {
      const date = readLine();
      
      console.log(getDayName(date));
  }
}