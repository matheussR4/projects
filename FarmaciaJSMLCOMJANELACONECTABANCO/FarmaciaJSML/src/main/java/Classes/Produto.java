/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Classes;

/**
 *
 * @author Petheus Rodrigues
 */
public class Produto {
    public String nome;
    public String tipo;
    public int cod_fornecedor;
    public double preco;

    public Produto(String nome, String tipo,int cod_fornecedor, double preco) {
        this.nome = nome;
        this.tipo = tipo;
        this.cod_fornecedor = cod_fornecedor;
        this.preco=preco;
    }

    public String getNome() {
        return nome;
    }

    public String getTipo() {
        return tipo;
    }


    public int getCod_fornecedor() {
        return cod_fornecedor;
    }

    public double getPreco() {
        return preco;
    }
    
    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public void setCod_fornecedor(int cod_fornecedor) {
        this.cod_fornecedor = cod_fornecedor;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }
   
}
