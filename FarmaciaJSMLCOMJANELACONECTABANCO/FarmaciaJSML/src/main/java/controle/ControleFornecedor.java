/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controle;

import Classes.Fornecedor;
import bancodedados.BDFornecedor;
import interfaceDados.IFornecedor;
import java.util.ArrayList;

/**
 *
 * @author Petheus Rodrigues
 */
public class ControleFornecedor {
    private String mensagem;
    private IFornecedor dadosFornecedores;

    public ControleFornecedor() {
        dadosFornecedores= new BDFornecedor();
    }
    
    
    public boolean adicionarFornecedor(String nome, String tipoDeProdutoFornecido, String CEP, String CNPJ, String contato){
        boolean adicionou;
        Fornecedor fornecedor = new Fornecedor(nome, tipoDeProdutoFornecido,CEP,CNPJ, contato);
        adicionou = dadosFornecedores.adicionarFornecedor(fornecedor);
        mensagem = dadosFornecedores.getMensagem();
        return adicionou;
    }
    
    public ArrayList<Fornecedor> consultarFornecedores(){
        return dadosFornecedores.consultarFornecedores();
    }

    public String getMensagem() {
        return mensagem;
    }
    
}
