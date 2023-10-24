/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controle;

import bancodedados.ConexaoBanco;

/**
 *
 * @author Petheus Rodrigues
 */
public class ControleConectaBanco {
    private ConexaoBanco conexaoBanco;
    private String mensagem;
    
    public ControleConectaBanco(){
        conexaoBanco = ConexaoBanco.getInstanceConexaoBanco();
    }

    public String getMensagem() {
        return mensagem;
    }
    
    public boolean abrirConexao(String url,
                                String usuario,
                                String senha){
        boolean conectou;
        conectou = conexaoBanco.abrirConexao(url, usuario, senha);
        mensagem = conexaoBanco.getMensagem();
        return conectou;
    }
}
