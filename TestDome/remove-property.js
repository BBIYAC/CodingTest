function removeProperty(obj, prop) {
  if (prop in obj) {
    delete obj[prop];
    return true;
  }
  return false;
}