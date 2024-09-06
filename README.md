# Creating an RAG system using POLM

Este notebook implementa um sistema RAG completo utilizando o stack de IA `POLM` (Python, OpenAI, LlamaIndex, MongoDB). O stack de IA, também chamado de GenAI stack, é composto por modelos, bancos de dados, bibliotecas e frameworks que permitem a construção de aplicações modernas com capacidades de IA generativa.

Neste projeto, utilizamos o modelo `text-embedding-3-small` da `OpenAI` para gerar embeddings, o `LlamaIndex` como estrutura de orquestração, e o `MongoDB`, que atua tanto como banco de dados operacional quanto como armazenamento vetorial.

### Estrutura do Projeto:
1. Carregamento do Dataset: O conjunto de dados é carregado a partir do `Hugging Face`.
2. Geração de Embeddings: Embeddings são gerados utilizando o modelo de embeddings da `OpenAI`.
3. Configuração do Banco de Dados Vetorial: Um banco de dados vetorial é configurado no `MongoDB` para armazenar os embeddings.
4. Estabelecimento de Conexão: Uma conexão segura é estabelecida com o banco de dados `MongoDB`.
5. Criação de Índice de Busca Vetorial: Um índice de busca vetorial é criado para permitir consultas eficientes.

### Bibliotecas Necessárias:

`LlamaIndex`: Framework de dados que facilita a integração de fontes de dados (arquivos, PDFs, sites) com LLMs como OpenAI e Cohere e LLMs de código aberto (como Llama).

`LlamaIndex` para `MongoDB`: Extensão do LlamaIndex que fornece métodos para conectar e interagir com o MongoDB Atlas.

`LlamaIndex` para `OpenAI`: Extensão do LlamaIndex que inclui os métodos necessários para acessar os modelos de embeddings da OpenAI.

`PyMongo`: Biblioteca Python utilizada para conectar-se ao MongoDB, realizar consultas em coleções e manipular documentos.

`Hugging Face datasets`: biblioteca Hugging Face que contém varios datasets prontos para uso.

`Pandas`:  para processamento e análise eficientes de dados tabulares usando Python.

Inspirado em https://www.mongodb.com/developer/products/atlas/rag-with-polm-stack-llamaindex-openai-mongodb/#step-6--data-ingestion-to-vector-database
