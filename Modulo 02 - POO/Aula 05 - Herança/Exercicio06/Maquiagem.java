package Exercicio06;

public class Maquiagem extends Produto {
    private String cor;
 
    public Maquiagem(String nome, String cor) {
        super(nome);
        this.cor = cor;
    }
 
    public String getCor() {
        return cor;
    }
}
