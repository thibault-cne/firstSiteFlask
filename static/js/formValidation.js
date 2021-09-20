// Fonction to validate if the user input is an email adress


function ValidateEmail(input) {
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (input.value.match(validRegex)) {
      alert("Valid email address!");
      document.form.eMail.focus();
      return true;
    } else {
      alert("Votre adresse mail est invalide !\nMerci de réessayer avec une adresse valide.");
      document.form.eMail.focus();
      return false;
    }
  }