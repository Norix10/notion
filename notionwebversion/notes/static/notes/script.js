function ListOne(){
    let list = document.getElementsByClassName('list-one')[0]
    list.classList.toggle('unvisible');
}

function Delete_note(){
    console.log("+")
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const url = "/work-page/note_delete"
    let xhr = new XMLHttpRequest()
    xhr.open('POST', url, true)
    xhr.setRequestHeader("X-CSRFToken", csrftoken)
    xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')
    xhr.send();
    xhr.onload = function () {
        if(xhr.status === 201) {
            console.log("Post successfully created!") 
        }
    }
    location.reload()
}