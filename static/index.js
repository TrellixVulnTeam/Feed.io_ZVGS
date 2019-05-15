// index.js

// dom elements

let loginButton = document.getElementById('login_button')
let inputPass = document.getElementById('inputPassword')
let inputEmail = document.getElementById('inputEmail')

// dom methods



loginButton.onclick = () => {
    let data = {
        email:inputEmail.value,
        password:inputPass.value
    }
    $.post( "/api/login_post_db", {
        canvas_data: JSON.stringify(data)
      }, function(err, req, resp){
        console.log(resp["responseJSON"] ["d"])
      });
}