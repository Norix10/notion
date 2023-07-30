function Delete_note(){
    const selected_notes = document.querySelectorAll(".note-select:checked")
    let ids = []
    selected_notes.forEach(element => {
        ids.push(element.dataset.id)
    });
    console.log(ids)
    if (ids.length === 0){
        return
    }
    var numberJSON = JSON.stringify(ids)
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const url = "/work-page/note_delete"
    let xhr = new XMLHttpRequest()
    xhr.open('POST', url, true)
    xhr.setRequestHeader("X-CSRFToken", csrftoken)
    xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')
    xhr.send(numberJSON);
    xhr.onload = function () {
        if(xhr.status === 201) {
            console.log("Post successfully created!") 
        }
    }
    location.reload()
}

