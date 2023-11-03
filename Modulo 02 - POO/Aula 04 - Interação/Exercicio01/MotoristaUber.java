package Exercicio01;

public class MotoristaUber {
    private String nome;
    private String idMotorista;
    private Carro carro;

    public MotoristaUber(String nome, String idMotorista, Carro carro) {
        this.nome = nome;
        this.idMotorista = idMotorista;
        this.carro = carro;
    }

    // Getters
    public String getNome() {
        return this.nome;
    }

    public String getIdMotorista() {
        return this.idMotorista;
    }

    public Carro getCarro() {
        return this.carro;
    }

    // Setters
    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setIdMotorista(String idMotorista) {
        this.idMotorista = idMotorista;
    }

    public void setCarro(Carro carro) {
        this.carro = carro;
    }
    
    public String toString() {
        return "Motorista [Nome = " + nome + ", ID = " + idMotorista + ", Carro = " + carro.toString() + "]";
    }

    public static void main(String[] args) {
        Carro carro = new Carro("Renault", "Kwid Branco", 2023, "ABC-1234");
        MotoristaUber motorista = new MotoristaUber("João", "M1234", carro);

        System.out.println(motorista);

        motorista.setNome("José");
        motorista.getCarro().setModelo("Sandero");

        System.out.println(motorista);
    }
}
