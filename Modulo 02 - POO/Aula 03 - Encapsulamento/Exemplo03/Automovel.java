package Exemplo03;
/*EXEMPLOExemplo de aplicação 3: Crie um algoritmo em Java contendo uma classe chamada Automovel. Ela deve possuir atributos públicos (public), protegidos (protected) e privados (private).*/
public class Automovel {
    public String marca;
    protected String modelo;
    private String placa;

    public Automovel(String marca, String modelo, String placa) {
        this.marca = marca;
        this.modelo = modelo;
        this.placa = placa;
    }

    public String getPlaca() {
        return this.placa;
    }
}
