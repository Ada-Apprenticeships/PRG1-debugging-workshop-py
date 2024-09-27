function convertFromPenceToPounds(pence) {
  const pounds = pence / 100;
  return `£${Math.round(pounds)}`; // Format to two decimal places
}

convertFromPenceToPounds(1299); // should return "£12.99"
