package Exercicio01;

public class Carro {
    private String marca;
    private String modelo;
    private int ano;
    private String placa;

    public Carro(String marca, String modelo, int ano, String placa) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.placa = placa;
    }

// Getters
    public String getMarca() {
        return this.marca;
    }

    public String getModelo() {
        return this.modelo;
    }

    public int getAno() {
        return this.ano;
    }

    public String getPlaca() {
        return this.placa;
    }

// Setters
    public void setMarca(String marca) {
        this.marca = marca;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }
    
    public String toString() {
        return "Carro [Marca = " + marca + ", Modelo = " + modelo + ", Ano = " + ano + ", Placa = " + placa + "]";
    }
}
