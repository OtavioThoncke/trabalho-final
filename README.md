# trabalho-final
repositorio do trabalho final



Explicação do codigo "Codigo builder": ele é exemplo, temos a classe House que representa uma casa, com atributos como foundation (fundação), walls (paredes) e roof (telhado). A classe HouseBuilder define a interface para construir uma casa, com métodos como build_foundation, build_walls e build_roof. Em seguida, temos implementações concretas de builders, como SimpleHouseBuilder e LuxuryHouseBuilder, que constroem diferentes tipos de casas.

O ConstructionDirector é responsável por controlar o processo de construção e usa o builder correspondente para construir a casa desejada. No exemplo, construímos uma casa simples e uma casa de luxo usando diferentes builders. O resultado é impresso no final.
