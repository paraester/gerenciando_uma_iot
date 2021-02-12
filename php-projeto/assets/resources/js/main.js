function inserirResposta() {
    var htmlInner = " Teste aqui";
    htmlInner += ' dede';
    document.getElementById("grid").innerHTML = htmlInner
}

$(function () {
    $("#apagartudo").on("click", function () {
        $.post("apagar-tudo.php"); //a ideia é executar e colocar uma resposta na função acima
        inserirResposta();
    });
});
$(function () {
    $("#acendertudo").on("click", function () {
        $.post("acender-tudo.php");
    });
});
$(function () {
    $("#escolherqualacender").on("click", function () {
        $.post("escolher-qual-acender.php");
    });
});
$(function () {
    $("#quaisacesas").on("click", function () {
        $.post("quais-acesas.php");
    });
});