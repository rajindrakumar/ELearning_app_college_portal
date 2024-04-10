// User button function

function selectButton(buttonNumber) {
  // Remove 'selected' class from all buttons
  const buttons = document.querySelectorAll('.button');
  buttons.forEach(button => {
      button.classList.remove('selected');
  });

  // Add 'selected' class to the clicked button
  const selectedButton = document.querySelector(`.button:nth-child(${buttonNumber})`);
  selectedButton.classList.add('selected');
}