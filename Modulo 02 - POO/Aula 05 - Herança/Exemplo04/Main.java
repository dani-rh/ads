package Exemplo04;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        var carros = new ArrayList<Carro>();
        var motos = new ArrayList<Moto>();

        carros.add(new Carro("Ford Ka", "Zetec Rocam 1.2", 257));
        carros.add(new Carro("Fiat Uno", "Firefly 1.0", 290));

        motos.add(new Moto("Harley Davidson", "Milwaukee-Eight", 1868));
        motos.add(new Moto("Honda Biz", "OHC 4 tempos", 125));

        for (var carro : carros) {
            System.out.println(carro.imprimir());
        }

        for (var moto : motos) {
            System.out.println(moto.imprimir());
        }
    }
}
