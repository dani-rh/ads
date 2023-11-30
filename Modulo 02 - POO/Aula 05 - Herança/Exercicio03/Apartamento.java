package Exercicio03;

public class Apartamento extends Casa{
    @Override
     public double precoPorNoite() {
         return super.precoPorNoite() * 1.2;  // Preço por noite para Apartamento.
     }
}
