## Preparando o Ambiente
Baixe os arquivos necessários, precisaremos configurar nosso ambiente virtual para que nossa aplicação rode igualmente para todos os desenvolvedores. Isso evita o famoso caso, _"na minha máquina funciona!"_

1. Baixe a ferramenta venv, esta ferramenta  precisa receber um nome para que possamos chama-lá no prompt, nomeei de "venv".
   
    ``python -m venv venv``

2. Para ativar o ambiente virtual você precisa estar no mesmo nível do diretório do projeto. Execute o script de acordo com o seu SO e, insira o mesmo nome que você nomeou no inicio quando baixou o venv. 

    Windows: ``venv/Script/activate``<br>Linux: ``source venv/bin/activate``

    <br>Observação: em alguns caso ao tentar ativar o venv pode gerar um erro, não irei abordar sobre isso neste readme. Porém, veja como solucionar neste [Link](https://cursos.alura.com.br/forum/topico-bug-mensagem-de-erro-ao-tentar-ativar-o-venv-347661)

3. Instale as bibliotecas necessárias para a conexão do banco de dados.
   <br>``pip install -r requirements.txt``
   
