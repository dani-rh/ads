package Exercicio04;

public class Viagem {
    // Preço base da viagem
    private static final double PRECO_BASE = 2.0;
    // Preço por quilômetro
    private static final double PRECO_POR_KM = 1.0;
    // Preço por quilômetro no horário de pico
    private static final double PRECO_PICO_POR_KM = 2.0;

    // Método para calcular o preço apenas com a distância
    public double calcularPreco(double distancia) {
        return PRECO_BASE + PRECO_POR_KM * distancia;
    }

    // Método sobrecarregado para calcular o preço com distância e horário
    public double calcularPreco(double distancia, boolean horarioDePico) {
        if (horarioDePico) {
            return PRECO_BASE + PRECO_PICO_POR_KM * distancia;
        } else {
            return calcularPreco(distancia);
        }
    }
}
