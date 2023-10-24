/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Interface.java to edit this template
 */
package interfaceDados;

import Classes.Produto;
import java.util.ArrayList;

/**
 *
 * @author Petheus Rodrigues
 */
public interface IProduto {
    public abstract boolean adicionarProduto(Produto produto);
    public abstract ArrayList<Produto> consultarProdutos();
    public String getMensagem();
}
