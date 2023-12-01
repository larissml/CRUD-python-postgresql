<h1>Título do Repositório: Projeto de CRUD Python com PostgreSQL</h1>

<p><strong>Descrição:</strong></p>

<p>Este repositório contém um projeto de CRUD (Create, Read, Update, Delete) desenvolvido em Python para interagir com um banco de dados PostgreSQL. O trabalho foi realizado como parte da disciplina de Banco de Dados II. O projeto está dividido em dois módulos distintos:</p>

<ol>
  <li>
    <strong>Módulo de Acesso ao Banco de Dados:</strong> Este módulo, <code>acessoBd.py</code>, é responsável por estabelecer a conexão com o banco de dados PostgreSQL utilizando a biblioteca psycopg2. Ele apresenta funções para criar a tabela necessária (<code>createTable()</code>), realizar operações de inserção (<code>insert()</code>), atualização (<code>updateNome()</code>, <code>updateAlbuns()</code>, <code>updateMedia()</code>, <code>updateData()</code>) e exclusão (<code>delete()</code>), bem como consultas (<code>selectUma()</code>, <code>selectGeral()</code>) para buscar informações no banco de dados.
  </li>
  <li>
    <strong>Módulo de Menu para Usuários:</strong> O segundo módulo é uma interface de usuário implementada no próprio script Python, permitindo que os usuários interajam com as funcionalidades do CRUD. Ele apresenta um menu interativo com opções para inserir, atualizar, deletar e buscar informações das cantoras no banco de dados.
  </li>
</ol>

<p>O projeto ilustra a aplicação prática das operações CRUD em Python com PostgreSQL, oferecendo exemplos de como criar, acessar, modificar e excluir dados de um banco de dados relacional. O objetivo deste repositório é fornecer um exemplo funcional de como implementar um sistema de CRUD utilizando Python e PostgreSQL, facilitando a interação e manipulação de dados de forma eficiente.</p>
