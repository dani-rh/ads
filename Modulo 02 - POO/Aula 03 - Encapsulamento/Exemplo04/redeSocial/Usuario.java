package Exemplo04.redeSocial;

public class Usuario {
    static void curtirPostagem() {
        System.out.println("Usuário curtiu a postagem");
        Postagem.mostrarCurtidas();
        int x = Postagem.curtidas;
        System.out.println("Curtidas antes = " + x);
        Postagem.curtidas++;
        System.out.println("Curtidas agora = " + Postagem.curtidas);
    }

    public static void main(String args[]) {
        curtirPostagem();
    }
}
