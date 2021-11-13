onload = function(e) {
  console.log('onload');
  document.getElementById("minhasTarefas").addEventListener("change", filtraMensagens);

  // setInterval(pegaMensagens, 5000)
}

let bla = "blabla";

function filtraMensagens(){
  console.log('filtra')
  console.log(this.checked);

  let url= '';
  if(this.checked){
    url = 'minhasTarefas/';
  }

  console.log('url', url)
  var xmlhttp;
  xmlhttp = new XMLHttpRequest();
  xmlhttp.open('GET', url , true);
  xmlhttp.onreadystatechange = function(e) {
    if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
      var response = JSON.parse(xmlhttp.responseText);
      console.log(response)
  //     if(response.data ==0 ) return;
  // //
  //     var tabela = document.getElementById('tabela');
  //     var novaTabela = document.createElement('table');
  //     novaTabela.setAttribute('id', "tabela");
  //     var tr, th, td, thead, tbody;
  //     thead = document.createElement('thead');
  //     tr = document.createElement('tr');
  //     tr.setAttribute('class', 'table-primary');
  //     th = document.createElement('th');
  //
  //     th.appendChild(document.createTextNode('Autor'));
  //     tr.appendChild(th);
  //
  //     th = document.createElement('th');
  //     th.appendChild(document.createTextNode('Data'));
  //     tr.appendChild(th);
  //
  //     th = document.createElement('th');
  //     th.appendChild(document.createTextNode('Tarefa'));
  //     tr.appendChild(th);
  //
  //     th = document.createElement('th');
  //     th.appendChild(document.createTextNode('Privacidade'));
  //     tr.appendChild(th);
  //
  //     th = document.createElement('th');
  //     th.appendChild(document.createTextNode('Ações'));
  //     tr.appendChild(th);
  //
  //     novaTabela.appendChild(tr)
  //
  //     for(var i in response.data){
  //       var todo = response.data[i];
  //       console.log('todo', todo);
  //       tr = document.createElement('tr');
  //
  //       td = document.createElement('td');
  //       td.appendChild(document.createTextNode(todo.author_id));
  //       tr.appendChild(td);
  //
  //       td = document.createElement('td');
  //       td.appendChild(document.createTextNode(todo.prazo));
  //       tr.appendChild(td);
  //
  //       td = document.createElement('td');
  //       td.appendChild(document.createTextNode(todo.texto));
  //       tr.appendChild(td);
  //
  //       td = document.createElement('td');
  //       td.appendChild(document.createTextNode(todo.privada));
  //       tr.appendChild(td);
  //
  //       td = document.createElement('td');
  //       td.appendChild(document.createTextNode(todo.privada));
  //       tr.appendChild(td);
  //
  //
  //
  //       novaTabela.appendChild(tr);
  //     }
  //
  //     tabela.parentNode.replaceChild(novaTabela, tabela);
  //   }
  };
  xmlhttp.send(null);
}
