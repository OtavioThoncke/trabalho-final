// Codigo com builder :

class House {
  foundation: string | null = null;
  walls: string | null = null;
  roof: string | null = null;

  toString(): string {
    return `Casa com fundação: ${this.foundation}, paredes: ${this.walls}, e telhado: ${this.roof}`;
  }
}

// Interface do Builder para definir os métodos de construção da casa
interface HouseBuilder {
  buildFoundation(): void;
  buildWalls(): void;
  buildRoof(): void;
  getHouse(): House;
}

// Implementação concreta do Builder para construir uma casa simples
class SimpleHouseBuilder implements HouseBuilder {
  private house: House = new House();

  buildFoundation(): void {
    this.house.foundation = "Concreto";
  }

  buildWalls(): void {
    this.house.walls = "Tijolos";
  }

  buildRoof(): void {
    this.house.roof = "Telhas";
  }

  getHouse(): House {
    return this.house;
  }
}

// Implementação concreta do Builder para construir uma casa de luxo
class LuxuryHouseBuilder implements HouseBuilder {
  private house: House = new House();

  buildFoundation(): void {
    this.house.foundation = "Mármore";
  }

  buildWalls(): void {
    this.house.walls = "Vidro";
  }

  buildRoof(): void {
    this.house.roof = "Telhado de vidro";
  }

  getHouse(): House {
    return this.house;
  }
}

// Diretor para controlar o processo de construção da casa
class ConstructionDirector {
  private builder: HouseBuilder;

  constructor(builder: HouseBuilder) {
    this.builder = builder;
  }

  constructHouse(): void {
    this.builder.buildFoundation();
    this.builder.buildWalls();
    this.builder.buildRoof();
  }

  getHouse(): House {
    return this.builder.getHouse();
  }
}

// Uso do padrão Builder para construir diferentes tipos de casa
const simpleBuilder: HouseBuilder = new SimpleHouseBuilder();
const luxuryBuilder: HouseBuilder = new LuxuryHouseBuilder();

const director: ConstructionDirector = new ConstructionDirector(simpleBuilder);
director.constructHouse();
const simpleHouse: House = director.getHouse();
console.log(simpleHouse.toString());

director = new ConstructionDirector(luxuryBuilder);
director.constructHouse();
const luxuryHouse: House = director.getHouse();
console.log(luxuryHouse.toString());


// codigo sem builder:

class House {
  foundation: string;
  walls: string;
  roof: string;
  floors: number;
  rooms: number;
  garage: boolean;
  garden: boolean;

  constructor(foundation: string, walls: string, roof: string, floors: number, rooms: number, garage: boolean, garden: boolean) {
    this.foundation = foundation;
    this.walls = walls;
    this.roof = roof;
    this.floors = floors;
    this.rooms = rooms;
    this.garage = garage;
    this.garden = garden;
  }

  addGarage(): void {
    this.garage = true;
  }

  addGarden(): void {
    this.garden = true;
  }

  toString(): string {
    let houseDescription = Casa com fundação: ${this.foundation}, paredes: ${this.walls}, telhado: ${this.roof}, ${this.floors} andares e ${this.rooms} quartos.;

    if (this.garage) {
      houseDescription += ' Possui garagem.';
    }

    if (this.garden) {
      houseDescription += ' Possui jardim.';
    }

    return houseDescription;
  }
}

// Construção de uma casa simples
const simpleHouse = new House("Concreto", "Tijolos", "Telhas", 1, 3, true, false);
simpleHouse.addGarden();
console.log(simpleHouse.toString());

// Construção de uma casa de luxo
const luxuryHouse = new House("Mármore", "Vidro", "Telhado de vidro", 3, 6, true, true);
console.log(luxuryHouse.toString());

