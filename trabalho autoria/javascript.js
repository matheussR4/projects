let questao1=document.querySelector(".questao1");
let questao2=document.querySelector(".questao2");
let questao3=document.querySelector(".questao3");
let questao4=document.querySelector(".questao4");
let questao5=document.querySelector(".questao5");
let btnBuscar=document.querySelector("#buscar");
let cmbBusca=document.querySelector("#selecionaQuestao");


questao1.classList.add('invisivel');
questao2.classList.add('invisivel');
questao3.classList.add('invisivel');
questao4.classList.add('invisivel');
questao5.classList.add('invisivel');

btnBuscar.addEventListener('click',function(event){
    questao1.classList.add('invisivel');
    questao2.classList.add('invisivel');
    questao3.classList.add('invisivel');
    questao4.classList.add('invisivel');
    questao5.classList.add('invisivel');
    questao1.classList.remove('aparecer');
    questao2.classList.remove('aparecer');
    questao3.classList.remove('aparecer');
    questao4.classList.remove('aparecer');
    questao5.classList.remove('aparecer');

    event.preventDefault();
    if(cmbBusca.value==1){
        questao1.classList.remove('invisivel');
        questao1.classList.add('aparecer');
        
    }
    if(cmbBusca.value==2){
        questao2.classList.remove('invisivel');
        questao2.classList.add('aparecer');
    }
    if(cmbBusca.value==3){
        questao3.classList.remove('invisivel');
        questao3.classList.add('aparecer');
    }
    if(cmbBusca.value==4){
        questao4.classList.remove('invisivel');
        questao4.classList.add('aparecer');
    }
    if(cmbBusca.value==5){
        questao5.classList.remove('invisivel');
        questao5.classList.add('aparecer');
    }
})



let body = document.querySelector('body');
let codigoinserido = document.querySelector('#codigo');
let form = document.querySelector('.questao1 form');
let quantidadeinserida = document.querySelector('#quantidadeInserida');
/* let linhas=document.querySelectorAll('tr'); *//*
let campos=document.querySelectorAll('tr td'); */
let pValor = document.createElement('div');
body.appendChild(pValor);
form.addEventListener('submit', function (event) {
    pValor.classList.remove('pValor');
    event.preventDefault();
    /* console.log(codigoinserido.value); */
    /* for(let i=0; i<linhas.length;i++){
        let linha=linhas[i];
        let codigo=linha.querySelector('td').textContent;
        console.log(codigo);
    } */
    questao1.appendChild(pValor);
    pValor.classList.add('pValor');
    pValor.classList.add('surgir');
    let valor = (recebeCodigo() * quantidadeinserida.value);
    pValor.textContent = 'Valor: R$' + valor.toFixed(2);
    /* pValor.style = 'width:150px;height:30px;margin:50px auto;font-size:20px;background-color:white;border:5px solid #1e554f;border-radius:3px;color:black;text-align:center; animation-name:surgir; animation-duration:2s;'; */
    /* pValor.style.animation = 'surgir 2s'; */
    /*  console.log(linhas.children); */
});

function recebeCodigo() {
    switch (codigoinserido.value) {
        case '100': return 1.20;
        case '101': return 1.30;
        case '102': return 1.50;
        case '103': return 1.20;
        case '104': return 1.30;
        case '105': return 1.00;
    }
}



let numero1=document.querySelector('.questao2 #numero1');
let numero2=document.querySelector('.questao2 #numero2');
let form2=document.querySelector('.questao2 form');
let tabela=document.querySelector('.questao2 table');

let linhasomaCriada=document.createElement('tr');
let somaCriada=document.createElement('td');
let valorsomaCriado=document.createElement('td');
tabela.appendChild(linhasomaCriada);

let linhasubtracaoCriada=document.createElement('tr');
let subtracaoCriada=document.createElement('td');
let valorsubtracaoCriado=document.createElement('td');
tabela.appendChild(linhasubtracaoCriada);

let linhaprodutoCriada=document.createElement('tr');
let produtoCriado=document.createElement('td');
let valorprodutoCriado=document.createElement('td');
tabela.appendChild(linhaprodutoCriada);

let linhadivisaoCriada=document.createElement('tr');
let divisaoCriada=document.createElement('td');
let valordivisaoCriado=document.createElement('td');
tabela.appendChild(linhadivisaoCriada); 

let linharestoCriada=document.createElement('tr');
let restoCriado=document.createElement('td');
let valorrestoCriado=document.createElement('td');
tabela.appendChild(linharestoCriada);


form2.addEventListener('submit', function(event) {
    event.preventDefault();
    /* console.log(codigoinserido.value); */
    /* for(let i=0; i<linhas.length;i++){
        let linha=linhas[i];
        let codigo=linha.querySelector('td').textContent;
        console.log(codigo);
    } */
   
    somaCriada.textContent=numero1.value+ '+'+numero2.value;
    valorsomaCriado.textContent=parseFloat(numero1.value,10)+parseFloat(numero2.value,10);
    linhasomaCriada.appendChild(somaCriada);
    linhasomaCriada.appendChild(valorsomaCriado);
    linhasomaCriada.classList.add('surgir1');
   

   
    subtracaoCriada.textContent=numero1.value+ '-'+numero2.value;
    valorsubtracaoCriado.textContent=numero1.value-numero2.value;
    linhasubtracaoCriada.appendChild(subtracaoCriada);
    linhasubtracaoCriada.appendChild(valorsubtracaoCriado);
    linhasubtracaoCriada.classList.add('surgir1');
   

   
    produtoCriado.textContent=numero1.value+ '*'+numero2.value;
    valorprodutoCriado.textContent=numero1.value*numero2.value;
    linhaprodutoCriada.appendChild(produtoCriado);
    linhaprodutoCriada.appendChild(valorprodutoCriado);
    linhaprodutoCriada.classList.add('surgir1');
   

   
    divisaoCriada.textContent=numero1.value+ '/'+numero2.value;
    valordivisaoCriado.textContent=(numero1.value/numero2.value).toFixed(2);
    linhadivisaoCriada.appendChild(divisaoCriada);
    linhadivisaoCriada.appendChild(valordivisaoCriado);
    linhadivisaoCriada.classList.add('surgir1');

    restoCriado.textContent=numero1.value+ '%'+numero2.value;
    valorrestoCriado.textContent=numero1.value%numero2.value;
    linharestoCriada.appendChild(restoCriado);
    linharestoCriada.appendChild(valorrestoCriado);
    linharestoCriada.classList.add('surgir1');
   

    /* pValor.style='text-align:center; animation-name:surgir; animation-duration:2s;';
    pValor.style.animation='surgir 2s'; */
   /*  console.log(linhas.children); */
});





let lblData=document.querySelector('.questao3 #lblData');
let data=document.querySelector('.questao3 #data');
let form3=document.querySelector('.questao3 form');

let dataPorExtenso=document.createElement('h2');
form3.addEventListener('submit', function(event) {
    event.preventDefault();
    let vetorData=data.value.split('-');
    console.log(vetorData);
    let mesExtenso=converteMes(vetorData[1]);
    dataPorExtenso.textContent='DATA: '+vetorData[2]+' de '+ mesExtenso+ ' de '+ vetorData[0];
    dataPorExtenso.style='width:400px; margin-left:-50px;background-color:white;border:2px solid greenyellow;';
    questao3.appendChild(dataPorExtenso);
});
function converteMes(mes){
    if(mes=='01'){
        return 'janeiro';
    }
    if(mes=='02'){
        return 'fevereiro';
    }
    if(mes=='03'){
        return 'marco';
    }
    if(mes=='04'){
        return 'abril';
    }
    if(mes=='05'){
        return 'maio';
    }
    if(mes=='06'){
        return 'junho';
    }
    if(mes=='07'){
        return 'julho';
    }
    if(mes=='08'){
        return 'agosto';
    }
    if(mes=='09'){
        return 'setembro';
    }
    if(mes=='10'){
        return 'outubro';
    }
    if(mes=='11'){
        return 'novembro';
    }
    if(mes=='12'){
        return 'dezembro';
    }
}




let txtNome=document.querySelector('.questao4 #txtNome');
let rdSuco=document.querySelector('.questao4 #suco');
let rdRefrigerante=document.querySelector('.questao4 #refrigerante');
let rdAgua=document.querySelector('.questao4 #agua');
let chkBolo=document.querySelector('.questao4 #bolo');
let chkPastel=document.querySelector('.questao4 #pastel');
let chkTorta=document.querySelector('.questao4 #torta');
let form4=document.querySelector('.questao4 form');
let btnCalcular=document.querySelector('.questao4 #calcular');
let btnLimpar=document.querySelector('.questao4 #limpar');

let valor;
let bebidas;
let comidas;
let mensagem=document.createElement('h2');
btnCalcular.addEventListener('click',function(event){
    mensagem.classList.remove('invisivel');
    event.preventDefault();
    valor='0';
    bebidas='';
    comidas='';
    mensagem.textContent='';
    mensagem.style='color: black;margin:-60px auto; text-align:center;background-color:white;border:2px solid greenyellow;';
    checarRadios();
    checarChecks();
    mensagem.innerHTML="Nome do cliente: "+txtNome.value+"<br>"+"Bebidas:"+bebidas+"<br>"+"Comidas:"+comidas+"<br>"+"Valor: R$"+ valor;
    questao4.appendChild(mensagem);
});

function checarRadios(){
    if(rdSuco.checked==true){
        valor=parseFloat(valor,10)+parseFloat(5.00,10);
        bebidas+='\n   Suco';
    }
    if(rdRefrigerante.checked==true){
        valor=parseFloat(valor,10)+parseFloat(4.50,10);
        bebidas+='\n   Refrigerante';
    }
    if(rdAgua.checked==true){
        valor=parseFloat(valor,10)+parseFloat(1.50,10);
        bebidas+='\n   Água';
    }
    if((rdSuco.checked==false)&&(rdAgua.checked==false)&&(rdRefrigerante.checked==false)){
        bebidas+=" Nenhuma bebida selecionada";
    }
}
function checarChecks(){
    if(chkBolo.checked==true){
        valor=parseFloat(valor,10)+parseFloat(4.50,10);
        comidas+='\n   Bolo';
    }
    if(chkPastel.checked==true){
        valor=parseFloat(valor,10)+parseFloat(5.00,10);
        comidas+='\n   Pastel';
    }
    if(chkTorta.checked==true){
        valor=parseFloat(valor,10)+parseFloat(6.00,10);
        comidas+='\n   Torta';
    }
    if((chkBolo.checked==false)&&(chkPastel.checked==false)&&(chkTorta.checked==false)){
        comidas+="  Nenhuma comida selecionada";
    }
}

btnLimpar.addEventListener('click',function(event){
    event.preventDefault();
    txtNome.value='';
    limparRadios();
    limparChecks();
    mensagem.classList.add('invisivel');
});
function limparRadios(){
    rdAgua.checked=false;
    rdRefrigerante.checked=false;
    rdSuco.checked=false;
}
function limparChecks(){
    chkBolo.checked=false;
    chkPastel.checked=false;
    chkTorta.checked=false;
}





let btn1=document.querySelector('.questao5 #btn1');
let btn2=document.querySelector('.questao5 #btn2');
let btn3=document.querySelector('.questao5 #btn3');
let btn4=document.querySelector('.questao5 #btn4');
let btn5=document.querySelector('.questao5 #btn5');
let btn6=document.querySelector('.questao5 #btn6');
let btn7=document.querySelector('.questao5 #btn7');
let btn8=document.querySelector('.questao5 #btn8');
let btn9=document.querySelector('.questao5 #btn9');
let btn0=document.querySelector('.questao5 #btn0');
let btnOP=document.querySelector('.questao5 #btnOP');
let btnC=document.querySelector('.questao5 #btnC');
let btnPonto=document.querySelector('.questao5 #btnPonto');
let btnIgual=document.querySelector('.questao5 #btnIgual');
let txtValorSelecionado=document.querySelector('.questao5 #txtValorSelecionado');
let txtResultado=document.querySelector('.questao5 #resultado')


txtValorSelecionado.disabled=true;
txtResultado.disabled=true;
btn1.addEventListener('click',function(event){
    event.preventDefault();
    txtValorSelecionado.value = '1';
    //txtValorSelecionado.textContent+='1';
});
btn2.addEventListener('click',function(event){
    event.preventDefault();
    txtValorSelecionado.value+='2'
});
btn3.addEventListener('click',function(event){
    event.preventDefault();
    txtValorSelecionado.value+='3'
});
btn4.addEventListener('click',function(event){
    event.preventDefault();
    txtValorSelecionado.value+='4'
});
btn5.addEventListener('click',function(event){
    event.preventDefault();
    txtValorSelecionado.value+='5'
});
btn6.addEventListener('click',function(event){
    event.preventDefault();
    txtValorSelecionado.value+='6'
});
btn7.addEventListener('click',function(event){
    event.preventDefault();
    txtValorSelecionado.value+='7'
});
btn7.addEventListener('click',function(event){
    event.preventDefault();
    txtValorSelecionado.value+='7'
});
btn8.addEventListener('click',function(event){
    event.preventDefault();
    txtValorSelecionado.value+='8'
});
btn9.addEventListener('click',function(event){
    event.preventDefault();
    txtValorSelecionado.value+='9'
});
btn0.addEventListener('click',function(event){
    event.preventDefault();
    txtValorSelecionado.value+='0'
});
btnC.addEventListener('click',function(event){
    event.preventDefault();
    txtValorSelecionado.value='';
    txtResultado.value='';
});
btnPonto.addEventListener('click',function(event){
    event.preventDefault();
    txtValorSelecionado.value+='.'
});
btnOP.addEventListener('click',function(event){
    event.preventDefault();
    if(operacao.value=='soma'){
        operacao.disabled=true;
        txtValorSelecionado.value+='+';
    }
    if(operacao.value=='subtracao'){
        operacao.disabled=true;
        txtValorSelecionado.value+='-';
    }
    if(operacao.value=='multiplicacao'){
        operacao.disabled=true;
        txtValorSelecionado.value+='*';
    }
    if(operacao.value=='divisao'){
        operacao.disabled=true;
        txtValorSelecionado.value+='/';
    }
});
btnIgual.addEventListener('click',function(event){
    event.preventDefault();
    txtResultado.value=eval(txtValorSelecionado.value);
    txtValorSelecionado.value='';
    operacao.disabled=false;
});