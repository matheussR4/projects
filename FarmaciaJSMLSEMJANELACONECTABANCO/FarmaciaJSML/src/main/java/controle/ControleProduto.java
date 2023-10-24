/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controle;

import Classes.Produto;
import bancodedados.BDProduto;
import interfaceDados.IProduto;

/**
 *
 * @author Petheus Rodrigues
 */
public class ControleProduto {
    private String mensagem;
    private IProduto dadosProdutos;

    public ControleProduto() {
        dadosProdutos=new BDProduto();
    }
    
    public boolean adicionarProduto(String nome, String tipo,int cod_fornecedor, double preco){
        boolean adicionou;
        Produto novoProduto= new Produto(nome, tipo, cod_fornecedor, preco);
        adicionou=dadosProdutos.adicionarProduto(novoProduto);
        mensagem=dadosProdutos.getMensagem();
        return adicionou;
    }
    
    public String getMensagem(){
        return mensagem;
    }
}
