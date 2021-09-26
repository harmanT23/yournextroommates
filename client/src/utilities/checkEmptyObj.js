export function checkEmptyObj(obj) {
  // Check if an object is empty
  for (var i in obj) return false;
  return true;
}
