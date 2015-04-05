function detalharServidor(id) {

    json = $.getJSON('/anuario/pessoa/'+id+'/detail/', {}, function(json, textStatus) {
        $('#cargoServidor').text(json['cargo']);
        $('#salaServidor').text(json['salas']);
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


// funcoes chamadas mostrar os modais dos forms
function showFormUorg(uorgId){
    if(uorgId)
        alert('Form de Edicao Uorg : ' + uorgId);
    else
        alert('Form de Edicao Uorg');
}
function showFormPessoa(pessoaId) {
    if(pessoaId)
        alert('Form de Edicao Pessoa: '+pessoaId);
    else
        alert('Form de Edicao Pessoa');
}
function showFormSala(salaId) {
    if(salaId)
        alert('Form Edicao Sala : ' + salaId);
    else
        alert('Form Edicao Sala');
}
function showFormLotacao(lotacaoId) {
    if(lotacaoId)
        alert('Form edicao Lotacao - Lotacao: ' + lotacaoId);
    else
        alert('Form edicao Lotacao');

}

function serializeForm(formJson) {
    json = [];
    for (var i = 0; i < formJson.length; i++) {
        json[formJson[i].name] = formJson[i].value;
    };
    return json;
}


// funcoes chamadas para salvar as alteracoes feitas no form
$('#form-test').submit(function(event) {
    json = serializeForm(event.target);
    console.log(json);
    return false;
});

$('#form-manter-uorg').submit(function(event) {
    json = serializeForm(event.target);
    console.log(json);
    return false; 
});

$('#form-manter-funcao').submit(function(event) {
    json = serializeForm(event.target);
    console.log(json);
    return false; 
});

$('#form-manter-servidor').submit(function(event) {
    json = serializeForm(event.target);
    console.log(json);
    return false; 
});

function submitFormPessoa() {}
function submitFormSala() {}
function submitFormLotacao() {}
