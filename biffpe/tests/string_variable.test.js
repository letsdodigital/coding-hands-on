// testing 

const final_message = require('../string_variable');

test('Checking if string', () => {
  expect(final_message("John Doe", 38.5)).toBeDefined();
});