package exercicio04;
/*4. Modifique o exercício anterior para adicionar um novo arquivo no projeto com o nome de Episodio.java. Este arquivo deve conter uma classe chamada Episodio, o qual possui três atributos (título e duração), e um método que mostra na tela esses dois atributos. Instancie cinco objetos desta classe. */
public class Usuario {
    // Atributos da classe
    String nome;
    String email;
    String senha;

    // Método construtor
    Usuario(String nome, String email, String senha) {
        this.nome = nome;
        this.email = email;
        this.senha = senha;
    }

    //Método para imprimir informações
    void imprimirInfo(){
        System.out.println("Nome: "+this.nome);
        System.out.println("Email: "+this.email);
    }

    //Método que verifica a senha
    boolean verificarSenha(String senhaFornecida){
        return this.senha.equals(senhaFornecida);
    }

    //Método principal
    public static void main(String[] args){
        //Criação de uma instancia de usuario        
        Usuario usuario = new Usuario("João", "joao@exemplo.com", "senhaSegura123");
        
        //Imprime as infos
        usuario.imprimirInfo();

        //Verifica senha
        boolean senhaCorreta = usuario.verificarSenha("senhaSegura123");
        System.out.println("Senha fornecida está correta? "+senhaCorreta);

        boolean senhaIncorreta = usuario.verificarSenha("senhaSegura000");
        System.out.println("Senha fornecida está correta? "+senhaIncorreta);
    }
}
