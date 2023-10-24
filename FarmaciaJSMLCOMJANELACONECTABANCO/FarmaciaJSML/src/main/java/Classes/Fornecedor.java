/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Classes;

/**
 *
 * @author Petheus Rodrigues
 */
public class Fornecedor {
    public int codigo;
    public String tipoDeProdutoFornecido;
    public String nome;
    public String CEP;
    public String CNPJ;
    public String contato;

    public Fornecedor(String nome,String tipoDeProdutoFornecido, String CEP, String CNPJ, String contato) {
        this.tipoDeProdutoFornecido = tipoDeProdutoFornecido;
        this.nome = nome;
        this.CEP = CEP;
        this.CNPJ = CNPJ;
        this.contato = contato;
    }
    public Fornecedor(int codigo,String nome,String tipoDeProdutoFornecido, String CEP, String CNPJ, String contato) {
        this.tipoDeProdutoFornecido = tipoDeProdutoFornecido;
        this.nome = nome;
        this.CEP = CEP;
        this.CNPJ = CNPJ;
        this.contato = contato;
        this.codigo=codigo;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }
    
    public String getTipoDeProdutoFornecido() {
        return tipoDeProdutoFornecido;
    }

    public String getNome() {
        return nome;
    }

    public String getCEP() {
        return CEP;
    }

    public String getCNPJ() {
        return CNPJ;
    }

    public String getContato() {
        return contato;
    }

    public void setTipoDeProdutoFornecido(String tipoDeProdutoFornecido) {
        this.tipoDeProdutoFornecido = tipoDeProdutoFornecido;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setCEP(String CEP) {
        this.CEP = CEP;
    }

    public void setCNPJ(String CNPJ) {
        this.CNPJ = CNPJ;
    }

    public void setContato(String contato) {
        this.contato = contato;
    }
    
    
}
