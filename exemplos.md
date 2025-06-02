# Adicionar um livro

- Método: `POST`  
- URL: `http://localhost:5000/livros`  
- Body: 
`Body` > `raw`, > `JSON`

(um por vez)

```json
{
  "titulo": "O Hobbit",
  "autor": "J.R.R. Tolkien",
  "status": "para ler"
}

{
  "titulo": "A Revolução dos Bichos",
  "autor": "George Orwell",
  "status": "lido"
}

{
  "titulo": "Clean Code",
  "autor": "Robert C. Martin",
  "status": "lendo"
}
```

# Listar todos os livros:

- Método: `GET`
- URL: `http://localhost:5000/livros`

# Filtrar por status:

- Método: `GET`
- URL:
 - Para livros lidos: `http://localhost:5000/livros/status/lido`
 - Para livros sendo lidos: `http://localhost:5000/livros/status/lendo`
 - Para livros a serem lidos: `http://localhost:5000/livros/status/para ler`
