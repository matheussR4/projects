/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package bancodedados;

import Classes.Produto;
import interfaceDados.IProduto;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

/**
 *
 * @author Petheus Rodrigues
 */
public class BDProduto implements IProduto{
    private String mensagem;
    private Statement statement;
    private PreparedStatement preparedStatement;
    private ResultSet resultSet;
    private ConexaoBanco conexaoBanco;
    private Connection connection;

    public BDProduto() {
        conexaoBanco=ConexaoBanco.getInstanceConexaoBanco();
    }
    
    
    @Override
    public boolean adicionarProduto(Produto produto) {
        try {
            String strSQL = "insert into produto (nome, tipo,cod_fornecedor,preco) ";
            strSQL += " values (?, ?, ?, ?);";
            System.out.println(strSQL);
            preparedStatement = conexaoBanco.getConexao().prepareStatement(strSQL);
            
            preparedStatement.setString(1, produto.getNome());
            preparedStatement.setString(2, produto.getTipo());
            preparedStatement.setInt(3, produto.getCod_fornecedor());
            preparedStatement.setDouble(4, produto.getPreco());
            preparedStatement.execute();
            preparedStatement.close();
            mensagem = "Inserção realizada com sucesso.";
            return true;
             
        } catch (SQLException ex) {
            mensagem = ex.getMessage();
            return false;
        } catch (Exception ex) {
            mensagem = ex.getMessage();
            return false;
        }
    }

    @Override
    public ArrayList<Produto> consultarProdutos() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }

    @Override
    public String getMensagem() {
        return mensagem;
    }
    
}
