function detalharServidor(id) {

    json = $.getJSON('/anuario/pessoa/'+id+'/detail/', {}, function(json, textStatus) {
        $('#cargoServidor').text(json['cargo']);
        $('#salaServidor').text(json['sala']);
        $('#funcaoServidor').text(json['funcao']);
        $('#nomeServidor').text(json['nome']);
    });

    console.log(json);

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