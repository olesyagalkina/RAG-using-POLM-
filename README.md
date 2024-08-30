# Creating an RAG system using POLM

Este notebook vai implementar um sistema RAG de ponta a ponta usando o "POLM" (Python, OpenAI, LlamaIndex, MongoDB) AI Stack. O stack de IA, ou GenAI stack, refere-se à composição de modelos, bancos de dados, bibliotecas e frameworks usados para construir e desenvolver aplicações modernas com capacidades de IA generativa.

Os componentes do AI stack incluem: modelos, orquestradores ou integradores, e bancos de dados operacionais e vetoriais. Neste projeto usamos o modelo `text-embedding-3-small` do `OpenAI`, `LlamaIndex` como orquestrador, e o `MongoDB` atuará tanto como banco de dados operacional quanto vetorial.

As bibliotecas necessárias:
- `LlamaIndex`: framework de dados que fornece funcionalidades para conectar fontes de dados (arquivos, PDFs, sites) tanto a LLM fechados (OpenAI, Cohere) quanto de código aberto (Llama)
- `LlamaIndex` para `MongoDB`: biblioteca de extensão do LlamaIndex que importa todos os métodos necessários para conectar e trabalhar com o MongoDB Atlas.
- `LlamaIndex` para `OpenAI`: biblioteca de extensão do LlamaIndex que importa todos os métodos necessários para acessar os modelos de embedding da OpenAI.
- `PyMongo`: biblioteca Python para interagir com o MongoDB, conectar a um cluster e consultar dados armazenados em coleções e documentos.
- `Hugging Face datasets`: biblioteca Hugging Face que contém varios datasets. 
- `Pandas`: para processamento e análise eficientes de dados usando Python.

Inspirado em https://www.mongodb.com/developer/products/atlas/rag-with-polm-stack-llamaindex-openai-mongodb/#step-6--data-ingestion-to-vector-database
