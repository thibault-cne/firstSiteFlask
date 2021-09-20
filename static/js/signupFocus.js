function onFocusPwd() {
	document.getElementById("pwd").style.display = "none";
}

function onFocusOutPwd() {
	if (document.getElementById("pwdInput").value == "") {
		document.getElementById("pwd").style.display = "block";
	}
}

function onFocusMail() {
	document.getElementById("mail").style.display = "none";
}

function onFocusOutMail() {
	if (document.getElementById("mailInput").value == "") {
		document.getElementById("mail").style.display = "block";
	}
}

function onFocusUser() {
	document.getElementById("userName").style.display = "none";
}

function onFocusOutUser() {
	if (document.getElementById("userNameInput").value == "") {
		document.getElementById("userName").style.display = "block";
	}
}

function onFocusPwdConfirm() {
	document.getElementById("pwdConfirm").style.display = "none";
}

function onFocusOutPwdConfirm() {
	if (document.getElementById("pwdConfirmInput").value == "") {
		document.getElementById("pwdConfirm").style.display = "block";
	}
}