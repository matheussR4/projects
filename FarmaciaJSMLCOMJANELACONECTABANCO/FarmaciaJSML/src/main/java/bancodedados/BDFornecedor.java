/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package bancodedados;

import Classes.Fornecedor;
import interfaceDados.IFornecedor;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import javax.swing.JOptionPane;

/**
 *
 * @author Petheus Rodrigues
 */
public class BDFornecedor implements IFornecedor{
    private String mensagem;
    private Statement statement;
    private PreparedStatement preparedStatement;
    private ResultSet resultSet;
    private ConexaoBanco conexaoBanco;
    private Connection connection;

    public BDFornecedor() {
        conexaoBanco=ConexaoBanco.getInstanceConexaoBanco();
    }
    
    
    @Override
    public boolean adicionarFornecedor(Fornecedor fornecedor) {
try {
            String strSQL = "insert into fornecedor (nome, tipodeprodutofornecido, cep, cnpj, contato) ";
            strSQL += " values (?, ?, ?, ?, ?);";
            System.out.println(strSQL);
            preparedStatement = conexaoBanco.getConexao().prepareStatement(strSQL);
            
            preparedStatement.setString(1, fornecedor.getNome());
            preparedStatement.setString(2, fornecedor.getTipoDeProdutoFornecido());
            preparedStatement.setString(3, fornecedor.getCEP());
            preparedStatement.setString(4, fornecedor.getCNPJ());
            preparedStatement.setString(5, fornecedor.getContato());
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
        }    }

    @Override
    public ArrayList<Fornecedor> consultarFornecedores() {
        ArrayList<Fornecedor> fornecedores;
        fornecedores= new ArrayList<Fornecedor>();
        String strSQL="select * from fornecedor;";
        try {
            statement = conexaoBanco.getConexao().createStatement();
            resultSet=statement.executeQuery(strSQL);
            while(resultSet.next()){
                Fornecedor fornecedorAtual=new Fornecedor(-1,"","","","","");
                fornecedorAtual.setCodigo(resultSet.getInt("codigo"));
                fornecedorAtual.setNome(resultSet.getString("nome"));
                fornecedorAtual.setTipoDeProdutoFornecido(resultSet.getString("tipodeprodutofornecido"));
                fornecedorAtual.setCEP(resultSet.getString("cep"));
                fornecedorAtual.setCNPJ(resultSet.getString("cnpj"));
                fornecedorAtual.setContato(resultSet.getString("contato"));
                fornecedores.add(fornecedorAtual);
            }
            return fornecedores;
        } catch (SQLException ex) {
            JOptionPane.showMessageDialog(null, ex);
            return null;
        }
        
    }

    @Override
    public String getMensagem() {
        return mensagem;
    }
    
}
