# Construindo Consultas Rápidas em um CSV com Python 🐍

Neste projeto, exploramos a construção de consultas rápidas em um arquivo CSV com a ajuda da linguagem de programação Python. Utilizamos Python 3.10.6 e as bibliotecas csv e tabulate para implementar funcionalidades que permitem consultar laptops com base em critérios de preço e atributos específicos.

## Implementação de Novas Funcionalidades 🚀

### 1. find_laptops_in_price_range 💲
   - Esta funcionalidade permite encontrar laptops dentro de um intervalo de preço especificado.
   - Útil para buscar o produto que cabe no seu bolso.

### 2. find_laptops_with_features 🎯
   - Essa funcionalidade permite encontrar laptops com base em critérios de atributos específicos definidos por um dicionário.
   - É útil para pesquisar laptops com recursos personalizados.

## Análise de Complexidade 📊

Aqui, analisamos a complexidade das duas principais funcionalidades implementadas:

|         | `find_laptops_in_price_range` 💰 | `find_laptops_with_features` 🛠️ |
|:-------:|:-----------------------------:|:-----------------------------------:|
| `Big O` |            O(n)               |            O(n * m)                 |
| `Big θ` |            Θ(n)               |            Θ(n * m)                 |
| `Big Ω` |            Ω(1)               |            Ω(1)                     |

### find_laptops_in_price_range 💲

1. **Big O (O)**:
   - A complexidade de tempo no pior caso é **O(n)**, onde **n** é o número de laptops em `self.rows_by_price`.
   - Isso ocorre porque a função percorre todos os laptops em `self.rows_by_price` para verificar se cada laptop está dentro do intervalo de preço especificado.
   - Mesmo que seja utilizado um loop `for`, o pior caso é percorrer todos os laptops, pois o loop não é interrompido até que todos sejam verificados.

2. **Big Theta (Θ)**:
   - A complexidade de tempo no caso médio é também **Θ(n)**, pois, em média, a função terá que percorrer metade dos laptops em `self.rows_by_price`.
   - Isso ocorre porque o loop é interrompido assim que um laptop com preço maior que `max_price` é encontrado, o que reduz o número de iterações necessárias no caso médio.

3. **Big Omega (Ω)**:
   - A complexidade de tempo no melhor caso é **Ω(1)**.
   - Isso ocorre quando o primeiro laptop em `self.rows_by_price` já está dentro do intervalo de preço especificado.
   - Nesse caso, a função retorna imediatamente sem fazer mais iterações.

Portanto, a complexidade da função `find_laptops_in_price_range` é linear em relação ao número de laptops em `self.rows_by_price` (n), mas pode ser interrompida mais cedo no caso médio e no melhor caso, dependendo da localização dos laptops dentro do intervalo de preço especificado.

### find_laptops_with_features 🎯

1. **Big O (O)**:
   - A complexidade de tempo no pior caso é **O(n * m)**, onde **n** é o número de laptops no inventário e **m** é o número de atributos no dicionário `features`.
   - A função verifica cada laptop para cada atributo especificado.

2. **Big Theta (Θ)**:
   - A complexidade de tempo no caso médio também é **Θ(n * m)**.
   - A função verifica uma fração dos laptops em relação ao total e um número médio de atributos.

3. **Big Omega (Ω)**:
   - A complexidade de tempo no melhor caso é **Ω(1)**.
   - Isso ocorre quando o primeiro laptop no inventário corresponde a todos os critérios de atributo especificados.

### Documentação e Código 📄

Para acessar o código-fonte deste projeto, confira [aqui](./main.py).

### Vídeo Explicativo 📹

Um vídeo explicativo deste projeto está disponível [aqui](./video.mp4). 🚀