# Pokédex

Uma aplicação GUI simples desenvolvida em Python usando Tkinter para exibir informações sobre Pokémon. A aplicação permite buscar Pokémon por nome, número ou tipo, e navegar entre eles.

## Funcionalidades

- **Buscar Pokémon**: Pesquisar Pokémon por nome, número ou tipo.
- **Exibição de Detalhes**: Mostrar detalhes como número, nome, tipo, HP, ataque, defesa e velocidade.
- **Navegação**: Navegar entre Pokémon usando botões "Anterior" e "Próximo".
- **Imagens**: Exibir imagens dos Pokémon e uma imagem padrão de Pokébola.

## Requisitos

- Python 3.x
- Bibliotecas Python: `tkinter`, `PIL` (Pillow), `json`

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/yanfurlan/pokedex.git
   cd pokedex

2. Instale as dependências:

   pip install pillow

3. Adicione um arquivo pokemons.json na raiz do projeto com o formato esperado. Um exemplo de estrutura do arquivo pokemons.json:

[
    {
        "id": 1,
        "name": "Bulbasaur",
        "type": ["Grass", "Poison"],
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "speed": 45,
        "image": "assets/bulbasaur.png"
    }
    // Adicione mais Pokémon aqui
]

4. Adicione a imagem padrão da Pokébola em assets/pokeball.png.

Uso

Execute o programa:


python pokedex.py

Utilize a barra de rolagem e os botões de navegação para explorar a Pokédex.

Use o campo de busca para encontrar Pokémon por nome, número ou tipo.

Estrutura do Projeto

pokedex.py: O arquivo principal que contém o código da aplicação.

pokemons.json: Arquivo JSON contendo os dados dos Pokémon.

assets/: Pasta contendo imagens dos Pokémon e a imagem da Pokébola.

Contribuições

Sinta-se à vontade para fazer um fork deste repositório e enviar pull requests com melhorias e correções.

Licença

Este projeto está licenciado sob a Licença MIT.


### Instruções para Personalizar o `README`:

1. **Substitua o URL do repositório Git**: Atualize o link para o repositório com o seu URL, se estiver hospedado em algum serviço como GitHub.
2. **Atualize o Exemplo do `pokemons.json`**: Ajuste o exemplo de JSON conforme a estrutura real dos dados no seu arquivo.
3. **Adicione Detalhes Adicionais**: Inclua quaisquer instruções específicas ou informações adicionais que sejam relevantes para o seu projeto.