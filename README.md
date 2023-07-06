# trabalho-final
repositorio do trabalho final



Builder:

O padrão de desenvolvimento Builder é um padrão de criação de software que visa facilitar a construção de objetos complexos passo a passo. Ele é usado quando um objeto requer uma configuração detalhada e personalizada durante o processo de criação, permitindo que o desenvolvedor defina e altere facilmente os parâmetros de criação.

O padrão Builder separa a construção de um objeto complexo de sua representação, permitindo que o mesmo processo de construção possa criar diferentes representações do objeto. Isso é útil quando existem várias formas de construir um objeto, mas o processo de construção em si é independente da estrutura do objeto final.

A ideia por trás do padrão Builder é ter uma classe principal, chamada de "Builder", que define uma interface para criar as diferentes partes de um objeto. Em seguida, são implementadas classes de construtor concretas, que herdam ou implementam essa interface, para construir objetos específicos.

O processo de construção ocorre passo a passo, onde cada parte do objeto é configurada através dos métodos fornecidos pelo Builder. No final, o Builder retorna o objeto completo e configurado para o cliente.

O padrão Builder oferece vantagens, como a criação de objetos complexos de forma flexível e modular, permitindo diferentes representações do mesmo objeto. Ele também ajuda a evitar a chamada "construção telescópica" de construtores, onde existem muitos construtores com diferentes parâmetros.

Em resumo, o padrão de desenvolvimento Builder é usado para separar o processo de construção de um objeto complexo de sua representação, permitindo a criação flexível e modular de diferentes objetos através de um processo de construção passo a passo. Isso promove um código mais legível, flexível e reutilizável.
