const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

function habilitar() {
  pw = document.getElementById("pw");
  ckpw = document.getElementById("check-pw");
  username = document.getElementById("username");
  email = document.getElementById("email");
  boton = document.getElementById("btnReg");

  let flag = true;
  // Validar campos vacios
  if (pw.value.length == 0 || username.value.length == 0 || email.value.length == 0 ) {
    document.getElementById("pTipd").innerHTML = "*     Debe llenar todos los campos";
    flag = true;
  } else {
    document.getElementById("pTipd").innerHTML = "";
    flag = false;
  }


  // Validar contraseñas
  if (pw.value != ckpw.value ) {
    document.getElementById("pPass").innerHTML = "*     Las contraseñas no coniciden";
    flag = true;
  } else{
    if (pw.value.length == 0) {
      flag = true;
    } else {
      document.getElementById("pPass").innerHTML = "";
      flag = false;
    }
    document.getElementById("pPass").innerHTML = "";
  }

  boton.disabled = flag;
}
