package Exemplo03;

public class Carro extends Veiculo{    
    private int portaMalas;
    
    public Carro(String marca, String motor, int portaMalas) {
        super(marca, motor);
        this.portaMalas = portaMalas;
    }

    public int getPortaMalas() {
        return portaMalas;
    }
    
    public String imprimir() {
        return "Marca: " + this.marca + ", Motor: " + this.motor + 
            " Porta-malas: " + this.portaMalas + " litros.";                 
    }
}