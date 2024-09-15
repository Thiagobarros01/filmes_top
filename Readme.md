# API de Filmes

## Visão Geral

Esta é uma API para acessar filmes dos usuários da FilmesTop.com. Ela permite listar filmes, alugar filmes, adicionar notas e consultar aluguéis de usuários.

## Funcionalidades

- **Listar Filmes:** Obtém uma lista de todos os filmes ou filtra filmes por gênero.
- **Detalhes do Filme:** Obtém informações detalhadas sobre um filme específico.
- **Alugar Filme:** Aluga um filme para um usuário.
- **Adicionar Nota:** Adiciona ou atualiza uma nota para um filme alugado por um usuário.
- **Consultar Aluguéis:** Obtém todos os aluguéis realizados por um usuário.

## Endpoints

1. GET /api/filmes
exemplo : /api/filmes?genero=Crime

Descrição: Lista todos os filmes ou filtra filmes por gênero.

200 OK: Retorna uma lista de filmes.

404 Not Found: Nenhum filme encontrado.

exemplo resposta:

[
    {
        "id": 1,
        "nome": "O Poderoso Chefão",
        "genero": "Crime",
        "ano": 1972,
        "sinopse": "A história da família mafiosa Corleone.",
        "diretor": "Francis Ford Coppola"
    },
    ...
]



2. GET /api/filmes/<int:id_filme>

Descrição: Obtém os detalhes de um filme específico pelo ID.

Parâmetros de URL:
id_filme: ID do filme.

Respostas:

200 OK: Retorna os detalhes do filme.
404 Not Found: Filme não encontrado.

exemplo resposta: 

[
    {
        "id": 1,
        "nome": "O Poderoso Chefão",
        "genero": "Crime",
        "ano": 1972,
        "sinopse": "A história da família mafiosa Corleone.",
        "diretor": "Francis Ford Coppola"
    }
]


3. POST /api/filmes/alugar

Descrição: Aluga um filme para um usuário.

Parâmetros de Formulário:
user_id: ID do usuário.
filme_id: ID do filme.

Respostas:
201 Created: Filme alugado com sucesso.
400 Bad Request: Parâmetros ausentes ou inválidos.

exemplo de resposta: 

{
    "Message": "Filme alugado com sucesso!"
}



4. PUT /api/filmes/<int:id_filme>/usuario/<int:id_usuario>

Descrição: Adiciona ou atualiza uma nota para um filme alugado por um usuário.

Parâmetros de URL:

id_filme: ID do filme.
id_usuario: ID do usuário.
Parâmetros de JSON:

nota: Nota do filme.
Respostas:

200 OK: Nota atualizada com sucesso.
400 Bad Request: Parâmetros ausentes, usuário ou filme não encontrados, ou o usuário não alugou o filme.

exemplo de resposta: 

{
    "Message": "Nota atualizada com sucesso"
}


5. GET /api/filmes/usuario/<int:id_usuario>/alugueis
Descrição: Obtém todos os aluguéis de um usuário.

Parâmetros de URL:

id_usuario: ID do usuário.
Respostas:

200 OK: Retorna uma lista de aluguéis.
404 Not Found: Usuário não encontrado.

exemplo de resposta:

[
    {
        "filme": "O Poderoso Chefão",
        "nota": 5,
        "data_aluguel": "2024-09-15T14:45:00"
    },
    ...
]

Erros
400 Bad Request: Parâmetros ausentes ou inválidos.
404 Not Found: Recurso não encontrado.

Requisitos
Certifique-se de que o banco de dados esteja configurado corretamente e as tabelas necessárias (Filme, Usuario, Aluguel) estejam criadas.

