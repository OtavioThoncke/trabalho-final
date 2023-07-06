# trabalho-final
repositorio do trabalho final



Builder:

O padrão de desenvolvimento Builder é um padrão de criação de software que visa facilitar a construção de objetos complexos passo a passo. Ele é usado quando um objeto requer uma configuração detalhada e personalizada durante o processo de criação, permitindo que o desenvolvedor defina e altere facilmente os parâmetros de criação.

O padrão Builder separa a construção de um objeto complexo de sua representação, permitindo que o mesmo processo de construção possa criar diferentes representações do objeto. Isso é útil quando existem várias formas de construir um objeto, mas o processo de construção em si é independente da estrutura do objeto final.

A ideia por trás do padrão Builder é ter uma classe principal, chamada de "Builder", que define uma interface para criar as diferentes partes de um objeto. Em seguida, são implementadas classes de construtor concretas, que herdam ou implementam essa interface, para construir objetos específicos.

O processo de construção ocorre passo a passo, onde cada parte do objeto é configurada através dos métodos fornecidos pelo Builder. No final, o Builder retorna o objeto completo e configurado para o cliente.

O padrão Builder oferece vantagens, como a criação de objetos complexos de forma flexível e modular, permitindo diferentes representações do mesmo objeto. Ele também ajuda a evitar a chamada "construção telescópica" de construtores, onde existem muitos construtores com diferentes parâmetros.

Em resumo, o padrão de desenvolvimento Builder é usado para separar o processo de construção de um objeto complexo de sua representação, permitindo a criação flexível e modular de diferentes objetos através de um processo de construção passo a passo. Isso promove um código mais legível, flexível e reutilizável.



Pontos fortes do padrão Builder:

Separação da lógica de construção: O padrão Builder permite que você separe a lógica de construção de um objeto complexo dos detalhes específicos de sua implementação. Isso simplifica o código e torna mais fácil entender e modificar a lógica de construção.

Flexibilidade na criação de objetos: Com o padrão Builder, você pode criar objetos com diferentes configurações ou estados, dependendo das necessidades. Isso é útil quando você precisa criar objetos com várias variações ou combinações de propriedades.

Código mais legível e manutenível: O padrão Builder promove um código mais legível, uma vez que a lógica de construção é separada em etapas claras e bem definidas. Isso torna mais fácil entender e dar manutenção ao código no futuro.

Encapsulamento da complexidade: Se o processo de construção de um objeto é complexo, o padrão Builder ajuda a encapsular essa complexidade dentro de um construtor específico. Isso oculta os detalhes internos do processo de construção e simplifica o uso do objeto para os clientes. 



Pontos fracos do padrão Builder:

Overhead adicional: O uso do padrão Builder pode adicionar alguma complexidade e sobrecarga ao código. É necessário criar classes adicionais para representar o Builder e definir métodos para cada etapa de construção. Isso pode aumentar a quantidade de código necessário e dificultar a compreensão em projetos pequenos e simples.

Aumento da complexidade em objetos simples: Se o objeto a ser construído é simples e possui apenas algumas propriedades, o uso do padrão Builder pode adicionar complexidade desnecessária ao código. Nesses casos, pode ser mais simples e direto criar o objeto diretamente, sem o uso do padrão Builder.

Possível violação do princípio da segregação de interfaces: Em alguns casos, o padrão Builder pode levar a uma violação do princípio da segregação de interfaces, já que a interface do Builder precisa abranger todas as etapas de construção possíveis. Isso pode resultar em uma interface maior e menos coesa.

Aumento do acoplamento: O padrão Builder pode aumentar o acoplamento entre as classes envolvidas, uma vez que o Builder precisa ter conhecimento detalhado sobre a estrutura interna do objeto que está construindo. Isso pode dificultar a substituição ou modificação de partes do objeto sem afetar o código do Builder.
