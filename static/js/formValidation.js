// Fonction to validate if the user input is an email adress

function validateForm() {
  pwd = document.getElementById('pwdInput').value;
  pwdConfirm = document.getElementById('pwdConfirmInput').value;


  if (pwd='' || pwd.length < 4 || pwd.length > 20 ) {
    alert("Merci de rentrer un mot de passe entre 4 et 20 caractères !");
    return false;
  }

  if (pwdConfirm!=pwd) {
    alert("Les deux mots de passe ne sont pas identiques");
    return false;
  }

  return true;
    
}