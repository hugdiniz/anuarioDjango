function detalharServidor(id) {

    //TODO: Ajax do para comunuicação
    $("#modalServidor").modal("show");
}

function detalharUorg(idComponente) {
    //TODO: Ajax do para comunuicação
    $(".ativo").addClass("naoAtivo");
    $(".ativo").removeClass("ativo");
    $("#"+idComponente).addClass("ativo");
   $("#"+idComponente).removeClass("naoAtivo");
}

$(document).ready(function () {
    $('label.tree-toggler').click(function () {
        $(this).parent().children('ul.tree').toggle(300);
    });
}); 