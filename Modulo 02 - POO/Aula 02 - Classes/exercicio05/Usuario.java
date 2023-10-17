package exercicio05;

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
