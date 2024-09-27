function isValidTriangle(a, b, c) {
  // Check if all sides are positive
  if (a <= 0 || b <= 0 || c <= 0) {
    return false;
  }

  // Check the triangle inequality
  if (a + b > c && b + c > a && c + a > b) {
    return true;
  }

  return false;
}

// Test cases
console.log(isValidTriangle(3, 4, 5)); // Should return true
console.log(isValidTriangle(1, 1, 3)); // Should return false
console.log(isValidTriangle(5, 10, 25)); // Should return false
console.log(isValidTriangle(-1, 2, 3)); // Should return false
