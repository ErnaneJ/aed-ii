# Small Worlds - Project U2

## Objetivos

Explorar os conteúdos das semanas 7 e 8.

- *Assortatividade*;
- Distâncias;
- Componentes conectados;
- Coeficiente de clustering.

Para esse trabalho foram solicitados o cumprimento de três requisitos:

- **Requisito 1**: escolher cinco redes presentes no site [SNAP](https://snap.stanford.edu/data/) para serem analisadas;
- **Requisito 2**: construir e interpretar gráficos bipartidos sobre a `assortatividade` em relação ao grau dos nós de cada uma dessas redes;
- **Requisito 3**: montar e interpretar uma tabela cujas colunas representam propriedades relativas a cada uma dessas redes, tais como quantidade de vértices, quantidade de arestas, coeficiente de `assortatividade` do grau, tamanho do GCC e coeficiente de clustering.

## Fonte de dados

[Stanford Large Network Dataset Collection](https://snap.stanford.edu/data/).

## Requisito 01 - Escolher pelo menos 5 redes do SNAP

### [Rede de Comunicação por E-mail da UE](https://snap.stanford.edu/data/email-EuAll.html)

A rede foi gerada usando dados de e-mail de uma grande instituição de pesquisa europeia. Durante um período de outubro de 2003 a maio de 2005 (18 meses), temos informações anonimizadas sobre todos os e-mails de entrada e saída da instituição de pesquisa. Para cada mensagem de e-mail enviada ou recebida, temos informações sobre o horário, o remetente e o destinatário do e-mail. No total, temos 3.038.531 e-mails entre 287.755 endereços de e-mail diferentes. É importante observar que possuímos um grafo de e-mail completo para apenas 1.258 endereços de e-mail provenientes da instituição de pesquisa. Além disso, existem 34.203 endereços de e-mail que enviaram e receberam e-mails dentro do período de nosso conjunto de dados. Todos os outros endereços de e-mail são inexistentes, digitados incorretamente ou spam.

### [Rede de Colaboração em Física de Altas Energias - Teoria](https://snap.stanford.edu/data/ca-HepTh.html)

A rede de colaboração Arxiv HEP-TH (Física de Altas Energias - Teoria) é proveniente do e-print arXiv e abrange colaborações científicas entre autores de artigos submetidos à categoria de Física de Altas Energias - Teoria. Se um autor i coescreveu um artigo com o autor j, o grafo contém uma aresta não direcionada de i para j. Se o artigo é coescrito por k autores, isso gera um (sub)grafo completamente conectado com k nós.

### [Rede de Estradas da Pensilvânia](https://snap.stanford.edu/data/roadNet-PA.html)

Esta é uma rede de estradas da Pensilvânia. Interseções e pontos finais são representados por nós, e as estradas que conectam essas interseções ou pontos finais são representadas por arestas não direcionadas.

### [Rede Peer-to-Peer Gnutella, 9 de agosto de 2002](https://snap.stanford.edu/data/p2p-Gnutella09.html)

Uma sequência de capturas instantâneas da rede de compartilhamento de arquivos peer-to-peer Gnutella de agosto de 2002. Existem um total de 9 capturas instantâneas da rede Gnutella coletadas em agosto de 2002. Os nós representam hosts na topologia da rede Gnutella e as arestas representam as conexões entre os hosts da Gnutella.

### [Conjunto de Dados Higgs no Twitter](https://snap.stanford.edu/data/higgs-twitter.html)

Este conjunto de dados Higgs foi criado após monitorar os processos de disseminação no Twitter antes, durante e depois do anúncio da descoberta de uma nova partícula com características do esquivo bóson de Higgs em 4 de julho de 2012. As mensagens postadas no Twitter sobre essa descoberta entre 1º e 7 de julho de 2012 são consideradas.

## Requisito 02

Para cada uma das redes escolhidas, projetar e interpretar um gráfico bipartido sobre as *assortatividade* em relação ao grau dos nós da rede. As figuras devem ser realizadas em layout de Grid.

- [Requirements](./U2T2.pdf);
- [Requisito](./Requisito_02/README.md).

## Requisito 03

Desenvolver tabela específica com base na apresentada no slide de requerimento (página 07).

- [Requirements](./U2T2.pdf);
- [Requisito](./Requisito_03/README.md).

## Referências

- [Stanford Large Network Dataset Collection](https://snap.stanford.edu/data/);
- [NetworkX: Network Analysis in Python](https://networkx.org/).
