function edit_task(id) {
    var Formulario = document.getElementById('formulario_edit');  
    Formulario.action =  "edit/"+id;
}

function delete_task(id) {
    var Formulario = document.getElementById('formulario_delete');  
    Formulario.action =  "delete/"+id;
}