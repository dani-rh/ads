package Exercicio05;

public class Main {
    public static void main(String[] args) {
        Playlist playlist = new Playlist();

        // Adicionando uma música e um podcast à playlist
        playlist.adicionarMidia(new Musica());
        playlist.adicionarMidia(new Podcast());
        playlist.adicionarMidia(new Podcast());
        playlist.adicionarMidia(new Podcast());
        playlist.adicionarMidia(new Musica());
        playlist.adicionarMidia(new Podcast());

        // Tocando a playlist
        playlist.tocarPlaylist();
    } 
}
