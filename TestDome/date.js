function formatDate(userDate) {
  const [month, day, year] = userDate.split('/');
  let date = year;

  if (Number(month) < 10) date += '0';
  date += month;

  if (Number(day) < 10) date += '0';
  date += day;

  return date;
}

console.log(formatDate("12/31/2014"));