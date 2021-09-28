/*
    Author : Thibault Cheneviere
    Date : 28/09/2021
*/

// Fonction to validate if the user input is an email adress

$(function () {
  $("#btnSignup").click(function () {
      var password = $("#pwdInput").val();
      var confirmPassword = $("#pwdConfirmInput").val();
      if (password != confirmPassword) {
          alert("Les mots de passes ne sont pas identiques.");
          return false;
      }
      if (password.length < 4 || password.length > 20) {
        alert("Merci de choisir un mot de passe entre 4 et 20 caractères.");
        return false;
      }
      return true;
  });
});