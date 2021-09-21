// Fonction to validate if the user input is an email adress

function ValidateForm() {
  eMail = document.getElementById('mailInput').value;
  userName = document.getElementById('userNameInput').value;
  pwd = document.getElementById('pwdInput').value;
  pwdConfirm = document.getElementById('pwdConfirmInput').value;

  if (eMail=='') {
    alert("Merci de rentrer une adresse mail !");
    return false;
  }

  if (userName='') {
    alert("Merci de rentrer un nom d'utilisateur !");
    return false;
  }

  if (pwd='' || pwd.length < 4 || pwd.length > 20 ) {
    alert("Merci de rentrer un mot de passe entre 4 et 20 caractères !");
    return false;
  }

  if (pwdConfirm='') {
    alert("Merci de confirmer votre mot de passe !");
    return false;
  }

  return true;
    
}