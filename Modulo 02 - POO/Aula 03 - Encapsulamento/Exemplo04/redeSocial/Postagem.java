package Exemplo04.redeSocial;

public class Postagem {
    static int curtidas;

    static void mostrarCurtidas() {
        System.out.println("------------------");
        System.out.println("... Postagem recebeu curtida!");
        System.out.println("... Total de curtidas = " + curtidas);
        System.out.println("------------------");
    }
}
