package Exercicio05;

import java.util.ArrayList;

public class Playlist {
    private ArrayList listaDeMidia;
 
    public Playlist() {
        this.listaDeMidia = new ArrayList();
    }
 
    public void adicionarMidia(Midia media) {
        this.listaDeMidia.add(media);
    }
 
    public void tocarPlaylist() {
        for (Midia media : listaDeMidia) {
            media.play();
        }
    }
}
